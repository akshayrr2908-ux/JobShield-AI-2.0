import streamlit as st
import re
from urllib.parse import urlparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="JobShield AI",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# SAMPLE TRAINING DATA
# ============================================================

SCAM_EXAMPLES = [
    "Pay registration fee to receive your offer letter",
    "Earn 50000 per month with no experience required",
    "Urgent hiring apply immediately limited seats available",
    "Send Aadhaar and PAN card for verification",
    "Pay processing fee before joining",
    "Work from home and earn huge salary without interview",
    "Contact recruiter only through WhatsApp",
    "Pay security deposit to confirm your internship",
    "Guaranteed job with instant joining after payment",
    "Congratulations you are selected pay fee to activate offer",
    "No interview required earn 60000 monthly",
    "Send your documents immediately to secure your position",
    "Limited vacancies apply now and pay registration charges",
    "Easy online job high income no skills needed",
    "Pay 999 to receive internship certificate and offer letter",
    "Immediate joining guaranteed salary 40000",
    "Share bank details and identity documents for verification",
    "Work from home opportunity registration fee required"
]

SAFE_EXAMPLES = [
    "We are looking for students interested in Python and web development.",
    "The internship includes a technical interview and mentor support.",
    "Applicants should submit their resume through the company's official careers page.",
    "The selected candidate will work with the engineering team on software projects.",
    "Internship duration is three months.",
    "Candidates will complete an interview before selection.",
    "Apply through the official company careers website.",
    "The internship provides mentorship and practical software development experience.",
    "Students can submit their resume and portfolio for consideration.",
    "The company will contact shortlisted candidates through the official recruitment process.",
    "The role includes technical training and supervised project work.",
    "Applicants should review the job description before submitting their application.",
    "The position requires knowledge of Python and basic web development.",
    "Candidates will be evaluated through an interview process.",
    "The internship is designed for students interested in software engineering."
]


# ============================================================
# TRAIN LOCAL AI / NLP MODEL
# ============================================================

training_text = SCAM_EXAMPLES + SAFE_EXAMPLES
training_labels = [1] * len(SCAM_EXAMPLES) + [0] * len(SAFE_EXAMPLES)

vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    stop_words="english"
)

X = vectorizer.fit_transform(training_text)

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(X, training_labels)


# ============================================================
# DEMO SAMPLES
# ============================================================

SAMPLES = {

    "High Risk — Fake Internship": """
URGENT! Work From Home Internship

Earn ₹50,000 per month with no experience required.

Pay ₹999 as a registration fee to receive your offer letter.

Send your Aadhaar card and PAN card immediately for verification.

Contact our recruiter only through WhatsApp.

Limited seats available. Apply immediately!
""",

    "Medium Risk — Suspicious Offer": """
Software Internship Opportunity

Work from home internship for students.

Earn up to ₹30,000 per month.

Selected candidates must complete a quick registration process.

Contact the recruiter through WhatsApp for further details.

Apply today as positions are limited.
""",

    "Lower Risk — Normal Internship": """
We are looking for students interested in Python and web development.

The internship includes a technical interview and mentor support.

Applicants should submit their resume through the company's official careers page.

The selected candidate will work with the engineering team on software projects.

Internship duration: 3 months.
""",

    "Custom Input": ""
}


# ============================================================
# CYBERSECURITY ANALYSIS
# ============================================================

def analyze_cybersecurity(text):

    text_lower = text.lower()

    signals = []
    score = 0

    # Payment / fee requests
    payment_patterns = [
        "registration fee",
        "processing fee",
        "joining fee",
        "security deposit",
        "pay ₹",
        "pay rs",
        "pay rs.",
        "payment required",
        "pay fee",
        "pay before joining",
        "send money",
        "deposit"
    ]

    if any(pattern in text_lower for pattern in payment_patterns):
        signals.append(
            "💰 Payment or fee request detected"
        )
        score += 30

    # Sensitive personal information
    sensitive_patterns = [
        "aadhaar",
        "aadhar",
        "pan card",
        "bank details",
        "bank account",
        "otp",
        "identity document",
        "identity proof",
        "passport",
        "driving licence",
        "driving license"
    ]

    found_sensitive = [
        pattern for pattern in sensitive_patterns
        if pattern in text_lower
    ]

    if found_sensitive:
        signals.append(
            "📄 Sensitive personal information requested"
        )
        score += 25

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
        "quickly"
    ]

    if any(pattern in text_lower for pattern in urgency_patterns):
        signals.append(
            "🚨 Urgency or pressure language detected"
        )
        score += 15

    # Unrealistic earning claims
    salary_patterns = [
        "₹50,000",
        "₹50000",
        "₹60,000",
        "₹60000",
        "₹70,000",
        "₹70000",
        "50000 per month",
        "60000 per month",
        "70000 per month",
        "huge salary",
        "guaranteed income",
        "earn huge"
    ]

    if any(pattern.lower() in text_lower for pattern in salary_patterns):
        signals.append(
            "💸 High earning claim detected"
        )
        score += 15

    # No experience / guaranteed job
    experience_patterns = [
        "no experience required",
        "no experience",
        "guaranteed job",
        "guaranteed selection",
        "instant joining",
        "no interview required"
    ]

    if any(pattern in text_lower for pattern in experience_patterns):
        signals.append(
            "🎯 Unrealistic or low-barrier hiring claim detected"
        )
        score += 10

    # WhatsApp-only contact
    whatsapp_patterns = [
        "only through whatsapp",
        "contact only through whatsapp",
        "whatsapp recruiter",
        "contact recruiter on whatsapp"
    ]

    if any(pattern in text_lower for pattern in whatsapp_patterns):
        signals.append(
            "📱 Recruiter contact is restricted to WhatsApp"
        )
        score += 10

    return min(score, 100), signals


