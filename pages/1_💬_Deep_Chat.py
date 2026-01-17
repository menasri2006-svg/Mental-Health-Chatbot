import streamlit as st
import logic
import style
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Wellness Hub • Your Mental Health Companion",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styles
style.apply_styles()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_start" not in st.session_state:
    st.session_state.session_start = datetime.now()
if "show_timestamps" not in st.session_state:
    st.session_state.show_timestamps = True
if "export_clicked" not in st.session_state:
    st.session_state.export_clicked = False
if "wellness_score" not in st.session_state:
    st.session_state.wellness_score = 0

# Helper function to format timestamp
def get_timestamp():
    return datetime.now().strftime("%I:%M %p")

# Helper function to export conversation
def export_conversation():
    if not st.session_state.messages:
        return "No conversation to export."
    
    export_text = f"=== Wellness Hub Conversation Export ===\n"
    export_text += f"Date: {datetime.now().strftime('%B %d, %Y')}\n"
    export_text += f"Session Duration: {(datetime.now() - st.session_state.session_start).seconds // 60} minutes\n"
    export_text += f"Total Messages: {len(st.session_state.messages)}\n\n"
    export_text += "=" * 50 + "\n\n"
    
    for i, msg in enumerate(st.session_state.messages, 1):
        role = "You" if msg["role"] == "user" else "Wellness Guide"
        timestamp = msg.get("timestamp", "")
        export_text += f"[{i}] {role}"
        if timestamp:
            export_text += f" - {timestamp}"
        export_text += f"\n{msg['content']}\n\n"
    
    return export_text

