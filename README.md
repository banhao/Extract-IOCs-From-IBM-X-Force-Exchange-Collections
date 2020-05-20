Extract_IOCs_From_IBM_XForce_Exchange_Collections.py is used to grab the IOCs from IBM X-Force Exchange Collections.
You don't need IBM X-Force API and the script will auto skip the login screen.

How to use it:
If you want to get all the IOCs from one IBM X-Force Exchange Collection web page, so just run the command like following:

	python3 Extract_IOCs_From_IBM_XForce_Exchange_Collections.py https://exchange.xforce.ibmcloud.com/collection/Mirai-and-Hoaxcalls-Botnets-Target-Legacy-Symantec-Web-Gateways-5a72685d9ca610f6cbaab4d3acacfe91
	
Example result IBM_X_Force_Collections.list was uploaded.

This can be run in Windows or Linux(haven't tested). but don't use the 'root' to run the script in Linux, because seems in Linux you can't use 'root' account to open a browser.

Please install the "selenium" first.
	
	https://pypi.org/project/selenium/

And you also need to download the browser drivers
	
	https://selenium-python.readthedocs.io/installation.html#drivers

Test results:

	OS			|	Window10	|	Linux
	Python3 + FireFox	|	passed		|	haven't tested
	Python3 + Chrome	|	passed		|	haven't tested 
------------------------------------------------------------------------

I didn't test in IE and Edge, because I rarely use that 2 browers.
	
Notice: If you run the Python script in Windows, the end line is CRLF, you need use dos2unix to change it to UNIX format before you start the next steps in Linux.
