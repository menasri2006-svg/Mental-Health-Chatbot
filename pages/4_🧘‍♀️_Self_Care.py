import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import random
import requests
from streamlit_lottie import st_lottie
import datetime
import time

# Apply modern mindful styles
st.markdown("""
<style>
/* Global peaceful background with gradient animation */
@keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp {
    background: linear-gradient(-45deg, #fef3c7, #fde68a, #e0f2fe, #ddd6fe, #fce7f3);
    background-size: 400% 400%;
    animation: gradient-shift 15s ease infinite;
}

/* Floating animations */
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}

@keyframes float-delayed {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
}

@keyframes glow-pulse {
    0%, 100% { box-shadow: 0 0 20px rgba(167, 243, 208, 0.4); }
    50% { box-shadow: 0 0 40px rgba(167, 243, 208, 0.8); }
}

/* Modern glassmorphism cards */
.mindful-card {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 2.5rem;
    border-radius: 32px;
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.08),
        inset 0 1px 0 rgba(255, 255, 255, 0.6);
    margin: 2rem 0;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.mindful-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(
        45deg,
        transparent,
        rgba(255, 255, 255, 0.1),
        transparent
    );
    transform: rotate(45deg);
    transition: all 0.6s;
}

.mindful-card:hover::before {
    left: 100%;
}

.mindful-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 
        0 16px 48px rgba(0, 0, 0, 0.12),
        inset 0 1px 0 rgba(255, 255, 255, 0.8);
}

/* Stat cards with depth */
.stat-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7));
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.4);
    padding: 2rem;
    border-radius: 24px;
    text-align: center;
    box-shadow: 
        0 10px 30px rgba(0, 0, 0, 0.08),
        inset 0 1px 0 rgba(255, 255, 255, 0.5);
    transition: all 0.3s ease;
    animation: float 6s ease-in-out infinite;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12);
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #8b5cf6, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0.5rem 0;
}

.stat-label {
    font-size: 0.9rem;
    color: #64748b;
    font-weight: 500;
}

/* Affirmation card with shimmer */
.affirmation-card {
    background: linear-gradient(135deg, rgba(167, 243, 208, 0.3), rgba(253, 230, 138, 0.3));
    backdrop-filter: blur(20px);
    border: 2px solid rgba(255, 255, 255, 0.5);
    padding: 3rem;
    border-radius: 32px;
    text-align: center;
    box-shadow: 
        0 20px 60px rgba(0, 0, 0, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.8);
    position: relative;
    overflow: hidden;
    animation: glow-pulse 4s ease-in-out infinite;
}

.affirmation-text {
    font-size: 1.8rem;
    font-weight: 600;
    color: #065f46;
    line-height: 1.6;
    text-shadow: 0 2px 4px rgba(255, 255, 255, 0.8);
}

/* Timer with 3D effect */
.timer-display {
    background: linear-gradient(135deg, #a855f7, #ec4899);
    color: white;
    padding: 3rem;
    border-radius: 28px;
    text-align: center;
    font-size: 4rem;
    font-weight: 800;
    box-shadow: 
        0 20px 60px rgba(168, 85, 247, 0.4),
        inset 0 -5px 20px rgba(0, 0, 0, 0.2),
        inset 0 5px 20px rgba(255, 255, 255, 0.2);
    letter-spacing: 0.1em;
    animation: float-delayed 4s ease-in-out infinite;
}

/* Achievement badge with glow */
.achievement-badge {
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    color: white;
    padding: 1.5rem 3rem;
    border-radius: 24px;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 700;
    box-shadow: 
        0 10px 40px rgba(251, 191, 36, 0.5),
        inset 0 1px 0 rgba(255, 255, 255, 0.3);
    margin: 2rem 0;
    animation: glow-pulse 3s ease-in-out infinite;
}

/* Modern buttons */
.stButton > button {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7)) !important;
    backdrop-filter: blur(10px) !important;
    border: 2px solid rgba(255, 255, 255, 0.5) !important;
    color: #1e293b !important;
    padding: 1rem 2rem !important;
    border-radius: 16px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08) !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.05) !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12) !important;
    border-color: rgba(139, 92, 246, 0.5) !important;
}

/* Tab styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 1rem;
    background: rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(10px);
    padding: 0.5rem;
    border-radius: 20px;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 16px;
    padding: 1rem 2rem;
    font-weight: 600;
    transition: all 0.3s ease;
}

.stTabs [aria-selected="true"] {
    background: rgba(255, 255, 255, 0.9);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

/* Input fields */
.stTextArea textarea, .stTextInput input {
    background: rgba(255, 255, 255, 0.8) !important;
    backdrop-filter: blur(10px) !important;
    border: 2px solid rgba(255, 255, 255, 0.5) !important;
    border-radius: 16px !important;
    padding: 1rem !important;
    transition: all 0.3s ease !important;
}

.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: rgba(139, 92, 246, 0.6) !important;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1) !important;
}

/* Progress bars */
.stProgress > div > div {
    background: linear-gradient(90deg, #10b981, #6ee7b7) !important;
    border-radius: 20px !important;
    height: 12px !important;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3) !important;
}

/* Radio buttons */
.stRadio > div {
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(10px);
    padding: 1rem;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.4);
}

/* Selectbox */
.stSelectbox > div > div {
    background: rgba(255, 255, 255, 0.8) !important;
    backdrop-filter: blur(10px) !important;
    border: 2px solid rgba(255, 255, 255, 0.5) !important;
    border-radius: 16px !important;
}

/* Hide streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Floating decorative elements */
.floating-icon {
    position: fixed;
    font-size: 3rem;
    opacity: 0.1;
    animation: float 8s ease-in-out infinite;
    z-index: 0;
    pointer-events: none;
}

/* Page header gradient text */
.gradient-text {
    background: linear-gradient(135deg, #8b5cf6, #ec4899, #f59e0b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    font-size: 3.5rem;
    text-align: center;
    margin: 2rem 0;
    text-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.subtitle-text {
    text-align: center;
    color: #64748b;
    font-size: 1.3rem;
    font-weight: 500;
    margin-bottom: 3rem;
}

/* Section headers */
.section-header {
    font-size: 1.8rem;
    font-weight: 700;
    color: #1e293b;
    margin: 1.5rem 0 1rem 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* Info boxes with soft shadows */
.stAlert {
    background: rgba(255, 255, 255, 0.8) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(255, 255, 255, 0.5) !important;
    border-radius: 20px !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08) !important;
}
</style>
""", unsafe_allow_html=True)

