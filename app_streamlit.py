import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/books"

st.title("📚 Book Management App")

# 📌 Fetch Books
def fetch_books():
    response = requests.get(API_URL)
    return response.json() if response.status_code == 200 else []

# 📌 Get Book by Title
def get_book_by_title(title):
    response = requests.get(f"{API_URL}/title/{title}")
    return response.json() if response.status_code == 200 else {"error": "Book not found"}

# 📌 Get Book by ID
def get_book_by_id(book_id):
    response = requests.get(f"{API_URL}/{book_id}")
    return response.json() if response.status_code == 200 else {"error": "Book not found"}

# 📌 Add Book
def add_book(title, author, year):
    response = requests.post(API_URL, json={"title": title, "author": author, "year": year})
    return response.json()

# 📌 Update Book
def update_book(book_id, title, author, year):
    response = requests.put(f"{API_URL}/{book_id}", json={"title": title, "author": author, "year": year})
    return response.json()

# 📌 Delete Book
def delete_book(book_id):
    response = requests.delete(f"{API_URL}/{book_id}")
    return response.json()

# 📌 Streamlit UI
option = st.selectbox("Select an option", 
                      ["List Books", "View Book Info by Title", "Add Book", "Update Book", "Delete Book"])

if option == "List Books":
    books = fetch_books()
    if books:
        for book in books:
            st.write(f"📖 **{book['title']}** by {book['author']} (Year: {book['year']}) - ID: {book['id']}")
    else:
        st.warning("No books available.")

elif option == "View Book Info by Title":
    title = st.text_input("Enter Book Title")
    if st.button("Check Book Info"):
        result = get_book_by_title(title)
        if "error" in result:
            st.error(result["error"])
        else:
            st.write(f"📖 **Title:** {result['title']}")
            st.write(f"✍ **Author:** {result['author']}")
            st.write(f"📅 **Year:** {result['year']}")

elif option == "Add Book":
    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author")
    year = st.number_input("Enter Year", min_value=1000, max_value=9999, step=1)
    if st.button("Add Book"):
        response = add_book(title, author, year)
        st.success(response["message"])

elif option == "Update Book":
    book_id = st.number_input("Enter Book ID", min_value=1, step=1)
    title = st.text_input("Enter New Title")
    author = st.text_input("Enter New Author")
    year = st.number_input("Enter New Year", min_value=1000, max_value=9999, step=1)
    if st.button("Update Book"):
        response = update_book(book_id, title, author, year)
        if "error" in response:
            st.error(response["error"])
        else:
            st.success(response["message"])

elif option == "Delete Book":
    book_id = st.number_input("Enter Book ID to Delete", min_value=1, step=1)
    if st.button("Delete Book"):
        response = delete_book(book_id)
        st.success(response["message"])
