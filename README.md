# arp-table-monitor
Monitoring ARP Table Changes - For Linux

Can be described as ##**“ARP Table Monitoring Tool”**##

Implemented for Linux Systems

Written in Python3

Monitors the ARP Table Changes Every 10seconds 

Outputs:

&emsp;&emsp;Terminal

&emsp;&emsp;Text file Report Generation with Timestamps

The output text file may be valuable when Forensics Analysis takes place.



Prerequisites:

Python3 Installed



Usage:

On a **Linux System**, where python3 is installed, open terminal and execute the command:

	python3 arp_monitor arp.txt

This command executes the python3 arp_monitor.py script and then generates a report to a newly created file which name is "arp.txt" .

Let's see a screenshot of it's syntax:

![arp_monitor - Copy](https://github.com/GreekSploit/arp-table-monitor/assets/137961015/98386872-c560-4504-82b0-b098b01a0f07)

Imporovements of the project would be:
1. The creation of a csv file containing the timestamp of the attack and arp table entries which were presented and the ones that were changed, in order to be analyzed easier from other tools.
2. To run the script as background process.
3. To create a Windows System version of arp_monitor arp.txt.
4. To develop one or more ARP Poisoning Defensive Mechanisms.
5. To add "smarter" features on it. For example, AI could be used for recognizing with better accuracy if other Patterns of Network Threats exist.
6. To make it a plugin for other programs/tools.


Copyright (c) 2023 GreekSploit, under MIT Licence
   
