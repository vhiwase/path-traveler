#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_path_traveler
----------------------------------
Tests for `path_traveler` module.
"""

import unittest
from click.testing import CliRunner
from path_traveler import travelling, path_identifier_cli

__all__ = ['Test_path_traveler']


class Test_path_traveler(unittest.TestCase):
    def setUp(self):
        self.root_path = '.'
        self.find = 'spec.json'

    def test_fields(self):
        journey = travelling(root_path=self.root_path)
        self.assertEqual(
            journey._fields,
            ('root_path', 'cwd', 'absolute_paths', 'relative_paths', 'travel')
        )

    def test_command_line_interface_1st_arg(self):
        root_path = self.root_path
        target = '\nType True if you want to display absolute paths of your \
search otherwise type [Enter] [y/N]: \n\nType True if you want to display \
relative paths of your search otherwise type [Enter] [y/N]: \n\nType True \
if you want to display default examples otherwise type [Enter] [y/N]: \n'
        runner = CliRunner()
        result = runner.invoke(path_identifier_cli.main, args=[
            "--root_path", root_path])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(target in result.output)

    def test_command_line_interface_1st_and_2nd_args(self):
        root_path = self.root_path
        find = self.find
        target = '\nType True if you want to display absolute paths of your \
search otherwise type [Enter] [y/N]: \n\nType True if you want to display \
relative paths of your search otherwise type [Enter] [y/N]: \n\nType True \
if you want to display default examples otherwise type [Enter] [y/N]: \n'
        runner = CliRunner()
        result = runner.invoke(path_identifier_cli.main, args=[
            "--root_path", root_path,
            "--find", find])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(target in result.output)

    def test_command_line_interface_1st_2nd_and_3r_args(self):
        root_path = self.root_path
        find = self.find
        show_absolute_paths = False
        target = '\nType True if you want to display relative paths of your \
search otherwise type [Enter] [y/N]: \n\nType True if you want to display \
default examples otherwise type [Enter] [y/N]: \n'
        runner = CliRunner()
        result = runner.invoke(path_identifier_cli.main, args=[
            "--root_path", root_path,
            "--find", find,
            "--show_absolute_paths", show_absolute_paths])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(target in result.output)

    def test_command_line_interface_1st_2nd_3rd_and_4th_args(self):
        root_path = self.root_path
        find = self.find
        show_absolute_paths = False
        show_relative_paths = False
        target = '\nType True if you want to display default examples \
otherwise type [Enter] [y/N]: \n'
        runner = CliRunner()
        result = runner.invoke(path_identifier_cli.main, args=[
            "--root_path", root_path,
            "--find", find,
            "--show_absolute_paths", show_absolute_paths,
            "--show_relative_paths", show_relative_paths])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(target in result.output)

    def test_command_line_interface_1st_2nd_3rd_4th_and_5th_args(self):
        root_path = self.root_path
        find = self.find
        show_absolute_paths = False
        show_relative_paths = False
        show_examples = False
        target = ''
        runner = CliRunner()
        result = runner.invoke(path_identifier_cli.main, args=[
            "--root_path", root_path,
            "--find", find,
            "--show_absolute_paths", show_absolute_paths,
            "--show_relative_paths", show_relative_paths,
            "--show_examples", show_examples])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(target in result.output)


if __name__ == '__main__':
    unittest.main()
