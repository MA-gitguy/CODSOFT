#Recommendation_System


bollywood_movies_data = [
    {'Title': 'Dangal', 'Genre': 'Drama', 'Description': 'A story of a father training his daughters in wrestling.'},
    {'Title': '3 Idiots', 'Genre': 'Comedy', 'Description': 'A humorous take on the Indian education system.'},
    {'Title': 'PK', 'Genre': 'Comedy', 'Description': 'A satirical comedy-drama questioning societal norms.'},
    {'Title': 'Bahubali', 'Genre': 'Action', 'Description': 'An epic historical fiction film with grand visuals.'},
    {'Title': 'Queen', 'Genre': 'Drama', 'Description': 'A woman\'s journey of self-discovery during her solo honeymoon.'}
]

def cosine_similarity(movie1, movie2):
    words1 = set(movie1['Description'].lower().split())
    words2 = set(movie2['Description'].lower().split())
    common_words = words1.intersection(words2)
    similarity = len(common_words) / (len(words1) * len(words2)) ** 0.5
    return similarity

def get_bollywood_recommendations(user_preferences, bollywood_movies_data):
    recommendations = []

    for movie in bollywood_movies_data:
        score = 0
        for genre, preference in user_preferences.items():
            if movie['Genre'] == genre:
                score += cosine_similarity(movie, movie) * preference

        recommendations.append((movie['Title'], score))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

user_preferences_bollywood = {}
genres = set(movie['Genre'] for movie in bollywood_movies_data)

print("Genres available:", genres)
print("Rate each genre from 1 to 5 (5 being the highest preference):")

for genre in genres:
    rating = int(input(f"Rate {genre}: "))
    user_preferences_bollywood[genre] = rating

bollywood_recommendations = get_bollywood_recommendations(user_preferences_bollywood, bollywood_movies_data)

print("\nTop 3 Recommended Bollywood Movies:")
for i in range(3):
    print(f"{i + 1}. {bollywood_recommendations[i][0]}")


