from math import sqrt

def euclidean_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    sum_of_squares = 0
    for item in si:
        sum_of_squares += pow((prefs[person1][item] - prefs[person2][item]), 2)
    sum_of_squares = 1 / (1 + sqrt(sum_of_squares))
    return sum_of_squares