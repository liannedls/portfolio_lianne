import streamlit as st

# Set page configuration
st.set_page_config(page_title="Lianne de la Salle - Software Developer", page_icon=":computer:", layout="wide")

# Inject Custom CSS
st.markdown("""
    <style>
        /* Customize the sidebar */
        [data-testid="stSidebar"] {
            background-color: #2E3B4E !important;
            color: white !important;
        }

        /* Change title font and color */
        .title {
            font-size: 3rem !important;
            color: #4CAF50;
            font-weight: bold;
            text-align: center;
        }

        /* Change background color */
        body {
            background-color: #F5F5F5 !important;
        }

        /* Style buttons */
        .stButton>button {
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 16px !important;
            border-radius: 10px !important;
            padding: 10px !important;
        }

        .stButton>button:hover {
            background-color: #388E3C !important;
        }

        /* Style headers */
        h1, h2, h3 {
            color: #2E3B4E !important;
        }

        /* Center text */
        .center-text {
            text-align: center !important;
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
    <div class="center-text">
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
    
    # Add more projects as needed...

# Contact Page
elif selection == "Contact":
    st.title("Contact Me")
    st.markdown("""
    Feel free to reach out to me for collaborations, opportunities, or any questions you may have!
    
    **Email**: [lianne@example.com] (Update with your email)  
    **LinkedIn**: [Lianne de la Salle](https://www.linkedin.com/in/lianne-de-la-salle-72b51999?originalSubdomain=ca)  
    **GitHub**: [GitHub Profile](https://github.com/yourusername)
    """)

