#!/usr/bin/env python
# coding:utf-8
import os
import sys
import subprocess
			 
if (1 == len(sys.argv)):
	print("Miss pcap file...")
	sys.exit(0)

filename	= sys.argv[1]

pcap_tools	= [("strings -a", "> result_strings.txt"),
			   ("strings -a", "| grep -i 'flag' > result_flag.txt"),
			   ("strings -a", "| grep -i 'ctf' > result_ctf.txt"),
			   ("strings -a", "| grep -i 'f.*l.*a.*g' > result_f#l#a#g.txt"),
			   ("strings -a", "| grep -i 'c.*t.*f' > result_c#t#f.txt"),
			   ("strings -a", "| grep -i '{.*}' > result_{#}.txt"),
			   ("strings -a", "| grep 'GET' > result_GET.txt"),
			   ("strings -a", "| grep 'POST' > result_POST.txt"),
			   ("remove0x00", ""),
			   ("cat result_remove0x00.txt", "| grep -i 'flag' > result_remove0x00_flag.txt"),
			   ("cat result_remove0x00.txt", "| grep -i 'ctf' > result_remove0x00_ctf.txt"),
			   ("cat result_remove0x00.txt", "| grep -i 'f.*l.*a.*g' > result_remove0x00_f#l#a#g.txt"),
			   ("cat result_remove0x00.txt", "| grep -i 'c.*t.*f' > result_remove0x00_c#t#f.txt"),
			   ("cat result_remove0x00.txt", "| grep -i '{.*}' > result_remove0x00_{#}.txt"),
			   ("tshark -r", "-T fields -e tcp.urgent_pointer | egrep -vi '^0$' | tr '\n' ' ' > result_tshark_urgp.txt"),
			   ("tshark -r", "-T fields -e dns.qry.name > result_tshark_dns.txt"),
			   ("tshark -r", "-T fields -e data > result_tshark_data.txt"),
			   ("foremost", "> result_foremost.txt"),
			   ("binwalk -e", "> result_binwalk.txt"),
			   ("python keyboard1.py", "> result_keyboard1.txt"),
			   ("python keyboard2.py", "> result_keyboard2.txt"),
			   ("python mice.py", "LEFT"),
			   ("python mice.py", "RIGHT"),
			   ("python mice.py", "MOVE"),
			   ("python mice.py", "ALL")]

for i in range(0, len(pcap_tools)):
	cmd = pcap_tools[i][0] + " " + filename + " " + pcap_tools[i][1]
	print(cmd)
	result = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	result.wait()
	lines = result.stdout.readlines()
	for line in lines:
		print("%s" % line)
'''
os.system("python mice.py %s LEFT" % filename)
os.system("python mice.py %s RIGHT" % filename)
os.system("python mice.py %s MOVE" % filename)
os.system("python mice.py %s ALL" % filename)
'''
