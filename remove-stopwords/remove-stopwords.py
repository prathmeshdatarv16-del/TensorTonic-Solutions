def remove_stopwords(tokens, stopwords):
    blocked = set(stopwords)
    return [token for token in tokens if token not in blocked]
