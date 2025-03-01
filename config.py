# Load settings from autoconfig.yml if available
config.load_autoconfig()

# Set default search engines
c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
    "ddg": "https://duckduckgo.com/?q={}",
    "b": "https://www.bing.com/search?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
    "gh": "https://github.com/search?q={}",
    "wp": "https://en.wikipedia.org/wiki/{}"
}

# Set start page
c.url.start_pages = ["https://www.google.com"]

# Enable ad blocking
c.content.blocking.method = "both"
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt"
]

# Enable JavaScript (optional)
c.content.javascript.enabled = True

# Set a custom user agent (optional)
c.content.headers.user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Change the default font size (optional)
c.fonts.default_size = "12pt"
