from top_match import topMatch
from film_recommendation import getRecommendation
def listTrans(pref):
    result = {}
    for person in pref:
        for film in pref[person]:
            result.setdefault(film, {})
            result[film][person] = pref[person][film]
    return result

def filmRelate(pref, film, method):
    return topMatch(listTrans(pref), film, method)

def watchWith(pref, film, method):
    return getRecommendation(listTrans(pref), film, method)