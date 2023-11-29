import pathlib
from collections import defaultdict
from collections import namedtuple
from string import punctuation

__all__ = ['travelling']


def _walk(path: str, search_name: str = None, absolute_key: bool = False,
          absolute_value: bool = True, output_dict: bool = True):
    """
    Function for walking to every path and return its hierarchy in dictionary
    or list.

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
        This field specify whether we want absolute path of parent dir path in
        the final result.
    absolute_value: bool, optional
        This field specify whether we want absolute path of child dir path in
        the finalresult.
    output_dict: bool, optional
        This field specify whether we want dictionary output or list output.

    Returns
    -------
    list or dict
        dictionary with key as parent path and value as file or folder path
        list which list down all the files available in current directory and
        all subdirectories.

    >>> location = pathlib.Path('.')

    >>> find = None

    >>> absolute_paths = _walk(location.as_posix(), absolute_key=False, absolute_value=True, search_name=find, output_dict=False)

    >>> type(absolute_paths)
    <class 'list'>

    >>> relative_paths = _walk(location.as_posix(), absolute_key=False, absolute_value=False, search_name=find, output_dict=False)

    >>> type(relative_paths)
    <class 'list'>

    >>> absolute_paths = _walk(location.as_posix(), absolute_key=False, absolute_value=True, search_name=find, output_dict=True)

    >>> type(absolute_paths)
    <class 'dict'>

    >>> relative_paths = _walk(location.as_posix(), absolute_key=False, absolute_value=False, search_name=find, output_dict=True)

    >>> type(relative_paths)
    <class 'dict'>
    """
    BASE_PATH = pathlib.Path(path)
    path_dict = defaultdict(list)
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
            if isinstance(file_path, pathlib.Path):
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


def find_available_path(from_list: list):
    """
    Function to identify non empty items from nested list

    Parameters
    ----------
    from_list : list
        Nested list containing None and not None entries.

    Returns
    -------
    available_item_list: list
        1D list

    >>> relative_paths = ['spec.json', [None, None, None, [None, None, None, None], None, \
['directory2/directory22/spec.json', None, None, None, None]], ['directory1/spec.json', \
[None, None, None, None], None, None, [None, None, None, None], None, None]]

    >>> find_available_path(relative_paths)
    ['spec.json', 'directory2/directory22/spec.json', 'directory1/spec.json']
    """
    available_item_list = []
    for item in from_list:
        if isinstance(item, list):
            ret_item = find_available_path(item)
            if ret_item:
                available_item_list.extend(ret_item)
        elif isinstance(item, str):
            available_item_list.append(item)
    return available_item_list


def walk(path: str, search_name: str = None):
    """
    Function for walking to every path and return its hierarchy in dictionary
    or list.

    Parameters
    ----------
    path : str
        Used to walk through every file in folders and its sub folders.
    search_name : str, optional
        Used to locate any file with its name (ex. search_name = 'main.py')
        within all the folders and its sub folders from the path location.
        Otherwise assign None if file not found.
        The default is None and is used to locate all files.

    Returns
    -------
    list or dict
        dictionary with key as parent path and value as file or folder path
        list which list down all the files available in current directory and
        all subdirectories.

    >>> walking_result = walk(path='.', search_name='some_file_name')

    >>> type(walking_result)
    <class 'dict'>
    """
    BASE_PATH = pathlib.Path(path)
    path_dict = defaultdict(list)
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
            if file_path == {}:
                file_path = {path_item.name: []}
            parent = path_item.parent
            if isinstance(file_path, pathlib.Path):
                file_path = file_path.absolute().as_posix()
            path_dict[parent.absolute().name].append(file_path)
    return dict(path_dict)


def validate_identifier(identifier: str):
    """
    This function is used to validate variable identifier for namedtuple
    object.

    Parameters
    ----------
    identifier : str
        Valid/Invalid variable name in the form of string.

    Returns
    -------
    identifier : str
        Valid variable name in the form of string. Validation is done by
        replacing all punctuation charachters by '_' and putting 'prefix'
        string if any variable starts with any punctuation character.

    >>> validate_identifier(identifier='file1.py')
    'file1_py'

    >>> validate_identifier(identifier='spec.json')
    'spec_json'

    >>> validate_identifier(identifier='.git')
    'prefix_git'

    >>> validate_identifier(identifier='__init__.py')
    'prefix__init___py'
    """
    if not identifier:
        return identifier
    identifier = pathlib.Path(identifier)
    identifier = identifier.name
    identifier = identifier.replace(' ', '_')
    for symbol in punctuation:
        if symbol in identifier:
            if identifier.startswith(symbol):
                identifier = identifier.replace(symbol, '_')
                identifier = 'prefix' + identifier
            else:
                identifier = identifier.replace(symbol, '_')
    if identifier and identifier[0].isnumeric():
        identifier = 'numeric_' + identifier
    return identifier