# ============================================================
# URL ANALYSIS
# ============================================================

def analyze_urls(text):

    urls = re.findall(
        r'https?://[^\s]+|www\.[^\s]+',
        text
    )

    results = []
    url_score = 0

    if not urls:
        return 0, results

    for raw_url in urls:

        url = raw_url.rstrip(".,);")

        if not url.startswith("http"):
            parsed = urlparse("http://" + url)
        else:
            parsed = urlparse(url)

        hostname = parsed.hostname or ""

        warnings = []

        # HTTP instead of HTTPS
        if parsed.scheme == "http":
            warnings.append("Uses HTTP instead of HTTPS")
            url_score += 10

        # IP address instead of domain
        if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", hostname):
            warnings.append("Uses an IP address instead of a domain")
            url_score += 20

        # Suspicious URL words
        suspicious_words = [
            "verify",
            "payment",
            "fee",
            "claim",
            "offer",
            "urgent",
            "login"
        ]

        if any(word in hostname.lower() for word in suspicious_words):
            warnings.append("Domain contains suspicious keywords")
            url_score += 10

        # Very long URL
        if len(url) > 100:
            warnings.append("Unusually long URL")
            url_score += 5

        results.append({
            "url": url,
            "warnings": warnings
        })

    return min(url_score, 40), results


# ============================================================
# AI / NLP ANALYSIS
# ============================================================

def analyze_ai(text):

    transformed = vectorizer.transform([text])

    probability = model.predict_proba(transformed)[0][1]

    ai_score = round(probability * 100)

    return ai_score


# ============================================================
# FINAL ANALYSIS ENGINE
# ============================================================

def analyze_advertisement(text):

    cyber_score, cyber_signals = analyze_cybersecurity(text)

    url_score, url_results = analyze_urls(text)

    ai_score = analyze_ai(text)

    # Combine AI + cybersecurity analysis
    final_score = round(
        (ai_score * 0.45) +
        (cyber_score * 0.40) +
        (url_score * 0.15)
    )

    final_score = min(max(final_score, 0), 100)

    # Risk classification
    if final_score >= 70:
        risk_level = "HIGH RISK"
        risk_icon = "🔴"

    elif final_score >= 40:
        risk_level = "MEDIUM RISK"
        risk_icon = "🟠"

    else:
        risk_level = "LOWER RISK"
        risk_icon = "🟢"

    return {
        "ai_score": ai_score,
        "cyber_score": cyber_score,
        "url_score": url_score,
        "final_score": final_score,
        "risk_level": risk_level,
        "risk_icon": risk_icon,
        "signals": cyber_signals,
        "urls": url_results
    }


# ============================================================
# HEADER
# ============================================================

st.title("🛡️ JobShield AI")

st.subheader(
    "Fake Job & Internship Scam Detector"
)

st.write(
    "AI + Cybersecurity analysis for suspicious job and internship advertisements."
)

st.divider()


# ============================================================
# QUICK DEMO
# ============================================================

st.header("🧪 Quick Demo")

sample_choice = st.selectbox(
    "Choose a sample advertisement",
    list(SAMPLES.keys())
)


# ============================================================
# TEXT INPUT
# ============================================================

if sample_choice == "Custom Input":

    default_text = ""

else:

    default_text = SAMPLES[sample_choice]


