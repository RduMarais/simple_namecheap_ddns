# Simple Dynamic DNS script for Namecheap

since Namecheap DNS doesn't provide any API or client other than windows, here is a very simple client.
Basically it does a simple GET request for each host.

## Usage

```
usage: ddns.py [-h] --config CONFIG [-l]

python script to update namecheap Dynamic DNS

optional arguments:
  -h, --help       show this help message and exit
  --config CONFIG  required INI config file with Domain credentials
  -l               logs update result, in a log file specified in the config file
```


## install

```
pip install configparser, argparse
git clone https://github.com/RduMarais/simple_namecheap_ddns.git
chmod +x simple_namecheap_ddns/ddns.py
```

## cron job

use this command to edit your cron tab
```
crontab -e
```
add the following line, with X being the time interval between 2 updates :
```
*/X * * * * ~/simple_namecheap_ddns/ddns.py --config ~/simple_namecheap_ddns/config.ini -l
```