def dict2obj(d: dict):
    """
    A recursive calling function which creates objects of every folders and
    returns every files present in folder in the form of list.

    Parameters
    ----------
    d : dict
        Dictionary containing hierarchy of files and folders.

    Returns
    -------
    object
        Object whcih identify files and folders recursively.

    >>> my_dict = {\
        'sample': ['/home/vaibhav/path-traveler/path_traveler/sample/spec.json',\
            {'directory2': ['/home/vaibhav/path-traveler/path_traveler/sample/directory2/file22.py',\
                            '/home/vaibhav/path-traveler/path_traveler/sample/directory2/file22.txt',\
                            '/home/vaibhav/path-traveler/path_traveler/sample/directory2/file21.py',\
                            {'directory21': ['/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory21/file211.py',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory21/file212.txt',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory21/file211.txt',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory21/file212.py']},\
                            '/home/vaibhav/path-traveler/path_traveler/sample/directory2/file21.txt',\
                            {'directory22': ['/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/spec.json',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/file221.txt',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/file222.py',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/file221.py',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/file222.txt']}]},\
            {'directory1': ['/home/vaibhav/path-traveler/path_traveler/sample/directory1/spec.json',\
                            {'directory11': ['/home/vaibhav/path-traveler/path_traveler/sample/directory1/directory11/file112.py',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory1/directory11/file111.py',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory1/directory11/file111.txt',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory1/directory11/file112.txt']},\
                            '/home/vaibhav/path-traveler/path_traveler/sample/directory1/file11.txt',\
                            '/home/vaibhav/path-traveler/path_traveler/sample/directory1/file11.py',\
                            {'directory12': ['/home/vaibhav/path-traveler/path_traveler/sample/directory1/directory12/file121.py',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory1/directory12/file122.py',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory1/directory12/file122.txt',\
                                             '/home/vaibhav/path-traveler/path_traveler/sample/directory1/directory12/file121.txt']},\
                            '/home/vaibhav/path-traveler/path_traveler/sample/directory1/file12.py',\
                            '/home/vaibhav/path-traveler/path_traveler/sample/directory1/file12.txt']}]}

    >>> obj = dict2obj(my_dict)

    >>> obj
    sample
    """
    # checking whether object d is a
    # instance of class list
    if isinstance(d, list):
        FilesAndFolders = namedtuple("FilesAndFolders",
                                     """
                                    files
                                    folders
                                    """)
        from_list = [dict2obj(x) for x in d]
        my_file_list = []
        my_folder_list = []
        for item in from_list:
            if isinstance(item, str):
                my_file_list.append(item)
            else:
                my_folder_list.append(item)
        named_tuple = FilesAndFolders(files=my_file_list,
                                      folders=my_folder_list)
        return named_tuple
    # if d is not a instance of dict then
    # directly object is returned
    if not isinstance(d, dict):
        return d
    # declaring a class
    class C:
        def __repr__(self):
            folder_or_file_name = list(
                self.__dict__.keys()) and list(
                self.__dict__.keys()) and list(
                self.__dict__.keys())[0]
            if not isinstance(folder_or_file_name, str):
                folder_or_file_name = ''
            folder_or_file_name = validate_identifier(
                identifier=folder_or_file_name)
            return folder_or_file_name
    # constructor of the class passed to obj
    obj = C()
    if not d:
        obj.__dict__['object'] = dict2obj([])
        return obj
    for k in d:
        v = dict2obj(d[k])
        k = validate_identifier(identifier=k)
        obj.__dict__[k] = v
    return obj


