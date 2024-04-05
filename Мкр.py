def read_file(file_path):
    with open(file_path, 'r') as file:
        return set(file.readlines())

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.writelines(content)
def compare_files(file1, file2):
    common_lines = file1.intersection(file2)
    only_file1_lines = file1 - file2
    only_file2_lines = file2 - file1
    return common_lines, only_file1_lines, only_file2_lines

def main():
    file1_path = "file1.txt"
    file2_path = "file2.txt"
    same_path = "same.txt"
    diff_path = "diff.txt"

    file1_content = read_file(file1_path)
    file2_content = read_file(file2_path)

    common_lines, only_file1_lines, only_file2_lines = compare_files(file1_content, file2_content)

    write_file(same_path, common_lines)
    write_file(diff_path, only_file1_lines.union(only_file2_lines))

if __name__ == "__main__":
    main()
