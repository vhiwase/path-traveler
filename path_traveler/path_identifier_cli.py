try:
    from .path_identifier import travelling
except ImportError:
    from path_identifier import travelling

import click
import pathlib

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
    journey = travelling(root_path=root_path, find=find)
    root_path = journey.root_path
    current_working_directory = journey.cwd
    print("""Input parameters:
{}""".format("-" * 23))
    print("root_path = {}".format(root_path))
    print("find = {}".format(find))
    print()
    print("""Output:
{}""".format("-" * 23))
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
    print("""{}""".format("#" * 75))

    print()
    root_path = None
    find = 'spec.json'
    print("Identifying '{}' file".format(find))
    print("""{}""".format("-" * 28))
    journey = travelling(root_path=root_path, find=find)
    root_path = journey.root_path
    current_working_directory = journey.cwd
    print("""Input parameters:
{}""".format("-" * 23))
    print("root_path = {}".format(root_path))
    print("find = {}".format(find))
    print()
    print("""Output:
{}""".format("-" * 23))
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
    print("""{}""".format("#" * 75))

    root_path = './sample'
    find = None
    journey = travelling(root_path=root_path, find=find)
    root_path = journey.root_path
    current_working_directory = journey.cwd
    print("""Input parameters:
{}""".format("-" * 23))
    print("root_path = {}".format(root_path))
    print("find = {}".format(find))
    print()
    print("""Output:
{}""".format("-" * 23))
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
    print("""{}""".format("#" * 75))

    print()
    root_path = './sample'
    find = 'spec.json'
    print("Identifying '{}' file".format(find))
    print("""{}""".format("-" * 28))
    journey = travelling(root_path=root_path, find=find)
    root_path = journey.root_path
    current_working_directory = journey.cwd
    print("""Input parameters:
{}""".format("-" * 23))
    print("root_path = {}".format(root_path))
    print("find = {}".format(find))
    print()
    print("""Output:
{}""".format("-" * 23))
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
    print("""{}""".format("#" * 75))


@click.command()
@click.option('--root_path', '-P', prompt='Type . for current root directory. \
\nEnter your root path', default=None, show_default=None,
            type=str, help="Any path from which you want to start \
travelling. If None is given then the root directory of this module will \
act as root path. The default is None.")
@click.option('--find', '-F', default=None, show_default=None,
            type=str, help="Find any file name which you want to search. \
The default is None.")
@click.option('--show_absolute_paths', '-A', prompt='\nType True if you want \
to display absolute paths of your search otherwise type [Enter]',
            default=False, show_default='False', type=bool,
            help="Print absolute paths")
@click.option('--show_relative_paths', '-R', prompt='\nType True if you want \
to display relative paths of your search otherwise type [Enter]',
            default=False, show_default='False', type=bool,
            help="Print relative paths")
@click.option('--show_examples', '-E', prompt='\nType True if you want to \
display default examples otherwise type [Enter]',
            default=False, show_default='False', type=bool,
            help="Print predefined examples")
def main(root_path=None, find=None, show_absolute_paths=False,
         show_relative_paths=False, show_examples=False):
    if not (pathlib.PosixPath(root_path).is_dir()
            or pathlib.PosixPath(root_path).is_file()):
        click.echo("\nPlease enter the correct root path. You can use . for \
current directory\n")
        return main()
    try:
        journey = travelling(root_path=root_path, find=find)
    except (SyntaxError, TypeError, NameError, FileNotFoundError):
        click.echo("Please enter the valid arguments\n")
        return main()
    if show_examples:
        try:
            examples()
        except FileNotFoundError:
            click.echo("Examples cannot be shown.")            
    if show_absolute_paths:
        print()
        print("Absolute paths: {}".format(journey.absolute_paths))
        print()
    if show_relative_paths:
        print()
        print("Absolute paths: {}".format(journey.relative_paths))
        print()
    return journey


if __name__ == '__main__':
    main()
