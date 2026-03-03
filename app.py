import streamlit as st
import projects

# Page Configuration
st.set_page_config(page_title="Tushar Patil | Data Analyst", layout="wide")
st.set_page_config(page_title="Tushar Patil | Portfolio", layout="wide")

# ---------- HIDE SIDEBAR NAV ---------- #
hide_sidebar = """
<style>
[data-testid="stSidebarNav"] {display: none;}
</style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)


# ---------- NAVBAR ---------- #
page = st.radio("", ["Home", "Projects"], horizontal=True)


# ================= HOME PAGE ================= #
if page == "Home":

    st.title("Tushar Patil")
    st.subheader("Data Science & Analytics Enthusiast | Python | SQL | Machine Learning")

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

        st.markdown("### Programming")
        st.write("• Python")
        st.write("• SQL")

        st.markdown("### Libraries")
        st.write("• Pandas")
        st.write("• NumPy")
        st.write("• Matplotlib")
        st.write("• Seaborn")

        st.markdown("### Data Skills")
        st.write("• Data Cleaning")
        st.write("• Data Visualization")
        st.write("• Exploratory Data Analysis")
        st.write("• Machine Learning")

    # Experience
    st.header("💼 Experience")
    st.write("7 months experience in Data Analysis projects and practical implementations.")

    st.markdown("---")

    # Contact
    st.header("📫 Contact")
    st.write("📧 Email: tusharpatil0227@gmail.com")
    st.write("🔗 LinkedIn: www.linkedin.com/in/tushar-patil-698766277")
    st.write("💻 GitHub:[github.com/Tushar-Patil28](https://github.com/Tushar-Patil28)")
    


# ================= PROJECTS PAGE ================= #
elif page == "Projects":

    projects.show_projects()




st.markdown("---")







