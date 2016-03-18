import os
DIR_PATH = "./"
RES_FILE = "wei_fixed.txt"

with open(RES_FILE, "w") as res:
  # first blank line
  res.write('\n')

  for root, dirs, files in os.walk(DIR_PATH):
    files.sort()
    cnt = len(files)

    # append contents to target file
    for i in range(0, cnt):
      print(files[i])
      with open(DIR_PATH+files[i], "r") as f:
        res.write(f.read())
      f.close()

    # # delete last line in last file
    with open(DIR_PATH+files[cnt-1], "r") as ff:
      lines = ff.readlines()
      lines = lines[:-1]
      for line in lines:
        res.write(line)
    ff.close()

res.close()