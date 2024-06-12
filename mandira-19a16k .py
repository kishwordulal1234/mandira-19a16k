import subprocess
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def fetch_all_urls(target_url):
    try:
        # Use getallurls tool to fetch all URLs from the website
        output = subprocess.check_output(['getallurls', target_url]).decode('utf-8')
        urls = output.splitlines()
        return urls
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error fetching URLs: {e}")
        return []

def fetch_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.RequestException as e:
        print(Fore.RED + f"Error fetching the URL: {e}")
        return None

def find_technologies(url):
    # Placeholder for technology detection
    return {}

def extract_urls(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    urls = set()

    # Extract URLs from various HTML elements
    for tag in soup.find_all(['a', 'link', 'script', 'img', 'source']):
        if tag.name in ['a', 'link']:
            href = tag.get('href')
        elif tag.name in ['script', 'img', 'source']:
            href = tag.get('src')
        else:
            continue

        if href:
            absolute_url = urljoin(base_url, href)
            urls.add(absolute_url)

    return urls

def categorize_urls(urls):
    images = []
    scripts = []
    styles = []
    others = []

    for url in urls:
        if url.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
            images.append(url)
        elif url.endswith('.js'):
            scripts.append(url)
        elif url.endswith('.css'):
            styles.append(url)
        else:
            others.append(url)

    return images, scripts, styles, others

def print_urls(images, scripts, styles, others):
    if images:
        print(Fore.GREEN + "[*] URLs containing images found")
        for img in images:
            print(Fore.MAGENTA + img)

    if scripts:
        print(Fore.GREEN + "[*] URLs containing JavaScript files found")
        for script in scripts:
            print(Fore.YELLOW + script)

    if styles:
        print(Fore.GREEN + "[*] URLs containing CSS files found")
        for style in styles:
            print(Fore.BLUE + style)

    if others:
        print(Fore.GREEN + "[*] Other URLs found")
        for other in others:
            print(Fore.WHITE + other)

def search_for_credentials(content):
    # Placeholder for searching credentials
    pass

def search_for_sensitive_urls(urls):
    # Placeholder for searching sensitive URLs
    pass

def search_for_configuration_data(content):
    # Placeholder for searching configuration data
    pass

def search_for_error_messages(content):
    # Placeholder for searching error messages
    pass

def search_for_personal_information(content):
    # Placeholder for searching personal information
    pass

def search_for_comments_and_metadata(content):
    # Placeholder for searching comments and metadata
    pass

def search_for_api_endpoints(content):
    # Placeholder for searching API endpoints
    pass

def search_for_security_vulnerabilities(content):
    # Placeholder for searching security vulnerabilities
    pass

def search_for_intellectual_property(content):
    # Placeholder for searching intellectual property
    pass

def search_for_hidden_directories(urls):
    # Placeholder for searching hidden directories
    pass

def search_in_javascript_files(urls):
    for url in urls:
        if url.endswith('.js'):
            try:
                response = requests.get(url)
                response.raise_for_status()
                javascript_content = response.text

                # Placeholder for searching leaked information in JavaScript files
                # You can implement the logic to search for specific patterns in the JavaScript content
                # Example: search_for_leaked_information(javascript_content)

            except requests.RequestException as e:
                print(Fore.RED + f"Error fetching JavaScript file at {url}: {e}")

def main():
    target_url = input("Enter the target website URL: ")
    
    print(Fore.GREEN + "\n[*] Fetching all URLs from the website...\n")
    all_urls = fetch_all_urls(target_url)
    if all_urls:
        print(Fore.GREEN + f"[*] Found {len(all_urls)} URLs.")

        print(Fore.GREEN + "\n[*] Checking what technologies are being used on the website...\n")
        tech_info = find_technologies(target_url)
        if tech_info:
            for tech, categories in tech_info.items():
                print(Fore.CYAN + f"{tech}:")
                for category in categories:
                    print(Fore.CYAN + f"  - {category}")

        print(Fore.GREEN + "\n[*] Looking for files on the website, please wait...\n")
        for url in all_urls:
            page_content = fetch_page(url)
            if page_content:
                urls = extract_urls(page_content, url)
                images, scripts, styles, others = categorize_urls(urls)
                print(Fore.YELLOW + f"\n[*] Analyzing {url}\n")
                print_urls(images, scripts, styles, others)

                # Perform additional analysis
                search_for_credentials(page_content)
                search_for_sensitive_urls(urls)
                search_for_configuration_data(page_content)
                search_for_error_messages(page_content)
                search_for_personal_information(page_content)
                search_for_comments_and_metadata(page_content)
                search_for_api_endpoints(page_content)
                search_for_security_vulnerabilities(page_content)
                search_for_intellectual_property(page_content)
                search_for_hidden_directories(urls)
                search_in_javascript_files(urls)
            else:
                print(Fore.RED + f"[*] Unable to fetch content from URL: {url}")
    else:
        print(Fore.RED + "No URLs found or unable to fetch the webpage.")

if __name__ == "__main__":
    main()

