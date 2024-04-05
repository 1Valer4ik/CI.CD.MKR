import pytest
from Task import compare_files

@pytest.fixture
def file1_content(tmp_path):
    content = ["line1\n", "line2\n", "line3\n"]
    file_path = tmp_path / "file1.txt"
    with open(file_path, "w") as file:
        file.writelines(content)
    return file_path

@pytest.fixture
def file2_content(tmp_path):
    content = ["line2\n", "line3\n", "line4\n"]
    file_path = tmp_path / "file2.txt"
    with open(file_path, "w") as file:
        file.writelines(content)
    return file_path

def test_compare_files(file1_content, file2_content):
    file1_content = set(open(file1_content, 'r').readlines())
    file2_content = set(open(file2_content, 'r').readlines())

    common_lines, only_file1_lines, only_file2_lines = compare_files(file1_content, file2_content)

    assert common_lines == {"line2\n", "line3\n"}
    assert only_file1_lines == {"line1\n"}
    assert only_file2_lines == {"line4\n"}

