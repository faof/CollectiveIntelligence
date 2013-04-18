def topMatch(pref, person, method):
    scores = []
    for item in pref:
        if item != person:
            node = (method(pref, person, item), item)
            scores.append(node)
    scores.sort()
    scores.reverse()
    return scores