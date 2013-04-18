from tag_list import critics
from euclidean_distance import euclidean_distance
from pearson_corretation import pearson_corretation
from top_match import topMatch
from film_recommendation import getRecommendation
from film_relation import filmRelate, watchWith

print euclidean_distance(critics, 'Lisa Rose', 'Gene Seymour')
print pearson_corretation(critics, 'Lisa Rose', 'Gene Seymour')
print topMatch(critics, 'Toby', pearson_corretation)
print getRecommendation(critics, 'Toby', pearson_corretation)
print filmRelate(critics, 'Superman Returns', pearson_corretation)
print watchWith(critics, 'Just My Luck', pearson_corretation)