import math
import os

# define your working path
DIR_PATH = "../files_to_merge/"
# define your target path
DST_PATH = "./"
# define your destination file prefix
DST_FILE = "merged_info.txt"

dvf = []
dvf_sum = 0
dvf_num = 0
dvf_ratio = 0
root_info = [[]]*10
organized_info = []
res = []

# Reading
for root, dirs, files in os.walk(DIR_PATH):
  for file in files:
    with open(DIR_PATH + file, 'r') as f:
      # for dvf_sum and dvf_num
      dvf = f.readline().split(' ')
      dvf_sum += float(dvf[1])
      dvf_num += int(dvf[3])

      # for part remain
      tmp_block = []
      index = 0
      lines = f.readlines()
      for line in lines:
        if line != '\n':
          # num_of_opcode
          if line.startswith("num_of_opcode"):
            tmp_opcode = line.split(' ')
            tmp_block.append(tmp_opcode[0].split(':') + tmp_opcode[1:])
          else:
            tmp_block.append(line.split(':'))
        # put into block
        else:
          if tmp_block is not []:
            root_info[index] = root_info[index] + tmp_block
            tmp_block = []
            index += 1
      # in case
      if tmp_block is not []:
        root_info[index] = root_info[index] + tmp_block

# Merging
dvf_ratio = dvf_sum / dvf_num

index = 0
for info in root_info:
  if info != []:
    organized_info.append({})
    for line in info:
      tmp_obj = {}
      # title
      if line[1] == '\n':
        tmp_obj['value'] = '\n'
      # merge item value
      elif organized_info[index].has_key(line[0]):
        tmp_obj['value'] = organized_info[index][line[0]]['value'] + float(line[1])
      # intert items
      else:
        tmp_obj['value'] = float(line[1])

      # storage is_processed
      if len(line) > 2:
        tmp_obj['else'] = ''.join(line[2:])
      else:
        tmp_obj['else'] = ''
      organized_info[index][line[0]] = tmp_obj
    index += 1

# Outputting
with open(DST_PATH + DST_FILE, "w+") as merged_info:
  info = "dvf_sum: " + str(dvf_sum) + " dvf_num: " + str(dvf_num) + " dvf_ratio: " + str(dvf_ratio) + '\n'
  merged_info.write(info)
  for block in organized_info:
    for key, value in iter(sorted(block.iteritems())):
      info = key + ':' + str(value['value'])
      if value['else'] != '':
        info += ' ' + value['else']
      if not info.endswith('\n'):
        info += '\n'
      merged_info.write(info)
    merged_info.write('\n')





