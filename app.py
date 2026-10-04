import streamlit as st
from google import genai
from google.genai import types

from prompts import (
    SUMMARY_REQUEST_PROMPT,
    SYSTEM_PROMPT,
    WELCOME_MESSAGE_TEMPLATE
)

from deadline_parser import extract_deadlines
from notifier import send_email


# --------------------------------
# Page settings
# --------------------------------

st.set_page_config(
    page_title="DeadlineLens",
    page_icon="📅"
)


# --------------------------------
# Gemini connection
# --------------------------------

@st.cache_resource
def get_gemini_client():

    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    return client


client = get_gemini_client()


# --------------------------------
# Store user information
# --------------------------------

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

if "chat" not in st.session_state:
    st.session_state.chat = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "deadlines" not in st.session_state:
    st.session_state.deadlines = []

if "digest" not in st.session_state:
    st.session_state.digest = ""


# --------------------------------
# App title
# --------------------------------

st.title("📅 DeadlineLens")

st.caption("AI Academic Deadline Tracker")

st.write(
    "Upload your academic documents and let AI find "
    "important deadlines for you."
)


# --------------------------------
# Onboarding screen
# --------------------------------

if st.session_state.chat is None:

    st.subheader("👋 Welcome to DeadlineLens")

    st.write(
        "Enter your details to start tracking your academic deadlines."
    )

    # Create onboarding form
    with st.form("onboarding_form"):

        name = st.text_input(
            "Your name"
        )

        email = st.text_input(
            "Your email address"
        )

        submitted = st.form_submit_button(
            "Start DeadlineLens 🚀"
        )


        # When button is clicked
        if submitted:

            if not name.strip():

                st.error(
                    "Please enter your name."
                )

            elif not email.strip():

                st.error(
                    "Please enter your email address."
                )

            else:

                # Save user details
                st.session_state.user_name = name.strip()

                st.session_state.user_email = email.strip()


                # Create Gemini chat
                st.session_state.chat = client.chats.create(
                    model="gemini-3.5-flash-lite",
                    config={
                        "system_instruction": SYSTEM_PROMPT
                    }
                )


                st.success(
                    "Your DeadlineLens account is ready! 🎉"
                )


                # Refresh the page
                st.rerun()


# --------------------------------
# Chat screen
# --------------------------------

if st.session_state.chat is not None:


    # --------------------------------
    # Welcome message
    # --------------------------------

    welcome_message = WELCOME_MESSAGE_TEMPLATE.format(
        name=st.session_state.user_name
    )

    st.write(
        welcome_message
    )


    # --------------------------------
    # Show previous messages
    # --------------------------------

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.write(
                message["text"]
            )


    # --------------------------------
    # Chat box with image upload
    # --------------------------------

    user_input = st.chat_input(
        "Ask something or upload a document 📸",
        accept_file=True,
        file_type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )


    # --------------------------------
    # If the user sends something
    # --------------------------------

    if user_input:

        user_text = user_input.text

        uploaded_files = user_input.files


        # If there is no text
        if not user_text:

            user_text = (
                "Look at this image and find all important "
                "academic deadlines, dates, assignments, exams, "
                "submissions, and events."
            )


        # --------------------------------
        # Show user's message
        # --------------------------------

        with st.chat_message("user"):

            if uploaded_files:

                st.image(
                    uploaded_files[0]
                )

            st.write(
                user_text
            )


        # --------------------------------
        # Save user's message
        # --------------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "text": user_text
            }
        )


        # --------------------------------
        # If image was uploaded
        # --------------------------------

        if uploaded_files:

            image = uploaded_files[0]


            # Create image part
            image_part = types.Part.from_bytes(
                data=image.getvalue(),
                mime_type=image.type
            )


            # --------------------------------
            # Send image to Gemini
            # --------------------------------

            try:

                response = st.session_state.chat.send_message(
                    [
                        user_text,
                        image_part
                    ]
                )

            except Exception as e:

                st.error(
                    "Sorry, I could not process the image right now."
                )

                st.write(e)

                response = None


            # --------------------------------
            # Extract deadlines
            # --------------------------------

            try:

                deadline_data = extract_deadlines(
                    client,
                    image
                )

            except Exception as e:

                st.error(
                    "I could not extract the deadlines from this image."
                )

                st.write(e)

                deadline_data = []


            # --------------------------------
            # Save deadlines
            # --------------------------------

            for deadline in deadline_data:

                if deadline not in st.session_state.deadlines:

                    st.session_state.deadlines.append(
                        deadline
                    )


            # --------------------------------
            # Show extracted deadlines
            # --------------------------------

            if deadline_data:

                st.subheader(
                    "📅 Extracted Deadlines"
                )

                for deadline in deadline_data:

                    st.write(
                        f"**{deadline['date']}** - "
                        f"{deadline['subject']} - "
                        f"{deadline['task']}"
                    )

            else:

                st.info(
                    "No clear deadlines were found in this image."
                )


            # --------------------------------
            # Show Gemini response
            # --------------------------------

            if response:

                with st.chat_message(
                    "assistant"
                ):

                    st.write(
                        response.text
                    )


                # Save Gemini response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "text": response.text
                    }
                )


        # --------------------------------
        # If only text was entered
        # --------------------------------

        else:

            try:

                response = st.session_state.chat.send_message(
                    user_text
                )


                with st.chat_message(
                    "assistant"
                ):

                    st.write(
                        response.text
                    )


                # Save Gemini response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "text": response.text
                    }
                )

            except Exception as e:

                st.error(
                    "Sorry, I could not get a response from Gemini."
                )

                st.write(e)


    # --------------------------------
    # Deadline digest
    # --------------------------------

    st.divider()

    st.subheader(
        "📋 Deadline Digest"
    )


    if len(st.session_state.deadlines) > 0:

        st.write(
            "Your deadlines are ready. Create a simple summary below."
        )

        if st.button(
            "📋 Create Deadline Digest"
        ):

            response = st.session_state.chat.send_message(
                SUMMARY_REQUEST_PROMPT
            )

            st.session_state.digest = response.text

    else:

        st.button(
            "📋 Create Deadline Digest",
            disabled=True
        )


    # --------------------------------
    # Show deadline digest
    # --------------------------------

    if st.session_state.digest:

        st.subheader(
            "📋 Your Deadline Digest"
        )

        st.write(
            st.session_state.digest
        )


        # --------------------------------
        # Send digest by email
        # --------------------------------

        if st.button(
            "📧 Send deadline digest"
        ):

            try:

                send_email(
                    st.secrets["GMAIL_EMAIL"],
                    st.secrets["GMAIL_APP_PASSWORD"],
                    st.session_state.user_email,
                    "DeadlineLens - Your Academic Deadline Digest",
                    st.session_state.digest
                )

                st.success(
                    "Deadline digest sent successfully! 📧"
                )

            except Exception as e:

                st.error(
                    "Could not send the email."
                )

                st.write(e)