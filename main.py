#Dork Script for google code-in 
#By FajarTheGGman

# some package
import urllib3 as url
from bs4 import BeautifulSoup

class GCIDork:
    def banner():
	    print("[---- GCI-Dork By FajarTheGGman ----]\n")
	
	
    def main():
        req = url.PoolManager()
	    # user input
        user = str(input("[Dork] >_ "))
        page = str(input("[Page] >_ "))
        print("[+] Here's The Results")
	    # Send Request to search engine
        send = req.request("GET", "http://www1.search-results.com/web?q=" + user + "&page=" + page)
	    # Parsing The Result
        parsing = BeautifulSoup(send.data, features="html.parser")
        for data in parsing.find_all("cite"):
            print(data.string)
 

x = GCIDork
x.banner()
x.main()