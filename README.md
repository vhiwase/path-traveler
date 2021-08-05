# Create a journey to walk and search on files.
Walk and travel from any root path directory into all of its children directories and files coming in the journey and perform search operation to list down all available path(s) of the file(s).

<img src="./gif/named_tuple.gif" alt="My Project GIF">

## How to install this package
```
pip install path-traveler
```
Visit [path-traveler](https://pypi.org/project/path-traveler/ "path-traveler pypi package") 

## How to use this package in python code
Following are some of the sample examples to show the use of the ```path-traveler``` package. This package has a function named ```travelling``` which takes optional input 2 arguments. ```root_path``` is the first argument used to set the root directory path and ```find``` is the second argument used to search any file in the root directory and all of its children directories. The default is ```None``` which searches all files from ```root_path```. Let's take a look.

## How to download sample directories and identify its root path

```
$ pwd
/home/vaibhav

$ git clone https://github.com/vhiwase/path-traveler.git

$ cd path-traveler/path_traveler/sample/

$ pwd
/home/vaibhav/path-traveler/path_traveler/sample
```

## How to use this package to search a specific file named 'spec.json'

```
$ python3
>>> from path_traveler import travelling

>>> root_path = '/home/vaibhav/path-traveler/path_traveler/sample'

>>> find = 'spec.json'

>>> journey = travelling(root_path=root_path, find=find)

>>> journey._fields
('root_path', 'cwd', 'absolute_paths', 'relative_paths', 'travel')

>>> root_path = journey.root_path

>>> root_path
'/home/vaibhav/path-traveler/path_traveler/sample'

>>> current_working_directory = journey.cwd

>>> current_working_directory
'/home/vaibhav/path-traveler/path_traveler/sample'

>>> absolute_paths = journey.absolute_paths

>>> absolute_paths
['/home/vaibhav/path-traveler/path_traveler/sample/spec.json', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/spec.json', '/home/vaibhav/path-traveler/path_traveler/sample/directory1/spec.json']

>>> relative_paths = journey.relative_paths

>>> relative_paths
['spec.json', 'directory2/directory22/spec.json', 'directory1/spec.json']

>>> traveller = journey.travel

>>> traveller.directory1.directory11.file111_py
'/home/vaibhav/path-traveler/path_traveler/sample/directory1/directory11/file111.py'

>>> traveller.directory2.directory21.file212_txt
'/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory21/file212.txt'

>>> traveller.directory2.directory22.spec_json
'/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/spec.json'

```

## How to use this package to search all files

```
$ python3
>>> from path_traveler import travelling

>>> root_path='/home/vaibhav/path-traveler/path_traveler/sample/directory2/'

>>> journey = travelling(root_path=root_path)

>>> journey._fields
('root_path', 'cwd', 'absolute_paths', 'relative_paths', 'travel')

>>> root_path = journey.root_path

>>> root_path
'/home/vaibhav/path-traveler/path_traveler/sample/directory2'

>>> current_working_directory = journey.cwd

>>> current_working_directory
'/home/vaibhav/path-traveler/path_traveler/sample/directory2'

>>> absolute_paths = journey.absolute_paths

>>> absolute_paths
['/home/vaibhav/path-traveler/path_traveler/sample/directory2/file22.py', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/file22.txt', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/file21.py', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory21/file211.py', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory21/file212.txt', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory21/file211.txt', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory21/file212.py', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/file21.txt', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/spec.json', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/file221.txt', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/file222.py', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/file221.py', '/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory22/file222.txt']

>>> relative_paths = journey.relative_paths

>>> relative_paths
['file22.py', 'file22.txt', 'file21.py', 'directory21/file211.py', 'directory21/file212.txt', 'directory21/file211.txt', 'directory21/file212.py', 'file21.txt', 'directory22/spec.json', 'directory22/file221.txt', 'directory22/file222.py', 'directory22/file221.py', 'directory22/file222.txt']

>>> traveller = journey.travel

>>> traveller.directory21.file211_txt
'/home/vaibhav/path-traveler/path_traveler/sample/directory2/directory21/file211.txt'

```
## How to use this package to travel using namedtuple() factory function 

<img src="./gif/named_tuple_demo.gif" alt="My Project GIF">

## How to use this package in command line interface (CLI)

```path_traveler --help```
```
Usage: path-traveler [OPTIONS]

Options:
  -P, --root_path TEXT            Any path from which you want to start
                                  travelling. If None is given then the root
                                  directory of this module will act as root
                                  path. The default is None.

  -F, --find TEXT                 Find any file name which you want to
                                  identify no matter whether is it present in
                                  any of the subdirectories. If None is given
                                  all find will be searching. The default is
                                  None.

  -A, --show_absolute_paths BOOLEAN
                                  Print absolute paths  [default: (False)]
  -R, --show_relative_paths BOOLEAN
                                  Print relative paths  [default: (False)]
  -E, --show_examples BOOLEAN     Print predefined examples  [default:
                                  (False)]

  --help                          Show this message and exit.
```

### Calling for python package
```path_traveler``` can be directly called without using ```python3``` to work with command line interface (CLI).

#### Calling without argument
Calling without any argument passing
```
path_traveler
```

#### Calling with --root_path or -P
Here default arguments will be ```find=None```
```
path_traveler --root_path /home/vaibhav/path-traveler/path_traveler/sample/
path_traveler -P /home/vaibhav/path-traveler/path_traveler/sample
```

#### Calling with --root_path or -P and --find or -F
```
path_traveler --root_path /home/vaibhav/path-traveler/path_traveler/sample/ --find spec.json
path_traveler -P /home/vaibhav/path-traveler/path_traveler/sample -F spec.json
```

#### Calling with --root_path or -P, --find or -F or and --show_absolute_paths or -A
Here default arguments will be ```print_matrix=False```
```
path_traveler --root_path /home/vaibhav/path-traveler/path_traveler/sample/ --find spec.json --show_absolute_paths True
path_traveler -P /home/vaibhav/path-traveler/path_traveler/sample -F spec.json -A True
```

#### Calling with --root_path or -P, --find or -F or, --show_absolute_paths or -A and --show_relative_paths or -R
```
path_traveler --root_path /home/vaibhav/path-traveler/path_traveler/sample/ --find spec.json --show_absolute_paths False --show_relative_paths True
path_traveler -P /home/vaibhav/path-traveler/path_traveler/sample -F spec.json -A False -R True
```

#### Calling with --root_path or -P, --find or -F or, --show_absolute_paths or -A, --show_relative_paths or -R and --show_examples or -E
```
path_traveler --root_path /home/vaibhav/path-traveler/path_traveler/sample/ --find spec.json --show_absolute_paths False --show_relative_paths False --show_examples True
path_traveler -P /home/vaibhav/path-traveler/path_traveler/sample -F spec.json -A False -R False -E True
```

### Calling from Command Line Interface (CLI) using ```python3```
You can also run the same using ```python3``` as well:
```
python3 path_traveler/path_identifier_cli.py 

python3 path_traveler/path_identifier_cli.py --root_path /home/vaibhav/path-traveler/path_traveler/sample/

python3 path_traveler/path_identifier_cli.py --root_path /home/vaibhav/path-traveler/path_traveler/sample/ --find spec.json

python3 path_traveler/path_identifier_cli.py --root_path /home/vaibhav/path-traveler/path_traveler/sample/ --find spec.json --show_absolute_paths True

python3 path_traveler/path_identifier_cli.py --root_path /home/vaibhav/path-traveler/path_traveler/sample/ --find spec.json --show_absolute_paths False --show_relative_paths True

python3 path_traveler/path_identifier_cli.py --root_path /home/vaibhav/path-traveler/path_traveler/sample/ --find spec.json --show_absolute_paths False --show_relative_paths False --show_examples True
```

## Calling for tox automation
tox is a command line driven CI frontend and development task automation tool. At its core tox provides a convenient way to run arbitrary commands in isolated environments to serve as a single entry point for build, test and release activities.

To create and run tox supported environment use the following command:
```
sudo sh requirements_tox.sh
tox
```

### Calling for doctest:
```
python3 -m doctest path_traveler/path_identifier.py
```

Use the following command to run sample examples in the python code:
```
>>> from path_traveler import examples
>>> examples()
```

# License
MIT License

Note: If you find this project useful, please include reference link in your work.
