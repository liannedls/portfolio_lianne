import streamlit as st

# Set page configuration
st.set_page_config(page_title="Lianne de la Salle - Software Developer", page_icon=":computer:", layout="wide")

# Inject Custom CSS for the Soft Pastel Color Palette
st.markdown("""
    <style>
        /* Set background color */
        body {
            background-color: #BDDDE4 !important; /* Soft muted pink */
        }

        /* Customize the sidebar */
        [data-testid="stSidebar"] {
            background-color: #9EC6F3 !important; /* Light purple */
            color: #333 !important;
        }

        /* Title Styling */
        .title {
            font-size: 2.8rem !important;
            color: #9FB3DF !important; /* Soft blue */
            font-weight: bold;
            text-align: center;
        }

        /* Style buttons */
        .stButton>button {
            background-color: #FFF1D5 !important; /* Soft beige */
            color: #4A4A4A !important;
            font-size: 16px !important;
            border-radius: 8px !important;
            padding: 10px !important;
            width: 100%;
        }

        .stButton>button:hover {
            background-color: #F4E3C1 !important; /* Slightly darker beige */
        }

        /* Style headers */
        h1, h2, h3 {
            color: #9FB3DF !important; /* Soft blue */
        }

        /* Contact Form Styling */
        .contact-box {
            background: #FFF1D5;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            width: 60%;
            margin: auto;
        }

        .contact-box h3 {
            color: #9FB3DF;
            text-align: center;
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = ["Home", "About Me", "Skills", "Projects", "Contact"]
selection = st.sidebar.radio("Go to", pages)

# Home Page
if selection == "Home":
    st.markdown('<h1 class="title">Welcome to My Portfolio!</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center;">
        <p>Hello, I'm <b>Lianne de la Salle</b>, a passionate Software Developer with experience in building innovative and scalable software applications.</p>
        <p>I'm excited to share my journey with you. Explore the sections below to know more about me, my skills, and my projects.</p>
    </div>
    """, unsafe_allow_html=True)

# About Me Page
elif selection == "About Me":
    st.title("About Me")
    st.markdown("""
    Hi! I'm **Lianne de la Salle**, a Software Developer with a background in Computer Science. 
    I specialize in full-stack development and am passionate about building web applications that are both functional and user-friendly.
    
    **Education**:
    - Bachelor's in Computer Science, [University Name] (Update with your university details)
    - [Any certifications or bootcamps you've completed]
    
    **Experience**:
    - Software Developer at [Company Name] (Dates)
    - [Other relevant work experience or internships]
    """)

# Skills Page
elif selection == "Skills":
    st.title("Skills")
    st.markdown("""
    I have experience with a variety of programming languages and technologies. Here are some of the skills I bring to the table:
    
    **Languages**:
    - Python, JavaScript, Java, C++
    
    **Web Development**:
    - HTML, CSS, JavaScript (React, Vue.js)
    
    **Databases**:
    - MySQL, PostgreSQL, MongoDB
    
    **Tools & Frameworks**:
    - Docker, Kubernetes, AWS, Git, Flask, Django, Node.js
    
    **Other**:
    - Agile Methodology, REST APIs, Unit Testing
    """)

# Projects Page
elif selection == "Projects":
    st.title("Projects")
    
    # Example project 1
    st.header("Project 1: Portfolio Website")
    st.markdown("""
    A personal portfolio website showcasing my skills and projects, built using Streamlit. It's responsive and designed to present my work in an engaging way.
    
    **Technologies Used**: Streamlit, Python, GitHub Pages  
    **Link**: [GitHub Link](https://github.com/yourusername/portfolio)
    """)
    
    # Example project 2
    st.header("Project 2: E-commerce Application")
    st.markdown("""
    An e-commerce platform built using React for the front end and Node.js for the backend. It includes user authentication, product catalog, and shopping cart functionality.
    
    **Technologies Used**: React, Node.js, Express, MongoDB  
    **Link**: [GitHub Link](https://github.com/yourusername/e-commerce-app)
    """)

# Contact Page
elif selection == "Contact":
    st.title("Contact Me")
    
    st.markdown("""
    <div class="contact-box">
        <h3>Let's Connect!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        submit_button = st.form_submit_button(label="Send Message")

    if submit_button:
        if name and email and message:
            st.success(f"Thank you, {name}! Your message has been received. I'll get back to you soon.")
        else:
            st.error("Please fill out all fields before submitting.")

