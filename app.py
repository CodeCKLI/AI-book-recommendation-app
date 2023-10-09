import pickle
import streamlit as st
import numpy as np


st.header('Book Recommendation System')
st.subheader('Made by CHUN KAI LI')

model = pickle.load(open('models/model.pkl','rb'))  
book_names = pickle.load(open('models/book_names.pkl','rb'))
book_ratings = pickle.load(open('models/book_ratings.pkl','rb'))
pivot_table = pickle.load(open('models/pivot_table.pkl','rb'))

st.write("Ask for recommendation by searching title of the book you like or pick one from the list below ")
book_selected = st.selectbox(
    "e.g. 'Lord of the rings' or 'Harry Potter'",
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
    distance, suggestion = model.kneighbors(pivot_table.iloc[book_id,:].values.reshape(1,-1), n_neighbors=10 )
    poster_url = fetch_poster(suggestion)

    for num in range(len(suggestion)):
            books = pivot_table.index[suggestion[num]]
            for book in books:
                books_list.append(book)
    return books_list , poster_url    

if st.button('Surprise me!'):
    recommended_books,poster_url = recommend_function(book_selected)
    col11, col12, col13= st.columns(3)
    col21, col22, col23= st.columns(3)
    col31, col32, col33= st.columns(3)

    st.write("How would you rate this recommendation?")
    st.button("I LIKE the recommendations", type="primary")
    st.button("I DON'T LIKE the recommendations")

    with col11:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col12:
        st.text(recommended_books[2])
        st.image(poster_url[2])
    with col13:
        st.text(recommended_books[3])
        st.image(poster_url[3])

    with col21:
        st.text(recommended_books[4])
        st.image(poster_url[4])
    with col22:
        st.text(recommended_books[5])
        st.image(poster_url[5])
    with col23:
        st.text(recommended_books[6])
        st.image(poster_url[6])

    with col31:
        st.text(recommended_books[7])
        st.image(poster_url[7])
    with col32:
        st.text(recommended_books[8])
        st.image(poster_url[8])
    with col33:
        st.text(recommended_books[9])
        st.image(poster_url[9])
