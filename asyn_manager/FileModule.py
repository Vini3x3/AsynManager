import AsynManager
import os


class FileChecker(AsynManager.Executor):
    def __init__(self):
        self.base_directory = ''

    def set_dir(self, directory):
        self.base_directory = directory

    def get_dir(self):
        return self.base_directory

    def get_line_cnt(self, file_name, with_dir=True):
        if with_dir:
            path = os.path.join(self.base_directory, file_name)
        else:
            path = file_name
        with open(path, 'r') as f:
            return len(f.readlines())

    def scan_dir(self):
        with os.scandir(self.base_directory) as entries:
            return [entry.name for entry in entries if entry.is_file()]

class FilePlanner(AsynManager.Planner):

    @staticmethod
    def get_folder_files_line_cnt(target_directory, file_checker):
        files = file_checker.scan_dir(target_directory)
        for file in files:


