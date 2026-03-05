import streamlit as st
import projects

# Page Configuration

st.set_page_config(page_title="Tushar Patil | Portfolio", layout="wide")
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Section Headers */
h1, h2, h3 {
    color: #f1f5f9;
}

/* Navbar spacing */
div.row-widget.stRadio > div {
    justify-content: center;
}

/* Skill boxes */
.skill-box {
    background-color: #1e293b;
    color: white;
    padding: 14px;
    border-radius: 10px;
    text-align: center;
    font-weight: 600;
    margin-bottom: 10px;
    border: 1px solid #334155;
    transition: 0.25s;
}

.skill-box:hover {
    background-color: #3b82f6;
    transform: scale(1.04);
}

/* Section titles */
.section-title {
    font-size:18px;
    font-weight:700;
    margin-top:10px;
    margin-bottom:8px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HIDE SIDEBAR NAV ---------- #
hide_sidebar = """
<style>
[data-testid="stSidebarNav"] {display: none;}
</style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

#-------------CSS---------------#
st.markdown("""
<style>

.skill-box {
    background-color: #1f2937;
    color: white;
    padding: 14px;
    border-radius: 10px;
    text-align: center;
    font-weight: 600;
    margin-bottom: 10px;
    border: 1px solid #374151;
    transition: 0.3s;
}

.skill-box:hover {
    background-color: #2563eb;
    transform: scale(1.03);
}

.section-title {
    font-size:18px;
    font-weight:700;
    margin-top:10px;
    margin-bottom:8px;
}

</style>
""", unsafe_allow_html=True)


# ---------- NAVBAR ---------- #
tab1, tab2 = st.tabs(["🏠 Home", "📁 Projects"])

# ================= HOME PAGE ================= #
with tab1:

    st.markdown("""
    <div style='text-align:center; padding:30px 0;'>
    <h1 style='margin-bottom:0;'>Tushar Patil</h1>
    <p style='font-size:18px; color:gray;'>
    Data Analyst | Python | SQL | Machine Learning
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience
    st.header("💼 Experience")
    st.write("7 months experience in Data Analysis projects and practical implementations.")

    st.markdown("---")
    # Title Section

    st.write("""
    I specialize in transforming raw data into actionable intelligence.
    With experience across data preprocessing, visualization, and predictive modeling,
    I focus on building analytical solutions that solve real-world problems and
    support data-driven strategies.

    My work involves handling messy datasets, uncovering meaningful patterns,
    and developing models that enhance decision-making processes. I am continuously
    expanding my expertise in data science, exploring advanced analytics and machine
    learning techniques to build scalable and impactful data solutions.
    """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    # -------- LEFT COLUMN (Education) -------- #
    with col1:
        st.header("🎓 Education")

        st.markdown("### Master of Computer Applications (MCA)")
        st.write("Medi Caps University, Indore")
        st.write("2022 - 2024")

        st.markdown("### Bachelor of Computer Applications (BCA)")
        st.write("Shri Shankaracharya Mahavidyalaya, Durg")
        st.write("2019 - 2022")

# -------- RIGHT COLUMN (Skills) -------- #
    with col2:
        st.header("🛠 Technical Skills")

        st.markdown('<div class="section-title">Programming</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="skill-box">Python</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="skill-box">SQL</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-title">Libraries</div>', unsafe_allow_html=True)

        c3, c4 = st.columns(2)
        with c3:
            st.markdown('<div class="skill-box">Pandas</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-box">Matplotlib</div>', unsafe_allow_html=True)

        with c4:
            st.markdown('<div class="skill-box">NumPy</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-box">Seaborn</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-title">Data Skills</div>', unsafe_allow_html=True)

        c5, c6 = st.columns(2)
        with c5:
            st.markdown('<div class="skill-box">Data Cleaning</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-box">EDA</div>', unsafe_allow_html=True)

        with c6:
            st.markdown('<div class="skill-box">Data Visualization</div>', unsafe_allow_html=True)
            st.markdown('<div class="skill-box">Machine Learning</div>', unsafe_allow_html=True)
    
    #------Certifications--------#
    st.markdown("---")
    st.header("📜 Certifications")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="skill-box">
        🐍 <b>Python Certification Course</b><br>
        Seed IT Solution (2022)
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="skill-box">
        📊 <b>Data Science Certification</b><br>
        Cisco (2024)
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="skill-box">
        🤖 <b>Introduction to Machine Learning</b><br>
        Kaggle (2024)
        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="skill-box">
        🧠 <b>Introduction to Deep Learning</b><br>
        Kaggle (2024)
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="skill-box">
        📈 <b>Data Science Course</b><br>
        CodeWithHarry (2026)
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    # Contact


    st.markdown("""
    <div style='text-align:center; padding:10px;'>

    <p>© 2026 Tushar Patil</p>

    <p>
    <a href="https://github.com/Tushar-Patil28" target="_blank">GitHub</a> |
    <a href="https://www.linkedin.com/in/tushar-patil-698766277" target="_blank">LinkedIn</a>
    </p>



    </div>
    """, unsafe_allow_html=True)
    


# ================= PROJECTS PAGE ================= #
with tab2:

    projects.show_projects()




st.markdown("---")







