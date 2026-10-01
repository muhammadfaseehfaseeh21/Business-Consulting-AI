import streamlit as st

from crew import run_business_consulting


# PAGE CONFIGURATION

st.set_page_config(
    page_title="Business Consulting AI",
    page_icon="💼",
    layout="wide"
)


# CUSTOM UI

st.markdown("""
<style>

.stApp {
    background: #ffffff;
}

h1, h2, h3, h4, p, label, li, td, th, span {
    color: #111827 !important;
}

.stButton > button {
    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color: white !important;
    border-radius: 10px;
    border: none;
    padding: 12px;
    font-weight: bold;
}

.stButton > button p {
    color: white !important;
}

.stButton > button:hover {
    background: #4f46e5;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# HEADER

st.title("💼 Business Consulting AI")

st.subheader(
    "Your AI-Powered Multi-Agent Business Strategy Team"
)

st.write(
    "Six AI consultants collaborate to analyze your business "
    "and generate a professional strategy report."
)

st.divider()


# BUSINESS INPUT

st.header("📋 Business Information")

col1, col2 = st.columns(2)

with col1:

    business_name = st.text_input(
        "Business Name",
        placeholder="Example: SmartLearn AI"
    )

    industry = st.selectbox(
        "Industry",
        [
            "Technology",
            "Education",
            "Healthcare",
            "E-commerce",
            "Food & Beverage",
            "Real Estate",
            "Finance",
            "Other"
        ]
    )

    target_market = st.text_input(
        "Target Customers",
        placeholder="Example: University students"
    )


with col2:

    country = st.text_input(
        "Country / Region",
        placeholder="Example: Pakistan"
    )

    budget = st.selectbox(
        "Startup Budget",
        [
            "Under $1,000",
            "$1,000 - $5,000",
            "$5,000 - $10,000",
            "$10,000 - $50,000",
            "Above $50,000"
        ]
    )

    objective = st.selectbox(
        "Business Objective",
        [
            "Launch a new business",
            "Grow an existing business",
            "Increase revenue",
            "Improve marketing",
            "Reduce operational costs",
            "Expand into a new market"
        ]
    )


business_idea = st.text_area(
    "Describe Your Business Idea",

    placeholder=(
        "Explain your product or service, "
        "customer problem, and business goals..."
    ),

    height=150
)


# GENERATE REPORT

st.divider()

st.header("🚀 Generate Business Strategy")

if st.button(
    "Generate Consulting Report",
    use_container_width=True
):

    if not business_name.strip():
        st.warning("Please enter your business name.")

    elif not business_idea.strip():
        st.warning("Please describe your business idea.")

    elif not target_market.strip():
        st.warning("Please enter your target customers.")

    elif not country.strip():
        st.warning("Please enter your country.")

    else:

        business_info = f"""
        Business Name: {business_name}

        Industry: {industry}

        Business Idea: {business_idea}

        Target Market: {target_market}

        Country: {country}

        Startup Budget: {budget}

        Business Objective: {objective}
        """

        try:

            with st.spinner(
                "🤖 Six AI consultants are working..."
            ):

                report = run_business_consulting(
                    business_info
                )

            st.success("Business Strategy Generated!")

            st.divider()

            st.header("📊 Your Business Strategy Report")

            st.markdown(report)

            st.download_button(
                label="📥 Download Business Report",
                data=report,
                file_name="business_strategy_report.md",
                mime="text/markdown",
                use_container_width=True
            )

        except Exception as e:

            st.error("An error occurred while generating the report.")

            st.code(str(e))


# FOOTER

st.divider()

st.caption(
    "Business Consulting AI | Powered by CrewAI, Groq and Streamlit"
)
