"""Check whether a piece of text is a palindrome."""


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards.

    Case, spaces and punctuation are ignored.
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    for phrase in ["Race car", "A man, a plan, a canal: Panama", "Hello"]:
        print(f"{phrase!r}: {is_palindrome(phrase)}")
