def get_todos(filepath="ps.txt"):
  with open(filepath, 'r') as file:
    todos = file.readlines()
  return todos


def write_todos(todos_arg, filepath="ps.txt"):
  with open(filepath, 'w') as file_local:
    file_local.writelines(todos_arg)


print(__name__)  #writes name of this file in output of another file
#writes the name of another file in output of this file

# to hide these statements in output of another file use below function

if __name__ == "__main__":
  print("yash boss")
  print("i am a fan of him")

#but these are printed in this file
