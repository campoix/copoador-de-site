import requests
from bs4 import BeautifulSoup
import re

def get_page_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching page: {e}")
        return None

def extract_css_js(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    css_links = [link.get('href') for link in soup.find_all('link', rel='stylesheet')]
    js_scripts = [script.get('src') for script in soup.find_all('script', src=True)]
    return css_links, js_scripts

def save_content(content, filename):
    with open(filename, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    url = "https://www.apple.com/"
    html_content = get_page_content(url)
    
    if html_content:
        css_links, js_scripts = extract_css_js(html_content)
        
        # Save HTML content
        save_content(html_content, "cloned_page.html")
        
        # Save CSS and JavaScript files
        for i, css_link in enumerate(css_links):
            css_content = get_page_content(css_link)
            if css_content:
                save_content(css_content, f"style_{i}.css")
        
        for j, js_script in enumerate(js_scripts):
            js_content = get_page_content(js_script)
            if js_content:
                save_content(js_content, f"script_{j}.js")
