import streamlit as st
from getDb import get_database #importing database connection function

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#These functions will set the views for each of the options selectable from the sidebar
# in the main program.

db=get_database()

def home():
    st.header("Making Christmas More Merry Since 1947!")
    #Can probably add more to this page

# def db_submit_donation():
    #code for sending donation info to db

# def db_submit_request():
    #code for sending request info to db

def donations():
    st.header("Make a Donation!")
    st.text_input("Monetary Donation amount:")
    st.text_input("Toy being donated:")
    radioOptions = st.radio("Would you like a receipt?", options = ["No", "Yes"])
    #if they select that they would like a receipt then get their name to put on it
    if radioOptions == "Yes":
         st.text_input("First Name")
         st.text_input("Last Name")
    st.button("Submit Donation", on_click= None)
    #the "on_click" will be the code to send to DB, 
    #create function and call here

def makeReq():
    st.header("Request a Donation!")
    st.text_input("What toy are you requesting?")
    st.text_input("hHw old is the child the request is for?")
    st.button("Submit Donation Request", on_click= None) 
        #the "on_click" will be the code to send to DB, 
        #create function and call here
        #need to add code to button to have it send the entered info to the MongoDB database
        # ref https://docs.streamlit.io/library/api-reference/widgets/st.button

@st.cache_data(ttl=600)
def seeReq():
    st.header("Requested Toys:")
    items = db.Requested.find()
    items == list(items)
    return items
    #Insert code to display all the toys requested and the ages of the kids requesting them
    #Maybe use selectbox?
    # ref https://docs.streamlit.io/library/api-reference/widgets/st.selectbox

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Databases/classes:
#"Toys" is a database of requested toys and the ages of the child asking for them
#"Sponsors" is a database of
