import streamlit as st
import pandas as pd 
import pickle

books= pd.read_excel("books.xlsx")

indices = pd.Series(books.index, index=books["title"].str.lower()).drop_duplicates()
with open('titles.pkl', 'rb') as file:
    titles = pickle.load(file)
with  open('cos_sim.pkl', 'rb') as file1:
    cosine_sim=pickle.load(file1)

st.title("Book Recomendation")
name=st.selectbox(label="Select Book Name",options=list(titles))
num=st.number_input(label='Enter number of Books',step=1)
st.markdown(name)
def recommend_books(title, top_n=5):
    # title = title.lower()
    if title not in list(titles):
        return ["Book not found in dataset"]
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1] 
    book_indices = [i[0] for i in sim_scores]
    return books.iloc[book_indices]["title"].tolist()
if st.button(label="Recomend"):
    books=recommend_books(name,num)
    st.success(books)
