import os
if os.path.exists("bahar.txt"):
  os.remove("bahar.txt")
else:
  print("The file does not exist")