from math import sqrt
def pearson_corretation(pref, person1, person2):
    si = {}
    for item in pref[person1]:
        if item in pref[person2]:
            si[item] = 1
    n = len(si)
    if n == 0:
        return 1
    sum1 = sum2 = sum1sq = sum2sq = psum = 0
    for item in si:
        sum1 += pref[person1][item]
        sum1sq += pow(pref[person1][item], 2)
        sum2 += pref[person2][item]
        sum2sq += pow(pref[person2][item], 2)
        psum += pref[person1][item] * pref[person2][item]
    num = psum - (sum1 * sum2 /n)
    den = sqrt((sum1sq - pow(sum1, 2)/n) * (sum2sq - pow(sum2, 2)/n))
    if den == 0:
        return 0
    return num/den