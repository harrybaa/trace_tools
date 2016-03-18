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
# define the number of split files
FILE_NUM = 10

_count = 0
_file_index = 0
_block_num = 0
_blocks_per_file = 0


print("Reading from source file...")
res_file = open(DIR_PATH + RES_FILE, "r")
lines_res = res_file.readlines()
res_file.close()

print("Organizing data sets...")
blocks = []
tmp_block = []
# store data in a structure form
lines_res.append('\n') # ensure to put the last block
for line_res in lines_res:
  if line_res != '\n':
    tmp_block.append(line_res)
  else:
    if tmp_block != []:
      blocks.append(tmp_block)
      tmp_block = []

_block_num = len(blocks)
_blocks_per_file = math.ceil(_block_num / FILE_NUM)

for i in range(0, FILE_NUM):
  dst_file = DST_PREFIX + str(i).zfill(3) + DST_SUFFIX
  print("Writing ", dst_file)
  # Prevent from out of array
  if i == FILE_NUM - 1:
    end = _block_num
  else:
    end = (i + 1) * _blocks_per_file
  # Create splite file
  with open(DST_PATH + dst_file, "w+") as dst_file:
    for j in range(i * _blocks_per_file, end):
      dst_file.write("\n")
      for line in blocks[j]:
        dst_file.write(line)
  dst_file.close()

print("Job done.")