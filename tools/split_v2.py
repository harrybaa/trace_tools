import math

# define your working path
DIR_PATH = "./"
# define your target path
DST_PATH = "./split_files/"
# define your resource file name
RES_FILE = "dynamic_trace_mg"
# define your destination file prefix
DST_PREFIX = "split_"
# define your destination file suffix
DST_SUFFIX = ".txt"
# define the number of blocks per file
# 2000000 is roughly equel to the number
# of blocks per file before
BLOCK_NUM_PER_FILE = 2000000

_count = 0
_file_index = 0

tmp_block = []
blocks = []

def writeIntoFile(index):
  dst_file = DST_PREFIX + str(index).zfill(3) + DST_SUFFIX
  print "Writing file: ", dst_file
  with open(DST_PATH+dst_file, "w+") as df:
    for block in blocks:
      df.write('\n')
      for trace_line in block:
        df.write(trace_line)
  df.close()
  return

print "Reading from source file..."
res_file = open(DIR_PATH + RES_FILE, "r")

line = res_file.readline()
while line:
  if line != '\n':
    tmp_block.append(line)
  else:
    if tmp_block != []:
      blocks.append(tmp_block)
      tmp_block = []
      _count += 1;

      #write into file
      if _count == BLOCK_NUM_PER_FILE:
        writeIntoFile(_file_index);
        blocks = []
        _file_index += 1
        _count = 0

  line = res_file.readline()
  # end of while loop

# write the last one block
if tmp_block != []:
  blocks.append(tmp_block)
if blocks != []:
  writeIntoFile(_file_index);

print "Job done."
res_file.close()
