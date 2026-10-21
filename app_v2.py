import streamlit as st
import re
from urllib.parse import urlparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ============================================================
# JOBSHIELD AI 2.0
# AI + CYBERSECURITY FAKE JOB / INTERNSHIP SCAM DETECTOR
# ============================================================

st.set_page_config(
    page_title="JobShield AI 2.0",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# FUTURISTIC CYBERSECURITY UI
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(0, 220, 255, 0.08), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(90, 70, 255, 0.10), transparent 25%),
        linear-gradient(135deg, #050914 0%, #08101f 45%, #030712 100%);
    color: #f5f7ff;
}

/* Main container */
.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Header */
.hero {
    padding: 28px 32px;
    border-radius: 24px;
    background:
        linear-gradient(135deg, rgba(8,20,40,.95), rgba(8,16,30,.90));
    border: 1px solid rgba(0, 220, 255, .25);
    box-shadow:
        0 0 40px rgba(0, 200, 255, .08),
        inset 0 0 30px rgba(0, 200, 255, .025);
    margin-bottom: 25px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #ffffff;
}

.hero-title span {
    color: #00e5ff;
    text-shadow: 0 0 18px rgba(0,229,255,.45);
}

.hero-sub {
    color: #91a4c5;
    font-size: 15px;
    margin-top: 5px;
}

.badge {
    display: inline-block;
    margin-top: 16px;
    padding: 7px 14px;
    border-radius: 20px;
    background: rgba(0,229,255,.08);
    border: 1px solid rgba(0,229,255,.3);
    color: #00e5ff;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
}

/* Section */
.section-title {
    font-size: 21px;
    font-weight: 800;
    color: #ffffff;
    margin: 20px 0 12px 0;
}

/* Cards */
.cyber-card {
    background: rgba(12, 23, 42, .86);
    border: 1px solid rgba(130, 160, 210, .16);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 12px 35px rgba(0,0,0,.20);
    height: 100%;
}

.cyber-card:hover {
    border-color: rgba(0,229,255,.30);
}

/* Metric */
.metric-card {
    background: linear-gradient(145deg, rgba(13,29,50,.95), rgba(8,17,32,.95));
    border-radius: 18px;
    border: 1px solid rgba(0,229,255,.14);
    padding: 20px;
    text-align: center;
    box-shadow: 0 0 25px rgba(0,200,255,.04);
}

.metric-label {
    color: #8195b7;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
}

.metric-value {
    font-size: 31px;
    font-weight: 800;
    margin-top: 5px;
    color: #ffffff;
}

/* Risk */
.risk-high {
    color: #ff5263;
    text-shadow: 0 0 20px rgba(255,82,99,.35);
}

.risk-medium {
    color: #ffbd4a;
    text-shadow: 0 0 20px rgba(255,189,74,.25);
}

.risk-low {
    color: #43e6a4;
    text-shadow: 0 0 20px rgba(67,230,164,.25);
}

/* Evidence */
.evidence {
    padding: 12px 15px;
    border-radius: 12px;
    background: rgba(255,255,255,.035);
    border-left: 4px solid #ff5263;
    margin: 8px 0;
}

.evidence-medium {
    border-left-color: #ffbd4a;
}

/* Pipeline */
.pipeline {
    text-align: center;
    padding: 18px 8px;
    border-radius: 15px;
    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.08);
}

.pipeline-icon {
    font-size: 26px;
}

.pipeline-text {
    font-size: 11px;
    color: #a8b6ce;
    margin-top: 6px;
    font-weight: 700;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #050b16;
    border-right: 1px solid rgba(0,229,255,.10);
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    border: 1px solid rgba(0,229,255,.28);
    background: linear-gradient(135deg, #0a263a, #08202d);
    color: #e9fbff;
    font-weight: 700;
    min-height: 42px;
    transition: .2s;
}

.stButton > button:hover {
    border-color: #00e5ff;
    box-shadow: 0 0 20px rgba(0,229,255,.15);
    transform: translateY(-1px);
}

/* Analyze button */
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, #00a8c7, #155df5);
    border: none;
    color: white;
    font-size: 16px;
    font-weight: 800;
}

/* Text area */
textarea {
    background: #071120 !important;
    color: #f5f7ff !important;
    border: 1px solid rgba(0,229,255,.20) !important;
    border-radius: 15px !important;
}

