import os
DIR_PATH = "./trace_refined_package_mg/"
RES_FILE = "wei_fixed.txt"

with open(RES_FILE, "w") as res:

  for root, dirs, files in os.walk(DIR_PATH):
    files.sort()
    cnt_file = len(files)

    # append contents to target file
    for i in range(0, cnt_file):
    # for i in range(1, 2):
      print("Working with: ", files[i])
      with open(DIR_PATH+files[i], "r") as f:
        lines = f.readlines()
        cnt_line = len(lines)
        # cross the blank line at end out
        if lines[cnt_line-1] == '\n':
          lines = lines[:-1]
        # if begin with a new phi block
        # insert a blank line
        if lines[0].startswith('0,'):
          lines.insert(0, '\n')
        #write into file
        for line in lines:
          res.write(line)
      f.close()

print("Finished...")
res.close()