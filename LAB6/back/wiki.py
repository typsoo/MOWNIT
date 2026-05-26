import wikipediaapi
import requests
import time

wiki = wikipediaapi.Wikipedia(language="en", user_agent="MyLabProject/1.0")

def get_random_titles(n=5):
    resp = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={"action": "query", "list": "random", "rnnamespace": 0, "rnlimit": n, "format": "json"},
        headers={"User-Agent": "MyLabProject/1.0"}
    )
    return [p["title"] for p in resp.json()["query"]["random"]]

titles = get_random_titles(500)
documents = []

start = time.time()
for i, title in enumerate(titles):
    page = wiki.page(title)
    if page.exists():
        documents.append(page.text)
        print(f"Downloaded: {i}")

    else:
        print(f"Skipped: {title}")
end = time.time()
print(f"\nDone! Collected {len(documents)} documents")
print(end - start)