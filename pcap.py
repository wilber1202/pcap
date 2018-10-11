import sys
import subprocess
import os
			 
if (1==len(sys.argv)):
	print("Miss pcap file...")
	sys.exit(0)
	
filename=sys.argv[1]

pcap_tools=[("strings -a", "> result_strings.txt"),
						("strings -a", "| grep -i 'flag' > result_flag.txt"),
						("strings -a", "| grep -i 'f.*l.*a.*g' > result_f#l#a#g.txt"),
						("strings -a", "| grep -i '{.*}' > result_{#}.txt"),
						("strings -a", "| grep 'GET' > result_get.txt"),
						("strings -a", "| grep 'POST' > result_POST.txt"),
						("foremost", "> result_foremost.txt"),
						("binwalk -e", "> result_binwalk.txt")]
	
for i in range(0, len(pcap_tools)):
	cmd = pcap_tools[i][0] + " " + filename + " " + pcap_tools[i][1]
	print(cmd)
	result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	result.wait()
	lines = result.stdout.readlines()
	for line in lines:
		print("%s" % line)