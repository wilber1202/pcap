#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

if len(sys.argv) != 2:
    print("keyboard2 missing args!")
    exit(1)

os.system("tshark -r %s -T fields -e usb.capdata 'usb.data_len == 8' > usb2.dat" % (sys.argv[1]))

mappings = {0x04:"A", 0x05:"B", 0x06:"C", 0x07:"D", 0x08:"E", 0x09:"F", 0x0a:"G", 0x0b:"H", 0x0c:"I", 0x0d:"J", 0x0e:"K", 0x0f:"L", 0x10:"M", 0x11:"N", 0x12:"O", 0x13:"P", 0x14:"Q", 0x15:"R", 0x16:"S", 0x17:"T", 0x18:"U", 0x19:"V", 0x1a:"W", 0x1b:"X", 0x1c:"Y", 0x1d:"Z",0x1e:"!", 0x1f:"@", 0x20:"#", 0x21:"$", 0x22:"%", 0x23:"^",0x24:"&",0x25:"*",0x26:"(",0x27:")",0x28:"<RET>",0x29:"<ESC>",0x2a:"<DEL>", 0x2b:"\t",0x2c:"<SPACE>",0x2d:"_",0x2e:"+",0x2f:"{",0x30:"}",0x31:"|",0x32:"<NON>",0x33:"\"",0x34:":",0x35:"<GA>",0x36:"<",0x37:">",0x38:"?",0x39:"<CAP>",0x3a:"<F1>",0x3b:"<F2>", 0x3c:"<F3>",0x3d:"<F4>",0x3e:"<F5>",0x3f:"<F6>",0x40:"<F7>",0x41:"<F8>",0x42:"<F9>",0x43:"<F10>",0x44:"<F11>",0x45:"<F12>"}
nums = []
keys = open('usb2.dat')

for line in keys:
    # if line[0]!='0' or line[1]!='0' or line[3]!='0' or line[4]!='0' or line[9]!='0' or line[10]!='0' or line[12]!='0' or line[13]!='0' or line[15]!='0' or line[16]!='0' or line[18]!='0' or line[19]!='0' or line[21]!='0' or line[22]!='0':
    if line[0]!='0' or line[1]!='0' or line[2]!='0' or line[3]!='0' or line[6]!='0' or line[7]!='0' or line[8]!='0' or line[9]!='0' or line[10]!='0' or line[11]!='0' or line[12]!='0' or line[13]!='0' or line[14]!='0' or line[15]!='0':
        # 如果提取出来的数据没有: 的话，上面一行就将改为：
        # if line[0]!='0' or line[1]!='0' or line[2]!='0' or line[3]!='0' or line[6]!='0' or line[7]!='0' or line[8]!='0' or line[9]!='0' or line[10]!='0' or line[11]!='0' or line[12]!='0' or line[13]!='0' or line[14]!='0' or line[15]!='0':
        continue
    # nums.append(int(line[6:8],16))
    nums.append(int(line[4:6],16))
	# 如果提取出来的数据没有: 的话，这里就将改为 nums.append(int(line[4:6],16))
keys.close()

output = ""
for n in nums:
    if n == 0 :
        continue
    if n in mappings:
        output += mappings[n]
    else:
        output += '[unknown]'
print('output :\n' + output)

'keyusb.txt'
'''
00:00:0b:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:08:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:0f:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:0f:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:12:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:1a:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:12:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:15:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:0f:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:07:00:00:00:00:00
00:00:00:00:00:00:00:00
02:00:00:00:00:00:00:00
02:00:1e:00:00:00:00:00
02:00:00:00:00:00:00:00
00:00:00:00:00:00:00:00
'''