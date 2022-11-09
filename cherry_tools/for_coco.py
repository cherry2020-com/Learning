import os
import re

path = r'C:\Users\I320057\Documents\testformd'  # main folder path
md_paths = []  # all md files path
p_old = r']\(/docs/.*?\)'  # pattern to match


# search for all md files, and return the all the md paths
def listdir(path, listname):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, listname)
        elif os.path.splitext(file_path)[1] == '.md':
            listname.append(file_path)


# replace pattern
def replace_things(src_file_data, p_old, md_path):
    find_lines = re.findall(p_old, src_file_data)
    if find_lines is None:
        return
    else:
        for find_line in find_lines:
            p_mid = re.split(r'/', find_line)
            p_new = u']{{ ref . "' + p_mid[-2] + '" }}'
            src_file_data = src_file_data.replace(find_line, p_new)
            print(md_path)
            print(p_new, find_line)
    return src_file_data


if __name__ == '__main__':
    listdir(path, md_paths)
    for md_path in md_paths:
        with open(md_path, encoding='utf-8') as f_r:
            src_file_data = f_r.read()
            src_file_data = replace_things(src_file_data, p_old, md_path)
        with open(md_path, 'w', encoding='utf-8') as f_w:
            f_w.write(src_file_data)
            f_w.close()
