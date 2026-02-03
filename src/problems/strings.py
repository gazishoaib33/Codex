"""String-related coding problems."""

from collections import Counter
from typing import Dict


def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome, ignoring case and non-alphanumerics."""
    normalized = "".join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]


def word_frequencies(text: str) -> Dict[str, int]:
    """Return lowercase word frequency counts for a given text."""
    words = ["".join(ch for ch in token if ch.isalnum()).lower() for token in text.split()]
    words = [word for word in words if word]
    return dict(Counter(words))
