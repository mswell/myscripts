import sys

subdomain = sys.argv[1]

open_redirect = [
    "go=",
    "return=",
    "r_url=",
    "returnUrl=",
    "returnUri=",
    "locationUrl=",
    "goTo=",
    "return_url=",
    "return_uri=",
    "ref=",
    "referrer=",
    "backUrl=",
    "returnTo=",
    "successUrl=",
]


for dork in open_redirect:
    google_url = f"https://www.google.com/search?q=site%3A{subdomain}+inurl%3A{dork}"
    print(google_url)
    
    
    
