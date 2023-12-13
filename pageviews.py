import streamlit as st
from getDb import get_database #importing database connection function

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#These functions will set the views for each of the options selectable from the sidebar
# in the main program.

dbname=get_database()

def home():
    st.header("Making Christmas More Merry Since 1947!")
    #Can probably add more to this page

def db_submit_donation(donor_name, monetary_donation, toy_donation): #code for sending donation info to db
    collection_name = dbname["Donated"]
    collection_name.insert_one({
        "donor_name": donor_name,
        "money_donated": monetary_donation,
        "toys_donated": toy_donation
    })

def donations():
    st.header("Make a Donation!")
    if 'donor_name' not in st.session_state:
        st.sesson_state['donor_name'] = ''
    if 'monetary_donation' not in st.session_state:
        st.session_state['monetary_donation'] = ''
    if 'toy_donation' not in st.session_state:
        st.session_state['toy_donation'] = ''
    donor_name = st.text_input("Enter your Full Name OR your organization's name")
    monetary_donation = st.text_input("Monetary Donation amount:")
    toy_donation = st.text_input("Toy being donated:")
    

    #Will probably remove this option, unless we have time to implement it at the end
    ###radioOptions = st.radio("Would you like a receipt?", options = ["No", "Yes"])
    ####if they select that they would like a reciept then get their name to put on it
    ###if radioOptions == "Yes":
    ###     code to create a receipt will go here


    if st.button("Submit Donation"):
        db_submit_donation(donor_name, monetary_donation, toy_donation)
        st.session_state.submitted = True
        st.session_state.donor_name = ""
        st.session_state.monetary_donation = ""
        st.session_state.toy_donation = ""
        st.session_state.submitted = False
        st.success("Donation submitted! Thank you for your generosity!")
    #the "on_click" will be the code to create an instance of the Sponsors Class
    # and send it's attributes to the DB, 
    #create function and call in the on_Click

def db_submit_request(parent_name, child_name, child_age, toy_requested): #code for sending request info to db
    collection_name = dbname["Requested"]
    collection_name.insert_one({
        "parent_name": parent_name,
        "child_name": child_name,
        "child_age": child_age,
        "toy_requested": toy_requested
    })
    st.session_state.submitted = False


def makeReq():
    st.header("Request a Donation!")
    if 'parent_name' not in st.session_state:
        st.session_state['parent_name'] = ''
    if 'child_name' not in st.session_state:
        st.session_state['child_name'] = ''
    if 'child_age' not in st.session_state:
        st.session_state['child_age'] = ''
    if 'toy_requested' not in st.session_state:
        st.session_state['toy_requested'] = ''
    parent_name = st.text_input("What is your first and last name?", value = st.session_state['parent_name'])
    child_name = st.text_input("What is the child's first and last name?", value = st.session_state['child_name'])
    child_age = st.text_input("How old is the child?", value = st.session_state['child_age'])
    toy_requested = st.text_input("What toy are you requesting?", value = st.session_state['toy_requested'])
    if st.button("Submit Donation Request"):
        db_submit_request(parent_name, child_name, child_age, toy_requested)
        st.session_state.submitted = True
        st.session_state.parent_name = ""
        st.session_state.child_name = ""
        st.session_state.child_age = ""
        st.session_state.toy_requested = ""
        st.session_state.submitted = False
        st.success("Request submitted!")
        #the "on_click" will be the code to send to DB, 
        #create function and call here
        #need to add code to button to have it send the entered info to the MongoDB database
        # ref https://docs.streamlit.io/library/api-reference/widgets/st.button

@st.cache_data(ttl=600)
def seeReq():
    st.header("Requested Toys:")
    items = dbname.Requested.find()
    items == list(items)
    # return items
    for item in items:
        st.write(f"{item}")
    #Insert code to display all the toys requested and the ages of the kids requesting them
    #Maybe use selectbox?
    # ref https://docs.streamlit.io/library/api-reference/widgets/st.selectbox



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#The Classes and their attributes:
#Kids#
# -name
# -age
# -toy

#Sponsors#
# -name
# -money
# -toy

#Requestor#
# -Name

#The tables in the database
#Requested#
# -parent's name (from "Requestor" class)
# -kids name (from "Kids" class)
# -kids age (from "Kids" class)
# -toy requested (from "Kids" class)

#Donated#
# -donator's name (from "Sponsors" class)
# -money donated (from "sponsors" class) - can be null
# -toy being donated (from "sponsors" class) - can be null 
