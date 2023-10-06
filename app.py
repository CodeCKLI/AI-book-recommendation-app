import pickle
import streamlit as st
import numpy as np


st.header('Book Recommender System Using Machine Learning')

model = pickle.load(open('models/model.pkl','rb'))  
book_names = pickle.load(open('models/book_names.pkl','rb'))
book_ratings = pickle.load(open('models/book_ratings.pkl','rb'))
pivot_table = pickle.load(open('models/pivot_table.pkl','rb'))

book_selected = st.selectbox(
    "Search for the title or pick one from the list below",
    book_names
)

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(pivot_table.index[book_id])

    for name in book_name[0]: 
        ids = np.where(book_ratings['BTitle'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = book_ratings.iloc[idx]['IMG']
        poster_url.append(url)

    return poster_url



def recommend_function(book_name):
    books_list = []
    book_id = np.where(pivot_table.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(pivot_table.iloc[book_id,:].values.reshape(1,-1), n_neighbors=4 )
    poster_url = fetch_poster(suggestion)

    for num in range(len(suggestion)):
            books = pivot_table.index[suggestion[num]]
            for book in books:
                books_list.append(book)
    return books_list , poster_url    

if st.button('Surprise me!'):
    recommended_books,poster_url = recommend_function(book_selected)
    col1, col2, col3= st.columns(3)

    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])