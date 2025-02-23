import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/books"

st.title("My Books Library")

# to fetch books
def fetch_books():
    response = requests.get(API_URL)
    return response.json() if response.status_code == 200 else []

# to get book by title
def get_book_by_title(title):
    response = requests.get(f"{API_URL}/title/{title}")
    return response.json() if response.status_code == 200 else {"error": "Book not found"}

# to get book by ID
def get_book_by_id(book_id):
    response = requests.get(f"{API_URL}/{book_id}")
    return response.json() if response.status_code == 200 else {"error": "Book not found"}

#to add a new book
def add_book(title, author, rating, fav_line):
    response = requests.post(API_URL, json={"title": title, "author": author, "rating": rating, "fav_line": fav_line})
    return response.json()

#to update a existing book
def update_book(book_id, title, author, rating):
    response = requests.put(f"{API_URL}/{book_id}", json={"title": title, "author": author, "rating": rating})
    return response.json()

# to delete a book
def delete_book(book_id):
    response = requests.delete(f"{API_URL}/{book_id}")
    return response.json()

# Streamlit Application
option = st.selectbox("Select an option", 
                      ["List all books", "Search a book", "Add a new book", "Update book details", "Delete a book"])

if option == "List all books":
    books = fetch_books()
    if books:
        for book in books:
            st.write(f"📖 **{book['title']}** by {book['author']} (rating: {book['rating']})")
    else:
        st.warning("No books available.")

elif option == "Search a book":
    title = st.text_input("Enter Book Title")
    if st.button("Check Book Info"):
        result = get_book_by_title(title)
        if "error" in result:
            st.error(result["error"])
        else:
            st.write(f"📖 **Title:** {result['title']}")
            st.write(f"✍ **Author:** {result['author']}")
            st.write(f"📅 **rating:** {result['rating']}")

elif option == "Add a new book":
    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author")
    rating = st.number_input("Add Your Ratings", min_value=0, max_value=5, step=1)
    fav_line = st.text_input("Add Your Favourite Line")
    if st.button("Add Book"):
        response = add_book(title, author, rating, fav_line)
        st.success(response["message"])

elif option == "Update book details":
    book_id = st.number_input("Enter Book ID", min_value=1, step=1)
    title = st.text_input("Enter New Title")
    author = st.text_input("Enter New Author")
    rating = st.number_input("Enter New rating", min_value=1000, max_value=9999, step=1)
    if st.button("Update Book"):
        response = update_book(book_id, title, author, rating)
        if "error" in response:
            st.error(response["error"])
        else:
            st.success(response["message"])

elif option == "Delete a book":
    book_id = st.number_input("Enter Book ID to Delete", min_value=1, step=1)
    if st.button("Delete Book"):
        response = delete_book(book_id)
        st.success(response["message"])
