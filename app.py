import streamlit as st

st.set_page_config(page_title="Archana Senthil | Portfolio", layout="wide")

# -------------------------------
# Custom CSS Styling
# -------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #f5f7fa, #c3cfe2);
}

.main {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
}

h1 {
    color: #2c3e50;
    text-align: center;
}

h2 {
    color: #34495e;
    border-bottom: 2px solid #6c63ff;
    padding-bottom: 5px;
}

.stMarkdown {
    font-size: 16px;
}

.section-card {
    background-color: #f9f9ff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.title("🎓 Student Portfolio")

# -------------------------------
# Section 1 – Student Profile
# -------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("👩‍💻 Student Profile")

st.subheader("Archana Senthil")
st.write("Aspiring Software Developer | Pursuing B.Tech in Computer Science Engineering at SRM University, Tiruchirappalli")
st.write("**Roll Number:** RA2411003050008")
st.write("**Email:** archanasenthil2607@gmail.com")

st.write("### Skills")
st.markdown("""
- Python  
- C++    
- HTML & CSS  
- Streamlit  
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# Section 2 – Academic Details
# -------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("📚 Academic Details")

st.write("### Semester Results")
st.table({
    "Semester": ["Semester 1", "Semester 2", "Semester 3"],
    "CGPA / Percentage": ["8.5 CGPA", "8.6 CGPA", "9.5 CGPA"]
})
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# Section 3 – Projects
# -------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("💻 Project")

st.subheader("Virtual Memory Management System")

st.write("""
A system that simulates paging and page replacement algorithms 
to demonstrate efficient memory allocation and page fault handling 
in operating systems.
""")

st.write("**Tools Used:** Python, Tkinter, SQL, VS Code")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# Section 4 – Certifications
# -------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("📜 Certifications")

certifications = [
    {"Course": "Learnathon'25: Learn AI and Gen AI Basics", "Platform": "Microsoft", "Date": "Oct 2025"},
    {"Course": "Java Programming for Beginners", "Platform": "Coursera", "Date": "Oct 2025"},
    {"Course": "MongoDB Basics for Students", "Platform": "MongoDB", "Date": "Jun 2025"},
    {"Course": "MATLAB Onramp", "Platform": "MathWorks", "Date": "Oct 2024"}
]

for cert in certifications:
    st.markdown(f"""
    **Course Name:** {cert['Course']}  
    **Platform:** {cert['Platform']}  
    **Date:** {cert['Date']}  
    """)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# Section 5 – Internship
# -------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("🏢 Internship")

internships = [
    {
        "Company": "Bluestock Fintech",
        "Duration": "May 2025 – June 2025",
        "Work": "Worked as Software Development Engineer."
    },
    {
        "Company": "Eduskills",
        "Duration": "Oct 2025 – Dec 2025",
        "Work": "Python Full Stack Developer Virtual Internship."
    }
]

for intern in internships:
    st.markdown(f"""
    **Company Name:** {intern['Company']}  
    **Duration:** {intern['Duration']}  
    **Work Done:** {intern['Work']}  
    """)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# Section 6 – Achievements
# -------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("🏆 Achievements")

st.write("### Events Organised")
st.markdown("""
- Organized SFLC x FOSS Workshop  
- Organizer of Yuva 24-hour Hackathon 2025  
""")

st.write("### Competitions")
st.markdown("""
- Participated in Noob Hackfest 2025  
""")
st.markdown('</div>', unsafe_allow_html=True)

st.success("✨ Thank you for visiting my portfolio!")