# Ultra Premium CSS with Mental Health Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Raleway:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #E0F7FA 0%, #B2EBF2 25%, #80DEEA 50%, #E1BEE7 75%, #F3E5F5 100%);
        background-size: 400% 400%;
        animation: gentleFlow 20s ease infinite;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(129, 212, 250, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(186, 104, 200, 0.15) 0%, transparent 50%);
        animation: particleFloat 15s ease-in-out infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes gentleFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes particleFloat {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.6; }
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    
    .main {
        padding: 0 !important;
        position: relative;
        z-index: 1;
    }
    
    .block-container {
        padding: 2.5rem 3rem !important;
        max-width: 1400px !important;
    }
    
    .premium-header {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.7) 100%);
        backdrop-filter: blur(30px);
        border: 2px solid rgba(255, 255, 255, 0.5);
        border-radius: 30px;
        padding: 3.5rem 2.5rem;
        margin-bottom: 2.5rem;
        box-shadow: 0 20px 60px rgba(129, 212, 250, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .premium-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        animation: shimmerFlow 4s ease-in-out infinite;
    }
    
    @keyframes shimmerFlow {
        0% { left: -100%; }
        100% { left: 200%; }
    }
    
    .premium-header::after {
        content: '🌸 ✨ 🦋 💫 🌺';
        position: absolute;
        top: 1rem;
        right: 2rem;
        font-size: 1.5rem;
        opacity: 0.3;
        animation: floatDecor 6s ease-in-out infinite;
    }
    
    @keyframes floatDecor {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .header-title {
        color: transparent;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin: 0;
        background: linear-gradient(135deg, #4FC3F7 0%, #BA68C8 50%, #FFB74D 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 2px 10px rgba(79, 195, 247, 0.3));
        position: relative;
        z-index: 1;
    }
    
    .header-subtitle {
        color: rgba(66, 66, 66, 0.8);
        text-align: center;
        font-size: 1.3rem;
        margin-top: 0.8rem;
        font-family: 'Raleway', sans-serif;
        position: relative;
        z-index: 1;
    }
    
    .header-stats {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 2rem;
        flex-wrap: wrap;
        position: relative;
        z-index: 1;
    }
    
    .stat-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.6) 100%);
        backdrop-filter: blur(20px);
        padding: 1rem 2rem;
        border-radius: 20px;
        border: 2px solid rgba(255, 255, 255, 0.8);
        text-align: center;
        box-shadow: 0 8px 32px rgba(79, 195, 247, 0.15);
        transition: all 0.4s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-8px) scale(1.05);
        box-shadow: 0 16px 48px rgba(186, 104, 200, 0.25);
    }
    
    .stat-value {
        background: linear-gradient(135deg, #4FC3F7, #BA68C8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2rem;
        font-weight: 800;
    }
    
    .stat-label {
        color: rgba(66, 66, 66, 0.7);
        font-size: 0.85rem;
        margin-top: 0.3rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600;
    }
    
    .chat-wrapper {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.85) 0%, rgba(255, 255, 255, 0.65) 100%);
        backdrop-filter: blur(25px);
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 25px;
        padding: 2.5rem;
        margin: 2rem 0;
        min-height: 520px;
        max-height: 620px;
        overflow-y: auto;
        box-shadow: 0 12px 40px rgba(79, 195, 247, 0.15);
    }
    
    .chat-wrapper::-webkit-scrollbar {
        width: 10px;
    }
    
    .chat-wrapper::-webkit-scrollbar-track {
        background: linear-gradient(135deg, rgba(224, 247, 250, 0.3), rgba(225, 190, 231, 0.3));
        border-radius: 10px;
    }
    
    .chat-wrapper::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #4FC3F7, #BA68C8);
        border-radius: 10px;
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    .stChatMessage {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.85) 100%) !important;
        backdrop-filter: blur(15px) !important;
        border: 2px solid rgba(255, 255, 255, 0.7) !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        margin: 1.2rem 0 !important;
        box-shadow: 0 8px 32px rgba(79, 195, 247, 0.12) !important;
        transition: all 0.4s ease !important;
    }
    
    .stChatMessage:hover {
        transform: translateX(8px);
        box-shadow: 0 12px 48px rgba(186, 104, 200, 0.18) !important;
    }
    
    .stChatMessage[data-testid="user-message"] {
        background: linear-gradient(135deg, rgba(79, 195, 247, 0.15) 0%, rgba(129, 212, 250, 0.1) 100%) !important;
        border-left: 4px solid #4FC3F7 !important;
    }
    
    .stChatMessage[data-testid="assistant-message"] {
        background: linear-gradient(135deg, rgba(186, 104, 200, 0.12) 0%, rgba(225, 190, 231, 0.08) 100%) !important;
        border-left: 4px solid #BA68C8 !important;
    }
    
    .stChatMessage p {
        color: rgba(33, 33, 33, 0.95) !important;
        line-height: 1.8 !important;
        font-size: 1.05rem !important;
    }
    
    .empty-state {
        text-align: center;
        padding: 5rem 2rem;
    }
    
    .empty-state-icon {
        font-size: 5rem;
        margin-bottom: 1.5rem;
        animation: gentleBounce 2s ease-in-out infinite;
        filter: drop-shadow(0 4px 12px rgba(79, 195, 247, 0.3));
    }
    
    @keyframes gentleBounce {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
    
    .empty-state-text {
        font-size: 1.4rem;
        font-weight: 500;
        color: rgba(66, 66, 66, 0.75);
    }
    
    .audio-premium {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.7) 100%);
        backdrop-filter: blur(25px);
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(186, 104, 200, 0.12);
        position: relative;
        overflow: hidden;
    }
    
    .audio-premium::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(79, 195, 247, 0.08) 0%, transparent 70%);
        animation: gentlePulse 5s ease-in-out infinite;
    }
    
    @keyframes gentlePulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.05); opacity: 0.8; }
    }
    
    .audio-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        color: rgba(66, 66, 66, 0.9);
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1.2rem;
        position: relative;
        z-index: 1;
    }
    
    .audio-icon {
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, #4FC3F7, #BA68C8);
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        box-shadow: 0 6px 20px rgba(79, 195, 247, 0.3);
    }
    
    .stChatInputContainer {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.85) 100%) !important;
        backdrop-filter: blur(25px) !important;
        border: 2px solid rgba(255, 255, 255, 0.7) !important;
        border-radius: 20px !important;
        padding: 0.8rem !important;
        box-shadow: 0 8px 32px rgba(79, 195, 247, 0.15) !important;
    }
    
    .stChatInputContainer textarea {
        background: transparent !important;
        color: rgba(33, 33, 33, 0.95) !important;
        border: none !important;
        font-size: 1.05rem !important;
    }
    
    .stChatInputContainer textarea::placeholder {
        color: rgba(66, 66, 66, 0.5) !important;
    }
    
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(224, 247, 250, 0.95) 0%, rgba(243, 229, 245, 0.95) 100%) !important;
        backdrop-filter: blur(30px) !important;
        border-right: 2px solid rgba(255, 255, 255, 0.5) !important;
    }
    
    section[data-testid="stSidebar"] > div {
        background: transparent !important;
    }
    
    .sidebar-title {
        background: linear-gradient(135deg, #4FC3F7, #BA68C8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid rgba(186, 104, 200, 0.2);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #4FC3F7 0%, #BA68C8 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 0.9rem 1.8rem !important;
        font-weight: 600 !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 6px 20px rgba(79, 195, 247, 0.3) !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 10px 35px rgba(186, 104, 200, 0.4) !important;
    }
    
    .stMetric {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.8) 0%, rgba(255, 255, 255, 0.5) 100%) !important;
        backdrop-filter: blur(15px) !important;
        padding: 1.2rem !important;
        border-radius: 15px !important;
        border: 2px solid rgba(255, 255, 255, 0.6) !important;
        box-shadow: 0 6px 20px rgba(79, 195, 247, 0.1) !important;
    }
    
    .stMetric label {
        color: rgba(66, 66, 66, 0.7) !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        background: linear-gradient(135deg, #4FC3F7, #BA68C8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.9rem !important;
        font-weight: 800 !important;
    }
    
    .typing-indicator {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 1.2rem;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.7) 100%);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        margin: 1.2rem 0;
        border: 2px solid rgba(186, 104, 200, 0.2);
    }
    
    .typing-dot {
        width: 10px;
        height: 10px;
        background: linear-gradient(135deg, #4FC3F7, #BA68C8);
        border-radius: 50%;
        animation: typingBounce 1.4s infinite ease-in-out;
        box-shadow: 0 2px 8px rgba(79, 195, 247, 0.4);
    }
    
    .typing-dot:nth-child(2) { animation-delay: -0.32s; }
    .typing-dot:nth-child(3) { animation-delay: -0.16s; }
    
    @keyframes typingBounce {
        0%, 80%, 100% { transform: scale(0.8); opacity: 0.5; }
        40% { transform: scale(1.2); opacity: 1; }
    }
    
    .message-time {
        font-size: 0.75rem;
        color: rgba(66, 66, 66, 0.5);
        margin-top: 0.6rem;
        text-align: right;
        font-weight: 500;
    }
    
    .stCheckbox {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.7) 0%, rgba(255, 255, 255, 0.5) 100%);
        backdrop-filter: blur(15px);
        padding: 0.9rem;
        border-radius: 12px;
        border: 2px solid rgba(255, 255, 255, 0.5);
    }
    
    .stCheckbox label {
        color: rgba(66, 66, 66, 0.9) !important;
        font-weight: 500 !important;
    }
    
    .settings-panel {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.7) 0%, rgba(255, 255, 255, 0.5) 100%);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 18px;
        padding: 1.8rem;
        margin: 1.2rem 0;
    }
    
    .settings-title {
        background: linear-gradient(135deg, #4FC3F7, #BA68C8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 1.2rem;
    }
    
    .convo-preview {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.8) 0%, rgba(255, 255, 255, 0.6) 100%);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.5);
        border-radius: 15px;
        padding: 1.2rem;
        margin: 0.7rem 0;
        transition: all 0.4s ease;
    }
    
    .convo-preview:hover {
        transform: translateX(6px);
        border-color: rgba(186, 104, 200, 0.4);
    }
    
    .convo-title {
        color: rgba(66, 66, 66, 0.9);
        font-weight: 600;
    }
    
    .convo-meta {
        color: rgba(66, 66, 66, 0.6);
        font-size: 0.8rem;
        margin-top: 0.3rem;
    }
    
    section[data-testid="stSidebar"] h3 {
        background: linear-gradient(135deg, #4FC3F7, #BA68C8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700 !important;
    }
    
    section[data-testid="stSidebar"] hr {
        border-color: rgba(186, 104, 200, 0.2) !important;
        margin: 1.5rem 0 !important;
    }
    
    .stAlert {
        background: linear-gradient(135deg, rgba(79, 195, 247, 0.15) 0%, rgba(186, 104, 200, 0.1) 100%) !important;
        border: 2px solid rgba(79, 195, 247, 0.3) !important;
        border-radius: 15px !important;
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .stChatMessage {
        animation: slideInUp 0.5s ease;
    }
</style>
""", unsafe_allow_html=True)

# Calculate stats
total_messages = len(st.session_state.messages)
user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
ai_messages = total_messages - user_messages
session_duration = (datetime.now() - st.session_state.session_start).seconds // 60

# Update wellness score
if total_messages > 0:
    st.session_state.wellness_score = min(100, (total_messages * 8) + (session_duration * 3))

# Header
st.markdown(f"""
<div class="premium-header">
    <h1 class="header-title">🌸 Wellness Hub 🦋</h1>
    <p class="header-subtitle">Your peaceful space for mental wellness and mindful conversations</p>
    <div class="header-stats">
        <div class="stat-card">
            <div class="stat-value">{total_messages}</div>
            <div class="stat-label">Messages Shared</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{session_duration}m</div>
            <div class="stat-label">Peaceful Time</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{"🟢 Connected" if total_messages > 0 else "🌟 Ready"}</div>
            <div class="stat-label">Status</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-title">🌺 Wellness Tools</div>', unsafe_allow_html=True)
    
    # Session Stats
    st.markdown("### 📊 Session Insights")
    st.metric("Wellness Score", f"{st.session_state.wellness_score}%", 
              delta="Keep going!" if st.session_state.wellness_score < 100 else "Amazing!")
    st.metric("Your Messages", user_messages)
    st.metric("Guide Responses", ai_messages)
    
    st.markdown("---")
    
    # Settings
    st.markdown("### ⚙️ Preferences")
    st.session_state.show_timestamps = st.checkbox("Show timestamps", value=True)
    
    st.markdown("---")
    
    # Export conversation
    st.markdown("### 💾 Save Your Journey")
    if st.button("📥 Export Conversation"):
        export_text = export_conversation()
        st.download_button(
            label="⬇️ Download",
            data=export_text,
            file_name=f"wellness_hub_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
            mime="text/plain"
        )
    
    # Clear chat
    if st.button("🔄 Start Fresh"):
        st.session_state.messages = []
        st.session_state.session_start = datetime.now()
        st.session_state.wellness_score = 0
        st.rerun()
    
    st.markdown("---")
    
    # Quick Tips
    st.markdown("### 💡 Wellness Tips")
    tips = [
        "Take deep breaths",
        "Practice gratitude",
        "Stay hydrated",
        "Move your body",
        "Connect with nature"
    ]
    tip_index = (total_messages % len(tips))
    st.info(f"✨ {tips[tip_index]}")

# Main chat area
col_left, col_main, col_right = st.columns([0.3, 8.4, 0.3])

with col_main:
    # Chat messages
    if st.session_state.messages:
        st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"], avatar="💭" if msg["role"] == "user" else "🌺"):
                st.write(msg["content"])
                if st.session_state.show_timestamps and "timestamp" in msg:
                    st.markdown(f'<div class="message-time">{msg["timestamp"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="chat-wrapper">
            <div class="empty-state">
                <div class="empty-state-icon">🌸 ✨ 🦋</div>
                <div class="empty-state-text">Welcome to your peaceful space</div>
                <p style="margin-top: 1rem; font-size: 1rem; color: rgba(66, 66, 66, 0.6);">
                    Share your thoughts, feelings, or simply say hello.<br>
                    I'm here to listen and support you on your wellness journey.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Audio Input
    st.markdown("""
    <div class="audio-premium">
        <div class="audio-header">
            <div class="audio-icon">🎙️</div>
            <span>Voice your thoughts</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    audio = st.audio_input("Speak from your heart", label_visibility="collapsed")
    
    if audio:
        with st.spinner("🎧 Listening to your voice..."):
            text = logic.speech_to_text(audio)
        
        if text:
            timestamp = get_timestamp()
            
            # Add user message
            st.session_state.messages.append({
                "role": "user",
                "content": text,
                "timestamp": timestamp
            })
            
            with st.chat_message("user", avatar="💭"):
                st.write(text)
                if st.session_state.show_timestamps:
                    st.markdown(f'<div class="message-time">{timestamp}</div>', unsafe_allow_html=True)
            
            # Show typing indicator
            typing_placeholder = st.empty()
            with typing_placeholder:
                st.markdown("""
                <div class="typing-indicator">
                    <span style="color: rgba(66, 66, 66, 0.8); font-weight: 500;">Reflecting on your words</span>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
                """, unsafe_allow_html=True)
            
            time.sleep(1.2)
            typing_placeholder.empty()
            
            # Get AI response
            reply = logic.get_ai_response(text, st.session_state.messages)
            reply_timestamp = get_timestamp()
            
            # Add assistant message
            st.session_state.messages.append({
                "role": "assistant",
                "content": reply,
                "timestamp": reply_timestamp
            })
            
            with st.chat_message("assistant", avatar="🌺"):
                st.write(reply)
                if st.session_state.show_timestamps:
                    st.markdown(f'<div class="message-time">{reply_timestamp}</div>', unsafe_allow_html=True)
            
            st.rerun()
    
    # Text Chat Input
    if prompt := st.chat_input("Type your thoughts here... 💭"):
        timestamp = get_timestamp()
        
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "timestamp": timestamp
        })
        
        with st.chat_message("user", avatar="💭"):
            st.write(prompt)
            if st.session_state.show_timestamps:
                st.markdown(f'<div class="message-time">{timestamp}</div>', unsafe_allow_html=True)
        
        # Show typing indicator
        typing_placeholder = st.empty()
        with typing_placeholder:
            st.markdown("""
            <div class="typing-indicator">
                <span style="color: rgba(66, 66, 66, 0.8); font-weight: 500;">Reflecting on your words</span>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
            """, unsafe_allow_html=True)
        
        time.sleep(1.2)
        typing_placeholder.empty()
        
        # Get AI response
        reply = logic.get_ai_response(prompt, st.session_state.messages)
        reply_timestamp = get_timestamp()
        
        # Add assistant message
        st.session_state.messages.append({
            "role": "assistant",
            "content": reply,
            "timestamp": reply_timestamp
        })
        
        with st.chat_message("assistant", avatar="🌺"):
            st.write(reply)
            if st.session_state.show_timestamps:
                st.markdown(f'<div class="message-time">{reply_timestamp}</div>', unsafe_allow_html=True)
        
        st.rerun()