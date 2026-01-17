import streamlit as st
import time
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mood Relaxation Sanctuary",
    page_icon="🌸",
    layout="wide"
)

# ---------------- ENHANCED PEACEFUL STYLES ----------------
st.markdown("""
<style>
/* GLOBAL BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 25%, #dbeafe 50%, #e5e7eb 75%, #f3f4f6 100%);
    font-family: 'Inter', sans-serif;
}

/* HERO SECTION */
.hero-section {
    background: linear-gradient(135deg, rgba(147, 197, 253, 0.3), rgba(191, 219, 254, 0.2)),
                url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600');
    background-size: cover;
    background-position: center;
    padding: 80px 40px;
    border-radius: 30px;
    color: #1e3a8a;
    margin-bottom: 50px;
    box-shadow: 0 20px 60px rgba(59, 130, 246, 0.15);
    backdrop-filter: blur(10px);
}

.hero-section h1 {
    font-size: 56px;
    font-weight: 700;
    margin-bottom: 20px;
    color: #1e40af;
    text-shadow: 0 2px 10px rgba(255,255,255,0.8);
}

.hero-section p {
    font-size: 22px;
    color: #3b82f6;
    max-width: 800px;
    line-height: 1.8;
}

/* MOOD AFFIRMATION CARD */
.affirmation-card {
    padding: 35px;
    border-radius: 25px;
    background: linear-gradient(135deg, #dbeafe, #bfdbfe);
    font-size: 24px;
    color: #1e40af;
    box-shadow: 0 15px 40px rgba(59, 130, 246, 0.2);
    text-align: center;
    font-weight: 500;
    margin: 40px 0;
    border: 2px solid rgba(147, 197, 253, 0.3);
}

/* CARD STYLES */
.content-card {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(59, 130, 246, 0.1);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    height: 100%;
    border: 1px solid rgba(191, 219, 254, 0.3);
}

.content-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 50px rgba(59, 130, 246, 0.2);
    border-color: rgba(96, 165, 250, 0.5);
    background: rgba(255, 255, 255, 1);
}

.card-icon {
    font-size: 60px;
    text-align: center;
    margin-bottom: 20px;
}

.card-title {
    font-size: 24px;
    font-weight: 700;
    color: #1e40af;
    text-align: center;
    margin-bottom: 15px;
}

.card-description {
    font-size: 16px;
    color: #64748b;
    text-align: center;
    line-height: 1.6;
    margin-bottom: 20px;
}

/* SECTION HEADERS */
.section-header {
    font-size: 38px;
    font-weight: 700;
    color: #1e40af;
    text-align: center;
    margin: 60px 0 40px 0;
    padding-bottom: 20px;
    border-bottom: 3px solid #93c5fd;
}

/* BREATHING GUIDE */
.breathing-container {
    background: linear-gradient(135deg, #e0f2fe, #bae6fd);
    border-radius: 30px;
    padding: 60px;
    text-align: center;
    margin: 30px 0;
    box-shadow: 0 15px 40px rgba(14, 165, 233, 0.15);
}

.breathing-circle {
    width: 200px;
    height: 200px;
    margin: 0 auto 30px;
    border-radius: 50%;
    background: linear-gradient(135deg, #7dd3fc, #38bdf8);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    font-weight: 700;
    color: white;
    box-shadow: 0 10px 40px rgba(14, 165, 233, 0.3);
    animation: breathe 4s ease-in-out infinite;
}

@keyframes breathe {
    0%, 100% { transform: scale(1); opacity: 0.9; }
    50% { transform: scale(1.15); opacity: 1; }
}

/* BOOK CARD */
.book-card {
    background: linear-gradient(135deg, #fef3c7, #fde68a);
    border-radius: 24px;
    padding: 35px;
    box-shadow: 0 12px 35px rgba(251, 191, 36, 0.2);
    border-left: 6px solid #f59e0b;
    margin: 25px 0;
    transition: all 0.3s;
}

.book-card:hover {
    transform: translateX(5px);
    box-shadow: 0 15px 45px rgba(251, 191, 36, 0.3);
}

.book-content {
    background: white;
    padding: 30px;
    border-radius: 16px;
    max-height: 400px;
    overflow-y: auto;
    font-family: 'Georgia', serif;
    line-height: 1.9;
    color: #451a03;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.05);
}

/* MUSIC PLAYER */
.music-card {
    background: linear-gradient(135deg, #e9d5ff, #ddd6fe);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(139, 92, 246, 0.15);
    margin: 20px 0;
}

/* ENHANCED YOGA CARD */
.yoga-pose-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(243, 232, 255, 0.95));
    border-radius: 24px;
    padding: 35px;
    box-shadow: 0 15px 40px rgba(168, 85, 247, 0.2);
    margin: 25px 0;
    border: 2px solid rgba(216, 180, 254, 0.4);
    transition: all 0.3s ease;
}

.yoga-pose-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 50px rgba(168, 85, 247, 0.3);
}

.yoga-video-container {
    background: white;
    border-radius: 16px;
    padding: 20px;
    margin-top: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.pose-info-box {
    background: linear-gradient(135deg, #f3e8ff, #e9d5ff);
    border-radius: 16px;
    padding: 25px;
    margin-top: 20px;
    border-left: 5px solid #a855f7;
}

/* BUTTONS */
.stButton>button {
    background: linear-gradient(135deg, #60a5fa, #3b82f6);
    color: white;
    border: none;
    padding: 16px 40px;
    border-radius: 15px;
    font-weight: 600;
    font-size: 17px;
    box-shadow: 0 8px 24px rgba(59, 130, 246, 0.3);
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 35px rgba(59, 130, 246, 0.4);
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width: 12px;
}

::-webkit-scrollbar-track {
    background: #dbeafe;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: #60a5fa;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #3b82f6;
}

/* FOOTER */
.peaceful-footer {
    text-align: center;
    padding: 50px;
    background: linear-gradient(135deg, rgba(224, 242, 254, 0.6), rgba(186, 230, 253, 0.6));
    border-radius: 30px;
    margin-top: 60px;
    color: #1e40af;
    font-size: 20px;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO HEADER ----------------
st.markdown("""
<div class="hero-section">
    <h1>🌸 Mood Relaxation Sanctuary</h1>
    <p>Welcome to your peaceful space. Take a deep breath, let your shoulders drop, 
    and allow yourself to be present. Here, you can explore calming stories, soothing music, 
    gentle yoga, and mindful breathing exercises designed to restore your inner peace.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- MOOD SELECTION ----------------
col_mood1, col_mood2 = st.columns([3, 1])

with col_mood1:
    mood = st.selectbox(
        "🌈 How are you feeling right now?",
        ["Stressed", "Anxious", "Sad", "Lonely", "Overwhelmed", "Low Energy", "Overthinking", "Restless"],
        key="mood_select"
    )

with col_mood2:
    current_time = datetime.now().strftime("%I:%M %p")
    st.info(f"🕐 {current_time}")

affirmations = {
    "Stressed": "🌊 You are safe. You don't need to solve everything right now. Take it one breath at a time.",
    "Anxious": "🦋 This feeling will pass. Breathe slowly. You are stronger than your worries.",
    "Sad": "🌻 It's okay to feel sad. You are not alone. Your feelings are valid and temporary.",
    "Lonely": "💫 You matter. You are connected to this moment. Reach out when you're ready.",
    "Overwhelmed": "🌿 One small step is enough. You don't have to do it all today.",
    "Low Energy": "🌱 Even small steps are enough today. Rest is productive too.",
    "Overthinking": "☁️ Your thoughts don't control you. Let them drift like clouds passing by.",
    "Restless": "🍃 This restlessness will settle. Ground yourself in this present moment."
}

st.markdown(
    f"<div class='affirmation-card'>{affirmations[mood]}</div>",
    unsafe_allow_html=True
)

# ---------------- BOOKS SECTION ----------------
st.markdown("<div class='section-header'>📚 Peaceful Reading Library</div>", unsafe_allow_html=True)

books = [
    {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "icon": "📖",
        "description": "Learn to live fully in the present moment and find peace beyond thought",
        "link": "https://www.amazon.com/Power-Now-Guide-Spiritual-Enlightenment/dp/1577314808"
    },
    {
        "title": "Peace Is Every Step",
        "author": "Thich Nhat Hanh",
        "icon": "🧘",
        "description": "Discover mindfulness in everyday activities and transform daily life",
        "link": "https://www.amazon.com/Peace-Every-Step-Mindfulness-Everyday/dp/0553351397"
    },
    {
        "title": "The Untethered Soul",
        "author": "Michael Singer",
        "icon": "🦋",
        "description": "Journey beyond yourself to find inner peace and freedom",
        "link": "https://www.amazon.com/Untethered-Soul-Journey-Beyond-Yourself/dp/1572245379"
    },
    {
        "title": "Wherever You Go, There You Are",
        "author": "Jon Kabat-Zinn",
        "icon": "🌏",
        "description": "Practical guidance for meditation and mindful living",
        "link": "https://www.amazon.com/Wherever-You-Go-There-Are/dp/1401307787"
    }
]

cols = st.columns(2)
for idx, book in enumerate(books):
    with cols[idx % 2]:
        st.markdown(f"""
        <div class='content-card'>
            <div class='card-icon'>{book['icon']}</div>
            <div class='card-title'>{book['title']}</div>
            <p style='text-align: center; color: #64748b; font-size: 14px; margin-bottom: 15px;'>by {book['author']}</p>
            <div class='card-description'>{book['description']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"📖 Read Excerpt", key=f"book_{idx}", use_container_width=True):
            st.session_state[f'show_book_{idx}'] = not st.session_state.get(f'show_book_{idx}', False)
        
        if st.session_state.get(f'show_book_{idx}', False):
            excerpts = {
                0: "The moment you realize you are not present, you are present. Whenever you are able to observe your mind, you are no longer trapped in it. Be present as the watcher of your mind.",
                1: "The mind can go in a thousand directions, but on this beautiful path, I walk in peace. Walk as if you are kissing the Earth with your feet.",
                2: "You are not the voice of the mind — you are the one who hears it. The only permanent solution is to let go of the part that resists reality.",
                3: "Wherever you go, there you are. Mindfulness means being awake to this moment. Notice the in-breath and the out-breath."
            }
            st.markdown(f"""
            <div class='book-card'>
                <div class='book-content'>{excerpts[idx]}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"🔗 Get Full Book", key=f"link_{idx}", use_container_width=True):
                st.markdown(f"[Open on Amazon]({book['link']})")

st.write("")

# ---------------- MUSIC SECTION ----------------
st.markdown("<div class='section-header'>🎵 Healing Soundscapes</div>", unsafe_allow_html=True)

music_options = [
    {
        "title": "Peaceful Piano",
        "icon": "🎹",
        "description": "Gentle piano melodies to calm your mind",
        "url": "https://www.youtube.com/watch?v=lTRiuFIWV54"
    },
    {
        "title": "Nature Sounds",
        "icon": "🌊",
        "description": "Rain, ocean waves, and forest ambience",
        "url": "https://www.youtube.com/watch?v=eKFTSSKCzWA"
    },
    {
        "title": "Meditation Music",
        "icon": "🧘‍♀️",
        "description": "Deep relaxation and healing frequencies",
        "url": "https://www.youtube.com/watch?v=1ZYbU82GVz4"
    },
    {
        "title": "Acoustic Guitar",
        "icon": "🎸",
        "description": "Soft acoustic melodies for tranquility",
        "url": "https://www.youtube.com/watch?v=N6IEF2_JGe8"
    }
]

cols = st.columns(2)
for idx, music in enumerate(music_options):
    with cols[idx % 2]:
        st.markdown(f"""
        <div class='content-card'>
            <div class='card-icon'>{music['icon']}</div>
            <div class='card-title'>{music['title']}</div>
            <div class='card-description'>{music['description']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"🎧 Play", key=f"music_{idx}", use_container_width=True):
            st.session_state[f'show_music_{idx}'] = not st.session_state.get(f'show_music_{idx}', False)
        
        if st.session_state.get(f'show_music_{idx}', False):
            st.markdown(f"""
            <div class='music-card'>
                <p style='text-align: center; margin-bottom: 15px; color: #6d28d9; font-weight: 600;'>Now Playing: {music['title']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.video(music['url'])

st.write("")

# ---------------- BREATHING GUIDE ----------------
st.markdown("<div class='section-header'>🌬️ Guided Breathing Practice</div>", unsafe_allow_html=True)

if 'breathing_active' not in st.session_state:
    st.session_state.breathing_active = False

st.markdown("""
<div class='breathing-container'>
    <h3 style='color: #0369a1; margin-bottom: 30px;'>Let's breathe together</h3>
    <div class='breathing-circle'>Breathe</div>
    <p style='font-size: 18px; color: #0c4a6e; margin-top: 20px;'>
        Follow the rhythm: Inhale deeply for 4 seconds, hold for 4 seconds, exhale slowly for 4 seconds
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🌬️ Start Breathing Exercise", use_container_width=True, key="start_breathing"):
        st.session_state.breathing_active = True

if st.session_state.breathing_active:
    placeholder = st.empty()
    
    for cycle in range(3):
        placeholder.info(f"🌬️ **Cycle {cycle + 1}/3** - Breathe IN (4 seconds)")
        time.sleep(4)
        placeholder.warning(f"⏸️ **Cycle {cycle + 1}/3** - HOLD (4 seconds)")
        time.sleep(4)
        placeholder.success(f"💨 **Cycle {cycle + 1}/3** - Breathe OUT (4 seconds)")
        time.sleep(4)
    
    placeholder.success("✨ Wonderful! You've completed the breathing exercise. Notice how you feel.")
    st.balloons()
    st.session_state.breathing_active = False

st.write("")

# ---------------- ENHANCED YOGA SECTION ----------------
st.markdown("<div class='section-header'>🧘‍♀️ Gentle Yoga Flow</div>", unsafe_allow_html=True)

st.info("💜 Follow along with these calming yoga poses. Each video will guide you through the proper technique for maximum relaxation and benefit.")

yoga_poses = [
    {
        "name": "Child's Pose",
        "duration": "2-3 minutes",
        "benefit": "Releases tension in back, shoulders, and chest",
        "instruction": "Kneel on the floor, sit back on your heels, then fold forward with arms extended. Rest your forehead on the mat and breathe deeply.",
        "video_url": "https://youtu.be/2MJGg-dUKh0?si=xeWSeCcNdeLalv55",
        "tips": ["Keep your hips on your heels", "Relax your shoulders", "Breathe into your back"]
    },
    {
        "name": "Cat-Cow Stretch",
        "duration": "1-2 minutes",
        "benefit": "Improves spine flexibility and relieves back pain",
        "instruction": "Start on hands and knees. Inhale, arch your back (cow). Exhale, round your spine (cat). Flow between these positions.",
        "video_url": "https://youtu.be/kqnua4rHVVA?si=PgAwuqZfVL4p4nYM",
        "tips": ["Move slowly with your breath", "Keep shoulders over wrists", "Engage your core"]
    },
    {
        "name": "Stress Relief Yoga",
        "duration": "5-10 minutes",
        "benefit": "Reduces anxiety and promotes deep relaxation",
        "instruction": "Lie on your back near a wall. Extend your legs up the wall, keeping your arms relaxed at your sides. Close your eyes and breathe.",
        "video_url": "https://youtu.be/yqeirBfn2j4?si=Bgl3-vVOWMotWYJi",
        "tips": ["Use a pillow under your hips", "Stay for 5-10 minutes", "Perfect before bedtime"]
    },
    {
        "name": "Finally Hear to This Calm Music ",
        "duration": "5-15 minutes",
        "benefit": "Complete body and mind relaxation",
        "instruction": "Lie flat on your back, arms slightly away from body, palms facing up. Close your eyes. Let your whole body relax completely.",
        "video_url": "https://youtu.be/7O1EJBO_bew?si=I1su0foiHaKazRZU",
        "tips": ["Let your feet fall naturally open", "Scan your body for tension", "Focus on your breath"]
    }
]

for idx, pose in enumerate(yoga_poses):
    st.markdown(f"""
    <div class='yoga-pose-card'>
        <h2 style='color: #7c3aed; margin-bottom: 15px; font-size: 28px;'>
            🧘 {pose['name']}
        </h2>
        <p style='color: #8b5cf6; font-weight: 600; font-size: 18px; margin-bottom: 10px;'>
            ⏱️ Hold for {pose['duration']}
        </p>
        <p style='color: #059669; font-weight: 600; font-size: 17px; margin-bottom: 20px;'>
            ✨ {pose['benefit']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(f"▶️ Watch {pose['name']} Tutorial", key=f"yoga_{idx}", use_container_width=True):
        st.session_state[f'show_yoga_{idx}'] = not st.session_state.get(f'show_yoga_{idx}', False)
    
    if st.session_state.get(f'show_yoga_{idx}', False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div class='yoga-video-container'>
                <p style='text-align: center; color: #7c3aed; font-weight: 600; margin-bottom: 15px; font-size: 18px;'>
                    Follow along with this guided tutorial
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.video(pose['video_url'])
        
        with col2:
            st.markdown(f"""
            <div class='pose-info-box'>
                <h4 style='color: #7c3aed; margin-bottom: 15px;'>📝 Instructions</h4>
                <p style='color: #4b5563; line-height: 1.8; margin-bottom: 20px;'>{pose['instruction']}</p>
                
                <h4 style='color: #059669; margin-bottom: 12px;'>💡 Pro Tips</h4>
                <ul style='color: #4b5563; line-height: 1.8;'>
            """, unsafe_allow_html=True)
            
            for tip in pose['tips']:
                st.markdown(f"<li style='margin-bottom: 8px;'>{tip}</li>", unsafe_allow_html=True)
            
            st.markdown("</ul></div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="peaceful-footer">
    🌸 You took time for yourself today. That's something to be proud of. 💙<br>
    <span style="font-size:17px; margin-top:12px; display:inline-block; color: #64748b;">
        May you find peace in every breath, strength in every moment, and joy in every heartbeat.
    </span>
</div>
""", unsafe_allow_html=True)