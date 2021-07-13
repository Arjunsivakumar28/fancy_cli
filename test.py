from plumbum import cli
from plumbum.cmd import ls

def get_files():
    ls_output = ls()
    print("start", ls_output, "end")
    return []

def test_get_files():
    files = get_files()
    assert len(files) == 5, "enough files"