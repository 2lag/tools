import requests
import time
import colorama
from colorama import Fore

'''INPUT USERNAME TO SEARCH'''
username = input('[+] Enter desired username: ')

# ------------------------SITE LIST----------------------------
aboutme = f'https://about.me/{username}'
angellist = f'https://angel.co/{username}'
badoo = f'https://www.badoo.com/en/{username}'
bandcamp = f'https://www.bandcamp.com/{username}'
basecamp = f'https://{username}.basecamphq.com/login'
behance = f'https://www.behance.net/{username}'
blipfm = f'https://blip.fm/{username}'
blogger = f'https://{username}.blogspot.com'
bitbucket = f'https://bitbucket.org/{username}'
buzzfeed = f'https://buzzfeed.com/{username}'
canva = f'https://www.canva.com/{username}'
cashme = f'https://cash.me/{username}'
codecademy = f'https://www.codecademy.com/{username}'
codementor = f'https://www.codementor.io/{username}'
colourlovers = f'https://www.colourlovers.com/love/{username}'
contently = f'https://{username}.contently.com'
creative_market = f'https://creativemarket.com/{username}'
dailymotion = f'https://www.dailymotion.com/{username}'
deviantart = f'https://{username}.deviantart.com'
disqus = f'https://disqus.com/by/{username}'
dribbble = f'https://dribbble.com/{username}'
ebay = f'https://www.ebay.com/usr/{username}'
ello = f'https://ello.co/{username}'
etsy = f'https://www.etsy.com/shop/{username}'
facebook = f'https://www.facebook.com/{username}'
five_hundred_px = f'https://500px.com/{username}'
flickr = f'https://www.flickr.com/people/{username}'
fotolog = f'https://fotolog.com/{username}'
foursquare = f'https://foursquare.com/{username}'
github = f'https://www.github.com/{username}'
goodreads = f'https://www.goodreads.com/{username}'
google_plus = f'https://plus.google.com/s/{username}/top'
gravatar = f'https://en.gravatar.com/{username}'
gumroad = f'https://www.gumroad.com/{username}'
hackernews = f'https://news.ycombinator.com/user?id={username}'
houzz = f'https://houzz.com/user/{username}'
hubpages = f'https://{username}.hubpages.com'
ifttt = f'https://www.ifttt.com/p/{username}'
imgur = f'https://imgur.com/user/{username}'
instagram = f'https://www.instagram.com/{username}'
instructables = f'https://www.instructables.com/member/{username}'
keybase = f'https://keybase.io/{username}'
kongregate = f'https://kongregate.com/accounts/{username}'
last_fm = f'https://last.fm/user/{username}'
livejournal = f'https://{username}.livejournal.com'
medium = f'https://medium.com/@{username}'
mixcloud = f'https://www.mixcloud.com/{username}'
newsground = f'https://{username}.newgrounds.com'
ogusers = f'https://flipd.gg/{username}'
okcupid = f'https://www.okcupid.com/profile/{username}'
pastebin = f'https://pastebin.com/u/{username}'
patreon = f'https://www.patreon.com/{username}'
pinterest = f'https://www.pinterest.com/{username}'
reddit = f'https://www.reddit.com/user/{username}'
reverb_nation = f'https://www.reverbnation.com/{username}'
roblox = f'https://www.roblox.com/user.aspx?username={username}'
scribd = f'https://www.scribd.com/{username}'
slack = f'https://{username}.slack.com'
slideshare = f'https://slideshare.net/{username}'
soundcloud = f'https://soundcloud.com/{username}'
spotify = f'https://open.spotify.com/user/{username}'
steam = f'https://steamcommunity.com/id/{username}'
trakt = f'https://www.trakt.tv/users/{username}'
trip = f'https://www.trip.skyscanner.com/user/{username}'
tumblr = f'https://{username}.tumblr.com'
twitter = f'https://www.twitter.com/{username}'
wattpad = f'https://www.wattpad.com/user/{username}'
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'
wordpress = f'https://{username}.wordpress.com'
vimeo = f'https://vimeo.com/{username}'
vk = f'https://vk.com/{username}'
youtube = f'https://www.youtube.com/{username}'
youtube2 = f'https://www.youtube.com/c/{username}'
youtube3 = f'https://www.youtube.com/@{username}'

WEBSITES = [
  aboutme, angellist, badoo, bandcamp, basecamp, behance, blipfm, blogger,
  bitbucket, buzzfeed, canva, cashme, codecademy, codementor, colourlovers,
  contently, creative_market, dailymotion, deviantart, disqus, dribbble, ebay,
  ello, etsy, facebook, five_hundred_px, flickr, fotolog, foursquare, github,
  goodreads, google_plus, gravatar, gumroad, hackernews, houzz, hubpages,
  ifttt, imgur, instagram, instructables, keybase, kongregate, last_fm,
  livejournal, medium, mixcloud, newsground, ogusers, okcupid, pastebin,
  patreon, pinterest, reddit, reverb_nation, roblox, scribd, slack,
  slideshare, soundcloud, spotify, steam, trakt, trip, tumblr, twitter,
  wattpad, wikipedia, wordpress, vimeo, vk, youtube, youtube2, youtube3
]

def banner():
	print(Fore.RED + '''
  _   
 | |  __   
 | | / /        ____________   
 | |/ / | | | |/      /  _  \   
 |  _ \ | |_| |\ ----/  (_)  \   
 |_| \ \|     |/\--- \       /   
      \ \-----/______/\_____/   
       \/   
  _              _    _   
 | |            | |  (_)   
 | |  ___   ___ | | ___ _ __   __ _   
 | | /   \ /   \| |/ / | '_ \ / _` |   
 | || Ꙩ   | Ꙩ  |   /| | | | | (_|  |   
 |_| \___/ \___/|_|\_\_|_| |_|\__, |   
                               __/ |   
                              |___/   
   _____ _                          __    
  / ____| |                        /_ |   
 | |  __| | __ _ ___ ___    __   __ | |   
 | | |_ | |/ _` / __/ __|   \ \ / / | |   
 | |__| | | (_| \__ \__ \    \ V /  | |   
  \_____|_|\__,_|___/___/     \_/   |_| by: oyasumi & day   
  
''')
# -------------------------------------------------------------
def search():
	print(Fore.WHITE + f'[+] Searching for username:{username}')
	time.sleep(0.25)
	print('.......')
	time.sleep(0.25)
	print('.......\n')
	time.sleep(0.25)
	
	
	print(Fore.GREEN + '[+] Looking-Glass is working\n')
	time.sleep(0.25)
	print('.......')
	time.sleep(0.25)
	print('.......\n')
	time.sleep(0.25)
	
	
	count = 0
	for url in WEBSITES:
		r = requests.get(url)
		print(Fore.YELLOW + f'\n{url} ::: {r.status_code}')
		if username in r.text:
			print(Fore.GREEN + '[+] account detected')
			count += 1
		else:
			print(Fore.RED + '[-] account undetected')
	total = len(WEBSITES)			
	print(Fore.WHITE + f'done: found a total of {count} matches found out of {total} websites.')
# -------------------------------------------------------------
if __name__ =='__main__':
	colorama.init()
	banner()
	search()
