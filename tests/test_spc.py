"""
Unit tests for `spc_spectra.spc` module
"""
# --- Imports

# Standard library
from __future__ import absolute_import, unicode_literals, print_function, division
from glob import glob
import os
import unittest
from io import StringIO

# External packages
import numpy as np
import pandas as pd

# Local package
import spc_spectra as spc


# --- Test Suites


class test_spc_spectra(unittest.TestCase):
    """
    Test suite for `spc_spectra.spc` module
    """

    # --- Fixtures

    def setUp(self):
        """
        Prepare for test.
        """
        self.test_data_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "data")
        )

    def tearDown(self):
        """
        Clean up after test.
        """

    # --- Tests

    def test_data_txt(self):
        """
        Test File.data_txt() method.
        """
        # Loop over test data files
        for filename in glob("*.[Ss][Pp][Cc]", root_dir=self.test_data_dir):
            # Load data from SPC file
            spc_file = spc.File(os.path.join(self.test_data_dir, filename))
            data = pd.read_csv(StringIO(spc_file.data_txt()), engine="python", sep=None)

            # Load expected data from reference file
            expected_data_path = os.path.join(self.test_data_dir, f"{filename}.txt")
            with open(expected_data_path, "r") as expected_data_file:
                expected_data = pd.read_csv(
                    expected_data_file, engine="python", sep=None
                )

            # Check that loaded data matches reference data
            assert np.allclose(data.to_numpy(), expected_data.to_numpy(), rtol=1e-8)
