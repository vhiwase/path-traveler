from path_identifier import path_traveller
import click

__all__ = ["main", "examples"]

def examples():
    """
    Run some exmaples
    Returns None
    -------
    None.
    """
    root_path = None
    find = None
    journey = path_traveller(root_path=root_path, find=find)
    root_path = journey.root_path
    current_working_directory = journey.cwd
    print("""Input parameters:
{}""".format("-"*23))
    print("root_path = {}".format(root_path))
    print("find = {}".format(find))
    print()
    print("""Output:
{}""".format("-"*23))
    print("Current Working Directory: {}".format(current_working_directory))
    print()
    absolute_paths = journey.absolute_paths
    print("Absolute paths: {}".format(absolute_paths))
    print()
    relative_paths = journey.relative_paths
    print("Relative paths: {}".format(relative_paths))
    print()
    traveller = journey.travel    
    print("Total files and directories available: {}".format(len(traveller)))
    print()
    print("""{}""".format("#"*75))
    

    print()
    root_path = None
    find = 'spec.json'
    print("Identifying '{}' file".format(find))
    print("""{}""".format("-"*28))
    journey = path_traveller(root_path=root_path, find=find)
    root_path = journey.root_path
    current_working_directory = journey.cwd
    print("""Input parameters:
{}""".format("-"*23))
    print("root_path = {}".format(root_path))
    print("find = {}".format(find))
    print()
    print("""Output:
{}""".format("-"*23))
    print("Current Working Directory: {}".format(current_working_directory))
    print()
    absolute_paths = journey.absolute_paths
    print("Absolute paths: {}".format(absolute_paths))
    print()
    relative_paths = journey.relative_paths
    print("Relative paths: {}".format(relative_paths))
    print()
    traveller = journey.travel    
    print("Total files and directories available: {}".format(len(traveller)))
    print()
    print("""{}""".format("#"*75))

    root_path = './sample'
    find = None
    journey = path_traveller(root_path=root_path, find=find)
    root_path = journey.root_path
    current_working_directory = journey.cwd
    print("""Input parameters:
{}""".format("-"*23))
    print("root_path = {}".format(root_path))
    print("find = {}".format(find))
    print()
    print("""Output:
{}""".format("-"*23))
    print("Current Working Directory: {}".format(current_working_directory))
    print()
    absolute_paths = journey.absolute_paths
    print("Absolute paths: {}".format(absolute_paths))
    print()
    relative_paths = journey.relative_paths
    print("Relative paths: {}".format(relative_paths))
    print()
    traveller = journey.travel    
    print("Total files and directories available: {}".format(len(traveller)))
    print()
    print("""{}""".format("#"*75))
    

    print()
    root_path = './sample'
    find = 'spec.json'
    print("Identifying '{}' file".format(find))
    print("""{}""".format("-"*28))
    journey = path_traveller(root_path=root_path, find=find)
    root_path = journey.root_path
    current_working_directory = journey.cwd
    print("""Input parameters:
{}""".format("-"*23))
    print("root_path = {}".format(root_path))
    print("find = {}".format(find))
    print()
    print("""Output:
{}""".format("-"*23))
    print("Current Working Directory: {}".format(current_working_directory))
    print()
    absolute_paths = journey.absolute_paths
    print("Absolute paths: {}".format(absolute_paths))
    print()
    relative_paths = journey.relative_paths
    print("Relative paths: {}".format(relative_paths))
    print()
    traveller = journey.travel    
    print("Total files and directories available: {}".format(len(traveller)))
    print()
    print("""{}""".format("#"*75))



@click.command()
@click.option('--matrix', '-M', prompt='Type "None" to display default \
examples.\nEnter your matrix', help='Use to show default examples of matrix \
rotation. Otherwise use the input matrix from command line.\nInput \
example : [["a", "b"],["d", "c"]]')
@click.option('--degree', '-D', default=1, show_default='1', help='Degree of \
rotation. Can rotate matrix in between 0 degree to 360 degree.')
@click.option('--clockwise', '-C', default=True, show_default='True',
              type=bool, help='Use True to rotate matrix in a clockwise direction. \
False for rotation in anticlockwise direction.')
@click.option('--print_matrix', '-S', default=False, show_default='False',
              type=bool, help='Use True to show the result of Original \
and Rotated Matrix.')
def main(matrix=None, degree=1, clockwise=True, print_matrix=False):
    try:
        matrix = eval(matrix)
        shape = np.array(matrix).shape
    except (SyntaxError, TypeError, NameError):
        matrix = None
        click.echo("Please Enter a Valid list for matrix\n")
        return main()

    try:
        if matrix and shape[0] != shape[1]:
            click.echo("Please Enter a Valid Square Matrix\n")
            return main()
    except IndexError:
        click.echo("Please Enter a Valid 2D List\n")
        return main()

    if not matrix:
        examples()
    else:
        if print_matrix:
            rotated_matrix = print_rotate_matrix(
                matrix, degree=degree, clockwise=clockwise)
        else:
            rotated_matrix = rotate_matrix(
                matrix, degree=degree, clockwise=clockwise)
        click.echo(rotated_matrix)
        return rotated_matrix


if __name__ == '__main__':
    main()