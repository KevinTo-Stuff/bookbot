from collections import Counter


def get_word_count(text):
    return len(text.split())

def get_each_character_count(text):
    return dict(Counter(text.lower()));

def sort_stats(stats):
    return dict(sorted(stats.items()))