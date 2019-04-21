#!/usr/bin/python3

# Import the necessary package to process data in JSON format
import configparser
import argparse
import datetime # pour logger
import json
import requests


def init(config_file_name):
	config=configparser.ConfigParser()
	config.read(config_file_name)
	PASSWORD = config['DNS']['PASSWORD']
	#HOST = config['DNS']['HOST']
	HOSTLIST = json.loads(config['DNS']['HOSTLIST'])
	DOMAIN_NAME = config['DNS']['DOMAIN_NAME']
	return(PASSWORD,HOSTLIST,DOMAIN_NAME)

def init_log(config_file_name):
	config=configparser.ConfigParser()
	config.read(config_file_name)
	log_filename = config['LOG']['FILENAME']
	return(log_filename)

def log_result(log_filename,result,host):
	outfile = open(log_filename, "a")
	if(result):
		outfile.write('## updated : '+host+' : '+str(datetime.date.today())+'\n')
		print('success')
	else:
		outfile.write('##  ERROR :  '+host+' : '+str(datetime.date.today())+'\n')
		print('error')
	outfile.close()

def update_dns(password,host,domain_name):
	query = 'https://dynamicdns.park-your-domain.com/update?host='+str(host)+'&domain='+domain_name+'&password='+password
	r = requests.get(query)
	print(r.text)
	return '<ErrCount>0</ErrCount>' in r.text
	



#-------------------------------------------------------------------------------------------------------------
# MAIN PROCESS
#-------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
	# Instantiate the parser
	parser = argparse.ArgumentParser(description='python script to update namecheap Dynamic DNS')
	parser.add_argument('--config', required=True, help='required INI config file with Domain credentials')
	parser.add_argument('-l', action='store_true', help='logs update result')
	args = parser.parse_args()

	print('using config file : '+str(args.config))
	(password, hostlist, domain_name) = init(args.config)
	log_filename=''
	if(args.l):
		log_filename = init_log(args.config)

	for host in hostlist :
		result = update_dns(password, host, domain_name)
		if(args.l):
			log_result(log_filename, result, host)


