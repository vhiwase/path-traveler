# Create a journey to walk and search on files.
Walk and travel from any root path directory into all of its children directories and files coming in the journey and perform search operation to list down all available path(s) of the file(s).

## How to install this package
```
pip install path-traveller
```
Visit [path-traveller](https://pypi.org/project/path-traveller/ "path-traveller pypi package") 

## How to use this package in python code
Following are some of the sample examples to show the use of the ```path-traveller``` package. This package has a function named ```travelling``` which takes optional input 2 arguments. ```root_path``` is the first argument used to set the root directory path and ```find``` is the second argument used to search any file in the root directory and all of its children directories. The default is ```None``` which searches all files from ```root_path```. Let's take a look.

## How to download sample directories and identify its root path

```
$ pwd
/home/vaibhav

$ git clone https://github.com/vhiwase/path-traveller.git

$ cd path-traveller/path_traveller/sample/

$ pwd
/home/vaibhav/path-traveller/path_traveller/sample
```

## How to use this package to search a specific file named 'spec.json'

```
$ python3
>>> from path_traveller import travelling

>>> root_path = '/home/vaibhav/path-traveller/path_traveller/sample'

>>> find = 'spec.json'

>>> journey = travelling(root_path=root_path, find=find)

>>> journey._fields
('root_path', 'cwd', 'absolute_paths', 'relative_paths', 'travel')

>>> root_path = journey.root_path

>>> root_path
'/home/vaibhav/path-traveller/path_traveller/sample'

>>> current_working_directory = journey.cwd

>>> current_working_directory
'/home/vaibhav/path-traveller/path_traveller/sample'

>>> absolute_paths = journey.absolute_paths

>>> absolute_paths
['/home/vaibhav/path-traveller/path_traveller/sample/spec.json', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory22/spec.json', '/home/vaibhav/path-traveller/path_traveller/sample/directory1/spec.json']

>>> relative_paths = journey.relative_paths

>>> relative_paths
['spec.json', 'directory2/directory22/spec.json', 'directory1/spec.json']

>>> traveller = journey.travel

>>> traveller.directory1.directory11.file111_py
'/home/vaibhav/path-traveller/path_traveller/sample/directory1/directory11/file111.py'

>>> traveller.directory2.directory21.file212_txt
'/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory21/file212.txt'

>>> traveller.directory2.directory22.spec_json
'/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory22/spec.json'

```

## How to use this package to search all files

```
$ python3
>>> from path_traveller import travelling

>>> root_path='/home/vaibhav/path-traveller/path_traveller/sample/directory2/'

>>> journey = travelling(root_path=root_path)

>>> journey._fields
('root_path', 'cwd', 'absolute_paths', 'relative_paths', 'travel')

>>> root_path = journey.root_path

>>> root_path
'/home/vaibhav/path-traveller/path_traveller/sample/directory2'

>>> current_working_directory = journey.cwd

>>> current_working_directory
'/home/vaibhav/path-traveller/path_traveller/sample/directory2'

>>> absolute_paths = journey.absolute_paths

>>> absolute_paths
['/home/vaibhav/path-traveller/path_traveller/sample/directory2/file22.py', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/file22.txt', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/file21.py', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory21/file211.py', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory21/file212.txt', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory21/file211.txt', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory21/file212.py', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/file21.txt', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory22/spec.json', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory22/file221.txt', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory22/file222.py', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory22/file221.py', '/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory22/file222.txt']

>>> relative_paths = journey.relative_paths

>>> relative_paths
['file22.py', 'file22.txt', 'file21.py', 'directory21/file211.py', 'directory21/file212.txt', 'directory21/file211.txt', 'directory21/file212.py', 'file21.txt', 'directory22/spec.json', 'directory22/file221.txt', 'directory22/file222.py', 'directory22/file221.py', 'directory22/file222.txt']

>>> traveller = journey.travel

>>> traveller.directory21.file211_txt
'/home/vaibhav/path-traveller/path_traveller/sample/directory2/directory21/file211.txt'

```



## How to use this package in command line interface (CLI)

```path_traveller --help```
```
Usage: path-traveller [OPTIONS]

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
```path_traveller``` can be directly called without using ```python3``` to work with command line interface (CLI).

#### Calling with --root_path or -P
Here default arguments will be ```find=None```
```
path_traveller --root_path /home/vaibhav/path-traveller/path_traveller/sample/
path_traveller -P /home/vaibhav/path-traveller/path_traveller/sample
```

#### Calling with --root_path or -P and --find or -F
```
path_traveller --root_path /home/vaibhav/path-traveller/path_traveller/sample/ --find spec.json
path_traveller -P /home/vaibhav/path-traveller/path_traveller/sample -F spec.json
```

#### Calling with --root_path or -P, --find or -F or and --show_absolute_paths or -A
Here default arguments will be ```print_matrix=False```
```
path_traveller --root_path /home/vaibhav/path-traveller/path_traveller/sample/ --find spec.json --show_absolute_paths True
path_traveller -P /home/vaibhav/path-traveller/path_traveller/sample -F spec.json -A True
```

#### Calling with --root_path or -P, --find or -F or, --show_absolute_paths or -A and --show_relative_paths or -R
```
path_traveller --root_path /home/vaibhav/path-traveller/path_traveller/sample/ --find spec.json --show_absolute_paths False --show_relative_paths True
path_traveller -P /home/vaibhav/path-traveller/path_traveller/sample -F spec.json -A False -R True
```

#### Calling with --root_path or -P, --find or -F or, --show_absolute_paths or -A, --show_relative_paths or -R and --show_examples or -E
```
path_traveller --root_path /home/vaibhav/path-traveller/path_traveller/sample/ --find spec.json --show_absolute_paths False --show_relative_paths False --show_examples True
path_traveller -P /home/vaibhav/path-traveller/path_traveller/sample -F spec.json -A False -R False -E True
```

### Calling from Command Line Interface (CLI) using ```python3```
You can also run the same using ```python3``` as well:
```
python3 path_traveller/path_identifier_cli.py 

python3 path_traveller/path_identifier_cli.py --root_path /home/vaibhav/path-traveller/path_traveller/sample/

python3 path_traveller/path_identifier_cli.py --root_path /home/vaibhav/path-traveller/path_traveller/sample/ --find spec.json

python3 path_traveller/path_identifier_cli.py --root_path /home/vaibhav/path-traveller/path_traveller/sample/ --find spec.json --show_absolute_paths True

python3 path_traveller/path_identifier_cli.py --root_path /home/vaibhav/path-traveller/path_traveller/sample/ --find spec.json --show_absolute_paths False --show_relative_paths True

python3 path_traveller/path_identifier_cli.py --root_path /home/vaibhav/path-traveller/path_traveller/sample/ --find spec.json --show_absolute_paths False --show_relative_paths False --show_examples True
```

### Calling for tox automation
tox is a command line driven CI frontend and development task automation tool. At its core tox provides a convenient way to run arbitrary commands in isolated environments to serve as a single entry point for build, test and release activities.

To create and run tox supported environment use the following command:
```
sudo sh requirements_tox.sh
tox
```

### Calling for doctest:
```
python3 -m doctest path_traveller/path_identifier.py
```

### Calling for unittest
```
python3 -m unittest discover
python3 -m pytest 
```

### Calling for sample examples
Use the following command to run sample examples from command line interface:
```
matrix_rotation
```
This command will prompt a message in the console. If you want to run sample examples just type ```None``` in the console.
```
Type "None" to display default examples.
Enter your matrix: <None>
```

Use the following command to run sample examples in the python code:
```
>>> from matrix_rotation import examples
>>> examples()
```

### Output of above sample examples
```
Original Matrix:
[['a', 'b'],
['d', 'c']]

Clockwise Rotated Matrix with Degree = 1:
[['d', 'a'],
 ['c', 'b']]
---------------------------------------------

Original Matrix:
[['a', 'b'],
 ['d', 'c']]

Anitclockwise Rotated Matrix with Degree = 1:
[['b', 'c'],
 ['a', 'd']]
---------------------------------------------

Original Matrix:
[['a', 'b', 'c'],
 ['h', 'i', 'd'],
 ['g', 'f', 'e']]

Anitclockwise Rotated Matrix with Degree = 1:
[['b', 'c', 'd'],
 ['a', 'i', 'e'],
 ['h', 'g', 'f']]
---------------------------------------------

Original Matrix:
[['a', 'b', 'c', 'd'],
 ['l', 'm', 'n', 'e'],
 ['k', 'p', 'o', 'f'],
 ['j', 'i', 'h', 'g']]

Clockwise Rotated Matrix with Degree = 2:
[['k', 'l', 'a', 'b'],
 ['j', 'o', 'p', 'c'],
 ['i', 'n', 'm', 'd'],
 ['h', 'g', 'f', 'e']]
---------------------------------------------

Original Matrix:
[['a', 'b', 'c', 'd', 'e'],
 ['p', 'q', 'r', 's', 'f'],
 ['o', 'x', 'y', 't', 'g'],
 ['n', 'w', 'v', 'u', 'h'],
 ['m', 'l', 'k', 'j', 'i']]

Clockwise Rotated Matrix with Degree = 2:
[['o', 'p', 'a', 'b', 'c'],
 ['n', 'w', 'x', 'q', 'd'],
 ['m', 'v', 'y', 'r', 'e'],
 ['l', 'u', 't', 's', 'f'],
 ['k', 'j', 'i', 'h', 'g']]
---------------------------------------------

Original Matrix:
[['1', '2', '3', '4', '5', '6'],
 ['20', '21', '22', '23', '24', '7'],
 ['19', '32', '33', '34', '25', '8'],
 ['18', '31', '36', '35', '26', '9'],
 ['17', '30', '29', '28', '27', '10'],
 ['16', '15', '14', '13', '12', '11']]

Clockwise Rotated Matrix with Degree = 3:
[['18', '19', '20', '1', '2', '3'],
 ['17', '30', '31', '32', '21', '4'],
 ['16', '29', '34', '35', '22', '5'],
 ['15', '28', '33', '36', '23', '6'],
 ['14', '27', '26', '25', '24', '7'],
 ['13', '12', '11', '10', '9', '8']]
---------------------------------------------

Original Matrix:
[['1', '2', '3', '4', '5', '6', '7'],
 ['24', '25', '26', '27', '28', '29', '8'],
 ['23', '40', '41', '42', '43', '30', '9'],
 ['22', '39', '48', '49', '44', '31', '10'],
 ['21', '38', '47', '46', '45', '32', '11'],
 ['20', '37', '36', '35', '34', '33', '12'],
 ['19', '18', '17', '16', '15', '14', '13']]

Anitclockwise Rotated Matrix with Degree = 4:
[['5', '6', '7', '8', '9', '10', '11'],
 ['4', '29', '30', '31', '32', '33', '12'],
 ['3', '28', '45', '46', '47', '34', '13'],
 ['2', '27', '44', '49', '48', '35', '14'],
 ['1', '26', '43', '42', '41', '36', '15'],
 ['24', '25', '40', '39', '38', '37', '16'],
 ['23', '22', '21', '20', '19', '18', '17']]
---------------------------------------------

```
# Application on image
Following are the sample application examples of the matrix rotation.
2D red channel of the 3D colored image is use to demonstrate this application.
Image is rotated clockwise and anticlockwise in 15 degree, 30 degree, 45 degree, 60 degree and 90 degree respectively.

<p align="center">
  <img src="matrix_rotation/images/Kills_skull_64x64.png" width="64" title="Kill Skull Image">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel.png" width="64" alt="accessibility text">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel_rotated_15_degree_clockwise.png" width="64" alt="accessibility text">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel_rotated_30_degree_clockwise.png" width="64" alt="accessibility text">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel_rotated_45_degree_clockwise.png" width="64" alt="accessibility text">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel_rotated_60_degree_clockwise.png" width="64" alt="accessibility text">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel_rotated_90_degree_clockwise.png" width="64" alt="accessibility text">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel_rotated_15_degree_anticlockwise.png" width="64" alt="accessibility text">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel_rotated_30_degree_anticlockwise.png" width="64" alt="accessibility text">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel_rotated_45_degree_anticlockwise.png" width="64" alt="accessibility text">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel_rotated_60_degree_anticlockwise.png" width="64" alt="accessibility text">
  <img src="matrix_rotation/images/Kill_skull_64x64_red_channel_rotated_90_degree_anticlockwise.png" width="64" alt="accessibility text">
</p>

# License
MIT License

Note: If you find this project useful, please include reference link in your work.
