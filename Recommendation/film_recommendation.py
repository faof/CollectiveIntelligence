from top_match import topMatch
def getRecommendation(pref, person, method):
    match = topMatch(pref, person, method)
    films = {}
    relation = {}
    result = []
    for item in match:
        if item[0] <= 0:
            continue
        for film in pref[item[1]]:
            if film in pref[person]:
                continue
            films.setdefault(film, 0)
            films[film] += item[0] * pref[item[1]][film]
            relation.setdefault(film, 0)
            relation[film] += item[0]
    for item in films:
        node = (films[item]/relation[item], item)
        result.append(node)
    result.sort()
    result.reverse()
    return result