# Add floating decorative elements
st.markdown("""
<div class="floating-icon" style="top: 10%; left: 5%;">🌸</div>
<div class="floating-icon" style="top: 20%; right: 8%; animation-delay: 1s;">✨</div>
<div class="floating-icon" style="top: 60%; left: 10%; animation-delay: 2s;">🍃</div>
<div class="floating-icon" style="bottom: 15%; right: 12%; animation-delay: 3s;">🦋</div>
<div class="floating-icon" style="bottom: 40%; left: 8%; animation-delay: 4s;">🌿</div>
""", unsafe_allow_html=True)

# Initialize session state
if "gratitude_score" not in st.session_state:
    st.session_state.gratitude_score = 0
if "streak_days" not in st.session_state:
    st.session_state.streak_days = 1
if "total_time_spent" not in st.session_state:
    st.session_state.total_time_spent = 0
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []
if "mood_log" not in st.session_state:
    st.session_state.mood_log = []
if "last_visit" not in st.session_state:
    st.session_state.last_visit = datetime.date.today()
if "breathing_completed" not in st.session_state:
    st.session_state.breathing_completed = 0
if "kindness_acts" not in st.session_state:
    st.session_state.kindness_acts = []

# Update streak
today = datetime.date.today()
if st.session_state.last_visit != today:
    if (today - st.session_state.last_visit).days == 1:
        st.session_state.streak_days += 1
    else:
        st.session_state.streak_days = 1
    st.session_state.last_visit = today


