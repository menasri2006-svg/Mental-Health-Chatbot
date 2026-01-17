import streamlit as st
import time
import random
from datetime import datetime

# ================================
# PAGE CONFIGURATION
# ================================
st.set_page_config(
    page_title="Immersive Wellness Journey",
    page_icon="🌺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================================
# SESSION STATE INITIALIZATION
# ================================
def initialize_session_state():
    """Initialize all session state variables"""
    defaults = {
        'stage': 'welcome',
        'game_selection': None,
        'book_selection': None,
        'game_score': 0,
        'bubbles': [],
        'simon_sequence': [],
        'user_sequence': [],
        'simon_level': 1,
        'achievements': [],
        'bubble_colors': ['🔴', '🔵', '🟢', '🟡', '🟣', '🟠'],
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_state()

# ================================
# ENHANCED PEACEFUL CSS STYLING
# ================================
def apply_peaceful_css():
    """Apply calming, soft CSS styling with enhanced visuals"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap');
        
        * {
            font-family: 'Quicksand', sans-serif;
        }
        
        .main {
            background: linear-gradient(135deg, #fef9f3 0%, #fef3e2 25%, #fce7cc 50%, #fad7b8 75%, #f8c9a5 100%);
            animation: gradientShift 15s ease infinite;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .welcome-hero {
            background: linear-gradient(135deg, rgba(255, 237, 213, 0.9), rgba(255, 224, 178, 0.9)),
                        url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600');
            background-size: cover;
            background-position: center;
            padding: 120px 50px;
            border-radius: 40px;
            text-align: center;
            box-shadow: 0 25px 70px rgba(244, 114, 182, 0.2);
            margin-bottom: 60px;
            border: 3px solid rgba(255, 255, 255, 0.5);
            position: relative;
            overflow: hidden;
        }
        
        .welcome-hero::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: shimmer 6s ease-in-out infinite;
        }
        
        @keyframes shimmer {
            0%, 100% { transform: translate(0, 0); }
            50% { transform: translate(10%, 10%); }
        }
        
        .welcome-hero h1 {
            font-size: 72px;
            font-weight: 700;
            color: #be185d;
            margin-bottom: 30px;
            text-shadow: 0 4px 15px rgba(255, 255, 255, 0.9);
            position: relative;
            z-index: 1;
        }
        
        .welcome-hero p {
            font-size: 26px;
            color: #831843;
            max-width: 900px;
            margin: 0 auto;
            line-height: 2;
            font-weight: 500;
            position: relative;
            z-index: 1;
        }
        
        .game-card, .book-card, .motivation-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(254, 242, 242, 0.95));
            border-radius: 32px;
            padding: 45px;
            box-shadow: 0 15px 45px rgba(251, 113, 133, 0.15);
            transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            height: 100%;
            border: 3px solid rgba(252, 165, 165, 0.25);
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        
        .game-card::before, .book-card::before, .motivation-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, transparent 0%, rgba(251, 207, 232, 0.1) 100%);
            opacity: 0;
            transition: opacity 0.5s ease;
        }
        
        .game-card:hover::before, .book-card:hover::before, .motivation-card:hover::before {
            opacity: 1;
        }
        
        .game-card:hover, .book-card:hover, .motivation-card:hover {
            transform: translateY(-12px) scale(1.03);
            box-shadow: 0 30px 70px rgba(251, 113, 133, 0.3);
            border-color: rgba(244, 114, 182, 0.6);
        }
        
        .card-icon {
            font-size: 90px;
            text-align: center;
            margin-bottom: 30px;
            animation: float 4s ease-in-out infinite;
            filter: drop-shadow(0 5px 15px rgba(251, 113, 133, 0.3));
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(5deg); }
        }
        
        .card-title {
            font-size: 32px;
            font-weight: 700;
            color: #9f1239;
            text-align: center;
            margin-bottom: 25px;
        }
        
        .card-description {
            font-size: 18px;
            color: #52525b;
            text-align: center;
            line-height: 1.9;
            margin-bottom: 30px;
            font-weight: 500;
        }
        
        .section-title {
            font-size: 48px;
            font-weight: 700;
            color: #881337;
            text-align: center;
            margin: 70px 0 50px 0;
            padding-bottom: 25px;
            border-bottom: 5px solid #fda4af;
            position: relative;
        }
        
        .section-title::after {
            content: '✨';
            position: absolute;
            right: 20px;
            top: -10px;
            font-size: 40px;
            animation: sparkle 2s ease-in-out infinite;
        }
        
        @keyframes sparkle {
            0%, 100% { transform: scale(1) rotate(0deg); opacity: 1; }
            50% { transform: scale(1.2) rotate(180deg); opacity: 0.7; }
        }
        
        .stButton>button {
            background: linear-gradient(135deg, #fb7185 0%, #f43f5e 50%, #e11d48 100%);
            color: white;
            border: none;
            padding: 20px 50px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 19px;
            box-shadow: 0 12px 35px rgba(244, 63, 94, 0.4);
            transition: all 0.4s ease;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }
        
        .stButton>button:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 18px 50px rgba(244, 63, 94, 0.5);
            background: linear-gradient(135deg, #f43f5e 0%, #e11d48 50%, #be123c 100%);
        }
        
        .bubble {
            display: inline-block;
            padding: 30px;
            margin: 12px;
            font-size: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(254, 242, 242, 0.95));
            box-shadow: 0 12px 35px rgba(251, 113, 133, 0.25);
            animation: float 3.5s ease-in-out infinite;
            border: 3px solid rgba(252, 165, 165, 0.4);
        }
        
        .score-display {
            font-size: 80px;
            font-weight: 800;
            background: linear-gradient(135deg, #fb7185, #f43f5e, #e11d48);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 40px 0;
            text-shadow: 0 5px 20px rgba(244, 63, 94, 0.3);
        }
        
        .achievement-badge {
            display: inline-block;
            padding: 18px 35px;
            background: linear-gradient(135deg, #fcd34d, #fbbf24, #f59e0b);
            color: #78350f;
            border-radius: 25px;
            font-weight: 700;
            margin: 12px;
            box-shadow: 0 10px 30px rgba(251, 191, 36, 0.4);
            font-size: 18px;
            border: 3px solid rgba(255, 255, 255, 0.5);
        }
        
        .book-excerpt {
            background: linear-gradient(135deg, #fef3c7, #fde68a, #fcd34d);
            border-radius: 28px;
            padding: 45px;
            box-shadow: 0 15px 45px rgba(251, 191, 36, 0.25);
            border-left: 8px solid #f59e0b;
            margin: 35px 0;
            font-family: 'Georgia', serif;
            font-size: 19px;
            line-height: 2;
            color: #451a03;
        }
        
        .motivation-visual {
            background: linear-gradient(135deg, #fce7f3, #fbcfe8, #f9a8d4);
            border-radius: 28px;
            padding: 40px;
            margin: 30px 0;
            box-shadow: 0 15px 45px rgba(236, 72, 153, 0.2);
            border: 3px solid rgba(244, 114, 182, 0.4);
        }
        
        .motivation-quote {
            font-size: 24px;
            font-style: italic;
            color: #831843;
            text-align: center;
            line-height: 2;
            margin: 25px 0;
            font-weight: 500;
        }
        
        .peaceful-footer {
            text-align: center;
            padding: 70px;
            background: linear-gradient(135deg, rgba(254, 226, 226, 0.8), rgba(254, 202, 202, 0.8));
            border-radius: 40px;
            margin-top: 80px;
            color: #9f1239;
            font-size: 24px;
            font-weight: 600;
            box-shadow: 0 10px 40px rgba(251, 113, 133, 0.2);
        }
        
        .stInfo {
            background: linear-gradient(135deg, #dbeafe, #bfdbfe);
            border-left: 5px solid #3b82f6;
            border-radius: 15px;
            padding: 20px;
            color: #1e40af;
            font-size: 17px;
        }
        
        .stSuccess {
            background: linear-gradient(135deg, #d1fae5, #a7f3d0);
            border-left: 5px solid #10b981;
            border-radius: 15px;
            padding: 20px;
            color: #065f46;
            font-size: 17px;
        }
        
        .stError {
            background: linear-gradient(135deg, #fee2e2, #fecaca);
            border-left: 5px solid #ef4444;
            border-radius: 15px;
            padding: 20px;
            color: #991b1b;
            font-size: 17px;
        }
        
        ::-webkit-scrollbar {
            width: 14px;
        }
        
        ::-webkit-scrollbar-track {
            background: linear-gradient(135deg, #fef2f2, #fee2e2);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #fb7185, #f43f5e);
            border-radius: 10px;
            border: 2px solid #fef2f2;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #f43f5e, #e11d48);
        }
        
        /* Soft glowing effect for cards */
        @keyframes softGlow {
            0%, 100% { box-shadow: 0 0 20px rgba(251, 113, 133, 0.3); }
            50% { box-shadow: 0 0 40px rgba(251, 113, 133, 0.5); }
        }
    </style>
    """, unsafe_allow_html=True)

apply_peaceful_css()

# ================================
# WELCOME STAGE
# ================================
def render_welcome():
    st.markdown("""
    <div class='welcome-hero'>
        <h1>🌺 Immersive Wellness Journey</h1>
        <p>Welcome to your sanctuary of peace and tranquility. Here you'll find interactive games to release stress, 
        inspiring books to nourish your soul, and motivational wisdom to uplift your spirit. Take a deep breath and begin your journey to inner calm.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Begin Your Journey", use_container_width=True, key="begin"):
            st.session_state.stage = 'main_menu'
            st.rerun()

# ================================
# MAIN MENU
# ================================
def render_main_menu():
    st.markdown("<div class='section-title'>🌸 Choose Your Wellness Path</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='game-card'>
            <div class='card-icon'>🎮</div>
            <div class='card-title'>Relaxation Games</div>
            <div class='card-description'>
                Play mindful games designed to release stress, bring joy, and restore inner balance through gentle interaction.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🎯 Play Games", use_container_width=True, key="play_games"):
            st.session_state.stage = 'games_menu'
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class='book-card'>
            <div class='card-icon'>📚</div>
            <div class='card-title'>Wisdom Library</div>
            <div class='card-description'>
                Explore peaceful readings, life-changing insights, and timeless wisdom from mindfulness masters.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📖 Browse Books", use_container_width=True, key="browse_books"):
            st.session_state.stage = 'books_menu'
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class='motivation-card'>
            <div class='card-icon'>💪</div>
            <div class='card-title'>Daily Inspiration</div>
            <div class='card-description'>
                Discover motivational quotes, uplifting messages, and gentle reminders to nurture your well-being.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("✨ Get Inspired", use_container_width=True, key="get_inspired"):
            st.session_state.stage = 'motivation'
            st.rerun()
    
    # Peaceful footer
    st.markdown("""
    <div class='peaceful-footer'>
        🌿 Take a moment to breathe. You are exactly where you need to be. 🌿
    </div>
    """, unsafe_allow_html=True)

# ================================
# GAMES MENU
# ================================
def render_games_menu():
    st.markdown("<div class='section-title'>🎮 Relaxation Games</div>", unsafe_allow_html=True)
    
    st.markdown(f"<div class='score-display'>Score: {st.session_state.game_score}</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='game-card'>
            <div class='card-icon'>🎯</div>
            <div class='card-title'>Bubble Pop Therapy</div>
            <div class='card-description'>
                Pop colorful bubbles to release tension and clear your mind. 
                Each bubble represents a worry floating away into the peaceful sky.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🫧 Play Bubble Pop", use_container_width=True, key="play_bubble"):
            st.session_state.stage = 'bubble_game'
            st.session_state.bubbles = [
                {'id': i, 'emoji': random.choice(st.session_state.bubble_colors), 'points': random.choice([10, 15, 20])}
                for i in range(15)
            ]
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class='game-card'>
            <div class='card-icon'>🧠</div>
            <div class='card-title'>Memory Challenge</div>
            <div class='card-description'>
                Train your focus and memory with this calming pattern game. 
                Watch the colors, remember the sequence, and find your peaceful flow state.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🎨 Play Memory Game", use_container_width=True, key="play_memory"):
            st.session_state.stage = 'simon_game'
            st.session_state.simon_sequence = [random.randint(0, 3)]
            st.session_state.user_sequence = []
            st.session_state.simon_level = 1
            st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.session_state.achievements:
        st.markdown("<h3 style='text-align: center; color: #881337; font-size: 36px; margin: 40px 0;'>🏆 Your Achievements</h3>", unsafe_allow_html=True)
        ach_html = "<div style='text-align: center;'>"
        for ach in st.session_state.achievements:
            ach_html += f"<span class='achievement-badge'>{ach}</span>"
        ach_html += "</div>"
        st.markdown(ach_html, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("⬅️ Back to Menu", use_container_width=True):
            st.session_state.stage = 'main_menu'
            st.rerun()

# ================================
# BUBBLE POP GAME
# ================================
def render_bubble_game():
    st.markdown("<h1 style='text-align: center; color: #881337; font-size: 54px;'>🎯 Bubble Pop Therapy</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='score-display'>{st.session_state.game_score}</div>", unsafe_allow_html=True)
    
    st.info("💭 Each bubble you pop represents releasing a worry. Take your time, breathe deeply, and enjoy this peaceful moment.")
    
    if st.session_state.bubbles:
        cols = st.columns(5)
        for idx, bubble in enumerate(st.session_state.bubbles):
            with cols[idx % 5]:
                st.markdown(f"<div style='text-align: center;'><div class='bubble'>{bubble['emoji']}</div></div>",
                           unsafe_allow_html=True)
                
                if st.button("Pop", key=f"bubble_{bubble['id']}", use_container_width=True):
                    st.session_state.game_score += bubble['points']
                    st.session_state.bubbles.remove(bubble)
                    
                    if len(st.session_state.bubbles) < 5:
                        new_bubbles = [
                            {'id': random.randint(1000, 9999), 
                             'emoji': random.choice(st.session_state.bubble_colors),
                             'points': random.choice([10, 15, 20])}
                            for i in range(10)
                        ]
                        st.session_state.bubbles.extend(new_bubbles)
                    
                    if st.session_state.game_score >= 100 and '🎯 Bubble Master' not in st.session_state.achievements:
                        st.session_state.achievements.append('🎯 Bubble Master')
                        st.balloons()
                    
                    st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back to Games", use_container_width=True):
            st.session_state.stage = 'games_menu'
            st.rerun()
    with col2:
        if st.button("🔄 New Bubbles", use_container_width=True):
            st.session_state.bubbles = [
                {'id': random.randint(1000, 9999), 
                 'emoji': random.choice(st.session_state.bubble_colors), 
                 'points': random.choice([10, 15, 20])}
                for i in range(15)
            ]
            st.rerun()

# ================================
# MEMORY GAME
# ================================
def render_simon_game():
    st.markdown("<h1 style='text-align: center; color: #881337; font-size: 54px;'>🧠 Memory Challenge</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='score-display'>Level {st.session_state.simon_level}</div>", unsafe_allow_html=True)
    
    st.info("👀 Watch the sequence carefully, then repeat it. Train your mind to be present, focused, and calm.")
    
    colors = [
        {'name': 'Rose', 'bg': '#fb7185'},
        {'name': 'Sky', 'bg': '#7dd3fc'},
        {'name': 'Mint', 'bg': '#6ee7b7'},
        {'name': 'Sun', 'bg': '#fcd34d'}
    ]
    
    cols = st.columns(2)
    
    for idx, color in enumerate(colors):
        target_col = cols[0] if idx < 2 else cols[1]
        with target_col:
            st.markdown(
                f"""<div style='background: {color['bg']}; height: 200px; border-radius: 28px; 
                margin: 18px; display: flex; align-items: center; justify-content: center; 
                font-size: 2.8em; color: white; font-weight: bold; box-shadow: 0 12px 35px rgba(0,0,0,0.2);
                border: 3px solid rgba(255,255,255,0.5);'>
                {color['name']}</div>""",
                unsafe_allow_html=True)
            
            if st.button(f"Press {color['name']}", key=f"simon_{idx}", use_container_width=True):
                st.session_state.user_sequence.append(idx)
                
                current_idx = len(st.session_state.user_sequence) - 1
                if st.session_state.user_sequence[current_idx] != st.session_state.simon_sequence[current_idx]:
                    st.error("💭 That's okay! Every mistake is a chance to learn. Let's start fresh and try again.")
                    time.sleep(1.5)
                    st.session_state.simon_sequence = [random.randint(0, 3)]
                    st.session_state.user_sequence = []
                    st.session_state.simon_level = 1
                    st.rerun()
                
                if len(st.session_state.user_sequence) == len(st.session_state.simon_sequence):
                    st.session_state.game_score += 25
                    st.session_state.simon_level += 1
                    st.success("✨ Perfect! You're in the flow. Moving to the next level!")
                    time.sleep(1)
                    
                    st.session_state.simon_sequence.append(random.randint(0, 3))
                    st.session_state.user_sequence = []
                    
                    if st.session_state.simon_level >= 5 and '🧠 Focus Master' not in st.session_state.achievements:
                        st.session_state.achievements.append('🧠 Focus Master')
                        st.balloons()
                    
                    st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back to Games", use_container_width=True):
            st.session_state.stage = 'games_menu'
            st.rerun()
    with col2:
        if st.button("🔄 Restart", use_container_width=True):
            st.session_state.simon_sequence = [random.randint(0, 3)]
            st.session_state.user_sequence = []
            st.session_state.simon_level = 1
            st.rerun()

# ================================
# BOOKS MENU
# ================================
def render_books_menu():
    st.markdown("<div class='section-title'>📚 Wisdom Library</div>", unsafe_allow_html=True)
    
    books = [
        {
            "title": "The Power of Now",
            "author": "Eckhart Tolle",
            "icon": "📘",
            "excerpt": "The moment you realize you are not present, you are present. Whenever you are able to observe your mind, you are no longer trapped in it. Be present as the watcher of your mind — of your thoughts and emotions as well as your reactions in various situations.",
            "link": "https://www.amazon.com/Power-Now-Guide-Spiritual-Enlightenment/dp/1577314808",
            "description": "A transformative guide to spiritual enlightenment and living fully in the present moment"
        },
        {
            "title": "Peace Is Every Step",
            "author": "Thich Nhat Hanh",
            "icon": "📗",
            "excerpt": "The mind can go in a thousand directions, but on this beautiful path, I walk in peace. With each step, the wind blows. With each step, a flower blooms. Walk as if you are kissing the Earth with your feet.",
            "link": "https://www.amazon.com/Peace-Every-Step-Mindfulness-Everyday/dp/0553351397",
            "description": "Mindfulness practices for transforming everyday activities into moments of peace"
        },
        {
            "title": "The Untethered Soul",
            "author": "Michael Singer",
            "icon": "📙",
            "excerpt": "You are not the voice of the mind — you are the one who hears it. The only permanent solution is to let go of the part that resists reality. See inner experiences as energy passing through you.",
            "link": "https://www.amazon.com/Untethered-Soul-Journey-Beyond-Yourself/dp/1572245379",
            "description": "A profound journey beyond yourself to discover inner peace and lasting freedom"
        },
        {
            "title": "Wherever You Go, There You Are",
            "author": "Jon Kabat-Zinn",
            "icon": "📕",
            "excerpt": "Wherever you go, there you are. Mindfulness means being awake to this moment. Notice the in-breath and the out-breath without changing anything. Simply be present with what is.",
            "link": "https://www.amazon.com/Wherever-You-Go-There-Are/dp/1401307787",
            "description": "Practical meditation guidance for cultivating everyday mindfulness and awareness"
        }
    ]
    
    for idx, book in enumerate(books):
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown(f"""
            <div style='text-align: center; padding: 40px;'>
                <div style='font-size: 130px;'>{book['icon']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='book-card'>
                <h2 style='color: #881337; margin-bottom: 15px; font-size: 32px;'>{book['title']}</h2>
                <p style='color: #a855f7; font-size: 20px; margin-bottom: 20px; font-weight: 600;'>by {book['author']}</p>
                <p style='color: #52525b; font-size: 17px; line-height: 1.8;'>{book['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"📖 Read Excerpt", key=f"book_{idx}", use_container_width=True):
                st.session_state[f'show_book_{idx}'] = not st.session_state.get(f'show_book_{idx}', False)
            
            if st.session_state.get(f'show_book_{idx}', False):
                st.markdown(f"""
                <div class='book-excerpt'>
                    <p style='margin-bottom: 25px;'>{book['excerpt']}</p>
                    <p style='text-align: right; font-size: 18px; color: #92400e; font-weight: 600;'>— {book['author']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button(f"🔗 Get Full Book", key=f"link_{idx}", use_container_width=True):
                        st.markdown(f"[Open on Amazon]({book['link']})")
                with col_b:
                    if st.button(f"❤️ Save to Favorites", key=f"save_{idx}", use_container_width=True):
                        st.success("✨ Saved to your reading list!")
        
        st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("⬅️ Back to Menu", use_container_width=True):
            st.session_state.stage = 'main_menu'
            st.rerun()

# ================================
# MOTIVATION
# ================================
def render_motivation():
    st.markdown("<div class='section-title'>💪 Daily Inspiration</div>", unsafe_allow_html=True)
    
    motivations = [
        {
            "title": "🌟 You Are Enough",
            "quote": "You don't need to be perfect. You don't need to have it all figured out. Right now, in this moment, exactly as you are, you are enough. Your worth is not determined by your productivity or achievements.",
            "visual": "https://images.unsplash.com/photo-1502786129293-79981df4e689?w=800",
            "author": "— Self-Love Wisdom"
        },
        {
            "title": "🌱 Growth Takes Time",
            "quote": "Some days you'll feel strong and capable. Other days you'll struggle to get out of bed. Both are part of the journey. Trust the process. Every step counts, even the backwards ones. Progress is not always linear.",
            "visual": "https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?w=800",
            "author": "— Growth Mindset"
        },
        {
            "title": "💚 Practice Self-Compassion",
            "quote": "Talk to yourself like you would to someone you love deeply. Be gentle with your imperfections. Be patient with your progress. Be kind to your struggling moments. You deserve the same compassion you freely give to others.",
            "visual": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800",
            "author": "— Brené Brown"
        },
        {
            "title": "🦋 This Too Shall Pass",
            "quote": "Whatever you're feeling right now—anxiety, sadness, overwhelm—it's temporary. Emotions are like waves in the ocean. They rise with intensity, they peak, and they inevitably fall. You have weathered storms before, and you will get through this one too.",
            "visual": "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800",
            "author": "— Ancient Wisdom"
        },
        {
            "title": "✨ Small Steps Matter",
            "quote": "Getting out of bed is an achievement. Taking a shower is progress. Asking for help is courage. Eating a meal is self-care. Never underestimate the power of small steps. On difficult days, surviving is thriving.",
            "visual": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=800",
            "author": "— Mental Health Advocacy"
        },
        {
            "title": "🌈 Your Journey is Unique",
            "quote": "Don't compare your chapter 1 to someone else's chapter 20. Everyone's journey unfolds differently. Go at your own pace. Rest when you need to. Celebrate your wins, no matter how small. Your timing is perfect for you.",
            "visual": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800",
            "author": "— Self-Care Reminder"
        }
    ]
    
    for idx, item in enumerate(motivations):
        st.markdown(f"""
        <div class='motivation-visual'>
            <h2 style='color: #881337; text-align: center; margin-bottom: 25px; font-size: 38px;'>{item['title']}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div style='padding: 25px;'>
                <p class='motivation-quote'>{item['quote']}</p>
                <p style='text-align: right; color: #9f1239; font-size: 18px; margin-top: 20px; font-weight: 600;'>{item['author']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.image(item['visual'], use_container_width=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='peaceful-footer'>
        🌸 Remember: You are doing better than you think. Be proud of yourself. 🌸
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("⬅️ Back to Menu", use_container_width=True):
            st.session_state.stage = 'main_menu'
            st.rerun()

# ================================
# MAIN APP FLOW
# ================================
def main():
    if st.session_state.stage == 'welcome':
        render_welcome()
    elif st.session_state.stage == 'main_menu':
        render_main_menu()
    elif st.session_state.stage == 'games_menu':
        render_games_menu()
    elif st.session_state.stage == 'bubble_game':
        render_bubble_game()
    elif st.session_state.stage == 'simon_game':
        render_simon_game()
    elif st.session_state.stage == 'books_menu':
        render_books_menu()
    elif st.session_state.stage == 'motivation':
        render_motivation()

if __name__ == "__main__":
    main()