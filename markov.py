import sys
from random import choice

filename = sys.argv[1]  # Allows user to specify file name from command line


def open_and_read_file(filename):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_string = open(filename).read()

    return file_string


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    word_pairs = []

    words = text_string.split()

    # Generate n-gram of two words to add to word_pairs for dictionary keys
    for number in range(len(words) - 1):
        word_pairs.append((words[number], words[number + 1]))

    for number in range(len(word_pairs) - 1):
        if word_pairs[number] not in chains:
            chains[word_pairs[number]] = [word_pairs[number + 1][1]]
        elif word_pairs[number] in chains:
           chains[word_pairs[number]] += [word_pairs[number + 1][1]]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
     
    start_text = choice(chains.keys())
    master_text = start_text[0] + " " + start_text[1]
    text_split = tuple(master_text.split())

    while text_split[-2:] in chains:
        new_word = choice(chains[text_split[-2:]])
        master_text += (" "+ new_word)
        text_split = tuple(master_text.split())

    return master_text

# Open the file and turn it into one long string
input_text = open_and_read_file(filename)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
