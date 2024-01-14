import streamlit as st
import pickle

# Load preprocessed data and models
movies = pickle.load(open('movies.pkl', 'rb'))
with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

# Function to get movie recommendations with posters
def get_recommendations_with_posters(title):
    idx = movies.index[movies['Series_Title'] == title].tolist()[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    recommendations = movies.iloc[movie_indices][['Series_Title', 'Poster_Link']]
    return recommendations

# Streamlit application
st.title('Movie Recommendation System')

# Get list of movie titles
titles = movies['Series_Title'].tolist()

movie_title = st.selectbox('Select a movie title', titles)
if st.button('Recommend'):
    if movie_title:
        recommendations = get_recommendations_with_posters(movie_title)
        for i in range(len(recommendations)):
            st.write('Title: ', recommendations.iloc[i]['Series_Title'])
            st.image(recommendations.iloc[i]['Poster_Link'])
    else:
        st.write('Please select a movie title')
