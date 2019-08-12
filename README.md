# Intro

A simple Python program that may be used as a service for Linux and Windows to get your external (public) IP and send it to yourself. Use at your own risk as password parameter for the email account being used has to be passed in unencrypted. The following is a printout of the help.

```
usage: IP Locator [-h] [-u URL] [-m MAX] [-s SLEEP] -e EMAIL -p PASSWORD
                  [--version]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     the URL of the site to get your external IP (default: https://myexternalip.com/raw)
                            Other sites that may work.
                                - https://www.ipchicken.com
                                - https://myexternalip.com/raw
                            
  -m MAX, --max MAX     maximum emails; set to -1 for indefinite (default: -1)
  -s SLEEP, --sleep SLEEP
                        seconds between checking/sending IP in email (default: 3600)
  -e EMAIL, --email EMAIL
                        gmail email address
  -p PASSWORD, --password PASSWORD
                        gmail email password
  --version             show program's version number and exit

One-Off Coder, http://www.oneoffcoder.com
```

Note that only the email `-e` and password `-p` are required, and that this program has only been tested against a `gmail` account. A quick and dirty example of using this program is as follows (of course, substitute the email and password values with your own).

```bash
python ip.py -e alan.turing@gmail.com -p codebreaker
```

# Installation

## CentOS Linux

```bash
# copy python file
sudo cp ip.py /usr/bin
sudo chmod 600 /usr/bin/ip.py

# copy service file
# make sure you modify ExecStart with the appropriate email and password
# make sure the path to python is absolute e.g. /home/super/anaconda3/bin/python
sudo cp pyip.service /lib/systemd/system
sudo nano /lib/systemd/system/pyip.service
sudo chmod 600 /lib/systemd/system/pyip.service 

# to enable, start, stop, etc.. the service
sudo systemctl daemon-reload
sudo systemctl enable pyip.service
sudo systemctl start pyip.service
sudo systemctl status pyip.service
sudo systemctl stop pyip.service
sudo systemctl restart pyip.service
```

## Windows

On Windows, use the [sc command](https://docs.microsoft.com/en-us/windows/win32/services/controlling-a-service-using-sc).

```bash
sc create PyIP binPath="C:\ProgramData\Anaconda3\python.exe C:\dev\ip.py -e alan.turing@gmail.com -p codebreaker"
sc start PyIP
sc delete PyIP
```

# References

* https://tecadmin.net/setup-autorun-python-script-using-systemd/
* https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/sc-create
* https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/sc-delete
* https://datatofish.com/python-script-windows-scheduler/
* https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units
* https://askubuntu.com/questions/814174/cannot-make-a-systemd-script-run

# Citation

```
@misc{oneoffcoder_ip_locator_2019, 
title={External IP locator using Python for Linux and Windows}, 
url={https://github.com/oneoffcoder/pyip}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Aug}}
```

# Copyright Stuff

```
Copyright 2019 One-Off Coder

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
