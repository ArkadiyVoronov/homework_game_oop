import unittest
from unittest import TestCase
from unittest.mock import patch
from main import valid_number

import importlib

rpg = importlib.import_module("main")


class RpgTestCase(TestCase):
    """Юнит тест для домашнего задания 1."""

    def test_valid_number(self):
        """Тестируем ввод."""
        self.assertEqual(valid_number(input(1)), 1)
        self.assertNotEqual(valid_number(number=5), 5)


if __name__ == "__main__":
    unittest.main()