def obj2namedtuple(path_traveler: dict2obj):
    """
    Function which can convert the object returned from dict2obj into the
    namedtuple object

    Parameters
    ----------
    path_traveler : dict2obj
        object returned from dict2obj.

    Returns
    -------
    named_tuple : namedtuple
        namedtuple object which is dynamically created using path name
        given by ls.files and ls.folder namedtuple used in dict2obj

    >>> my_dict ={\
        'sample': ['path-traveler/path_traveler/sample/spec.json',\
            {'directory2': ['path-traveler/path_traveler/sample/directory2/file22.py',\
                            'path-traveler/path_traveler/sample/directory2/file22.txt',\
                            'path-traveler/path_traveler/sample/directory2/file21.py',\
                            {'directory21': ['path-traveler/path_traveler/sample/directory2/directory21/file211.py',\
                                             'path-traveler/path_traveler/sample/directory2/directory21/file212.txt',\
                                             'path-traveler/path_traveler/sample/directory2/directory21/file211.txt',\
                                             'path-traveler/path_traveler/sample/directory2/directory21/file212.py']},\
                            'path-traveler/path_traveler/sample/directory2/file21.txt',\
                            {'directory22': ['path-traveler/path_traveler/sample/directory2/directory22/spec.json',\
                                             'path-traveler/path_traveler/sample/directory2/directory22/file221.txt',\
                                             'path-traveler/path_traveler/sample/directory2/directory22/file222.py',\
                                             'path-traveler/path_traveler/sample/directory2/directory22/file221.py',\
                                             'path-traveler/path_traveler/sample/directory2/directory22/file222.txt']}]},\
            {'directory1': ['path-traveler/path_traveler/sample/directory1/spec.json',\
                            {'directory11': ['path-traveler/path_traveler/sample/directory1/directory11/file112.py',\
                                             'path-traveler/path_traveler/sample/directory1/directory11/file111.py',\
                                             'path-traveler/path_traveler/sample/directory1/directory11/file111.txt',\
                                             'path-traveler/path_traveler/sample/directory1/directory11/file112.txt']},\
                            'path-traveler/path_traveler/sample/directory1/file11.txt',\
                            'path-traveler/path_traveler/sample/directory1/file11.py',\
                            {'directory12': ['path-traveler/path_traveler/sample/directory1/directory12/file121.py',\
                                             'path-traveler/path_traveler/sample/directory1/directory12/file122.py',\
                                             'path-traveler/path_traveler/sample/directory1/directory12/file122.txt',\
                                             'path-traveler/path_traveler/sample/directory1/directory12/file121.txt']},\
                            'path-traveler/path_traveler/sample/directory1/file12.py',\
                            'path-traveler/path_traveler/sample/directory1/file12.txt']}]}

    >>> obj = dict2obj(my_dict)

    >>> travel = obj2namedtuple(obj)

    >>> travel
    NamedTuple(directory1=NamedTuple(directory11=NamedTuple(file111_py='path-traveler/path_traveler/sample/directory1/directory11/file111.py', \
file111_txt='path-traveler/path_traveler/sample/directory1/directory11/file111.txt', \
file112_py='path-traveler/path_traveler/sample/directory1/directory11/file112.py', \
file112_txt='path-traveler/path_traveler/sample/directory1/directory11/file112.txt'), \
directory12=NamedTuple(file121_py='path-traveler/path_traveler/sample/directory1/directory12/file121.py', \
file121_txt='path-traveler/path_traveler/sample/directory1/directory12/file121.txt', \
file122_py='path-traveler/path_traveler/sample/directory1/directory12/file122.py', \
file122_txt='path-traveler/path_traveler/sample/directory1/directory12/file122.txt'), \
file11_py='path-traveler/path_traveler/sample/directory1/file11.py', \
file11_txt='path-traveler/path_traveler/sample/directory1/file11.txt', \
file12_py='path-traveler/path_traveler/sample/directory1/file12.py', \
file12_txt='path-traveler/path_traveler/sample/directory1/file12.txt', \
spec_json='path-traveler/path_traveler/sample/directory1/spec.json'), \
directory2=NamedTuple(directory21=NamedTuple(file211_py='path-traveler/path_traveler/sample/directory2/directory21/file211.py', \
file211_txt='path-traveler/path_traveler/sample/directory2/directory21/file211.txt', \
file212_py='path-traveler/path_traveler/sample/directory2/directory21/file212.py', \
file212_txt='path-traveler/path_traveler/sample/directory2/directory21/file212.txt'), \
directory22=NamedTuple(file221_py='path-traveler/path_traveler/sample/directory2/directory22/file221.py', \
file221_txt='path-traveler/path_traveler/sample/directory2/directory22/file221.txt', \
file222_py='path-traveler/path_traveler/sample/directory2/directory22/file222.py', \
file222_txt='path-traveler/path_traveler/sample/directory2/directory22/file222.txt', \
spec_json='path-traveler/path_traveler/sample/directory2/directory22/spec.json'), \
file21_py='path-traveler/path_traveler/sample/directory2/file21.py', \
file21_txt='path-traveler/path_traveler/sample/directory2/file21.txt', \
file22_py='path-traveler/path_traveler/sample/directory2/file22.py', \
file22_txt='path-traveler/path_traveler/sample/directory2/file22.txt'), \
spec_json='path-traveler/path_traveler/sample/spec.json')

    >>> type(travel)
    <class 'path_identifier.NamedTuple'>

    >>> travel._fields
    ('directory1', 'directory2', 'spec_json')

    >>> travel.directory1.directory11.file111_py
    'path-traveler/path_traveler/sample/directory1/directory11/file111.py'

    >>> travel.directory1.directory12
    NamedTuple(file121_py='path-traveler/path_traveler/sample/directory1/directory12/file121.py', \
file121_txt='path-traveler/path_traveler/sample/directory1/directory12/file121.txt', \
file122_py='path-traveler/path_traveler/sample/directory1/directory12/file122.py', \
file122_txt='path-traveler/path_traveler/sample/directory1/directory12/file122.txt')

    >>> travel.spec_json
    'path-traveler/path_traveler/sample/spec.json'
    """
    try:
        path_traveler._asdict()
    except AttributeError:
        # print("Converting object into namedtuple if present in the object")
        path_traveler = path_traveler.__dict__[
            list(path_traveler.__dict__.keys())[0]]
        # print("Converted")

    to_dict = path_traveler._asdict()
    as_dict = {}
    for key in path_traveler._fields:  # ('files', 'folders')
        if key == 'folders':
            for every_folder in to_dict[key]:
                every_folder_object = every_folder.__dict__[
                    list(every_folder.__dict__.keys())[0]]
                as_dict[validate_identifier(
                    str(every_folder))] = obj2namedtuple(
                    every_folder_object)
        elif key == 'files':
            for every_file in to_dict[key]:
                as_dict[validate_identifier(every_file)] = every_file
    NamedTuple = namedtuple("NamedTuple", sorted(as_dict))
    named_tuple = NamedTuple(**as_dict)
    return named_tuple


