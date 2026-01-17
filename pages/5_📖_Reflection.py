import streamlit as st
import json
from datetime import datetime
import os

# Page configuration
st.set_page_config(
    page_title="Mental Wellness Reflection",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 60px;
        font-size: 16px;
        font-weight: 500;
        transition: all 0.3s;
    }

    .mood-button {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        margin: 10px 0;
        transition: all 0.3s;
    }

    .mood-button:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: rgba(139, 92, 246, 0.5);
    }

    .feature-card {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 16px;
        padding: 24px;
        margin: 12px 0;
    }

    .privacy-badge {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(16, 185, 129, 0.1) 100%);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 12px;
        padding: 16px;
        margin: 20px 0;
    }

    .insight-card {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.15) 0%, rgba(59, 130, 246, 0.15) 100%);
        border-left: 4px solid #8b5cf6;
        border-radius: 8px;
        padding: 20px;
        margin: 16px 0;
    }

    .grounding-card {
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%);
        border: 1px solid rgba(6, 182, 212, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin: 16px 0;
    }

    h1, h2, h3 {
        color: #e5e7eb;
    }

    .stTextArea textarea {
        background: rgba(17, 24, 39, 0.5);
        border: 1px solid rgba(107, 114, 128, 0.3);
        border-radius: 12px;
        color: #e5e7eb;
    }

    .feeling-chip {
        display: inline-block;
        background: rgba(236, 72, 153, 0.2);
        border: 2px solid rgba(236, 72, 153, 0.4);
        border-radius: 8px;
        padding: 8px 16px;
        margin: 4px;
        cursor: pointer;
        transition: all 0.3s;
    }

    .feeling-chip-selected {
        background: rgba(236, 72, 153, 0.4);
        border-color: rgba(236, 72, 153, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = 'home'
if 'reflection_mode' not in st.session_state:
    st.session_state.reflection_mode = None
if 'mood_before' not in st.session_state:
    st.session_state.mood_before = None
if 'mood_after' not in st.session_state:
    st.session_state.mood_after = None
if 'selected_feelings' not in st.session_state:
    st.session_state.selected_feelings = []
if 'thought_patterns' not in st.session_state:
    st.session_state.thought_patterns = []
if 'guided_answers' not in st.session_state:
    st.session_state.guided_answers = {}
if 'current_prompt' not in st.session_state:
    st.session_state.current_prompt = 0
if 'free_text' not in st.session_state:
    st.session_state.free_text = ''
if 'self_compassion' not in st.session_state:
    st.session_state.self_compassion = ''
if 'reflection_history' not in st.session_state:
    st.session_state.reflection_history = []

# Data structures
MOODS = [
    {'emoji': '😌', 'label': 'Calm', 'value': 5},
    {'emoji': '😊', 'label': 'Happy', 'value': 4},
    {'emoji': '😐', 'label': 'Neutral', 'value': 3},
    {'emoji': '😔', 'label': 'Down', 'value': 2},
    {'emoji': '😰', 'label': 'Stressed', 'value': 1}
]

DEEP_FEELINGS = [
    'Overwhelmed', 'Disappointed', 'Lonely', 'Hopeful',
    'Anxious', 'Grateful', 'Frustrated', 'Content',
    'Worried', 'Peaceful', 'Confused', 'Energized'
]

THOUGHT_PATTERNS = [
    'Repeating thoughts',
    'Worry loops',
    'Self-criticism',
    'Overthinking',
    'Catastrophizing',
    'Comparing myself to others'
]

GUIDED_PROMPTS = [
    "What helped you calm down just now?",
    "What is one thing you handled better today?",
    "What felt heavy, even slightly?"
]

REFLECTION_MODES = [
    {
        'id': 'guided',
        'icon': '✨',
        'title': 'Guided Reflection',
        'desc': 'Short, gentle prompts based on your mood'
    },
    {
        'id': 'feelings',
        'icon': '💖',
        'title': 'Name the Feeling',
        'desc': 'Beyond basic emotions - identify nuanced feelings'
    },
    {
        'id': 'journal',
        'icon': '📖',
        'title': 'Free Reflection',
        'desc': 'A safe space just for you - no judgment'
    },
    {
        'id': 'patterns',
        'icon': '🧠',
        'title': 'Thought Patterns',
        'desc': 'Gentle awareness of your thinking'
    }
]


# Storage functions
def load_reflections():
    """Load reflection history from file"""
    if os.path.exists('reflections.json'):
        try:
            with open('reflections.json', 'r') as f:
                return json.load(f)
        except:
            return []
    return []


def save_reflection(data):
    """Save a new reflection"""
    reflections = load_reflections()
    data['timestamp'] = datetime.now().isoformat()
    data['date'] = datetime.now().strftime('%B %d, %Y')
    reflections.insert(0, data)

    # Keep only last 50 reflections
    reflections = reflections[:50]

    with open('reflections.json', 'w') as f:
        json.dump(reflections, f, indent=2)

    st.session_state.reflection_history = reflections


# Load reflections on startup
if not st.session_state.reflection_history:
    st.session_state.reflection_history = load_reflections()


# View functions
def show_home():
    """Home view with reflection mode selection"""
    st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>Take a moment</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: #9ca3af; margin-bottom: 40px;'>to reflect on how you're feeling</p>",
        unsafe_allow_html=True)

    # Reflection mode cards
    cols = st.columns(2)
    for idx, mode in enumerate(REFLECTION_MODES):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class='feature-card'>
                <div style='font-size: 32px; margin-bottom: 12px;'>{mode['icon']}</div>
                <h3 style='margin-bottom: 8px;'>{mode['title']}</h3>
                <p style='color: #9ca3af; font-size: 14px;'>{mode['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Start {mode['title']}", key=f"mode_{mode['id']}"):
                st.session_state.reflection_mode = mode['id']
                st.session_state.view = 'mood_before'
                st.rerun()

    # Privacy badge
    st.markdown("""
    <div class='privacy-badge'>
        <div style='display: flex; align-items: start;'>
            <div style='font-size: 24px; margin-right: 12px;'>🛡️</div>
            <div>
                <p style='margin: 0; color: #e5e7eb;'><strong>Private by Design</strong></p>
                <p style='margin: 4px 0 0 0; color: #9ca3af; font-size: 14px;'>Your reflections are stored locally on your device and remain completely private</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Reflection history
    if st.session_state.reflection_history:
        st.markdown("---")
        st.markdown("### 📅 Recent Reflections")
        st.caption("Your reflection timeline (no streaks, no pressure)")

        for reflection in st.session_state.reflection_history[:5]:
            with st.expander(f"{reflection['date']} - {reflection.get('type', 'reflection').title()}"):
                st.write(f"**Type:** {reflection.get('type', 'Unknown')}")
                if 'mood_before' in reflection:
                    st.write(f"Mood before: {reflection['mood_before']['emoji']} {reflection['mood_before']['label']}")
                if 'mood_after' in reflection:
                    st.write(f"Mood after: {reflection['mood_after']['emoji']} {reflection['mood_after']['label']}")


def show_mood_selector(stage):
    """Show mood selection interface"""
    title = "How are you feeling right now?" if stage == 'before' else "How are you feeling now?"
    subtitle = "Before we begin" if stage == 'before' else "After reflecting"

    st.markdown(f"<h2 style='text-align: center;'>{title}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #9ca3af; margin-bottom: 30px;'>{subtitle}</p>",
                unsafe_allow_html=True)

    for mood in MOODS:
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown(f"<div style='font-size: 48px; text-align: center;'>{mood['emoji']}</div>",
                        unsafe_allow_html=True)
        with col2:
            if st.button(mood['label'], key=f"mood_{stage}_{mood['value']}", use_container_width=True):
                if stage == 'before':
                    st.session_state.mood_before = mood
                    st.session_state.view = 'reflection'
                else:
                    st.session_state.mood_after = mood
                    st.session_state.view = 'insight'
                st.rerun()


def show_guided_reflection():
    """🔥 1. Guided Reflection Prompts (Adaptive)"""
    st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <div style='display: inline-block; background: rgba(139, 92, 246, 0.2); padding: 8px 16px; border-radius: 20px;'>
            <span style='margin-right: 8px;'>✨</span>
            <span style='color: #d1d5db;'>Guided Reflection</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Progress bar
    progress = st.session_state.current_prompt / len(GUIDED_PROMPTS)
    st.progress(progress)

    if st.session_state.current_prompt < len(GUIDED_PROMPTS):
        prompt = GUIDED_PROMPTS[st.session_state.current_prompt]

        st.markdown(f"""
        <div class='feature-card'>
            <p style='font-size: 18px; color: #e5e7eb; margin-bottom: 20px;'>{prompt}</p>
        </div>
        """, unsafe_allow_html=True)

        answer = st.text_area("Take your time...", height=120, key=f"prompt_{st.session_state.current_prompt}")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back", use_container_width=True):
                if st.session_state.current_prompt > 0:
                    st.session_state.current_prompt -= 1
                    st.rerun()
        with col2:
            if st.button("Continue →", use_container_width=True):
                if answer.strip():
                    st.session_state.guided_answers[st.session_state.current_prompt] = answer
                    st.session_state.current_prompt += 1
                    st.rerun()
    else:
        # Save and move to mood after
        save_reflection({
            'type': 'guided',
            'mode': 'Guided Reflection',
            'mood_before': st.session_state.mood_before,
            'answers': st.session_state.guided_answers
        })
        st.session_state.view = 'mood_after'
        st.session_state.current_prompt = 0
        st.rerun()


def show_feelings_reflection():
    """🪞 2. Name the Feeling - Deep Reflection"""
    st.markdown("""
    <div style='text-align: center; margin-bottom: 20px;'>
        <div style='display: inline-block; background: rgba(236, 72, 153, 0.2); padding: 8px 16px; border-radius: 20px;'>
            <span style='margin-right: 8px;'>💖</span>
            <span style='color: #d1d5db;'>Name the Feeling</span>
        </div>
        <p style='color: #9ca3af; margin-top: 10px; font-size: 14px;'>Select the words that match how you feel</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧠 Emotional Vocabulary")
    st.caption("This encourages emotional vocabulary growth")

    # Feelings selection grid
    cols = st.columns(3)
    for idx, feeling in enumerate(DEEP_FEELINGS):
        with cols[idx % 3]:
            is_selected = feeling in st.session_state.selected_feelings

            if st.button(
                    feeling,
                    key=f"feeling_{feeling}",
                    use_container_width=True,
                    type="primary" if is_selected else "secondary"
            ):
                if is_selected:
                    st.session_state.selected_feelings.remove(feeling)
                else:
                    st.session_state.selected_feelings.append(feeling)
                st.rerun()

    if st.session_state.selected_feelings:
        st.markdown("---")
        st.write("**You selected:**", ", ".join(st.session_state.selected_feelings))

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back", use_container_width=True):
                st.session_state.view = 'mood_before'
                st.rerun()
        with col2:
            if st.button("Continue →", use_container_width=True):
                save_reflection({
                    'type': 'feelings',
                    'mode': 'Name the Feeling',
                    'mood_before': st.session_state.mood_before,
                    'feelings': st.session_state.selected_feelings
                })
                st.session_state.view = 'mood_after'
                st.rerun()


def show_journal_reflection():
    """✍️ 3. One-Paragraph Free Reflection (Safe Journaling)"""
    st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <div style='display: inline-block; background: rgba(59, 130, 246, 0.2); padding: 8px 16px; border-radius: 20px;'>
            <span style='margin-right: 8px;'>📖</span>
            <span style='color: #d1d5db;'>Free Reflection</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='privacy-badge'>
        <div style='display: flex; align-items: start;'>
            <div style='font-size: 24px; margin-right: 12px;'>🛡️</div>
            <div>
                <p style='margin: 0; color: #93c5fd;'><strong>This space is just for you</strong></p>
                <p style='margin: 4px 0 0 0; color: #9ca3af; font-size: 14px;'>You don't need to make sense. No analysis. No scoring. No correction. This reflection stays only with you.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 💖 Very calming and ethical")

    journal_entry = st.text_area(
        "Write freely...",
        value=st.session_state.free_text,
        height=250,
        placeholder="This is your space. Write whatever comes to mind..."
    )
    st.session_state.free_text = journal_entry

    if len(journal_entry.strip()) > 10:
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back", use_container_width=True):
                st.session_state.view = 'mood_before'
                st.rerun()
        with col2:
            if st.button("Save Reflection", use_container_width=True):
                save_reflection({
                    'type': 'journal',
                    'mode': 'Free Reflection',
                    'mood_before': st.session_state.mood_before,
                    'entry_length': len(journal_entry)
                })
                st.session_state.view = 'mood_after'
                st.rerun()


def show_patterns_reflection():
    """🧠 4. Thought Pattern Awareness"""
    st.markdown("""
    <div style='text-align: center; margin-bottom: 20px;'>
        <div style='display: inline-block; background: rgba(99, 102, 241, 0.2); padding: 8px 16px; border-radius: 20px;'>
            <span style='margin-right: 8px;'>🧠</span>
            <span style='color: #d1d5db;'>Thought Pattern Awareness</span>
        </div>
        <p style='color: #9ca3af; margin-top: 10px; font-size: 14px;'>Gentle awareness, not judgment</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### This is awareness, not diagnosis")

    for pattern in THOUGHT_PATTERNS:
        is_selected = pattern in st.session_state.thought_patterns

        if st.button(
                f"{'✓ ' if is_selected else ''}{pattern}",
                key=f"pattern_{pattern}",
                use_container_width=True,
                type="primary" if is_selected else "secondary"
        ):
            if is_selected:
                st.session_state.thought_patterns.remove(pattern)
            else:
                st.session_state.thought_patterns.append(pattern)
            st.rerun()

    if st.session_state.thought_patterns:
        st.markdown("---")
        st.info(f"You noticed: {', '.join(st.session_state.thought_patterns)}")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back", use_container_width=True):
                st.session_state.view = 'mood_before'
                st.rerun()
        with col2:
            if st.button("Continue to Self-Compassion →", use_container_width=True):
                st.session_state.view = 'compassion'
                st.rerun()


def show_compassion():
    """💬 7. Self-Compassion Reflection"""
    st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <div style='display: inline-block; background: rgba(244, 63, 94, 0.2); padding: 8px 16px; border-radius: 20px;'>
            <span style='margin-right: 8px;'>💖</span>
            <span style='color: #d1d5db;'>Self-Compassion</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 💗 This is powerful and uncommon")

    st.markdown("""
    <div class='feature-card'>
        <p style='color: #e5e7eb; font-size: 16px; margin-bottom: 16px;'>If I spoke to myself kindly, I would say...</p>
    </div>
    """, unsafe_allow_html=True)

    compassion_text = st.text_area(
        "Speak to yourself with kindness...",
        value=st.session_state.self_compassion,
        height=150,
        placeholder="What would you say to a good friend in your situation?"
    )
    st.session_state.self_compassion = compassion_text

    if len(compassion_text.strip()) > 10:
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back", use_container_width=True):
                st.session_state.view = 'reflection'
                st.rerun()
        with col2:
            if st.button("Continue →", use_container_width=True):
                save_reflection({
                    'type': 'patterns_and_compassion',
                    'mode': 'Thought Patterns & Self-Compassion',
                    'mood_before': st.session_state.mood_before,
                    'patterns': st.session_state.thought_patterns,
                    'compassion_length': len(compassion_text)
                })
                st.session_state.view = 'mood_after'
                st.rerun()


def show_insight():
    """🎯 8. Gentle Insight Summary & Closing"""
    st.markdown("<h2 style='text-align: center;'>Your Reflection</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #9ca3af; margin-bottom: 30px;'>Here's what you noticed</p>",
                unsafe_allow_html=True)

    # 🔄 5. Before vs After Reflection Snapshot
    if st.session_state.mood_before and st.session_state.mood_after:
        st.markdown("### 🔄 Before & After Snapshot")

        mood_change = st.session_state.mood_after['value'] - st.session_state.mood_before['value']

        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.markdown(
                f"<div style='text-align: center; font-size: 48px;'>{st.session_state.mood_before['emoji']}</div>",
                unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center; color: #9ca3af;'>Before</p>", unsafe_allow_html=True)

        with col2:
            if mood_change > 0:
                st.progress(0.75)
                st.success("✨ Something shifted positively")
            elif mood_change < 0:
                st.progress(0.25)
                st.info("💭 Your feelings remained active")
            else:
                st.progress(0.5)
                st.info("😌 Your mood stayed steady")

        with col3:
            st.markdown(
                f"<div style='text-align: center; font-size: 48px;'>{st.session_state.mood_after['emoji']}</div>",
                unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center; color: #9ca3af;'>After</p>", unsafe_allow_html=True)

        st.markdown("### 📊 Makes progress visible without pressure")

    # Gentle Insight Summary
    st.markdown("""
    <div class='insight-card'>
        <h3 style='margin-top: 0;'>🎯 Gentle Insight</h3>
        <p style='color: #e5e7eb; line-height: 1.6;'>
            You took time to pause and reflect. That itself is a form of self-care. 
            Even when feelings stay complex, awareness matters. This was not about fixing or changing—
            it was about noticing and being present with yourself.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ✔ Safe and respectful - No labels. No diagnosis.")

    # 🌤️ 11. Closing Grounding Prompt
    st.markdown("""
    <div class='grounding-card'>
        <div style='display: flex; align-items: start;'>
            <div style='font-size: 28px; margin-right: 12px;'>🌬️</div>
            <div>
                <p style='margin: 0; color: #67e8f9;'><strong>Take one slow breath</strong></p>
                <p style='margin: 8px 0 0 0; color: #9ca3af;'>Before moving on, ground yourself in this moment.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧘 Soft closure")

    # ⭐ 12. Suggested Next Step
    st.markdown("---")
    st.markdown("### ⭐ What would you like to do next?")
    st.caption("Smart continuity - keeps flow natural")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Return to Home", use_container_width=True):
            reset_session()
            st.session_state.view = 'home'
            st.rerun()

    with col2:
        if st.button("✨ Start Another Reflection", use_container_width=True):
            reset_session()
            st.session_state.view = 'home'
            st.rerun()


def reset_session():
    """Reset session state for new reflection"""
    st.session_state.mood_before = None
    st.session_state.mood_after = None
    st.session_state.selected_feelings = []
    st.session_state.thought_patterns = []
    st.session_state.guided_answers = {}
    st.session_state.current_prompt = 0
    st.session_state.free_text = ''
    st.session_state.self_compassion = ''
    st.session_state.reflection_mode = None


# Main app routing
def main():
    # Add back button for non-home views
    if st.session_state.view != 'home':
        if st.button("← Back to Home", key="back_home"):
            reset_session()
            st.session_state.view = 'home'
            st.rerun()
        st.markdown("---")

    # Route to appropriate view
    if st.session_state.view == 'home':
        show_home()
    elif st.session_state.view == 'mood_before':
        show_mood_selector('before')
    elif st.session_state.view == 'mood_after':
        show_mood_selector('after')
    elif st.session_state.view == 'reflection':
        if st.session_state.reflection_mode == 'guided':
            show_guided_reflection()
        elif st.session_state.reflection_mode == 'feelings':
            show_feelings_reflection()
        elif st.session_state.reflection_mode == 'journal':
            show_journal_reflection()
        elif st.session_state.reflection_mode == 'patterns':
            show_patterns_reflection()
    elif st.session_state.view == 'compassion':
        show_compassion()
    elif st.session_state.view == 'insight':
        show_insight()


if __name__ == "__main__":
    main()
