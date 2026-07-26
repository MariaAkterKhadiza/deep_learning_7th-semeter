import streamlit as st

from modules.auth import register_user, login_user
from modules.pdf_loader import extract_text_from_pdf


# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="AI Learning Platform",
    page_icon="🎓",
    layout="wide"
)


# ==========================
# Custom CSS
# ==========================

st.markdown(
    """
<style>

.hero {

    padding:35px;
    border-radius:25px;

    background:
    linear-gradient(
        135deg,
        rgba(99,102,241,0.15),
        rgba(236,72,153,0.15)
    );

    text-align:center;

    border:1px solid rgba(128,128,128,0.2);

}


.hero h1{

    font-size:45px;
    font-weight:800;

}


.hero p{

    font-size:20px;
    opacity:0.7;

}


.card{

    padding:25px;

    border-radius:20px;

    border:1px solid rgba(128,128,128,0.25);

    background:
    rgba(128,128,128,0.08);

    min-height:150px;

}


.profile{

    padding:25px;

    border-radius:20px;

    background:
    rgba(128,128,128,0.1);

    border:1px solid rgba(128,128,128,0.25);

}


</style>

""",
unsafe_allow_html=True
)



# ==========================
# Session State
# ==========================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "email" not in st.session_state:

    st.session_state.email = ""


if "pdf_text" not in st.session_state:

    st.session_state.pdf_text = ""



# ==========================
# Header
# ==========================

st.markdown(
    """

<div class="hero">

<h1>
🎓 AI Personalized Learning Platform
</h1>

<p>
Learn smarter with LLM + RAG Technology
</p>

</div>

""",
unsafe_allow_html=True
)



# ==========================
# After Login Dashboard
# ==========================

if st.session_state.logged_in:


    # Sidebar

    st.sidebar.title("🎓 Navigation")


    menu = st.sidebar.radio(
        "Choose Section",
        [
            "Dashboard",
            "AI Tutor",
            "Courses",
            "Quiz",
            "Progress",
            "Profile"
        ]
    )


    st.sidebar.divider()


    st.sidebar.success(
        st.session_state.email
    )



    # ======================
    # Dashboard
    # ======================

    if menu == "Dashboard":


        st.markdown(
            f"""

<div class="profile">

<h2>
Welcome Back 👋
</h2>

<p>
Student Email:
{st.session_state.email}
</p>

<p>
Your personalized AI learning journey starts here.
</p>

</div>

""",
        unsafe_allow_html=True
        )


        st.write("")


        col1,col2,col3 = st.columns(3)


        with col1:

            st.markdown(
                """

<div class="card">

<h2>📚</h2>

<h3>
Courses
</h3>

Personalized learning materials

</div>

""",
            unsafe_allow_html=True
            )


        with col2:

            st.markdown(
                """

<div class="card">

<h2>🤖</h2>

<h3>
AI Tutor
</h3>

Ask questions from your PDF

</div>

""",
            unsafe_allow_html=True
            )


        with col3:

            st.markdown(
                """

<div class="card">

<h2>📝</h2>

<h3>
Assessment
</h3>

AI generated quizzes

</div>

""",
            unsafe_allow_html=True
            )



    # ======================
    # AI Tutor (RAG Section)
    # ======================

    elif menu == "AI Tutor":


        st.header(
            "🤖 AI Tutor"
        )


        st.write(
            "Upload your study materials and learn using AI."
        )


        uploaded_file = st.file_uploader(
            "Upload PDF File",
            type=["pdf"]
        )



        if uploaded_file:


            st.success(
                "PDF uploaded successfully!"
            )


            if st.button(
                "Process Document"
            ):


                extracted_text = extract_text_from_pdf(
                    uploaded_file
                )


                st.session_state.pdf_text = extracted_text


                st.success(
                    "Document processed successfully!"
                )



        if st.session_state.pdf_text:


            st.subheader(
                "📄 Extracted Text Preview"
            )


            with st.expander(
                "Show PDF Text"
            ):


                st.write(
                    st.session_state.pdf_text[:3000]
                )



            st.info(
                "Next step: Connect this text with RAG + LLM"
            )




    # ======================
    # Other Sections
    # ======================


    elif menu == "Courses":

        st.header("📚 Courses")

        st.info(
            "Course recommendation system coming soon."
        )



    elif menu == "Quiz":

        st.header("📝 Quiz Generator")

        st.info(
            "AI quiz generation coming soon."
        )



    elif menu == "Progress":

        st.header("📊 Learning Progress")

        st.info(
            "Student analytics coming soon."
        )



    elif menu == "Profile":

        st.header("👤 Student Profile")

        st.write(
            st.session_state.email
        )



    # Logout

    if st.sidebar.button("Logout"):


        st.session_state.logged_in = False

        st.session_state.email = ""

        st.session_state.pdf_text = ""

        st.rerun()



# ==========================
# Login / Register
# ==========================

else:


    col1,col2 = st.columns(2)



    with col1:


        st.markdown(
            """

<div class="card">

<h2>
🚀 Platform Features
</h2>


<ul>

<li>AI Personalized Learning</li>

<li>PDF Based AI Tutor</li>

<li>LLM Question Answering</li>

<li>Automatic Assessment</li>

<li>Learning Analytics</li>

</ul>

</div>

""",
        unsafe_allow_html=True
        )



    with col2:


        option = st.selectbox(
            "Select Option",
            [
                "Login",
                "Register"
            ]
        )



        # Register

        if option == "Register":


            st.subheader(
                "Create Account"
            )


            name = st.text_input(
                "Name"
            )


            email = st.text_input(
                "Email"
            )


            password = st.text_input(
                "Password",
                type="password"
            )


            if st.button(
                "Register"
            ):


                result = register_user(
                    name,
                    email,
                    password
                )


                if result:

                    st.success(
                        "Account created successfully"
                    )


                else:

                    st.error(
                        "Email already exists"
                    )



        # Login

        else:


            st.subheader(
                "Login"
            )


            email = st.text_input(
                "Email"
            )


            password = st.text_input(
                "Password",
                type="password"
            )


            if st.button(
                "Login"
            ):


                result = login_user(
                    email,
                    password
                )


                if result:


                    st.session_state.logged_in = True

                    st.session_state.email = email

                    st.rerun()



                else:

                    st.error(
                        "Invalid email or password"
                    )