/* Expander */
details {
    background: rgba(10,20,35,.7);
    border-radius: 14px;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 40px;
    padding: 20px;
    color: #667894;
    font-size: 11px;
    border-top: 1px solid rgba(255,255,255,.06);
}
 
 /* REMOVE STREAMLIT WHITE HEADER */
[data-testid="stHeader"] {
    display: none !important;
}

[data-testid="stToolbar"] {
    display: none !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}

/* REMOVE EMPTY TOP SPACE */
.block-container {
    padding-top: 1rem !important;
}

/* Make the main app fill the screen */
.stAppViewContainer {
    background: transparent !important;
}

.main {
    background: transparent !important;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# TRAINING DATA
# ============================================================

SCAM_EXAMPLES = [
    "pay registration fee before joining job",
    "pay processing fee to receive offer letter",
    "security deposit required for internship",
    "send money to confirm your job",
    "urgent job selected immediately pay fee",
    "work from home earn huge salary no experience",
    "send aadhaar pan bank details for verification",
    "limited seats apply immediately pay registration fee",
    "guaranteed job selection no interview",
    "contact recruiter only through whatsapp",
    "pay training fee before internship",
    "selected congratulations send documents immediately",
    "earn 50000 per month no experience required",
    "refundable registration fee required",
    "urgent internship offer apply today"
]

SAFE_EXAMPLES = [
    "software engineering internship apply through official company careers page",
    "internship includes technical interview and project discussion",
    "students can apply through university placement portal",
    "software developer internship with structured interview process",
    "company careers page lists internship requirements",
    "internship application requires resume and academic details",
    "selected candidates will attend a technical interview",
    "official recruitment process includes multiple interview rounds",
    "internship stipend will be discussed during selection",
    "apply using official company recruitment portal",
    "engineering internship for computer science students",
    "internship program includes mentorship and project work",
    "candidate should submit resume through official website",
    "job opening published on company careers page",
    "normal internship opportunity for students"
]

TRAINING_TEXTS = SCAM_EXAMPLES + SAFE_EXAMPLES
TRAINING_LABELS = [1] * len(SCAM_EXAMPLES) + [0] * len(SAFE_EXAMPLES)

vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    stop_words="english"
)

X = vectorizer.fit_transform(TRAINING_TEXTS)

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(X, TRAINING_LABELS)


# ============================================================
# SAMPLE DATA
# ============================================================

HIGH_RISK_SAMPLE = """URGENT! Work From Home Internship

Earn ₹50,000 per month with no experience required.

Congratulations! You have been selected immediately.

Pay ₹999 as a refundable registration fee to receive your offer letter.

Send your Aadhaar card and PAN card immediately for verification.

Limited vacancies available. Apply within 30 minutes!

Contact the recruiter only through WhatsApp.

Apply here:
http://192.0.2.123/urgent-job-offer
"""

MEDIUM_RISK_SAMPLE = """Work From Home Internship Opportunity

Earn up to ₹25,000 per month.

Selected candidates can start immediately.

Please contact the recruiter through WhatsApp for further details.

Complete the application today.
"""

LOW_RISK_SAMPLE = """Software Engineering Internship

Our company is offering a software engineering internship for computer science students.

Candidates should submit their resume through the official company careers portal.

The selection process includes a technical interview and project discussion.

The internship includes mentorship and project-based learning.
"""


# ============================================================
# CYBERSECURITY ANALYSIS
# ============================================================

