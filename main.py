import streamlit as st

# Set page configuration
st.set_page_config(page_title="Lianne de la Salle - Software Developer", page_icon=":computer:", layout="wide")

# Inject Custom CSS for Dark Mode with New Palette
st.markdown("""
    <style>
        /* Dark background */
        body {
            background-color: #432E54 !important; /* Deep Violet */
            color: #E8BCB9 !important; /* Soft Teal */
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #4B4376 !important; /* Rich Purple */
            color: #E8BCB9 !important;
        }

        /* Sidebar Radio Button Styling */
        div[data-baseweb="radio"] > div {
            color: #E8BCB9 !important; /* Teal Accent */
        }

        div[data-baseweb="radio"] > div:hover {
            color: #AE445A !important; /* Vibrant Indigo on Hover */
        }

        /* Title Styling */
        .title {
            font-size: 2.8rem !important;
            color: #E8BCB9 !important; /* Teal Accent */
            font-weight: bold;
            text-align: center;
        }

        /* Buttons */
        .stButton>button {
            background-color: #AE445A !important; /* Vibrant Indigo */
            color: #E8BCB9 !important;
            font-size: 16px !important;
            border-radius: 8px !important;
            padding: 10px !important;
            width: 100%;
        }

        .stButton>button:hover {
            background-color: #E8BCB9 !important; /* Soft Teal Hover */
            color: #432E54 !important; /* Dark Contrast */
        }

        .st-av {
            background-color: #E8BCB9 !important;
        }

        /* Headers */
        h1, h2, h3 {
            color: #E8BCB9 !important; /* Teal Accent */
        }

        /* Contact Form */
        .contact-box {
            background: #4B4376;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.1);
            width: 60%;
            margin: auto;
        }

        .contact-box h3 {
            color: #AE445A;
            text-align: center;
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = ["Home", "About Me", "Education & Courses", "Skills", "Projects", "Contact"]
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
    
    **Experience**:
    - Software Developer at [Company Name] (Dates)
    - [Other relevant work experience or internships]
    """)

# Education & Courses Page
elif selection == "Education & Courses":
    st.title("Education & Courses")
    
    st.header("🎓 Education")
    st.markdown("""
    - **Bachelor's in Computer Science** - [Your University Name], [Graduation Year]
    - [Add any other degrees or diplomas here]
    """)

    st.header("📚 Online Courses & Certifications")
    st.markdown("""
    - **Full-Stack Web Development** - [Platform Name] (e.g., Coursera, Udemy)
    - **Machine Learning Basics** - [Platform Name]
    - **Cloud Computing with AWS** - [Platform Name]
    - [Add any other relevant certifications]
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
    
    st.header("Project 1: Portfolio Website")
    st.markdown("""
    A personal portfolio website showcasing my skills and projects, built using Streamlit. It's responsive and designed to present my work in an engaging way.
    
    **Technologies Used**: Streamlit, Python, GitHub Pages  
    **Link**: [GitHub Link](https://github.com/yourusername/portfolio)
    """)
    
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
