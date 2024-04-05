from typing import Set, Tuple

def read_file(file_path: str) -> Set[str]:
    """Reads lines from a file and returns them as a set."""
    with open(file_path, 'r') as file:
        return set(file.readlines())


def write_file(file_path: str, content: Set[str]) -> None:
    """Writes content to a file."""
    with open(file_path, 'w') as file:
        file.writelines(content)


def compare_files(file1: Set[str], file2: Set[str]) -> Tuple[Set[str], Set[str], Set[str]]:
    """
    Compares lines between two sets and returns common lines,
    lines only in file1, and lines only in file2.
    """
    common_lines = file1.intersection(file2)
    only_file1_lines = file1 - file2
    only_file2_lines = file2 - file1
    return common_lines, only_file1_lines, only_file2_lines


def main() -> None:
    """Main function to compare files and write results."""
    file1_path = "file1.txt"
    file2_path = "file2.txt"
    same_path = "same.txt"
    diff_path = "diff.txt"

    file1_content: Set[str] = read_file(file1_path)
    file2_content: Set[str] = read_file(file2_path)

    common_lines, only_file1_lines, only_file2_lines = compare_files(file1_content, file2_content)

    write_file(same_path, common_lines)
    write_file(diff_path, only_file1_lines.union(only_file2_lines))


if __name__ == "__main__":
    main()