def analyze_cybersecurity(text):

    lower = text.lower()

    score = 0
    signals = []
    evidence = []

    # Payment
    payment_patterns = [
        r"registration fee",
        r"processing fee",
        r"joining fee",
        r"security deposit",
        r"pay ₹?\s*\d+",
        r"pay rs\.?\s*\d+",
        r"payment required",
        r"pay before joining",
        r"send money",
        r"deposit"
    ]

    if any(re.search(p, lower) for p in payment_patterns):
        score += 30
        signals.append("🔴 Payment / fee request detected")

        matches = re.findall(
            r".{0,55}(registration fee|processing fee|joining fee|security deposit|pay ₹?\s*\d+|pay rs\.?\s*\d+|send money).{0,70}",
            text,
            flags=re.I
        )

        for m in matches[:3]:
            evidence.append("Payment request detected in the advertisement.")

    # Sensitive information
    sensitive_patterns = [
        "aadhaar",
        "aadhar",
        "pan card",
        "bank details",
        "bank account",
        "otp",
        "identity proof",
        "passport",
        "driving license"
    ]

    sensitive_found = [
        x for x in sensitive_patterns if x in lower
    ]

    if sensitive_found:
        score += 25
        signals.append("🔴 Sensitive personal information requested")

        for item in sensitive_found:
            evidence.append(f"Sensitive information reference: {item}")

    # Urgency
    urgency_patterns = [
        "urgent",
        "immediately",
        "apply now",
        "apply immediately",
        "limited seats",
        "limited vacancies",
        "act now",
        "today only",
        "hurry",
        "within 30 minutes",
        "within 1 hour"
    ]

    urgency_found = [
        x for x in urgency_patterns if x in lower
    ]

    if urgency_found:
        score += 15
        signals.append("🟠 Urgency / pressure language detected")

        for item in urgency_found[:3]:
            evidence.append(f"Urgency phrase: “{item}”")

    # Salary
    salary_patterns = [
        r"₹\s*(5[0-9],?000|6[0-9],?000|7[0-9],?000)",
        r"rs\.?\s*(5[0-9],?000|6[0-9],?000|7[0-9],?000)",
        r"50,000",
        r"60,000",
        r"70,000",
        "huge salary",
        "guaranteed income",
        "earn huge"
    ]

    if any(re.search(p, lower) for p in salary_patterns):
        score += 15
        signals.append("🟠 Attractive / high salary signal detected")
        evidence.append("Attractive salary claim detected.")

    # Low barrier
    low_barrier = [
        "no experience required",
        "no experience",
        "guaranteed job",
        "guaranteed selection",
        "instant joining",
        "no interview required"
    ]

    low_found = [
        x for x in low_barrier if x in lower
    ]

    if low_found:
        score += 10
        signals.append("🟠 Low-barrier / instant-selection pattern detected")

        for item in low_found[:2]:
            evidence.append(f"Recruitment pattern: “{item}”")

    # WhatsApp
    whatsapp_patterns = [
        "only through whatsapp",
        "contact only through whatsapp",
        "whatsapp recruiter",
        "contact recruiter on whatsapp"
    ]

    if any(x in lower for x in whatsapp_patterns):
        score += 10
        signals.append("🟠 WhatsApp-only recruitment pattern detected")
        evidence.append("WhatsApp-only recruitment pattern detected.")

    return min(score, 100), signals, evidence


# ============================================================
# URL ANALYSIS
# ============================================================

def analyze_urls(text):

    urls = re.findall(
        r"(https?://[^\s]+|www\.[^\s]+)",
        text,
        flags=re.I
    )

    results = []
    total_score = 0

    for raw_url in urls:

        url = raw_url.rstrip(".,);]")

        check_url = url

        if url.lower().startswith("www."):
            check_url = "http://" + url

        parsed = urlparse(check_url)

        hostname = parsed.hostname or ""

        score = 0
        reasons = []

        if parsed.scheme.lower() == "http":
            score += 10
            reasons.append("HTTP connection")

        ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

        if re.match(ip_pattern, hostname):
            score += 20
            reasons.append("IP-based URL")

        suspicious_words = [
            "verify",
            "payment",
            "fee",
            "claim",
            "offer",
            "urgent",
            "login",
            "reward"
        ]

        suspicious_found = [
            word for word in suspicious_words
            if word in hostname.lower()
        ]

        if suspicious_found:
            score += 10
            reasons.append("Suspicious keyword in hostname")

        if len(url) > 100:
            score += 5
            reasons.append("Unusually long URL")

        score = min(score, 40)

        results.append({
            "url": url,
            "score": score,
            "hostname": hostname,
            "protocol": parsed.scheme.upper(),
            "ip_based": bool(re.match(ip_pattern, hostname)),
            "suspicious": bool(suspicious_found),
            "long": len(url) > 100,
            "reasons": reasons
        })

        total_score = max(total_score, score)

    return urls, total_score, results


# ============================================================
# FULL DETECTION ENGINE
# ============================================================

