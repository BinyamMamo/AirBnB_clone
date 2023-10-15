#!/usr/bin/python3

import console
import inspect
import pycodestyle
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """ Tests the HBNBCommand class for documentation and style"""

    def test_class_docs(self):
        """ Tests if the HBNBCommand class is documented"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand is not documented")
        self.assertTrue(len(HBNBCommand.__doc__) > 1,
                        "HBNBCommand is not documented")

    def test_module_docs(self):
        """ Tests if console.py is documented"""
        self.assertIsNot(console.__doc__, None,
                         "console.py is not documented")
        self.assertIsNot(len(console.__doc__) > 1,
                         "console.py is not documented")

    def test_pycodestyle(self):
        """ Tests if this module passes the pycodestyle checker"""
        for module in ["console.py",
                       "tests/test_console.py"]:
            with self.subTest("undocumented module", module=module):
                error = pycodestyle.Checker(module).check_all()
                self.assertEqual(error, 0)
