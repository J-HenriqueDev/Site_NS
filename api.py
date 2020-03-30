# -*- coding: utf-8 -*-

import auth
import requests

# Endpoint
BASEAPI = "https://discordapp.com/api/v6"

def _getheaders(token):
	return {
	'Authorization': 'Bearer {}'.format(token)
	}

def exchange_code(code):
	data = {
		'client_id': auth.id,
		'client_secret': auth.secret,
		'grant_type': 'authorization_code',
		'code': code,
		'redirect_uri': auth.redirect,
		'scope': auth.scopes
	}
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded'
	}
	r = requests.post('{}/oauth2/token'.format(auth.baseapi), data, headers)
	r.raise_for_status()
	return r.json()


def codigo_troca(codigo):
	data = {
    'client_id': auth.id,
		'client_secret': auth.secret,
		'grant_type': 'authorization_code',
		'code': codigo,
		'redirect_uri': auth.redirect,
		'scope': auth.scopes
	        }
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	r = requests.post('{}/oauth2/token'.format(auth.baseapi), data, headers)
	r.raise_for_status()
	return r.json()


def get_info(token):
	headers = _getheaders(token)

	r = requests.get('{}/users/@me'.format(auth.baseapi), headers=headers)
	r.raise_for_status()
	return r.json()

def get_guilds(token):
	headers = _getheaders(token)

	r = requests.get('{}/users/@me/guilds'.format(auth.baseapi), headers=headers)
	r.raise_for_status()
	return r.json()

def get_connections(token):
	headers = _getheaders(token)

	r = requests.get('{}/users/@me/connections'.format(auth.baseapi), headers=headers)
	r.raise_for_status()
	return r.json()

def get_user(user):
  try:  
    TOKEN = "Bot NjgyMjgwMjAwNjk5OTA0MDkx.XoAbsA.kaPR7eoomZo_seniwLkDswHev8M"
    r = requests.get('https://discordapp.com/api/v6/users/{}'.format(user), headers={'Authorization': TOKEN})
    r.raise_for_status()
    return r.json()
  except Exception as e:
     return None	
    
    
def get_user_guild(user):
  try:  
    TOKEN = "Bot NjgyMjgwMjAwNjk5OTA0MDkx.XoAbsA.kaPR7eoomZo_seniwLkDswHev8M"
    r = requests.get('https://discordapp.com/api/v6/guilds/570906068277002271/members/{}'.format(user), headers={'Authorization': TOKEN})
    r.raise_for_status()
    return r.json()
  except Exception as e:
     return None	  

def get_send(channel, content):
  try:  
    TOKEN = "Bot NjgyMjgwMjAwNjk5OTA0MDkx.XoAbsA.kaPR7eoomZo_seniwLkDswHev8M"
    requests.post('https://discordapp.com/api/v6/channels/{}/messages'.format(channel),headers={'Authorization': TOKEN},json= {"content":content})
  except Exception as e:
     return None	
def get_send_dm(channel, content):
  try:  
    TOKEN = "Bot NjgyMjgwMjAwNjk5OTA0MDkx.XoAbsA.kaPR7eoomZo_seniwLkDswHev8M"
    requests.post('https://discordapp.com/api/v6/channels/@me/{}/messages'.format(channel),headers={'Authorization': TOKEN},json= {"content":content})
  except Exception as e:
     return e	    