def analyze_offer(text):

    X_test = vectorizer.transform([text])

    ai_probability = model.predict_proba(X_test)[0][1]

    ai_score = round(ai_probability * 100)

    cyber_score, signals, evidence = analyze_cybersecurity(text)

    urls, url_score, url_results = analyze_urls(text)

    final_score = round(
        (0.45 * ai_score) +
        (0.40 * cyber_score) +
        (0.15 * url_score)
    )

    final_score = max(0, min(final_score, 100))

    if final_score >= 70:
        risk = "HIGH"
    elif final_score >= 40:
        risk = "MEDIUM"
    else:
        risk = "LOWER"

    return {
        "ai_score": ai_score,
        "cyber_score": cyber_score,
        "url_score": url_score,
        "final_score": final_score,
        "risk": risk,
        "signals": signals,
        "evidence": evidence,
        "urls": urls,
        "url_results": url_results
    }


# ============================================================
# SESSION STATE
# ============================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "analysis_count" not in st.session_state:
    st.session_state.analysis_count = 0

if "job_input" not in st.session_state:
    st.session_state.job_input = ""


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🛡️ <span>JOBSHIELD AI</span> 2.0
</div>

<div class="hero-sub">
CYBER INTELLIGENCE PLATFORM • AI-POWERED JOB SCAM DETECTION
</div>

<div class="badge">
⚡ DETECT &nbsp; • &nbsp; EXPLAIN &nbsp; • &nbsp; WARN
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🛡️ JOBSHIELD AI 2.0")

    st.markdown("---")

    st.markdown("### 🧪 SIMULATION LAB")

    if st.button("🔴 High-Risk Internship", use_container_width=True):
        st.session_state.job_input = HIGH_RISK_SAMPLE

    if st.button("🟠 Suspicious Offer", use_container_width=True):
        st.session_state.job_input = MEDIUM_RISK_SAMPLE

    if st.button("🟢 Normal Internship", use_container_width=True):
        st.session_state.job_input = LOW_RISK_SAMPLE

    st.markdown("---")

    st.markdown("### 📡 SYSTEM STATUS")

    st.success("AI Engine ONLINE")
    st.success("Cyber Engine ONLINE")
    st.success("URL Scanner ONLINE")

    st.markdown("---")

    st.caption(
        "JobShield AI is a cybersecurity proof-of-concept. "
        "Risk scores are indicators, not proof of fraud."
    )


# ============================================================
# INPUT AREA
# ============================================================

