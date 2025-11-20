import pyshorteners

# Create a Shortener object
s = pyshorteners.Shortener()

# Original URL
url = "https://sandesh.page.gd"

# Shorten the URL using TinyURL
short_url = s.tinyurl.short(url)

print("Shortened URL:", short_url)
