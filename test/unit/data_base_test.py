"""
Database Test Module
"""
import unittest
from unittest.mock import mock_open, patch
import json
from database_module import FileManager


class TestFileManager(unittest.TestCase):
    """
    Database Test Calss
    """
    def test_read_file_exists(self):
        """
        Test method to read file
        """
        mock_data = {'key': 'value'}
        mock_json = json.dumps(mock_data)
        with patch('builtins.open',
                   mock_open(read_data=mock_json)) as mocked_file:
            result = FileManager.read_file('dummy_path.json')
            mocked_file.assert_called_once_with('dummy_path.json',
                                                'r', encoding='utf-8')
            self.assertEqual(result, mock_data)

    def test_read_file_not_found(self):
        """
        Test method to read file
        """
        with patch('builtins.open', mock_open()) as mocked_file:
            mocked_file.side_effect = FileNotFoundError
            result = FileManager.read_file('nonexistent_path.json')
            mocked_file.assert_called_once_with('nonexistent_path.json',
                                                'r', encoding='utf-8')
            self.assertEqual(result, {})

    def test_write_file(self):
        """
        Test method to write file
        """
        mock_data = {'key': 'value'}
        with patch('builtins.open', mock_open()) as mocked_file, \
             patch('json.dump') as mocked_json_dump:
            FileManager.write_file('dummy_path.json', mock_data)
            mocked_file.assert_called_once_with('dummy_path.json',
                                                'w', encoding='utf-8')
            mocked_json_dump.assert_called_once_with(mock_data,
                                                     mocked_file.return_value,
                                                     indent=4)


if __name__ == '__main__':
    unittest.main()
