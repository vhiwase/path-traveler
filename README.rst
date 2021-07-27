# Travel any path and find some files
```path-traveller``` is a simple package to walk and travel from any root path directory into all of its children directories and files coming in the journey and perform search operation to list down all available path(s) of the file(s).

## Use in python code
Following are some of the sample examples to show the use of the ```path-traveller``` package. This package has a function named ```travelling``` which takes optional input 2 arguments. ```root_path``` is the first argument used to set the root directory path and ```find``` is the second argument used to search any file in the root directory and all of its children directories. The default is ```None``` which searches all files from ```root_path```. Let's take a look.
```
>>> from path_traveller import travelling

>>> root_path = './sample'
    
>>> find = 'spec.json'

>>> journey = travelling(root_path=root_path, find=find)

>>> journey._fields
('root_path', 'cwd', 'absolute_paths', 'relative_paths', 'travel')

>>> root_path = journey.root_path

>>> current_working_directory = journey.cwd

>>> absolute_paths = journey.absolute_paths

>>> relative_paths = journey.relative_paths

>>> traveller = journey.travel
```

## Use in command line interface (CLI)

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
For more information please visit [GitHub](https://github.com/vhiwase/path-traveller/ "Github Link")

# License
MIT License
