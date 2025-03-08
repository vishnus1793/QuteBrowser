# Load settings from autoconfig.yml if available
config.load_autoconfig()

# Set default search engines
c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
    "ddg": "https://duckduckgo.com/?q={}",
    "b": "https://www.bing.com/search?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
    "gh": "https://github.com/{}",
    "gs": "https://github.com/search?q={}",
    "wp": "https://en.wikipedia.org/wiki/{}",
    "in": "https://www.instagram.com/{}",
    "li": "https://www.linkedin.com/search/results/all/?keywords={}",
    "an": "https://hianime.sx/search?keyword={}"
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

# Enable dark mode for web pages
config.set("colors.webpage.darkmode.enabled", True)

# Colors for the completion widget
c.colors.completion.fg = "#ffffff"
c.colors.completion.category.bg = "#222222"
c.colors.completion.category.fg = "#ffffff"
c.colors.completion.item.selected.bg = "#555555"
c.colors.completion.item.selected.fg = "#ffffff"
c.colors.completion.item.selected.match.fg = "#ffcc00"
c.colors.completion.match.fg = "#ffcc00"
c.colors.completion.scrollbar.bg = "#333333"
c.colors.completion.scrollbar.fg = "#ffffff"

# Colors for the status bar
c.colors.statusbar.normal.bg = "#222222"
c.colors.statusbar.normal.fg = "#ffffff"
c.colors.statusbar.insert.bg = "#005f87"
c.colors.statusbar.insert.fg = "#ffffff"
c.colors.statusbar.passthrough.bg = "#8700af"
c.colors.statusbar.passthrough.fg = "#ffffff"
c.colors.statusbar.command.bg = "#333333"
c.colors.statusbar.command.fg = "#ffffff"

# Colors for the tab bar
c.colors.tabs.bar.bg = "#111111"
c.colors.tabs.odd.bg = "#222222"
c.colors.tabs.even.bg = "#333333"
c.colors.tabs.odd.fg = "#ffffff"
c.colors.tabs.even.fg = "#ffffff"
c.colors.tabs.selected.odd.bg = "#444444"
c.colors.tabs.selected.even.bg = "#555555"
c.colors.tabs.selected.odd.fg = "#ffffff"
c.colors.tabs.selected.even.fg = "#ffffff"

# Set background color for webpages if no specific styling is set
c.colors.webpage.bg = "#1e1e1e"
config.bind('1', 'tab-prev')
config.bind('2', 'tab-next')
config.bind('<Alt-Left>', 'back')
#config.bind('<XF86Launch1>', 'fake-key <Escape>')

# Set tabs to always show on startup
config.set("tabs.show", "always")

# Bind Alt+F3 to show the tab bar
config.bind("<Alt-F3>", "config-cycle tabs.show never always")

# Bind Alt+F1 to hide the tab bar
config.bind("<Alt-F1>", "config-cycle tabs.show always never")
