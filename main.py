import os

def write_hierarchy(start_dir, output_file):
    for dirpath, dirnames, filenames in os.walk(start_dir):
        level = dirpath.replace(start_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(dirpath)), file=output_file)
        subindent = ' ' * 4 * (level + 1)
        for f in filenames:
            print('{}{}'.format(subindent, f), file=output_file)

def main():
    start_dir = input("Enter the path of the directory: ")
    output_file_name = input("Enter the output file name (with .txt extension): ")

    with open(output_file_name, 'w') as output_file:
        write_hierarchy(start_dir, output_file)

if __name__ == "__main__":
    main()
