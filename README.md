# URL Looper

This project is a tool for automating the process of visiting a series of URLs. It supports both dynamically generated URLs based on a specified pattern and a fixed list of URLs. The tool uses Selenium WebDriver to open URLs in a browser and navigate through them at a specified interval.

## Features

- **Dynamic URL Generation**: Automatically generates URLs based on a pattern with alphabetic and numeric combinations.
- **Static URL List**: Use a predefined list of URLs for the loop.
- **Customizable Delay**: Set the delay between opening URLs.
- **Incognito Mode**: Option to open URLs in incognito mode.
- **Chrome Browser Integration**: Uses Selenium WebDriver with Chrome to navigate through URLs.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Set Up Venv**
    ```bash
     python -m venv venv
     venv\Scripts\activate
3. **Install Dependencies**
    ```bash
      pip install -r requirements.txt
      pip install webdriver-manager

If every thing done correctly, when you run program a new tab will open and all the urls start to load one after another in same tab 

***IT IS BASICALLY SLIDESHOW FOR URLS :)***




