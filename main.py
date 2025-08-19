import streamlit as st
import plotly.graph_objects as go
from prediction_helper import predict  # Ensure this is correctly linked

# ======================
# ⚙️ Page Config
# ======================
st.set_page_config(
    page_title="Credit Risk Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================
# 🎨 Custom CSS Styling
# ======================
st.markdown("""
<style>
    .main { padding-top: 1.2rem; font-family: 'Inter', sans-serif; }
    .stApp { 
        background: linear-gradient(160deg, #f1f5f9 0%, #e2e8f0 50%, #f9fafb 100%);
        color: #1e293b; 
    }

    /* Typography */
    h1 { font-size: 2rem !important; font-weight: 800 !important; margin-bottom: 0.5rem !important; }
    h2 { font-size: 1.4rem !important; font-weight: 700 !important; margin: 1rem 0 0.6rem 0 !important; }
    h3 { font-size: 1.05rem !important; font-weight: 600 !important; margin-bottom: 0.4rem !important; }
    p, label, .stMarkdown { font-size: 0.95rem !important; }

    /* Header */
    .title-container {
        background: linear-gradient(90deg, #1e3a8a, #2563eb, #0ea5e9, #10b981);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 1.5rem;
        color: white !important;
        box-shadow: 0 8px 18px rgba(0,0,0,0.25);
    }
    .title-container p { font-size: 1rem !important; opacity: 0.9; margin-top: 0.4rem; }

    /* Sections */
    .input-section {
        background: #f8fafc;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #e2e8f0;
        box-shadow: 0 3px 8px rgba(0,0,0,0.05);
    }

    /* Result Cards */
    .result-card {
        border-radius: 14px;
        padding: 1.3rem;
        text-align: center;
        color: white;
        min-height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 6px 16px rgba(0,0,0,0.18);
    }
    .result-card h3 { font-size: 1rem !important; font-weight: 600 !important; margin-bottom: 0.6rem; white-space: nowrap; }
    .result-card h1 { font-size: 1.8rem !important; font-weight: 800 !important; margin: 0.4rem 0; white-space: nowrap; }
    .result-card p { font-size: 0.9rem; margin: 0; opacity: 0.95; }

    .result-success { background: linear-gradient(135deg, #16a34a, #22c55e); }
    .result-warning { background: linear-gradient(135deg, #f59e0b, #facc15); }
    .result-danger  { background: linear-gradient(135deg, #dc2626, #ef4444); }
    .result-info    { background: linear-gradient(135deg, #2563eb, #3b82f6); }

    /* Sidebar */
    .stSidebar { 
        background: linear-gradient(180deg, #1e293b, #334155) !important;
        color: white !important;
    }
    .stSidebar h2, .stSidebar h3, .stSidebar p, .stSidebar li, .stSidebar div {
        color: white !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #6366f1) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.7rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 4px 12px rgba(99,102,241,0.35);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8, #2563eb) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 18px rgba(59,130,246,0.5);
    }

    /* Insights */
    .insight-card {
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin: 0.7rem 0;
        font-weight: 500;
        background: #ffffff;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .insight-card h4 {
        margin: 0 0 0.4rem 0;
        font-size: 1rem;
        font-weight: 700;
    }
    .insight-good { border-left: 6px solid #10b981; color: #065f46; background: #ecfdf5; }
    .insight-warning { border-left: 6px solid #f59e0b; color: #92400e; background: #fffbeb; }
    .insight-bad { border-left: 6px solid #ef4444; color: #991b1b; background: #fef2f2; }

    /* Footer */
    .footer-section { text-align: center; margin-top: 2rem; }
    .footer-section h4 { font-weight: 700; color: #1f2937 !important; }
    .footer-section p { font-size: 0.85rem; color: #475569 !important; }
</style>
""", unsafe_allow_html=True)

# ======================
# 🎯 Title
# ======================
st.markdown("""
<div class="title-container">
    <h1>📊 Credit Risk Analysis Dashboard</h1>
    <p>AI-powered credit risk assessment with actionable financial recommendations</p>
</div>
""", unsafe_allow_html=True)

# ======================
# 📊 Sidebar
# ======================
with st.sidebar:
    st.markdown("## Dashboard Info")
    st.info("This dashboard uses ML models to assess credit risk.")

    st.markdown("## Risk Categories")
    st.success("🟢 Excellent: 750-900")
    st.info("🔵 Good: 650-750") 
    st.warning("🟡 Average: 500-650")
    st.error("🔴 Poor: 300-500")

# ======================
# 📝 Inputs
# ======================
st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown("## Applicant Information")

c1, c2, c3 = st.columns(3)
with c1: age = st.number_input("🎂 Age", 18, 100, 28)
with c2: residence_type = st.selectbox("🏠 Residence Type", ["Owned","Rented","Mortgage"])
with c3: num_open_accounts = st.number_input("📂 Open Accounts", 1, 10, 2)

c1, c2, c3 = st.columns(3)
with c1: income = st.number_input("💵 Annual Income (₹)", min_value=0, value=1200000)
with c2: loan_amount = st.number_input("🏦 Loan Amount (₹)", min_value=0, value=2560000)
with c3: loan_tenure = st.number_input("⏳ Loan Tenure (months)", 1, 360, 36)

if income > 0:
    loan_to_income = loan_amount / income
    emi = loan_amount / loan_tenure if loan_tenure>0 else 0
    emi_percent = (emi/(income/12))*100
    d1, d2, d3 = st.columns(3)
    with d1: st.metric("Loan-to-Income", f"{loan_to_income:.2f}")
    with d2: st.metric("Monthly EMI", f"₹{emi:,.0f}")
    with d3: st.metric("EMI-to-Income %", f"{emi_percent:.1f}%")

c1, c2, c3 = st.columns(3)
with c1: avg_dpd = st.number_input("📌 Avg Days Past Due", 0, 100, 20)
with c2: delinquency = st.number_input("⚠️ Delinquency Ratio (%)", 0, 100, 30)
with c3: utilization = st.number_input("📊 Credit Utilization (%)", 0, 100, 30)

c1, c2 = st.columns(2)
with c1: purpose = st.selectbox("🎯 Loan Purpose", ["Education","Home","Auto","Personal"])
with c2: ltype = st.selectbox("🔐 Loan Type", ["Unsecured","Secured"])
st.markdown('</div>', unsafe_allow_html=True)

# ======================
# 🚀 Prediction
# ======================
st.markdown("---")
_, mid, _ = st.columns([1,2,1])
with mid:
    if st.button("🚀 Analyze Credit Risk", use_container_width=True):
        try:
            prob, score, rating = predict(
                age, income, loan_amount, loan_tenure,
                avg_dpd, delinquency/100, utilization/100,
                num_open_accounts, residence_type, purpose, ltype
            )

            st.markdown("## Risk Assessment Results")
            r1, r2, r3 = st.columns(3)

            def card_class(val, type="rating"):
                if type=="rating":
                    return "result-success" if val in ["Excellent","Good"] else "result-warning" if val=="Average" else "result-danger"
                if type=="score":
                    return "result-success" if val>=750 else "result-warning" if val>=500 else "result-danger"

            with r1:
                st.markdown(f"""
                <div class="result-card result-info">
                    <h3>📉 Default Probability</h3>
                    <h1>{prob:.1%}</h1>
                    <p>Likelihood of Default</p>
                </div>
                """, unsafe_allow_html=True)
            with r2:
                st.markdown(f"""
                <div class="result-card {card_class(score,'score')}">
                    <h3>💳 Credit Score</h3>
                    <h1>{score}</h1>
                    <p>Range 300-900</p>
                </div>
                """, unsafe_allow_html=True)
            with r3:
                st.markdown(f"""
                <div class="result-card {card_class(rating)}">
                    <h3>⭐ Credit Rating</h3>
                    <h1>{rating}</h1>
                    <p>Overall Quality</p>
                </div>
                """, unsafe_allow_html=True)

            # Gauge
            st.markdown("### Risk Visualization")
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prob*100,
                title={'text': "Default Risk %"},
                gauge={
                    'axis': {'range':[0,100]},
                    'bar': {'color': "#1d4ed8"},
                    'steps': [
                        {'range':[0,20],'color':"#bbf7d0"},
                        {'range':[20,50],'color':"#fde68a"},
                        {'range':[50,100],'color':"#fecaca"}
                    ]
                }
            ))
            fig.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)

            # ======================
            # 💡 Recommendations
            # ======================
            st.markdown("## 📌 Recommendations")

            def rec_card(style, title, text):
                st.markdown(f"""
                <div class="insight-card {style}">
                    <h4>{title}</h4>
                    <p>{text}</p>
                </div>
                """, unsafe_allow_html=True)

            if rating=="Excellent":
                rec_card("insight-good", "Approval Decision", "✅ Low risk. Loan can be approved confidently at standard terms.")
                rec_card("insight-good", "Risk Controls", "Maintain current credit utilization below 30% and continue timely repayments.")
                rec_card("insight-good", "Improvement Actions", "Explore premium loan products for better benefits as risk remains minimal.")

            elif rating=="Good":
                rec_card("insight-good", "Approval Decision", "✅ Good profile. Loan can be sanctioned with favorable terms.")
                rec_card("insight-warning", "Risk Controls", "Monitor utilization closely and ensure delinquency ratio stays below 20%.")
                rec_card("insight-warning", "Improvement Actions", "Lower utilization <25% and reduce overdue payments to reach Excellent rating.")

            elif rating=="Average":
                rec_card("insight-warning", "Approval Decision", "⚠️ Moderate risk. Loan approval only with stricter monitoring or reduced amount.")
                rec_card("insight-warning", "Risk Controls", "Cap EMI-to-Income ratio at 40% by reducing loan amount or increasing tenure.")
                rec_card("insight-warning", "Improvement Actions", "Improve repayment behavior by reducing Avg DPD below 15 days.")

            else:  # Poor
                rec_card("insight-bad", "Approval Decision", "❌ High risk. Loan should not be approved without collateral or guarantor.")
                rec_card("insight-bad", "Risk Controls", "Insist on security cover and reduce exposure to unsecured lending.")
                rec_card("insight-bad", "Improvement Actions", "Clear overdue balances, lower utilization drastically, and build 6-12 months of repayment history before reapplying.")

        except Exception as e:
            st.error(f"Error: {e}")

# ======================
# 🔻 Footer
# ======================
st.markdown("---")
st.markdown("""
<div class="footer-section">
    <h4>🏦 Credit Risk Analysis Dashboard</h4>
    <p>Built by SHRINIVASS RAJU</p>
</div>
""", unsafe_allow_html=True)
