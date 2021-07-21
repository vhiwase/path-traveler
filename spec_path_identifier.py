import pathlib
import pprint
from collections import defaultdict
from collections import namedtuple


def _walk(path: str, search_name: str=None, absolute_key: bool=False, 
          absolute_value: bool=True, output_dict: bool=True):
    """
    Function for walking to every path and return its hierarchy in dictionary.

    Parameters
    ----------
    path : str
        Used to walk through every file in folders and its sub folders.
    search_name : str, optional
        Used to locate any file with its name (ex. search_name = 'main.py') 
        within all the folders and its sub folders from the path location. 
        Otherwise assign None if file not found.
        The default is None and is used to locate all files.
    absolute_key: bool, optional
        This field specify whether we want absolute path of parent dir path in the 
        fianl result.
    absolute_value: bool, optional
        This field specify whether we want absolute path of child dir path in the 
        fianl result.
    output_dict: bool, optional
        This field specify whether we want dictionary output or list output.
        
    Returns
    -------
    TYPE
        dictionary with key as a file number or folder number and value 
        representing file path if present.

    """
    BASE_PATH = pathlib.PosixPath(path)
    path_dict=defaultdict(list)
    path_list = []
    if BASE_PATH.is_file():
        if search_name:
            if BASE_PATH.name == search_name:
                return BASE_PATH
            else:
                return None
        else:
            return BASE_PATH
    elif BASE_PATH.is_dir():
        ls = list(BASE_PATH.iterdir())
        for path_item in ls:
            file_path = _walk(path_item, search_name, 
                              absolute_key=absolute_key, 
                              absolute_value=absolute_value,
                              output_dict=output_dict)
            key = path_item.parent
            if isinstance(file_path, pathlib.PosixPath):
                if absolute_value:
                    file_path = file_path.absolute().as_posix()
                else:
                    file_path = file_path.as_posix()
            if absolute_key:
                path_dict[key.absolute().as_posix()].append(file_path)
            else:
                path_dict[key.name].append(file_path)

            path_list.append(file_path)
    if output_dict:
        return dict(path_dict)
    else:
        return path_list


def find_available_path(my_list: list):
    """
    Function to identify non empty items from nested list

    Parameters
    ----------
    my_list : list
        Nested list containing None and not None entries.

    Returns
    -------
    available_item_list : list
        1D list.

    """
    available_item_list = []
    for item in my_list:
        if isinstance(item, list):
            ret_item = find_available_path(item)
            if ret_item:
                available_item_list.extend(ret_item)
        elif isinstance(item, str):
            available_item_list.append(item)
    return available_item_list


def walk(path: str, search_name: str=None):
    """
    Function for walking to every path and return its hierarchy in dictionary.

    Parameters
    ----------
    path : str
        Used to walk through every file in folders and its sub folders.
    search_name : str, optional
        Used to locate any file with its name (ex. search_name = 'main.py') 
        within all the folders and its sub folders from the path location. 
        Otherwise assign None if file not found.
        The default is None and is used to locate all files.
    is_absolute: bool, optional
        This field specify whether we want absolute parent dir path in the 
        fianl result.

    Returns
    -------
    TYPE
        dictionary with key as a file number or folder number and value 
        representing file path if present.

    """
    BASE_PATH = pathlib.PosixPath(path)
    path_dict=defaultdict(list)
    if BASE_PATH.is_file():
        if search_name:
            if BASE_PATH.name == search_name:
                return BASE_PATH
            else:
                return None
        else:
            return BASE_PATH
    elif BASE_PATH.is_dir():
        ls = list(BASE_PATH.iterdir())
        for path_item in ls:
            file_path = walk(path_item, search_name)
            parent = path_item.parent
            if isinstance(file_path, pathlib.PosixPath):
                file_path = file_path.name
            path_dict[parent.absolute().name].append(file_path)
    return dict(path_dict)


def dict2obj(d: dict):
    """
    A recursive calling function which creates objects of every folders and
    returns every files present in folder in the form of list

    Parameters
    ----------
    d : dict
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    # checking whether object d is a
    # instance of class list
    if isinstance(d, list):
        my_named_tuple = namedtuple("ls",
                                    """
                                    files
                                    folders
                                    """)
        # d = [dict2obj(x) for x in d]
        my_list = [dict2obj(x) for x in d]
        my_file_list = []
        my_folder_list = []
        for item in my_list:
            if isinstance(item, str):
                my_file_list.append(item)
            else:
                my_folder_list.append(item)
                
        my_named_tuple = my_named_tuple(files=my_file_list,
                       folders=my_folder_list)
        return my_named_tuple
    
    # if d is not a instance of dict then
    # directly object is returned
    if not isinstance(d, dict):
           return d
   
    # declaring a class
    class C:
        def __repr__(self):
            folder_or_file_name = list(self.__dict__.keys()) and list(self.__dict__.keys())[0]
            if '-' in folder_or_file_name:
                folder_or_file_name = folder_or_file_name.replace('-', '_')
            return folder_or_file_name
   
    # constructor of the class passed to obj
    obj = C()
   
    for k in d:
        v = dict2obj(d[k])
        if '-' in k:
            k = k.replace('-', '_')
        obj.__dict__[k] = v
   
    return obj
  

if __name__ == '__main__':    
    
    location = pathlib.Path(__file__).parent
    file_name = 'spec.json'
    my_list = _walk(location.as_posix(), absolute_key=False, absolute_value=True, 
                    search_name = file_name, output_dict=False)
    print("walk through the path to search {} file in folder structure".format(file_name))
    pprint.pprint(my_list)
    my_list = find_available_path(my_list=my_list)
    print("walk through the path to search {} file without folder structure".format(file_name))
    pprint.pprint(my_list)

    print()
    
    # location = pathlib.PosixPath('.')
    my_dict = walk(location.as_posix())
    print("walk through every path to identify folder structures")
    print(my_dict)
    
    print()
    
    obj = dict2obj(my_dict)
    print("object to walking through every file and folders")
    print(obj)
    print(obj.path_traveller)
