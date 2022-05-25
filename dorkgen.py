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


print('Dorks for Open Redirect')
for dork in open_redirect:
    google_url = f"https://www.google.com/search?q=site%3A{subdomain}+inurl%3A{dork}"
    print(google_url)

print("\nDorks to login page\n")
login_page = f"https://www.google.com/search?q=site:{subdomain}+inurl:login+%7C+inurl:signin+%7C+intitle:Login+%7C+intitle:%22sign+in%22+%7C+inurl:auth"
print(login_page)
    
    
