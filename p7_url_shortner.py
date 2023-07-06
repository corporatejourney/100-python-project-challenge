import string
import random
import webbrowser

class URLShortener:
    """A class for shortening and expanding URLs."""

    def __init__(self):
        """Initialize the URLShortener."""
        self.characters = string.ascii_letters + string.digits
        self.short_to_long = {}
        self.long_to_short = {}

    def generate_short_url(self):
        """Generate a random 6-character short URL."""
        while True:
            short_url = ''.join(random.choice(self.characters) for _ in range(6))
            if short_url not in self.short_to_long:
                return short_url

    def shorten_url(self, long_url):
        """Shorten a long URL and return the corresponding short URL.

        Args:
            long_url (str): The long URL to be shortened.

        Returns:
            str: The corresponding short URL.
        """
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]

        short_url = self.generate_short_url()
        self.short_to_long[short_url] = long_url
        self.long_to_short[long_url] = short_url
        return short_url

    def expand_url(self, short_url):
        """Expand a short URL and return the corresponding long URL.

        Args:
            short_url (str): The short URL to be expanded.

        Returns:
            str: The corresponding long URL, or None if not found.
        """
        return self.short_to_long.get(short_url)
    
if __name__ == "__main__":
    url_shortener = URLShortener()
    long_url = "https://www.google.com/search?q=most+used+design+patterns+in+python&rlz=1C1CHZN_enIN1022IN1022&sxsrf=AB5stBgqSTONtclE4tTMbFLzrYVRbirAng%3A1688623478833&ei=dlmmZOqmMoPuseMP-7q8uA0&ved=0ahUKEwjqufXUtPn_AhUDd2wGHXsdD9cQ4dUDCA8&uact=5&oq=most+used+design+patterns+in+python&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEAcQHjIGCAAQBxAeMgUIABCABDoKCAAQRxDWBBCwAzoKCAAQigUQsAMQQzoNCAAQ5AIQ1gQQsAMYAToPCC4QigUQyAMQsAMQQxgCSgQIQRgAUIoVWN5FYKRHaAJwAXgAgAGkE4gBsEKSAQ0yLTUuMS4xLjMuOS0ymAEAoAEBwAEByAEQ2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz-serp"
    short_url = url_shortener.shorten_url(long_url)
    print(f"Short URL: {short_url}")
    # Open the shortened URL in a web browser
    webbrowser.open(short_url)
    expanded_url = url_shortener.expand_url(short_url)
    print(f"Expanded URL: {expanded_url}")
"""
Short URL: bmIu5N
Expanded URL: https://www.google.com/search?q=most+used+design+patterns+in+python&rlz=1C1CHZN_enIN1022IN1022&sxsrf=AB5stBgqSTONtclE4tTMbFLzrYVRbirAng%3A1688623478833&ei=dlmmZOqmMoPuseMP-7q8uA0&ved=0ahUKEwjqufXUtPn_AhUDd2wGHXsdD9cQ4dUDCA8&uact=5&oq=most+used+design+patterns+in+python&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEAcQHjIGCAAQBxAeMgUIABCABDoKCAAQRxDWBBCwAzoKCAAQigUQ
"""