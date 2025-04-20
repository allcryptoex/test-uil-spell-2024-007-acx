import streamlit as st
import time
from time import sleep
##### from streamlit.runtime.scriptrunner import get_script_run_ctx

# Function to get the current page name
def get_current_page_name():
    # Simply return the name of the page based on the script that is currently running
    # return st.experimental_get_query_params().get('page', ['streamlit_app'])[0]
    # `st.experimental_get_query_params` will be removed after 2024-04-11.
    # return st.query_params().get('page', ['streamlit_app'])[0]
    # return st.session_state.get("page", "streamlit_app.py")
    return "streamlit_app.py"
    
# Function to create the sidebar with page navigation
def make_sidebar():
    with st.sidebar:
        st.title("⚡ Curtis Speller ββ")
        st.write("")

        # Check if user is logged in
        if st.session_state.get("logged_in", False):
            # Create links for logged-in users
            st.page_link("pages/page1.py", label="5th-6th Grade - 📝List of Words", icon="🔹")
            st.page_link("pages/page2.py", label="5th-6th Grade - 👍Selected Spelling Game", icon="🔸")
            st.page_link("pages/page3.py", label="3rd-4th Grade - 📝List of Words", icon="🔹")
            st.page_link("pages/page4.py", label="5th-6th Grade - 👍Full Spelling Game", icon="🔸")
            st.page_link("pages/1_0_Summaries_no_graphs_Count.py", label="5th-6th Grade - 👍1_0_Summaries_no_graphs_Count", icon="🔸")
            st.page_link("pages/Pricing.py", label="5th-6th Grade - 👍Pricing", icon="🔸")
            st.page_link("pages/Chat_with_PDF.py", label="5th-6th Grade - 👍Chat_with_PDF", icon="🔸")
            st.page_link("pages/Chat_with_Images.py", label="5th-6th Grade - 👍Chat_with_Images", icon="🔸")
            st.page_link("pages/BEST_PDF_STUDY_APP.py", label="5th-6th Grade - 👍BEST_PDF_STUDY_APP", icon="🔸")
            st.page_link("pages/aws_quiz_st.py", label="5th-6th Grade - 👍aws_quiz_st", icon="🔸")
            st.page_link("pages/aws_simple_question_gen.py", label="5th-6th Grade - 👍aws_simple_question_gen", icon="🔸")
            st.page_link("pages/aws_utils.py", label="5th-6th Grade - 👍aws_utils", icon="🔸")
            
            st.write("")
            st.write("")

            if st.button("Log out"):
                logout()

        elif get_current_page_name() != "streamlit_app.py":
            # If someone tries to access a secret page without being logged in, redirect to login
            st.switch_page("streamlit_app.py")

# Function to check user inactivity and automatically log out after 15 minutes
def check_user_inactivity():
    inactivity_limit = 15 * 60  # 15 minutes in seconds
    current_time = time.time()

    # Track last activity time
    if 'last_activity_time' not in st.session_state:
        st.session_state.last_activity_time = current_time

    # Calculate inactivity time
    inactivity_time = current_time - st.session_state.last_activity_time

    # If the user is inactive for too long, log them out
    if inactivity_time > inactivity_limit:
        st.session_state.clear()  # Clear session state to log the user out
        st.write("You have been logged out due to inactivity.")
        st.experimental_rerun()  # Rerun the app to reset the session

    # Update the last activity time
    st.session_state.last_activity_time = current_time   

# Logout function
def logout():
    st.session_state.logged_in = False
    st.info("✔️Logged out successfully!")
    sleep(0.5)
    
    # st.switch_page("streamlit_app.py")

    # Instead of switching pages immediately, rerun the app to refresh the session state
    st.experimental_rerun()

# Main App Execution
def main():
    # Check for user inactivity
    check_user_inactivity()

    # Create the sidebar
    make_sidebar()

    # Rest of the main content can go here...
    if not st.session_state.get("logged_in", False):
        st.write("Please log in to access the app.")
    else:
        st.write("Welcome back!")

if __name__ == "__main__":
    main()
