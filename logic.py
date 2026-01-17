import os
import random
import re
from datetime import timedelta, datetime, date

import streamlit as st
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from openai import OpenAI

# =========================
# OPENAI CLIENT (HUMAN REFINER)
# =========================
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# =========================
# LOAD TRAINED ML MODEL (v3)
# =========================
@st.cache_resource
def load_ml_model():
    tfidf = joblib.load("tfidf_vectorizer_v3.pkl")
    X_train_tfidf = joblib.load("train_vectors_v3.pkl")
    y_train = joblib.load("train_responses_v3.pkl")  # list
    return tfidf, X_train_tfidf, y_train

tfidf, X_train_tfidf, y_train = load_ml_model()

# =========================
# EMERGENCY DETECTION
# =========================
def is_emergency(text):
    keywords = [
        "suicide", "kill myself", "end my life",
        "hurt myself", "self harm", "die"
    ]
    return any(k in text.lower() for k in keywords)

def emergency_message():
    return (
        "I’m really glad you reached out 💛\n\n"
        "If you’re feeling unsafe right now, please contact:\n\n"
        "📞 Call or Text **988**\n"
        "📱 Text **HOME** to **741741**\n\n"
        "You don’t have to face this alone."
    )

# =========================
# HYBRID RESPONSE (CORRECT WAY)
# =========================
def get_ai_response(user_input, chat_history=None):
    user_input = user_input.strip()

    # ---- Emergency override ----
    if is_emergency(user_input):
        return emergency_message()

    # ---- STEP 1: ML generates guidance (SILENT) ----
    user_vec = tfidf.transform([user_input.lower()])
    similarities = cosine_similarity(user_vec, X_train_tfidf)[0]
    best_idx = similarities.argmax()
    ml_guidance = y_train[best_idx]

    # ---- STEP 2: AI RESPONDS NATURALLY (NOT REWRITE) ----
    try:
        system_prompt = """
You are Zenith.

You are NOT an assistant.
You are NOT a therapist.
You are a calm, caring parent-friend sitting beside the user.

Important rules:
- Read the ML guidance silently. Do NOT repeat or rewrite it.
- Respond naturally as a human would speak.
- Sound warm, grounded, and reassuring.
- Use short paragraphs.
- Give simple, practical steps.
- Avoid diagnosis, labels, or lectures.
- Use gentle emojis (🌿 🤍 📘 🕊️) when helpful.
- End with ONE soft, caring question.

Tone:
Slow.
Kind.
Human.
Like a trusted elder who understands life.
"""

        user_prompt = f"""
User message:
"{user_input}"

(Background guidance for you to understand silently):
"{ml_guidance}"

Now respond naturally as a caring parent-friend.
"""

        response = client.responses.create(
            model="gpt-5-nano",
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        return response.output_text.strip()

    except Exception:
        # ---- Gentle fallback ----
        return (
            "I hear you 🤍 Let’s slow this moment down together. "
            "You don’t have to carry everything at once. "
            "What feels heaviest right now?"
        )

# =========================
# STRESS ANALYSIS
# =========================
def analyze_vitals(text):
    fillers = len(re.findall(r"\b(um|uh|like|so|actually)\b", text.lower()))
    polarity = TextBlob(text).sentiment.polarity

    if polarity < -0.6:
        stress = "High Stress"
    elif fillers > 3 or polarity < -0.2:
        stress = "Elevated"
    else:
        stress = "Calm"

    est_hr = int(72 + abs(polarity) * 30)
    return stress, est_hr

# =========================
# DAILY AFFIRMATION
# =========================
def get_daily_affirmation():
    affirmations = [
        "You are enough just as you are.",
        "Small steps still matter.",
        "You’re doing the best you can.",
        "It’s okay to go gently today.",
        "You don’t have to be perfect."
    ]
    random.seed(datetime.now().strftime("%Y-%m-%d"))
    return random.choice(affirmations)

# =========================
# WELLNESS GOALS
# =========================
def get_daily_wellness_goals(mood):
    return {
        "Stressed": [
            "Take 5 slow breaths",
            "Relax shoulders and jaw",
            "Drink water",
            "Study one small topic only"
        ],
        "Anxious": [
            "Name 3 things you see",
            "One grounding breath",
            "Stretch your hands",
            "Remind yourself: I am safe"
        ],
        "Sad": [
            "Sit quietly for 5 minutes",
            "Write one kind sentence",
            "Listen to a soft sound",
            "Let the feeling pass gently"
        ],
        "Low Energy": [
            "Wash your face",
            "Do one tiny task",
            "Step into sunlight",
            "Rest without guilt"
        ]
    }.get(mood, [])

# =========================
# STREAK SYSTEM
# =========================
def update_streak(completed_today):
    today = date.today()

    if "streak_count" not in st.session_state:
        st.session_state.streak_count = 0
        st.session_state.last_streak_date = None

    last = st.session_state.last_streak_date

    if completed_today:
        if last == today:
            return st.session_state.streak_count
        if last == today - timedelta(days=1):
            st.session_state.streak_count += 1
        else:
            st.session_state.streak_count = 1
        st.session_state.last_streak_date = today

    return st.session_state.streak_count

# =========================
# AUDIO PLACEHOLDERS
# =========================
def speech_to_text(audio):
    return None

def text_to_speech(text):
    return None
