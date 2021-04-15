"""We use this file as an example for some module."""
import os


def find_condaac_dir() -> str:
    """Locate .conda_ac file if it exists.
    Return dir w/ file, or "" if dne
    """
    conda_file = ".conda_ac"
    cur_dir = os.getcwd()
    while True:
        file_list = os.listdir(cur_dir)
        parent_dir = os.path.dirname(cur_dir)
        if conda_file in file_list:
            return cur_dir
        else:
            if cur_dir == parent_dir:  # if dir is root dir
                print("conda file not found")
                return ""
            else:
                cur_dir = parent_dir


def activate_conda():
    """Locate .conda_ac file if it exists.
    Return dir w/ file, or "" if dne
    """
    conda_dir: str = find_condaac_dir()
    if conda_dir:
        conda_ac = os.path.join(conda_dir, ".conda_ac")
        with open(conda_ac) as f:
            env = f.readline().strip()
        os.system(f"conda activate {env}")


__all__ = ["activate_conda"]
