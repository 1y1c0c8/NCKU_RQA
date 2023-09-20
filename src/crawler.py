from bs4 import BeautifulSoup
import requests

home_page = "https://www.cc.ncku.edu.tw/rule/index.php"
rules_prefix = "https://www.cc.ncku.edu.tw/rule/"

response = requests.get(home_page, verify=False)
# soup = BeautifulSoup(response.text, "html.parser")

if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Now, you can use BeautifulSoup to extract data from the HTML
    # For example, let's find all the links on the page
    links = soup.find_all('a')
    
    # Process and print the links
    rule_links = []
    file_path = "../data/links.txt"
    with open(file_path, 'w') as file:
        for link in links[39:-2]:
            if link.get('href') is not None and link.get('href') is not '#':
                complete_link = rules_prefix + link.get('href')
                file.write(complete_link + '\n')
                rule_links.append(complete_link)
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