st.markdown(
    '<div class="section-title">🔍 JOB OFFER ANALYZER</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="cyber-card">
<b>Paste a job or internship advertisement below.</b><br>
<span style="color:#8195b7">
JobShield will analyze language patterns, cybersecurity indicators and URLs.
</span>
</div>
""", unsafe_allow_html=True)

job_text = st.text_area(
    "Advertisement",
    value=st.session_state.job_input,
    height=230,
    placeholder="Paste suspicious job or internship advertisement here...",
    label_visibility="collapsed"
)

analyze = st.button(
    "⚡ ANALYZE OFFER",
    use_container_width=True
)


# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    if not job_text.strip():

        st.warning("Please enter a job or internship advertisement.")

    else:

        result = analyze_offer(job_text)

        st.session_state.analysis_count += 1

        st.session_state.history.append({
            "Scan": st.session_state.analysis_count,
            "Risk": result["risk"],
            "Score": result["final_score"],
            "AI": result["ai_score"],
            "Cyber": result["cyber_score"],
            "URL": result["url_score"]
        })

        # ----------------------------------------------------
        # THREAT ASSESSMENT
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">🚨 THREAT ASSESSMENT CENTER</div>',
            unsafe_allow_html=True
        )

        if result["risk"] == "HIGH":
            risk_class = "risk-high"
            risk_icon = "🔴"
        elif result["risk"] == "MEDIUM":
            risk_class = "risk-medium"
            risk_icon = "🟠"
        else:
            risk_class = "risk-low"
            risk_icon = "🟢"

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                f"""
                <div class="metric-card">
                <div class="metric-label">FINAL RISK SCORE</div>
                <div class="metric-value {risk_class}">
                {result["final_score"]}/100
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="metric-card">
                <div class="metric-label">AI / NLP</div>
                <div class="metric-value">
                🤖 {result["ai_score"]}
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"""
                <div class="metric-card">
                <div class="metric-label">CYBERSECURITY</div>
                <div class="metric-value">
                🛡️ {result["cyber_score"]}
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                f"""
                <div class="metric-card">
                <div class="metric-label">URL RISK</div>
                <div class="metric-value">
                🔗 {result["url_score"]}
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="cyber-card" style="text-align:center;">
            <div style="font-size:15px;color:#8195b7;font-weight:700;">
            THREAT LEVEL
            </div>
            <div class="{risk_class}" style="font-size:38px;font-weight:800;margin-top:5px;">
            {risk_icon} {result["risk"]} RISK
            </div>
            <div style="color:#8195b7;margin-top:5px;">
            Composite risk indicator
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(result["final_score"] / 100)

        # ----------------------------------------------------
        # RISK BREAKDOWN
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">📊 RISK CONTRIBUTION BREAKDOWN</div>',
            unsafe_allow_html=True
        )

        ai_contribution = round(result["ai_score"] * 0.45, 1)
        cyber_contribution = round(result["cyber_score"] * 0.40, 1)
        url_contribution = round(result["url_score"] * 0.15, 1)

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(
                f"""
                <div class="cyber-card">
                <b style="color:#00e5ff;">🤖 AI / NLP</b><br><br>
                Score: <b>{result["ai_score"]}/100</b><br>
                Weight: 45%<br>
                Contribution: <b>{ai_contribution}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f"""
                <div class="cyber-card">
                <b style="color:#ffbd4a;">🛡️ CYBERSECURITY</b><br><br>
                Score: <b>{result["cyber_score"]}/100</b><br>
                Weight: 40%<br>
                Contribution: <b>{cyber_contribution}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:
            st.markdown(
                f"""
                <div class="cyber-card">
                <b style="color:#43e6a4;">🔗 URL ANALYSIS</b><br><br>
                Score: <b>{result["url_score"]}/100</b><br>
                Weight: 15%<br>
                Contribution: <b>{url_contribution}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

        # ----------------------------------------------------
        # EVIDENCE
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">🚨 EVIDENCE DETECTED</div>',
            unsafe_allow_html=True
        )

        if result["evidence"]:

            for item in result["evidence"]:

                st.markdown(
                    f"""
                    <div class="evidence">
                    ⚠️ {item}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.success(
                "No major predefined cybersecurity warning evidence was detected."
            )

        # ----------------------------------------------------
        # WARNING SIGNALS
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">⚠️ DETECTED WARNING SIGNALS</div>',
            unsafe_allow_html=True
        )

        if result["signals"]:

            for signal in result["signals"]:
                st.markdown(f"**{signal}**")

        else:

            st.info("No major predefined warning signals detected.")

        # ----------------------------------------------------
        # URL SECURITY
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">🔗 URL SECURITY INSPECTOR</div>',
            unsafe_allow_html=True
        )

        if result["url_results"]:

            for url_data in result["url_results"]:

                st.markdown(
                    f"""
                    <div class="cyber-card">

                    <div style="color:#00e5ff;font-size:12px;font-weight:800;">
                    ANALYZED DESTINATION
                    </div>

                    <div style="font-size:15px;margin:8px 0 18px 0;">
                    {url_data["url"]}
                    </div>

                    <b>Protocol:</b>
                    {url_data["protocol"]}

                    &nbsp;&nbsp;&nbsp;

                    <b>IP-Based:</b>
                    {"🚨 YES" if url_data["ip_based"] else "✅ NO"}

                    &nbsp;&nbsp;&nbsp;

                    <b>Suspicious Keywords:</b>
                    {"🚨 YES" if url_data["suspicious"] else "✅ NO"}

                    &nbsp;&nbsp;&nbsp;

                    <b>Long URL:</b>
                    {"⚠️ YES" if url_data["long"] else "✅ NO"}

                    <br><br>

                    <b>URL Risk Score:</b>
                    {url_data["score"]}/40

                    <br><br>

                    <b>Static analysis:</b>
                    {" • ".join(url_data["reasons"]) if url_data["reasons"] else "No predefined URL warning detected."}

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.info("🔗 No URL detected in this advertisement.")

        # ----------------------------------------------------
        # WHY FLAGGED
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">🧠 WHY DID JOBSHIELD FLAG THIS?</div>',
            unsafe_allow_html=True
        )

        reasons = []

        if result["ai_score"] >= 50:
            reasons.append(
                "AI/NLP detected language patterns that resemble scam examples."
            )

        if result["cyber_score"] >= 30:
            reasons.append(
                "Multiple cybersecurity warning indicators were detected."
            )

        if result["url_score"] > 0:
            reasons.append(
                "The advertisement contains URL characteristics associated with increased risk."
            )

        if not reasons:
            reasons.append(
                "The current predefined rules did not detect major warning signals."
            )

        for reason in reasons:
            st.markdown(f"✓ {reason}")

        # ----------------------------------------------------
        # SAFETY ACTION
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">🛡️ SAFETY ACTION CENTER</div>',
            unsafe_allow_html=True
        )

        if result["risk"] == "HIGH":

            st.error(
                "🚨 HIGH RISK — Do not pay money or share sensitive documents. "
                "Verify the employer independently using official sources."
            )

            st.markdown("""
            **Recommended actions**

            ❌ DO NOT PAY REGISTRATION / PROCESSING FEES  
            ❌ DO NOT SHARE Aadhaar, PAN, OTP or BANK DETAILS  
            ⚠️ DO NOT TRUST URGENT PRESSURE  
            🔎 VERIFY THE EMPLOYER INDEPENDENTLY
            """)

        elif result["risk"] == "MEDIUM":

            st.warning(
                "⚠️ MEDIUM RISK — Verify the employer and recruitment process before proceeding."
            )

            st.markdown("""
            **Recommended actions**

            ⚠️ Verify the company  
            🔎 Check the official careers website  
            ❌ Avoid making payments until independently verified
            """)

        else:

            st.success(
                "🟢 LOWER RISK — No major predefined warning signals were detected."
            )

            st.markdown("""
            **Still recommended**

            ✅ Verify the employer  
            🔎 Use official recruitment channels  
            🛡️ Avoid sharing unnecessary sensitive information
            """)

        # ----------------------------------------------------
        # AI EXPLANATION
        # ----------------------------------------------------

        with st.expander("🤖 VIEW AI / NLP ANALYSIS"):

            st.write(
                "JobShield AI uses TF-IDF text features and a local Logistic "
                "Regression classifier."
            )

            st.write(
                f"The current AI/NLP score is **{result['ai_score']}/100**."
            )

            st.caption(
                "This prototype uses simulated demonstration examples. "
                "The AI score is a risk indicator, not proof of fraud."
            )

        # ----------------------------------------------------
        # PIPELINE
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">⚡ DETECTION PIPELINE</div>',
            unsafe_allow_html=True
        )

        pipeline = [
            ("📥", "INPUT"),
            ("🧹", "TEXT"),
            ("🤖", "AI / NLP"),
            ("🛡️", "CYBER"),
            ("🔗", "URL"),
            ("📊", "RISK"),
            ("🧠", "EXPLAIN"),
            ("🚨", "WARN")
        ]

        cols = st.columns(len(pipeline))

        for col, (icon, name) in zip(cols, pipeline):

            with col:

                st.markdown(
                    f"""
                    <div class="pipeline">
                    <div class="pipeline-icon">{icon}</div>
                    <div class="pipeline-text">{name}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# ============================================================
# SCAN HISTORY
# ============================================================

st.markdown(
    '<div class="section-title">📈 SCAN HISTORY</div>',
    unsafe_allow_html=True
)

if st.session_state.history:

    h1, h2, h3 = st.columns(3)

    high_count = sum(
        x["Risk"] == "HIGH"
        for x in st.session_state.history
    )

    medium_count = sum(
        x["Risk"] == "MEDIUM"
        for x in st.session_state.history
    )

    low_count = sum(
        x["Risk"] == "LOWER"
        for x in st.session_state.history
    )

    with h1:
        st.metric("🔴 HIGH", high_count)

    with h2:
        st.metric("🟠 MEDIUM", medium_count)

    with h3:
        st.metric("🟢 LOWER", low_count)

    st.dataframe(
        st.session_state.history,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No scans yet. Analyze an offer to create your first security scan."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

🛡️ JOBSHIELD AI 2.0

<br><br>

DETECT • EXPLAIN • WARN

<br><br>

Cybersecurity proof-of-concept for educational demonstration.

<br>

Risk scores are indicators, not proof that an advertisement is fraudulent.
Users should independently verify employers and offers.

</div>
""", unsafe_allow_html=True)
