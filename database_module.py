"""
Database  Module
"""
import json


class FileManager:
    """
    File Manager Class
    """
    @staticmethod
    def read_file(file_path):
        """
        Method to read file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def write_file(file_path, data):
        """
        Method to write file
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
