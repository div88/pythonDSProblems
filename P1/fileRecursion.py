import os
import os.path
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    if os.path.isfile(path):
      if path.endswith(suffix):
        print(f'File ends with: {path}')

    elif os.path.isdir(path):
        for f in os.listdir(path):
          newPath = path+"/"+f
          find_files(suffix,newPath)
  

# TestCases

def test_cases(d):
  listd = os.listdir(i)
  listd.remove('.DS_Store')

  for j in listd:
    pathA = i+j
    ext = ".c"
    find_files(ext,pathA)


listdire = ["./testdir1/", "./testdir2/","./testdir3/"]

for i in listdire:
  test_cases(i)





