import os 

def get_dir_files_list(path, recursive = False):
    """
    获取指定目录下的所有文件和文件夹的列表
    :param path: 指定目录的路径
    :param recursive: 是否递归查找子目录
    :return: 文件和文件夹的列表
    """
    dir_names = os.listdir(path)
    files = []

    for dir_name in dir_names:
        absolute_path = f"{path}/{dir_name}"
        if not os.path.isdir(absolute_path):
            files.append(absolute_path)
        else: 
            if recursive:
                files += get_dir_files_list(absolute_path, recursive)

    return files

def get_new_by_compare_lists(a_list, b_list):
    """
    Take 2 lists, and return the difference
    a_list: is the file name from the target directory 
    b_list: is obtained from SQL 
    """    

    return list(set(a_list) - set(b_list))