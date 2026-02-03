"""Problem solution registry."""

from .math import sum_of_multiples
from .strings import is_palindrome, word_frequencies

PROBLEMS = {
    "sum_of_multiples": sum_of_multiples,
    "is_palindrome": is_palindrome,
    "word_frequencies": word_frequencies,
}