job_text = st.text_area(
    "📋 Paste the job or internship advertisement",
    value=default_text,
    height=280,
    placeholder="Paste the complete job or internship advertisement here..."
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

if st.button(
    "🔍 ANALYZE WITH JOBSHIELD AI",
    use_container_width=True
):

    if not job_text.strip():

        st.warning(
            "Please enter a job or internship advertisement."
        )

    else:

        result = analyze_advertisement(job_text)

        st.divider()

        st.header("🎯 Analysis Result")

        # ----------------------------------------------------
        # RISK BANNER
        # ----------------------------------------------------

        if result["final_score"] >= 70:

            st.error(
                f"{result['risk_icon']} {result['risk_level']} — "
                f"{result['final_score']}/100"
            )

        elif result["final_score"] >= 40:

            st.warning(
                f"{result['risk_icon']} {result['risk_level']} — "
                f"{result['final_score']}/100"
            )

        else:

            st.success(
                f"{result['risk_icon']} {result['risk_level']} — "
                f"{result['final_score']}/100"
            )


        # ----------------------------------------------------
        # SCORE COLUMNS
        # ----------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🛡️ Cybersecurity Score",
                f"{result['cyber_score']}/100"
            )

        with col2:

            st.metric(
                "🤖 AI / NLP Score",
                f"{result['ai_score']}/100"
            )

        with col3:

            st.metric(
                "🎯 Final Risk Score",
                f"{result['final_score']}/100"
            )


        st.progress(result["final_score"] / 100)


        st.header("⚠️ Detected Warning Signals")

        if result["signals"]:

            for signal in result["signals"]:

                st.write(signal)

        else:

            st.success(
                "No major predefined cybersecurity warning signals were detected."
            )


        # ----------------------------------------------------
        # AI / NLP EXPLANATION
        # ----------------------------------------------------

        st.header("🤖 AI / NLP Analysis")

        st.write(
            "The local NLP classifier analyzed the wording "
            "and patterns in the advertisement and produced "
            "an AI-based scam-likelihood score."
        )

        st.progress(result["ai_score"] / 100)

        st.caption(
            "The classifier uses TF-IDF text features and "
            "Logistic Regression trained on simulated "
            "demonstration examples."
        )


        # ----------------------------------------------------
        # CYBERSECURITY ANALYSIS
        # ----------------------------------------------------

        st.header("🛡️ Cybersecurity Analysis")

        if result["cyber_score"] > 0:

            st.write(
                f"Cybersecurity warning score: "
                f"{result['cyber_score']}/100"
            )

            st.write(
                "The system identified security-related "
                "patterns such as payment requests, "
                "sensitive information requests, urgency, "
                "or suspicious recruitment behavior."
            )

        else:

            st.success(
                "No major predefined cybersecurity warning signals detected."
            )


        # ----------------------------------------------------
        # URL ANALYSIS
        # ----------------------------------------------------

        st.header("🔗 URL Analysis")

        if result["urls"]:

            for item in result["urls"]:

                st.write(f"**Detected URL:** {item['url']}")

                if item["warnings"]:

                    for warning in item["warnings"]:

                        st.write(
                            f"⚠️ {warning}"
                        )

                else:

                    st.success(
                        "No basic URL warning pattern detected."
                    )

        else:

            st.info(
                "No URL was detected in the advertisement."
            )


        # ----------------------------------------------------
        # EXPLANATION
        # ----------------------------------------------------

        st.header("🧠 Why did JobShield AI flag this?")

        reasons = []

        if result["ai_score"] >= 60:

            reasons.append(
                "The NLP model found wording patterns "
                "similar to the scam examples in its "
                "demonstration training set."
            )

        if result["cyber_score"] >= 30:

            reasons.append(
                "The advertisement contains multiple "
                "cybersecurity warning indicators."
            )

        if result["url_score"] > 0:

            reasons.append(
                "The advertisement contains a URL with "
                "one or more basic technical warning patterns."
            )

        if not reasons:

            reasons.append(
                "Only limited warning patterns were detected. "
                "The offer should still be independently verified."
            )

        for reason in reasons:

            st.write(
                f"• {reason}"
            )


        # ----------------------------------------------------
        # RECOMMENDED ACTION
        # ----------------------------------------------------

        st.header("💡 Recommended Action")

        if result["final_score"] >= 70:

            st.error(
                "Avoid making payments or sharing sensitive "
                "personal information. Verify the employer "
                "through an independently found official "
                "career channel before proceeding."
            )

        elif result["final_score"] >= 40:

            st.warning(
                "Proceed carefully. Verify the company, "
                "recruiter and offer through trusted sources "
                "before sharing information or making payments."
            )

        else:

            st.info(
                "No major warning pattern was detected. "
                "Continue verifying the employer and offer "
                "through trusted official channels."
            )


        # ----------------------------------------------------
        # SYSTEM PIPELINE
        # ----------------------------------------------------

        st.header("⚙️ JobShield AI Detection Pipeline")

        st.write(
            "ADVERTISEMENT"
            "  →  "
            "TEXT EXTRACTION"
            "  →  "
            "AI/NLP ANALYSIS"
            "  →  "
            "CYBERSECURITY RULES"
            "  →  "
            "RISK ENGINE"
            "  →  "
            "EXPLAIN + ASSIST"
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "JobShield AI — DETECT • EXPLAIN • WARN"
)

st.caption(
    "Cybersecurity proof-of-concept. "
    "Risk scores are indicators, not proof that an advertisement "
    "is fraudulent. Users should independently verify employers "
    "and offers."
)