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

# Enable JavaScript
c.content.javascript.enabled = True

# Set a custom user agent
c.content.headers.user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Change the default font size
c.fonts.default_size = "12pt"

# Enable dark mode for web pages
config.set("colors.webpage.darkmode.enabled", True)

# Dracula Theme Colors

# Colors for the completion widget
c.colors.completion.fg = "#f8f8f2"
c.colors.completion.category.bg = "#282a36"
c.colors.completion.category.fg = "#ff79c6"
c.colors.completion.item.selected.bg = "#44475a"
c.colors.completion.item.selected.fg = "#f8f8f2"
c.colors.completion.item.selected.match.fg = "#50fa7b"
c.colors.completion.match.fg = "#50fa7b"
c.colors.completion.scrollbar.bg = "#282a36"
c.colors.completion.scrollbar.fg = "#f8f8f2"

# Colors for the status bar
c.colors.statusbar.normal.bg = "#282a36"
c.colors.statusbar.normal.fg = "#f8f8f2"
c.colors.statusbar.insert.bg = "#50fa7b"
c.colors.statusbar.insert.fg = "#282a36"
c.colors.statusbar.command.bg = "#44475a"
c.colors.statusbar.command.fg = "#f8f8f2"
c.colors.statusbar.passthrough.bg = "#ffb86c"
c.colors.statusbar.passthrough.fg = "#282a36"

# Colors for the tab bar
c.colors.tabs.bar.bg = "#282a36"
c.colors.tabs.odd.bg = "#44475a"
c.colors.tabs.even.bg = "#282a36"
c.colors.tabs.odd.fg = "#f8f8f2"
c.colors.tabs.even.fg = "#f8f8f2"
c.colors.tabs.selected.odd.bg = "#50fa7b"
c.colors.tabs.selected.even.bg = "#50fa7b"
c.colors.tabs.selected.odd.fg = "#282a36"
c.colors.tabs.selected.even.fg = "#282a36"

# Set background color for webpages if no specific styling is set
c.colors.webpage.bg = "#282a36"

# Keybindings
config.bind('1', 'tab-prev')
config.bind('2', 'tab-next')
config.bind('<Alt-Left>', 'back')
# Zoom in with Space + L
config.bind('<Space>l', 'zoom-in')

# Zoom out with Space + K
config.bind('<Space>k', 'zoom-out')
# Set tabs to always show on startup
config.set("tabs.show", "always")

# Bind Alt+F3 to show the tab bar
config.bind("<Alt-F3>", "config-cycle tabs.show never always")

# Bind Alt+F1 to hide the tab bar
config.bind("<Alt-F1>", "config-cycle tabs.show always never")
