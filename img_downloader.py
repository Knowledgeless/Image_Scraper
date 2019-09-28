
import requests
import bs4 as bs
import urllib.request


print('''
    	88 8b    d8    db     dP""b8 888888                 
    	88 88b  d88   dPYb   dP   `" 88__                   
    	88 88YbdP88  dP__Yb  Yb  "88 88""                   
    	88 88 YY 88 dP""""Yb  YboodP 888888                 
                                                    
                                                           
.dP"Y8  dP""b8 88""Yb    db    88""Yb 888888 88""Yb 
`Ybo." dP   `" 88__dP   dPYb   88__dP 88__   88__dP 
o.`Y8b Yb      88"Yb   dP__Yb  88"""  88""   88"Yb  
8bodP'  YboodP 88  Yb dP""""Yb 88     888888 88  Yb
''')

print("""

-------------------------------------------------------------------------
	          Download All Images Using This Script\n
	For Few Website It May Not Work I Will Debug This Soon :)
-------------------------------------------------------------------------

1 => Help
2 => Use Script

	""")

u = int(input("Your Input: "))


if u == 1:
	print('''
		\t -------------
		\t| Information |
		\t -------------
	[+] To use this script you have to press (1). 
	[+] After that you have to enter the correct url of your website to 
		download all imagesfrom there.
	[+] Just it. ;)

		''')

elif u == 2:

	r = input("Your url: ")
	response = requests.get(r).text

	s = bs.BeautifulSoup(response, 'html.parser')

	imgs = s.find_all('img')

	links = []

	for img in imgs:
		link =  img.get('src')
		if 'http://' not in link:
		 	link = r + link
		links.append(link)

	print("Images Detected: " + str(len(links)))

	for i in range(len(links)):
		filename = 'img{}.png'.format(i)
		urllib.request.urlretrieve(links[i], filename)
		print('Done!')

else:
	print("Incorrect input")
