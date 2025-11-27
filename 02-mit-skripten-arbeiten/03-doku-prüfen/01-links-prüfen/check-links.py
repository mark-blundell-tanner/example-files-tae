import re
import requests
from pathlib import Path

def extract_https_links(markdown_content):
    """Extract all HTTPS links from markdown content."""
    # Pattern to match markdown links [text](https://...)
    pattern = r'\[([^\]]+)\]\((https://[^\)]+)\)'
    matches = re.findall(pattern, markdown_content)
    return matches

def check_link(url):
    """Check if a URL returns a 404 error."""
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        # If HEAD doesn't work, try GET
        if response.status_code == 405:
            response = requests.get(url, timeout=5, allow_redirects=True)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def check_markdown_file(filepath):
    """Check all HTTPS links in a markdown file."""
    print(f"Checking links in: {filepath}\n")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = extract_https_links(content)
    
    if not links:
        print("No HTTPS links found in the file.")
        return
    
    broken_links = []
    working_links = []
    
    for text, url in links:
        status = check_link(url)
        
        if status == 404:
            print(f"❌ 404 - [{text}]({url})")
            broken_links.append((text, url))
        elif isinstance(status, str) and status.startswith("Error"):
            print(f"⚠️  {status} - [{text}]({url})")
            broken_links.append((text, url))
        elif status == 200:
            print(f"✅ {status} - [{text}]({url})")
            working_links.append((text, url))
        else:
            print(f"ℹ️  {status} - [{text}]({url})")
            working_links.append((text, url))
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Working links: {len(working_links)}")
    print(f"  Broken links (404 or errors): {len(broken_links)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    # Check all markdown files in the current directory
    md_files = list(Path('.').glob('*.md'))
    
    if not md_files:
        print("No markdown files found in the current directory.")
    else:
        for md_file in md_files:
            check_markdown_file(md_file)
            print("\n")
