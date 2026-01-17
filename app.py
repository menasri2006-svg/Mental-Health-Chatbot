import streamlit as st
from datetime import datetime
import style
import logic

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Zenith AI Sanctuary",
    page_icon="🌿",
    layout="wide",
)

style.apply_styles()

# =========================
# ENHANCED STYLES
# =========================
st.markdown("""
<style>
/* SMOOTH PAGE TRANSITIONS */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.stApp {
    background: linear-gradient(135deg, #e8f5e9 0%, #f1f8f4 50%, #e0f2f1 100%);
    animation: fadeIn 0.6s ease-out;
}

/* HERO SECTION - Enhanced */
.hero {
    position: relative;
    height: 480px;
    border-radius: 40px;
    background-image:
        linear-gradient(135deg, rgba(16, 46, 38, 0.75), rgba(28, 69, 58, 0.65)),
        url("https://images.unsplash.com/photo-1511497584788-876760111969?w=1600");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    padding: 80px;
    color: white;
    margin-bottom: 60px;
    box-shadow: 0 30px 80px rgba(46, 125, 50, 0.3);
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 30% 50%, rgba(129, 199, 132, 0.2), transparent);
    animation: pulse 4s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 0.8; }
}

.hero h1 {
    font-size: 64px;
    font-weight: 800;
    letter-spacing: -1px;
    position: relative;
    z-index: 1;
    text-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

.hero p {
    font-size: 22px;
    max-width: 700px;
    color: #e8f5e9;
    line-height: 1.6;
    position: relative;
    z-index: 1;
    text-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

/* ENHANCED EQUAL CARDS */
.equal-card {
    background: white;
    border-radius: 28px;
    overflow: hidden;
    box-shadow: 0 15px 35px rgba(46, 125, 50, 0.12);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    height: 100%;
    border: 1px solid rgba(129, 199, 132, 0.1);
}

.equal-card:hover {
    transform: translateY(-12px) scale(1.02);
    box-shadow: 0 35px 70px rgba(46, 125, 50, 0.25);
    border-color: rgba(129, 199, 132, 0.3);
}

.card-img {
    height: 220px;
    background-size: cover;
    background-position: center;
    position: relative;
    overflow: hidden;
}

.card-img::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.15) 100%);
    transition: opacity 0.3s ease;
}

.equal-card:hover .card-img::before {
    opacity: 0.5;
}

.card-img::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at center, rgba(129, 199, 132, 0.2), transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.equal-card:hover .card-img::after {
    opacity: 1;
}

.card-content {
    padding: 28px;
    background: linear-gradient(180deg, white 0%, #fafffe 100%);
}

.card-content h3 {
    margin-bottom: 12px;
    font-size: 22px;
    color: #2e7d32;
    font-weight: 700;
}

.card-content p {
    color: #4a5f4a;
    line-height: 1.6;
    font-size: 15px;
}

/* PROGRESS RING - Enhanced */
.ring {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: conic-gradient(
        #4caf50 0deg,
        #66bb6a calc(var(--percent) * 3.6deg),
        #e8f5e9 calc(var(--percent) * 3.6deg)
    );
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    box-shadow: 0 8px 24px rgba(76, 175, 80, 0.3);
    animation: ringPulse 2s ease-in-out infinite;
}

@keyframes ringPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

.ring span {
    background: linear-gradient(135deg, #ffffff 0%, #f1f8f4 100%);
    width: 75px;
    height: 75px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 26px;
    color: #2e7d32;
    box-shadow: inset 0 2px 8px rgba(46, 125, 50, 0.1);
}

/* SECTION TITLE */
.section-title {
    font-size: 36px;
    font-weight: 800;
    color: #2e7d32;
    margin: 40px 0 30px 0;
    text-align: center;
    position: relative;
    padding-bottom: 20px;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 4px;
    background: linear-gradient(90deg, transparent, #66bb6a, transparent);
    border-radius: 2px;
}

/* DIVIDER */
hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(129, 199, 132, 0.3), transparent);
    margin: 50px 0;
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 60px 20px;
    background: linear-gradient(135deg, rgba(232, 245, 233, 0.5), rgba(224, 242, 241, 0.5));
    border-radius: 30px;
    margin-top: 50px;
    color: #4a5f4a;
    font-size: 20px;
    font-weight: 500;
    box-shadow: 0 10px 30px rgba(46, 125, 50, 0.08);
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .hero {
        height: 350px;
        padding: 40px;
    }

    .hero h1 {
        font-size: 40px;
    }

    .hero p {
        font-size: 18px;
    }
}

/* LOADING ANIMATION */
@keyframes shimmer {
    0% { background-position: -1000px 0; }
    100% { background-position: 1000px 0; }
}

.card-img {
    background-size: cover;
    animation: shimmer 3s infinite;
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
st.markdown("""
<div class="hero">
    <h1>🌿 Calm. Care. Connect.</h1>
    <p>
        A safe AI-powered sanctuary to slow down, breathe deeply,
        reflect gently, and reconnect with yourself. Your journey to inner peace starts here.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# TOP STATUS CARDS
# =========================
today = datetime.now().strftime("%A")
affirmation = logic.get_daily_affirmation()
streak = st.session_state.get("streak_count", 0)
percent = min(streak * 10, 100)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="equal-card">
        <div class="card-img" style="background-image:url('https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=800');"></div>
        <div class="card-content">
            <h3>🧠 Today's Journey</h3>
            <p style="font-size:32px; font-weight:800; color:#2e7d32;">{today}</p>
            <p style="font-size:14px; color:#81c784; margin-top:8px;">Embrace this beautiful day</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="equal-card">
        <div class="card-img" style="background-image:url('https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=800');"></div>
        <div class="card-content">
            <h3>🌱 Daily Affirmation</h3>
            <p style="font-style:italic; color:#2e7d32; font-weight:500;">{affirmation}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="equal-card">
        <div class="card-img" style="background-image:url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800');"></div>
        <div class="card-content">
            <h3>🔥 Wellness Streak</h3>
            <div class="ring" style="--percent:{percent}; margin:15px auto;">
                <span>{streak}</span>
            </div>
            <p style="font-size:14px; color:#81c784; text-align:center;">Keep going strong!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# WELLNESS DASHBOARD
# =========================
st.markdown('<div class="section-title">✨ Your Wellness Dashboard</div>', unsafe_allow_html=True)

st.write("")
st.write("")

r1, r2, r3 = st.columns(3)

with r1:
    st.markdown("""
    <div class="equal-card">
        <div class="card-img" style="background-image:url('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800');"></div>
        <div class="card-content">
            <h3>💬 Deep Chat</h3>
            <p>Talk freely with Zenith — calm, empathetic, judgment-free. Share your thoughts in a safe space.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with r2:
    st.markdown("""
    <div class="equal-card">
        <div class="card-img" style="background-image:url('https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=800');"></div>
        <div class="card-content">
            <h3>😌 Mood Relaxation</h3>
            <p>Soothing music, calming stories, breathing exercises, and peaceful visuals to restore balance.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with r3:
    st.markdown("""
    <div class="equal-card">
        <div class="card-img" style="background-image:url('https://images.unsplash.com/photo-1545389336-cf090694435e?w=800');"></div>
        <div class="card-content">
            <h3>🧘 Relaxation</h3>
            <p>Guided breathing techniques and soothing animations to help you find your center.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

r4, r5, r6 = st.columns(3)

with r4:
    st.markdown("""
    <div class="equal-card">
        <div class="card-img" style="background-image:url('https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800');"></div>
        <div class="card-content">
            <h3>🧘‍♀️ Self Care</h3>
            <p>Yoga practices, laughter therapy, and gentle self-care tools to nurture your wellbeing.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with r5:
    st.markdown("""
    <div class="equal-card">
        <div class="card-img" style="background-image:url('https://images.unsplash.com/photo-1455849318743-b2233052fcff?w=800');"></div>
        <div class="card-content">
            <h3>📖 Reflection</h3>
            <p>Write your thoughts, explore emotions, and gain clarity in a safe, private environment.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with r6:
    st.markdown("""
    <div class="equal-card">
        <div class="card-img" style="background-image:url('https://images.unsplash.com/photo-1516733725897-1aa73b87c8e8?w=800');"></div>
        <div class="card-content">
            <h3>🚨 Emergency Support</h3>
            <p>Immediate crisis help and resources when you need support most. You're not alone.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    🌱 You are safe here. You are heard. You matter. 🌱<br>
    <span style="font-size:16px; color:#81c784; margin-top:10px; display:inline-block;">
        Take your time. Breathe. You've got this.
    </span>
</div>
""", unsafe_allow_html=True)