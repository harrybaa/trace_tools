import os
DIR_PATH = "./backup/"

for root, dirs, files in os.walk(DIR_PATH):
  files.sort()
  file_num = len(files)

  # append contents to target file
  for i in range(0, file_num):
  # for i in range(1, 2):
    print "Working with: ", (i+1), "/", file_num, ' ', files[i]
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

    with open(DIR_PATH+files[i], "w") as ff:
      ff.write(''.join(lines))

print("Finished...")