import hashlib

class URLShortener:
    def __init__(self):
        # A dictionary to store the mapping between short and long URLs
        self.url_database = {}
        self.base_url = "http://short.url/"

    def shorten_url(self, long_url):
        # Generate a hash for the long URL
        short_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]
        short_url = self.base_url + short_hash
        
        # Store the mapping between the shortened hash and the long URL
        self.url_database[short_url] = long_url
        
        return short_url

    def retrieve_url(self, short_url):
        # Retrieve the long URL based on the shortened URL
        return self.url_database.get(short_url, "URL not found")

# Example usage
if __name__ == "__main__":
    url_shortener = URLShortener()

    # Input: Long URL
    long_url = input("Enter the long URL: ")

    # Shorten the URL
    short_url = url_shortener.shorten_url(long_url)
    print(f"Shortened URL: {short_url}")

    # Simulate retrieving the original URL
    retrieved_url = url_shortener.retrieve_url(short_url)
    print(f"Original URL retrieved from short URL: {retrieved_url}")
