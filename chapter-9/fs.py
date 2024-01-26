# File system access using python

# We can handle the difference between os ( linux , macOS, Windows)
# By using the built in package called pathlib

from pathlib import Path
import os


# we can use this package to handle path create path to files on your
# scripts we could also use the backslash to join paths
# however we need to be careful because when joining paths with / we need
# that one of the values being joined is a Path() object.

def PathToHome(files):
    for filename in files:
        print(Path(r'/home') / "foo" / "bar" / filename)

    homeFolder = Path(r'/home/vitor')

    subFolder = Path("spam")

    print(str(homeFolder / subFolder))

    # Path gives a lot of built in methods to access information about the 
    # file system
    print(Path.cwd())
    # print(Path.chmod("/some-folder/with-some-file.ext", 777))

    print(Path("/home/personal").exists())

    print(Path.home())

    print(Path("/dev").exists())


def createDirs():

    try:
        ## will throw an exception if the path already exists
        os.makedirs(Path.home() / "mocks" / "tests" / "python")
    except FileExistsError:
        print('Path already exists')
    
    defaultPath = Path("home/mocks/tests/python") 


    print(defaultPath.exists())

    # check is path is absolute or relative 
    print(defaultPath.is_absolute())

    print(Path('/etc').is_absolute())


print("////////////// Path to home //////////////")
PathToHome(["accounts.txt", "foo.txt", "bar.txt", "spam.txt"])

print("////////////// CREATE DIRS //////////////")
createDirs()
