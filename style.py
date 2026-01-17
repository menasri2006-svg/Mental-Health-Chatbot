import streamlit as st

def apply_styles():
    st.markdown(
        """
        <style>

        /* GLOBAL APP */
        .stApp {
            background: linear-gradient(135deg, #fdfcf0, #eef5ee);
            color: #3e4a3e;
            animation: fadeIn 0.6s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* SIDEBAR */
        [data-testid="stSidebar"] {
            background: rgba(255,255,255,0.5) !important;
            backdrop-filter: blur(16px);
            border-right: 1px solid rgba(0,0,0,0.05);
        }

        /* CHAT BUBBLES */
        .stChatMessage {
            background: rgba(255,255,255,0.7) !important;
            border-radius: 26px !important;
            padding: 14px 18px !important;
            box-shadow: 0 6px 20px rgba(0,0,0,0.05);
            animation: slideUp 0.35s ease;
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* BUTTONS */
        .stButton > button {
            background: linear-gradient(135deg, #769c76, #5f8f5f);
            color: white;
            border-radius: 28px;
            padding: 10px 26px;
            border: none;
            box-shadow: 0 6px 18px rgba(118,156,118,0.4);
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            transform: scale(1.06);
            box-shadow: 0 12px 28px rgba(118,156,118,0.6);
        }

        /* INPUTS */
        input, textarea {
            border-radius: 20px !important;
            border: 1px solid #cfd8cf !important;
            padding: 10px 14px !important;
        }

        input:focus, textarea:focus {
            border: 1px solid #769c76 !important;
            box-shadow: 0 0 0 3px rgba(118,156,118,0.15);
        }

        /* METRICS */
        [data-testid="stMetric"] {
            background: rgba(255,255,255,0.6);
            border-radius: 20px;
            padding: 16px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.04);
        }

        /* BREATHING ANIMATION */
        .breathe-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 420px;
            background: rgba(255,255,255,0.35);
            border-radius: 40px;
            box-shadow: inset 0 0 40px rgba(118,156,118,0.15);
        }

        .circle {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background: radial-gradient(circle, #a8c6a8, #769c76);
            animation: breathe 9s infinite ease-in-out;
            box-shadow: 0 0 40px rgba(118,156,118,0.45);
        }

        @keyframes breathe {
            0%,100% { transform: scale(1); opacity: 0.7; }
            50% { transform: scale(2.4); opacity: 1; }
        }

        /* EMERGENCY ALERT */
        .stAlert {
            border-radius: 22px;
            animation: pulse 1.6s infinite;
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255,0,0,0.25); }
            70% { box-shadow: 0 0 0 14px rgba(255,0,0,0); }
            100% { box-shadow: 0 0 0 0 rgba(255,0,0,0); }
        }

        </style>
        """,
        unsafe_allow_html=True
    )
