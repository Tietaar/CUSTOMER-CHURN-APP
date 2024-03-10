
import streamlit as st

# Create a function to authenticate users
def authenticate(username, password):

    if username == "Tietaar" and password == "abcd123":
        return True
    else:
        return False

# Create Streamlit app
def main():
    st.set_page_config(
        page_title="Home",
        page_icon=":)",
        layout="wide",
    )

    st.title("Welcome to Vodafone Churn App👋👋👋")
    st.subheader("Login Credentials")
    st.markdown(
        """
        * **User_Name:** Tietaar
        * **Password:** abcd123. 
        """
    )

    # Create input fields for username and password
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    # Check if the user has submitted the login form
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.success("Logged in as {}".format(username))
            # Once authenticated, show the rest of the app            
            show_app()
        else:
            st.error("Invalid username or password")

# Define the rest of the app to show after authentication
def show_app():
    st.subheader("About App:")
    st.markdown(
        """_The Vodafone Customer Churn Mitigation Project is an ambitious initiative aimed at understanding, analyzing, and ultimately reducing customer attrition within our telecommunications services.
        This app aims at using  machine learning models that will predict the likelihood of a customer churning._"""
    )
    st.subheader("Key Features:")
    st.markdown(
        """
        * **Data_page:** _Contains all the datasets that was used in analyzing and training machine learning models._
        * **Dashboard:** _This page contains all the visuals that were created during our analysis._
        * **Predict_page:** _This page allows you to predict the likelyhood of a customer churning._
        * **History_page:** _The predict page serves as an archive for all predictions that were done in the predict page._
        """
    )

    st.subheader("Contact Details:")
    st.markdown(
        """
        * **📧Email:** nyarlouis@gmail.com.
        * **🐱‍👤Github:** https://github.com/Tietaar.
        """
    )

    st.markdown(
        """_Dreams inspire but actions make. Keep trying, Keep coding. The world is full of endless possibilities_"""
    )


if __name__ == "__main__":
    main()

