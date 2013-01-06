 # -*- coding: utf-8 -*- в
from __future__ import unicode_literals
import requests,json, webbrowser
from requests_oauthlib import OAuth1
from pprint import pprint

client_key=''
client_secret=''


oauth = OAuth1(client_key, client_secret=client_secret)
request_token_url = 'https://api.twitter.com/oauth/request_token'
r = requests.get(url=request_token_url, auth=oauth)


from urlparse import parse_qs
credentials = parse_qs(r.content)
resource_owner_key = unicode(credentials['oauth_token'][0])
resource_owner_secret = unicode(credentials['oauth_token_secret'][0])


authorize_url = 'https://api.twitter.com/oauth/authorize?oauth_token=' + resource_owner_key
print 'Please authorize you: ' + authorize_url
verifier = unicode(raw_input('Verifier:'))


oauth = OAuth1(client_key,client_secret=client_secret,resource_owner_key=resource_owner_key,resource_owner_secret=resource_owner_secret,verifier=verifier)
r = requests.get('https://api.twitter.com/oauth/access_token', auth=oauth)
credentials = parse_qs(r.content)
resource_owner_key = unicode(credentials['oauth_token'][0])
resource_owner_secret = unicode(credentials['oauth_token_secret'][0])

#--------------------------------------

url_for_search = unicode('https://api.twitter.com/1.1/search/tweets.json?q=justin_bieber&count=100')
oauth = OAuth1(client_key, client_secret=client_secret, resource_owner_key=resource_owner_key,resource_owner_secret=resource_owner_secret, verifier=verifier)
list_of=[]
while True:
  r = requests.get(url=url_for_search, auth=oauth)
	dict1 = r.json()
	for tweets in dict1['statuses']: 
		# print tweets['text']
  
  # Retweet example.
	# url_for_retweet = 'https://api.twitter.com/1.1/statuses/retweet/%s.json' %(tweets['id'])
	# r = requests.post(url=url_for_retweet, auth=oauth)
