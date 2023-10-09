import pickle
import streamlit as st
import numpy as np


st.header('Book Recommendation System')
st.subheader('Made by CHUN KAI LI')

model = pickle.load(open('models/similarity_scores.pkl','rb'))  
book_names = pickle.load(open('models/book_names.pkl','rb'))
book_ratings = pickle.load(open('models/book_ratings.pkl','rb'))
pivot_table = pickle.load(open('models/pivot_table.pkl','rb'))

st.write("Ask for recommendation by searching title of the book you like or pick one from the list below ")
book_selected = st.selectbox(
    "e.g. 'Lord of the rings' or 'Harry Potter'",
    book_names
)


def recommend_function(book_name):
    index = np.where(pivot_table.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(model[index])),key=lambda x:x[1],reverse=True)[1:10]
    
    data = []
    for i in similar_items:
        item = []
        similarity = i
        item.extend(similarity)
        temp_df = book_ratings[book_ratings['BTitle'] == pivot_table.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('BTitle')['BTitle'].values))
        item.extend(list(temp_df.drop_duplicates('BTitle')['BAuthor'].values))
        item.extend(list(temp_df.drop_duplicates('BTitle')['IMG'].values))
        
        data.append(item)
    
    return data

if st.button('Surprise me!'):
    recommended_books = recommend_function(book_selected)

    col11, col12, col13= st.columns(3)
    col21, col22, col23= st.columns(3)

    st.write("How would you rate this recommendation?")
    st.button("I LIKE the recommendations", type="primary")
    st.button("I DON'T LIKE the recommendations")

    with col11:
      similarity1 = round((recommended_books[0][1])*100, 2)
      st.image(recommended_books[0][4])
      st.markdown(f"Similarity Score to target: {similarity1}")
      st.caption(recommended_books[0][2])
      st.caption(recommended_books[0][3])
    with col12:
      similarity2 = round((recommended_books[1][1])*100, 2)
      st.image(recommended_books[1][4])
      st.markdown(f"Similarity Score to target: {similarity2}")
      st.caption(recommended_books[1][2])
      st.caption(recommended_books[1][3])
    with col13:
      similarity3 = round((recommended_books[2][1])*100, 2)
      st.image(recommended_books[2][4])
      st.markdown(f"Similarity Score to target: {similarity3}")
      st.caption(recommended_books[2][2])
      st.caption(recommended_books[2][3])
    
    with col21:
      similarity4 = round((recommended_books[4][1])*100, 2)
      st.image(recommended_books[4][4])
      st.markdown(f"Similarity Score to target: {similarity4}")
      st.caption(recommended_books[4][2])
      st.caption(recommended_books[4][3])
    with col22:
      similarity5 = round((recommended_books[5][1])*100, 2)
      st.image(recommended_books[5][4])
      st.markdown(f"Similarity Score to target: {similarity5}")
      st.caption(recommended_books[5][2])
      st.caption(recommended_books[5][3])
    with col23:
      similarity6 = round((recommended_books[6][1])*100, 2)
      st.image(recommended_books[6][4])
      st.markdown(f"Similarity Score to target: {similarity6}")
      st.caption(recommended_books[6][2])
      st.caption(recommended_books[6][3])