def travelling(root_path: str = None, find: str = None):
    """
    Function which helps to travel the path from namedtuple. A function that
    helps to find out some files in the path hierarchy starting from
    the root path.

    Parameters
    ----------
    root_path : str, optional
        Any path from which you want to start travelling. If None is given then
        the root directory of this module will act as root path.
        The default is None.
    find : str, optional
        Find any file from root directory and all of its children directories.
        If None is given all find will be searching. The default is None.

    Returns
    -------
    TYPE
        namedtuple object providing root path, current working directory path,
        absolute paths, relative paths and a namedtuple object for travelling.

    >>> root_path = None

    >>> find = 'spec.json'

    >>> journey = travelling(root_path=root_path, find=find)

    >>> journey._fields
    ('root_path', 'cwd', 'absolute_paths', 'relative_paths', 'travel')
    """

    PathTraveller = namedtuple("PathTraveller",
                               """
                               root_path
                               cwd
                               absolute_paths
                               relative_paths
                               travel
                               """)
    # Set appropriate path locations
    root_path = root_path and pathlib.Path(
        root_path).absolute().as_posix()

    if not root_path:
        try:
            location = pathlib.Path(__file__).parent
        except NameError:
            location = pathlib.Path('./path_identifier.py').parent
    else:
        location = pathlib.Path(root_path)
        if not location.is_dir() and location.is_file():
            location = location.parent
    try:
        original_location = pathlib.Path(
            '.').absolute().as_posix()
    except NameError:
        original_location = pathlib.Path(
            './path_identifier.py').parent.absolute().as_posix()
    try:
        pathlib.os.chdir(location.absolute().as_posix())
    except FileNotFoundError:
        raise FileNotFoundError
    except TypeError:
        raise TypeError

    # Finding relative paths
    location = pathlib.Path('.')

    # Finding absolute path
    absolute_paths = _walk(location.as_posix(), absolute_key=False,
                           absolute_value=True, search_name=find,
                           output_dict=False)
    absolute_paths = find_available_path(from_list=absolute_paths)

    relative_paths = _walk(location.as_posix(), absolute_key=False,
                           absolute_value=False, search_name=find,
                           output_dict=False)
    relative_paths = find_available_path(from_list=relative_paths)

    # Travel to every path and create dictionary
    my_dict = walk(location.absolute().as_posix())

    # Convert dictionary to object
    obj = dict2obj(my_dict)

    # Convert object to namedtuple
    travel = obj2namedtuple(obj)

    # Namedtuple object
    traveller = PathTraveller(root_path=root_path,
                              cwd=location.absolute().as_posix(),
                              absolute_paths=absolute_paths,
                              relative_paths=relative_paths,
                              travel=travel)
    pathlib.os.chdir(original_location)
    return traveller


if __name__ == '__main__':
    root_path = '/home/vaibhav/path-traveler/path_traveler/sample'
    find = 'spec.json'
    journey = travelling(root_path=root_path, find=find)
    root_path = journey.root_path
    current_working_directory = journey.cwd
    absolute_paths = journey.absolute_paths
    relative_paths = journey.relative_paths
    traveller = journey.travel
