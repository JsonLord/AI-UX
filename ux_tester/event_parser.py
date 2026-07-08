import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_events(html_content, base_url):
    """
    Extracts event data from an HTML string using BeautifulSoup.

    Args:
        html_content (str): The HTML content to parse.
        base_url (str): The base URL to resolve relative links.

    Returns:
        list: A list of dictionaries, each containing:
              title, date, time, price, venue, description, url
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    events = []

    # Identify potential event containers (e.g., elements with 'event' in their class name)
    all_potential = soup.find_all(['div', 'article', 'li', 'section'],
                                 class_=re.compile(r'event', re.I))

    # Filter to only keep the outermost containers
    event_containers = []
    for candidate in all_potential:
        if not any(parent in all_potential for parent in candidate.parents):
            event_containers.append(candidate)

    # Fallback: look for Schema.org Event markup if no 'event' classes found
    if not event_containers:
        all_potential = soup.find_all(itemtype=re.compile(r'schema\.org/Event', re.I))
        for candidate in all_potential:
            if not any(parent in all_potential for parent in candidate.parents):
                event_containers.append(candidate)

    # If still nothing, maybe try common list item patterns if they exist
    if not event_containers:
        # This is a very broad fallback, might get false positives
        # but for a "simple" parser, we try our best.
        all_potential = soup.find_all('article')
        for candidate in all_potential:
            if not any(parent in all_potential for parent in candidate.parents):
                event_containers.append(candidate)

    for container in event_containers:
        # 1. Title
        title_elem = container.find(class_=re.compile(r'title|name|heading', re.I)) or \
                     container.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'strong'])
        title = title_elem.get_text(strip=True) if title_elem else "N/A"

        # 2. Date
        date_elem = container.find(class_=re.compile(r'date|day|calendar', re.I)) or \
                    container.find('time', datetime=True) or \
                    container.find('time')
        date = date_elem.get_text(strip=True) if date_elem else "N/A"

        # 3. Time
        time_elem = container.find(class_=re.compile(r'time|hour|clock', re.I))
        time = time_elem.get_text(strip=True) if time_elem else "N/A"

        # 4. Price
        price_elem = container.find(class_=re.compile(r'price|cost|ticket|fee', re.I))
        price = price_elem.get_text(strip=True) if price_elem else "N/A"

        # 5. Venue
        venue_elem = container.find(class_=re.compile(r'venue|location|place|address', re.I))
        venue = venue_elem.get_text(strip=True) if venue_elem else "N/A"

        # 6. Description
        desc_elem = container.find(class_=re.compile(r'description|summary|about|info|details', re.I)) or \
                    container.find('p')
        description = desc_elem.get_text(strip=True) if desc_elem else "N/A"

        # 7. URL
        link_elem = container.find('a', href=True)
        url = urljoin(base_url, link_elem['href']) if link_elem else base_url

        events.append({
            'title': title,
            'date': date,
            'time': time,
            'price': price,
            'venue': venue,
            'description': description,
            'url': url
        })

    return events
