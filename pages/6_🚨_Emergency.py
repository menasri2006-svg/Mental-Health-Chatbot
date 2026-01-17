import streamlit as st
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="You're Not Alone - We're Here",
    page_icon="🫂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for ultra-friendly, calming design
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        animation: gradientShift 15s ease infinite;
    }

    @keyframes gradientShift {
        0%, 100% { background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); }
        50% { background: linear-gradient(135deg, #f093fb 0%, #667eea 50%, #764ba2 100%); }
    }

    .hero-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 30px;
        padding: 50px;
        margin: 20px auto;
        max-width: 900px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        text-align: center;
        animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .breathing-circle {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea, #764ba2);
        margin: 30px auto;
        animation: breathe 4s ease-in-out infinite;
        box-shadow: 0 0 40px rgba(102, 126, 234, 0.6);
    }

    @keyframes breathe {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.2); opacity: 1; }
    }

    .emergency-card {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.1));
        border: 3px solid #ef4444;
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(239, 68, 68, 0.2);
        animation: pulse 2s ease-in-out infinite;
    }

    @keyframes pulse {
        0%, 100% { box-shadow: 0 10px 30px rgba(239, 68, 68, 0.2); }
        50% { box-shadow: 0 10px 40px rgba(239, 68, 68, 0.4); }
    }

    .crisis-hotline {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        border-left: 6px solid #ef4444;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        transition: all 0.3s;
    }

    .crisis-hotline:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }

    .support-card {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1));
        border: 2px solid #3b82f6;
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.15);
    }

    .grounding-exercise {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1));
        border: 2px solid #10b981;
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.15);
    }

    .affirmation-card {
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(147, 51, 234, 0.1));
        border: 2px solid #a855f7;
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        text-align: center;
        box-shadow: 0 8px 25px rgba(168, 85, 247, 0.15);
    }

    .phone-number {
        font-size: 32px;
        font-weight: bold;
        color: #ef4444;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }

    .friendly-text {
        font-size: 20px;
        line-height: 1.8;
        color: #1f2937;
        margin: 20px 0;
    }

    .gentle-reminder {
        background: linear-gradient(135deg, rgba(251, 191, 36, 0.1), rgba(245, 158, 11, 0.1));
        border: 2px solid #fbbf24;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        font-size: 16px;
        color: #78350f;
    }

    .stButton>button {
        border-radius: 15px;
        padding: 15px 30px;
        font-size: 18px;
        font-weight: 600;
        border: none;
        transition: all 0.3s;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    }

    .countdown-text {
        font-size: 48px;
        font-weight: bold;
        color: #667eea;
        text-align: center;
        margin: 20px 0;
    }

    .comfort-message {
        background: white;
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border-left: 6px solid #a855f7;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
    }

    h1, h2, h3 {
        color: #1f2937;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'main'
if 'breathing_active' not in st.session_state:
    st.session_state.breathing_active = False
if 'grounding_step' not in st.session_state:
    st.session_state.grounding_step = 0

# Crisis hotlines data
CRISIS_HOTLINES = {
    "USA": [
        {"name": "National Suicide Prevention Lifeline", "number": "988", "available": "24/7", "info": "Talk or text"},
        {"name": "Crisis Text Line", "number": "Text HOME to 741741", "available": "24/7", "info": "Text support"},
        {"name": "SAMHSA National Helpline", "number": "1-800-662-4357", "available": "24/7",
         "info": "Mental health & substance abuse"},
    ],
    "International": [
        {"name": "International Association for Suicide Prevention", "info": "Find your country's helpline",
         "link": "https://www.iasp.info/resources/Crisis_Centres/"},
    ]
}

# Grounding exercises
GROUNDING_EXERCISES = [
    {
        "name": "5-4-3-2-1 Technique",
        "icon": "👀",
        "steps": [
            "Name 5 things you can SEE around you",
            "Name 4 things you can TOUCH right now",
            "Name 3 things you can HEAR",
            "Name 2 things you can SMELL",
            "Name 1 thing you can TASTE"
        ]
    },
    {
        "name": "Box Breathing",
        "icon": "🫁",
        "steps": [
            "Breathe in for 4 counts",
            "Hold for 4 counts",
            "Breathe out for 4 counts",
            "Hold for 4 counts",
            "Repeat 4 times"
        ]
    },
    {
        "name": "Body Scan",
        "icon": "🧘",
        "steps": [
            "Notice your feet touching the ground",
            "Feel your legs and how they support you",
            "Notice your breathing in your chest",
            "Relax your shoulders",
            "Soften your jaw and face"
        ]
    }
]

AFFIRMATIONS = [
    "You are stronger than you know 💪",
    "This moment will pass 🌅",
    "You deserve kindness and care 💝",
    "Your feelings are valid 🫂",
    "You are not alone in this 🤝",
    "It's okay to ask for help 🆘",
    "You are doing the best you can 🌟",
    "Tomorrow is a new day 🌄",
]


def show_hero_section():
    """Main hero section with immediate comfort"""
    st.markdown("""
    <div class='hero-container'>
        <h1 style='font-size: 48px; margin-bottom: 20px; color: #667eea;'>
            💜 Hey, You're Not Alone 💜
        </h1>
        <p class='friendly-text'>
            I'm really glad you're here. Whatever you're going through right now, 
            you don't have to face it alone. Let's take this moment together.
        </p>
        <div class='breathing-circle'></div>
        <p style='font-size: 18px; color: #6b7280; margin-top: 20px;'>
            Just breathe with this circle for a moment... In and out... You're safe here.
        </p>
    </div>
    """, unsafe_allow_html=True)


def show_immediate_crisis():
    """Emergency contacts section"""
    st.markdown("""
    <div class='emergency-card'>
        <h2 style='color: #ef4444; margin-bottom: 20px;'>
            🚨 If You're in Immediate Danger
        </h2>
        <p class='friendly-text' style='font-size: 18px;'>
            If you're thinking about hurting yourself or someone else right now, 
            please reach out immediately. You matter, and people want to help.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='crisis-hotline'>
            <h3 style='color: #ef4444; margin-bottom: 15px;'>🇺🇸 USA - Call or Text</h3>
            <div class='phone-number'>988</div>
            <p style='font-size: 16px; color: #6b7280; margin-top: 10px;'>
                National Suicide Prevention Lifeline<br>
                Available 24/7 - Free & Confidential
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📞 How to Make the Call", use_container_width=True, type="primary"):
            st.session_state.current_view = 'call_guide'
            st.rerun()

    with col2:
        st.markdown("""
        <div class='crisis-hotline'>
            <h3 style='color: #ef4444; margin-bottom: 15px;'>💬 Prefer to Text?</h3>
            <div class='phone-number' style='font-size: 24px;'>Text HOME to 741741</div>
            <p style='font-size: 16px; color: #6b7280; margin-top: 10px;'>
                Crisis Text Line<br>
                24/7 Support via Text Message
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("💭 What to Expect", use_container_width=True, type="primary"):
            st.session_state.current_view = 'text_guide'
            st.rerun()


def show_gentle_grounding():
    """Gentle grounding exercises"""
    st.markdown("""
    <div class='comfort-message'>
        <h2 style='color: #10b981; margin-bottom: 15px;'>
            🌿 Let's Ground Together
        </h2>
        <p class='friendly-text'>
            When everything feels overwhelming, sometimes the simplest things can help. 
            Try one of these with me - no pressure, just gentle support.
        </p>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs([f"{ex['icon']} {ex['name']}" for ex in GROUNDING_EXERCISES])

    for idx, tab in enumerate(tabs):
        with tab:
            exercise = GROUNDING_EXERCISES[idx]

            st.markdown(f"""
            <div class='grounding-exercise'>
                <h3 style='color: #10b981;'>{exercise['icon']} {exercise['name']}</h3>
            </div>
            """, unsafe_allow_html=True)

            if exercise['name'] == "Box Breathing":
                if st.button("🫁 Start Guided Breathing", use_container_width=True, type="primary"):
                    st.session_state.current_view = 'breathing'
                    st.rerun()

            st.markdown("### Steps:")
            for step_num, step in enumerate(exercise['steps'], 1):
                st.markdown(f"""
                <div style='background: white; padding: 15px; margin: 10px 0; 
                     border-radius: 10px; border-left: 4px solid #10b981;'>
                    <strong style='color: #10b981;'>Step {step_num}:</strong> {step}
                </div>
                """, unsafe_allow_html=True)


def show_comfort_words():
    """Comforting affirmations and validation"""
    st.markdown("""
    <div class='affirmation-card'>
        <h2 style='color: #a855f7; margin-bottom: 20px;'>
            💝 Some Words Just for You
        </h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    for idx, affirmation in enumerate(AFFIRMATIONS):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(f"""
            <div class='support-card'>
                <p style='font-size: 20px; text-align: center; margin: 0;'>
                    {affirmation}
                </p>
            </div>
            """, unsafe_allow_html=True)


def show_what_happens_next():
    """Explain what reaching out looks like"""
    st.markdown("""
    <div class='comfort-message'>
        <h2 style='color: #3b82f6;'>
            🤝 What Happens When You Reach Out
        </h2>
        <p class='friendly-text'>
            I know reaching out can feel scary. Here's what you can expect - 
            no surprises, just support.
        </p>
    </div>
    """, unsafe_allow_html=True)

    steps = [
        ("Someone answers who genuinely cares", "They're trained, kind, and there just for you", "💙"),
        ("You can share as much or as little as you want", "There's no pressure - you're in control", "🗣️"),
        ("They'll listen without judgment", "Your feelings are valid, and they know that", "👂"),
        ("Together, you'll make a plan", "Small, manageable steps to help you feel safer", "📋"),
        ("Everything is confidential", "Your privacy matters and is protected", "🔒"),
    ]

    for title, desc, emoji in steps:
        st.markdown(f"""
        <div class='support-card'>
            <h3 style='color: #3b82f6;'>{emoji} {title}</h3>
            <p style='font-size: 16px; color: #4b5563; margin-top: 10px;'>{desc}</p>
        </div>
        """, unsafe_allow_html=True)


def show_gentle_reminders():
    """Gentle validation and encouragement"""
    st.markdown("""
    <div class='gentle-reminder'>
        <h3 style='color: #92400e; margin-bottom: 15px;'>
            ✨ Gentle Reminders
        </h3>
        <ul style='list-style: none; padding: 0;'>
            <li style='margin: 12px 0; font-size: 16px;'>
                💛 <strong>It's okay to not be okay</strong> - You don't have to pretend
            </li>
            <li style='margin: 12px 0; font-size: 16px;'>
                🌟 <strong>Asking for help is brave</strong> - Not weak, incredibly brave
            </li>
            <li style='margin: 12px 0; font-size: 16px;'>
                🫂 <strong>You deserve support</strong> - No matter what you're going through
            </li>
            <li style='margin: 12px 0; font-size: 16px;'>
                🌈 <strong>This feeling is temporary</strong> - Even if it doesn't feel like it now
            </li>
            <li style='margin: 12px 0; font-size: 16px;'>
                💪 <strong>You've survived 100% of your worst days</strong> - You're stronger than you know
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


def show_breathing_exercise():
    """Interactive breathing exercise"""
    st.markdown("""
    <div class='hero-container'>
        <h2 style='color: #667eea;'>🫁 Box Breathing Together</h2>
        <p class='friendly-text'>Follow along with me. We'll do this together.</p>
    </div>
    """, unsafe_allow_html=True)

    placeholder = st.empty()

    if st.button("← Back to Support", use_container_width=True):
        st.session_state.current_view = 'main'
        st.rerun()

    if st.button("🌬️ Start Breathing Exercise", use_container_width=True, type="primary"):
        cycle_steps = [
            ("Breathe In...", "1...2...3...4", "#667eea", 4),
            ("Hold...", "1...2...3...4", "#764ba2", 4),
            ("Breathe Out...", "1...2...3...4", "#f093fb", 4),
            ("Hold...", "1...2...3...4", "#764ba2", 4),
        ]

        for cycle in range(4):
            st.markdown(f"<h3 style='text-align: center; color: #667eea;'>Cycle {cycle + 1} of 4</h3>",
                        unsafe_allow_html=True)

            for instruction, count, color, duration in cycle_steps:
                with placeholder.container():
                    st.markdown(f"""
                    <div style='text-align: center; padding: 50px;'>
                        <div style='font-size: 36px; color: {color}; font-weight: bold; margin-bottom: 20px;'>
                            {instruction}
                        </div>
                        <div class='countdown-text' style='color: {color};'>
                            {count}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    time.sleep(duration)

        with placeholder.container():
            st.success("🌟 Amazing! You did it! How do you feel?")
            st.balloons()


def show_call_guide():
    """Guide for making the call"""
    st.markdown("""
    <div class='hero-container'>
        <h2 style='color: #ef4444;'>📞 Making the Call - Step by Step</h2>
        <p class='friendly-text'>
            I know calling can feel scary. Here's exactly what will happen, 
            so there are no surprises.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Back to Support", use_container_width=True):
        st.session_state.current_view = 'main'
        st.rerun()

    st.markdown("""
    <div class='support-card'>
        <h3>1️⃣ Dial 988</h3>
        <p>Just three numbers. That's all you need to remember.</p>
    </div>

    <div class='support-card'>
        <h3>2️⃣ Wait for Someone to Answer (Usually 30 seconds or less)</h3>
        <p>A trained, caring counselor will pick up. They want to help.</p>
    </div>

    <div class='support-card'>
        <h3>3️⃣ You Can Say Something Like:</h3>
        <ul style='font-size: 16px; line-height: 1.8;'>
            <li>"I'm having a really hard time right now"</li>
            <li>"I'm not sure what to do"</li>
            <li>"I need someone to talk to"</li>
            <li>Or just "Help" - that's enough</li>
        </ul>
    </div>

    <div class='support-card'>
        <h3>4️⃣ They'll Listen and Help</h3>
        <p>They'll ask how you're feeling, what's going on, and help you figure out next steps. 
        You're in control of the conversation.</p>
    </div>

    <div class='gentle-reminder'>
        <strong>Remember:</strong> You can hang up anytime. You can call back anytime. 
        There's no judgment, only support.
    </div>
    """, unsafe_allow_html=True)


def show_text_guide():
    """Guide for texting support"""
    st.markdown("""
    <div class='hero-container'>
        <h2 style='color: #3b82f6;'>💬 Texting for Support</h2>
        <p class='friendly-text'>
            Prefer to text? That's completely okay. Here's how it works.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Back to Support", use_container_width=True):
        st.session_state.current_view = 'main'
        st.rerun()

    st.markdown("""
    <div class='support-card'>
        <h3>📱 Text HOME to 741741</h3>
        <p style='font-size: 18px;'>Just open your messages and text the word "HOME" to that number.</p>
    </div>

    <div class='support-card'>
        <h3>💭 What Happens Next</h3>
        <ol style='font-size: 16px; line-height: 1.8;'>
            <li>You'll get an automated reply welcoming you</li>
            <li>Within minutes, a real counselor will text you</li>
            <li>They'll ask how you're feeling and what's going on</li>
            <li>You text back and forth - take your time with responses</li>
        </ol>
    </div>

    <div class='support-card'>
        <h3>✨ Why Texting is Great</h3>
        <ul style='font-size: 16px; line-height: 1.8;'>
            <li>💬 No need to talk out loud</li>
            <li>⏰ Respond at your own pace</li>
            <li>🔒 Completely private and confidential</li>
            <li>🌙 Available 24/7, even at 3am</li>
        </ul>
    </div>

    <div class='gentle-reminder'>
        <strong>Tip:</strong> You can text them even if you're "not sure" if it's serious enough. 
        There's no minimum level of crisis needed. If you're struggling, you deserve support.
    </div>
    """, unsafe_allow_html=True)


# Main app
def main():
    if st.session_state.current_view == 'breathing':
        show_breathing_exercise()
    elif st.session_state.current_view == 'call_guide':
        show_call_guide()
    elif st.session_state.current_view == 'text_guide':
        show_text_guide()
    else:
        # Main view
        show_hero_section()

        st.markdown("<br>", unsafe_allow_html=True)

        show_immediate_crisis()

        st.markdown("<br>", unsafe_allow_html=True)

        show_gentle_grounding()

        st.markdown("<br>", unsafe_allow_html=True)

        show_what_happens_next()

        st.markdown("<br>", unsafe_allow_html=True)

        show_comfort_words()

        st.markdown("<br>", unsafe_allow_html=True)

        show_gentle_reminders()

        # Footer
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div class='comfort-message' style='text-align: center;'>
            <h3 style='color: #667eea;'>💜 You Made It Here 💜</h3>
            <p class='friendly-text'>
                That took courage. Whatever you decide to do next, 
                know that you're worthy of support, care, and better days ahead.
            </p>
            <p style='font-size: 16px; color: #6b7280; margin-top: 20px;'>
                You are not alone. You never were. 🫂
            </p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