# Safe Lottie loader
def load_lottie(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.json()
    except:
        pass
    return None


# Page header
st.markdown("<h1 class='gradient-text'>Your Mindful Sanctuary 🧘‍♀️</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>A peaceful space to nurture your mind, body, and soul 🌸</p>",
            unsafe_allow_html=True)

# Stats dashboard
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class='stat-card'>
        <div style='font-size: 2.5rem;'>🔥</div>
        <div class='stat-number'>{st.session_state.streak_days}</div>
        <div class='stat-label'>Day Streak</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class='stat-card' style='animation-delay: 0.2s;'>
        <div style='font-size: 2.5rem;'>⏱️</div>
        <div class='stat-number'>{st.session_state.total_time_spent}</div>
        <div class='stat-label'>Minutes Today</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class='stat-card' style='animation-delay: 0.4s;'>
        <div style='font-size: 2.5rem;'>💚</div>
        <div class='stat-number'>{st.session_state.gratitude_score}</div>
        <div class='stat-label'>Gratitude Points</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class='stat-card' style='animation-delay: 0.6s;'>
        <div style='font-size: 2.5rem;'>🌟</div>
        <div class='stat-number'>{len(st.session_state.kindness_acts)}</div>
        <div class='stat-label'>Kind Acts</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Daily affirmation
affirmations = [
    "You are worthy of love and care",
    "Your mental health matters",
    "Small steps lead to big changes",
    "You deserve to take time for yourself",
    "Your feelings are valid",
    "Rest is productive",
    "You are stronger than you think",
    "Be kind to yourself today"
]

st.markdown(f"""
<div class="affirmation-card">
    <div style='font-size: 3rem; margin-bottom: 1rem;'>💫</div>
    <div style='font-size: 1.2rem; color: #64748b; margin-bottom: 0.5rem;'>Today's Affirmation</div>
    <div class='affirmation-text'>"{random.choice(affirmations)}"</div>
</div>
""", unsafe_allow_html=True)

# Guided breathing
st.markdown("<div class='mindful-card'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'> Guided Breathing Journey</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #64748b; margin-bottom: 1.5rem;'>✨ Just 5 minutes reduces stress hormones by 30%</p>",
            unsafe_allow_html=True)

breathing_duration = st.selectbox("Choose your journey:",
                                  ["🌙 1 minute - Quick Reset", "🌸 3 minutes - Calm Focus", "🌊 5 minutes - Deep Peace"])
duration_map = {"🌙 1 minute - Quick Reset": 1, "🌸 3 minutes - Calm Focus": 3, "🌊 5 minutes - Deep Peace": 5}

if st.button("🌬️ Begin Breathing Journey", use_container_width=True):
    minutes = duration_map[breathing_duration]
    cycles = minutes * 2

    progress_bar = st.progress(0)
    timer_display = st.empty()
    instruction_text = st.empty()

    for cycle in range(cycles):
        instruction_text.markdown("### 🌬️ **Breathe In... Feel the peace**")
        for i in range(5):
            progress_bar.progress((cycle * 10 + i) / (cycles * 10))
            timer_display.markdown(f"<div class='timer-display'>{5 - i}</div>", unsafe_allow_html=True)
            time.sleep(1)

        instruction_text.markdown("### 🤲 **Hold... Stay present**")
        for i in range(2):
            progress_bar.progress((cycle * 10 + 5 + i) / (cycles * 10))
            timer_display.markdown(f"<div class='timer-display'>{2 - i}</div>", unsafe_allow_html=True)
            time.sleep(1)

        instruction_text.markdown("### 💨 **Release... Let go of tension**")
        for i in range(5):
            progress_bar.progress((cycle * 10 + 7 + i) / (cycles * 10))
            timer_display.markdown(f"<div class='timer-display'>{5 - i}</div>", unsafe_allow_html=True)
            time.sleep(1)

    st.session_state.breathing_completed += 1
    st.session_state.total_time_spent += minutes
    st.success(f"✨ Beautiful! You completed {minutes} minutes of mindful breathing")
    st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# Mood check-in
st.markdown("<div class='mindful-card'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>📊 Mood Reflection</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #64748b; margin-bottom: 1.5rem;'>💭 Tracking emotions increases self-awareness by 60%</p>",
            unsafe_allow_html=True)

mood_options = {
    "😊 Joyful": 5,
    "🙂 Content": 4,
    "😐 Neutral": 3,
    "😔 Low": 2,
    "😢 Struggling": 1
}

selected_mood = st.radio("How does your heart feel?", list(mood_options.keys()), horizontal=True)
mood_note = st.text_area("Share what's on your mind... (optional)",
                         placeholder="Express yourself freely, without judgment...")

if st.button("💾 Save This Moment", use_container_width=True):
    st.session_state.mood_log.append({
        "date": datetime.datetime.now(),
        "mood": selected_mood,
        "score": mood_options[selected_mood],
        "note": mood_note
    })
    st.success("✅ Your feelings are honored and saved")

    if mood_options[selected_mood] <= 2:
        st.warning("💛 You're not alone. Reaching out is brave.")
        st.info("**Support is here:**\n- 🆘 Crisis: 988\n- 💬 Text: HOME to 741741\n- 🌐 NAMI: 1-800-950-6264")

if len(st.session_state.mood_log) > 0:
    recent_moods = st.session_state.mood_log[-7:]
    avg_score = sum([m['score'] for m in recent_moods]) / len(recent_moods)
    st.markdown(
        f"<p style='color: #64748b; margin-top: 1rem;'>Your emotional journey: {avg_score:.1f}/5 over {len(recent_moods)} check-ins</p>",
        unsafe_allow_html=True)
    st.progress(avg_score / 5)

st.markdown("</div>", unsafe_allow_html=True)

# Gratitude practice
st.markdown("<div class='mindful-card'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>🙏 Gratitude Garden</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #64748b; margin-bottom: 1.5rem;'>🌱 Daily gratitude increases happiness by 25%</p>",
            unsafe_allow_html=True)

gratitude_items = [
    "☀️ Sunshine", "💧 Water", "❤️ Love", "🏠 Home",
    "🎵 Music", "📚 Learning", "🌱 Growth", "😊 Smiles"
]

st.markdown("**What fills your heart with gratitude today?**")
cols = st.columns(4)
for i, item in enumerate(gratitude_items):
    with cols[i % 4]:
        if st.button(item, key=f"grat_{i}", use_container_width=True):
            st.session_state.gratitude_score += 1
            st.toast(f"✨ +1 Gratitude! You now have {st.session_state.gratitude_score} points")

gratitude_entry = st.text_area("✍️ What are you grateful for today?", height=100,
                               placeholder="Write 3 things that brought light to your day...")

if st.button("💖 Plant in Gratitude Garden", use_container_width=True):
    if gratitude_entry:
        st.session_state.journal_entries.append({
            "date": datetime.datetime.now(),
            "entry": gratitude_entry,
            "type": "gratitude"
        })
        st.success("✨ Your gratitude is blooming!")
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# Acts of kindness
st.markdown("<div class='mindful-card'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>🌍 Kindness Ripple</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #64748b; margin-bottom: 1.5rem;'>💝 One act of kindness touches 5+ lives</p>",
            unsafe_allow_html=True)

kindness_ideas = [
    "💬 Send a heartfelt message",
    "👋 Share a genuine smile",
    "🎁 Unexpected kindness",
    "📱 Call a loved one",
    "💌 Leave encouragement",
    "🤝 Offer help",
    "🌟 Give a compliment",
    "🧡 Listen deeply"
]

cols = st.columns(2)
for i, idea in enumerate(kindness_ideas):
    with cols[i % 2]:
        if st.button(f"✅ {idea}", key=f"kind_{i}", use_container_width=True):
            st.session_state.kindness_acts.append({
                "date": datetime.datetime.now(),
                "act": idea
            })
            st.success(f"🌟 You've created {len(st.session_state.kindness_acts)} kindness ripples!")
            st.balloons()

if len(st.session_state.kindness_acts) > 0:
    st.markdown(f"""
    <div class='achievement-badge'>
        🏆 Kindness Champion: {len(st.session_state.kindness_acts)} acts of love shared!
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Stress relief
st.markdown("<div class='mindful-card'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>🎨 Joy Moments</h2>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["😂 Laughter Medicine", "🎵 Sound Healing", "🧩 Mindful Games"])

with tab1:
    jokes = [
        "Why don't scientists trust atoms? They make up everything! 😄",
        "What do you call a bear with no teeth? A gummy bear! 🐻",
        "Why did the bicycle fall over? It was two-tired! 🚴",
        "What do you call a fake noodle? An impasta! 🍝"
    ]
    if st.button("😂 Share a smile with me", use_container_width=True):
        st.success(random.choice(jokes))
        st.info("🧠 Laughter releases endorphins - nature's joy medicine!")

with tab2:
    st.markdown("**🎶 Sound heals the soul**")
    music_types = ["🎼 Classical Peace", "🌊 Ocean Waves", "🎹 Gentle Piano", "🎸 Acoustic Calm", "🎧 Ambient Dream"]
    selected_music = st.selectbox("Choose your sound:", music_types)

    if st.button("✅ I listened mindfully", use_container_width=True):
        st.session_state.total_time_spent += 5
        st.success("🎶 Music is soul medicine. Well done!")

with tab3:
    st.markdown("**🧠 Gentle mental exercise**")

    if "game_sequence" not in st.session_state:
        st.session_state.game_sequence = [random.randint(0, 3) for _ in range(3)]
        st.session_state.user_sequence = []

    colors = ["🔴 Red", "🔵 Blue", "🟢 Green", "🟡 Yellow"]
    pattern = " → ".join([colors[i] for i in st.session_state.game_sequence])

    st.markdown(f"**Remember:** {pattern}")
    st.markdown("**Now tap the pattern:**")

    cols = st.columns(4)
    for i, color in enumerate(colors):
        with cols[i]:
            if st.button(color, key=f"game_{i}", use_container_width=True):
                st.session_state.user_sequence.append(i)

                if len(st.session_state.user_sequence) == len(st.session_state.game_sequence):
                    if st.session_state.user_sequence == st.session_state.game_sequence:
                        st.success("🎉 Perfect harmony!")
                        st.balloons()
                    else:
                        st.info("Try again - it's about the journey!")

                    st.session_state.game_sequence = [random.randint(0, 3) for _ in range(3)]
                    st.session_state.user_sequence = []
                    time.sleep(2)
                    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# Journal
st.markdown("<div class='mindful-card'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>📝 Soul Journal</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #64748b; margin-bottom: 1.5rem;'>✍️ Writing heals - reduces anxiety by 30%</p>",
            unsafe_allow_html=True)

reflection_prompts = [
    "What brought me peace today?",
    "What challenge did I overcome?",
    "What am I proud of?",
    "What do I need to release?",
    "Who touched my heart today?"
]

selected_prompt = st.selectbox("Choose inspiration or write freely:", ["💭 Free flow writing"] + reflection_prompts)
if selected_prompt != "💭 Free flow writing":
    st.markdown(f"**Reflect on:** *{selected_prompt}*")

journal_text = st.text_area("Pour your heart out...", height=150,
                            placeholder="Write without judgment. This is your safe space...")

