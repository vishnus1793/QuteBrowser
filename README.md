# Qutebrowser Configuration

This is a customized configuration file for [qutebrowser](https://qutebrowser.org/). It includes search engine settings, UI themes, keybindings, and privacy features.

## Features

- **Custom Search Engines**
  - Google (default)
  - DuckDuckGo (`ddg`)
  - Bing (`b`)
  - YouTube (`yt`)
  - GitHub (`gh`, `gs` for GitHub search)
  - Wikipedia (`wp`)
  - Instagram (`in`)
  - LinkedIn (`li`)
  - Hianime (`an`)

- **Privacy Enhancements**
  - Enables ad-blocking with EasyList and EasyPrivacy
  - JavaScript enabled
  - Custom User-Agent string for better compatibility

- **UI Customization**
  - Dracula theme for consistent dark mode experience
  - Dark mode enabled for all web pages
  - Custom font size set to `12pt`
  - Tab bar and status bar color themes

- **Keybindings**
  - `1`: Switch to the previous tab
  - `2`: Switch to the next tab
  - `<Alt-Left>`: Go back in history
  - `<Alt-F3>`: Toggle tab bar visibility (never/always)
  - `<Alt-F1>`: Toggle tab bar visibility (always/never)

- **Startup Settings**
  - Start page set to Google
  - Tabs are always shown on startup

## Installation
1. Copy the configuration into your `qutebrowser` config file:
   ```sh
   mkdir -p ~/.config/qutebrowser
   nano ~/.config/qutebrowser/config.py
   ```
2. Paste the content and save the file.
3. Restart `qutebrowser` for changes to take effect.





