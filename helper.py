"""
Helper functions module for Performance Management System
Contains utility functions, theme management, and UI components
"""

import streamlit as st
from datetime import datetime, date
from typing import List, Dict, Optional

# ============================================
# TIME & DATE UTILITIES
# ============================================

def get_quarter_months(quarter: int) -> List[int]:
    """Get list of month numbers for a given quarter"""
    quarter_map = {
        1: [4, 5, 6],
        2: [7, 8, 9],
        3: [10, 11, 12],
        4: [1, 2, 3]
    }
    return quarter_map.get(quarter, [])


def get_month_name(month_num: int) -> str:
    """Get month name from month number"""
    months = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return months[month_num] if 1 <= month_num <= 12 else ""


def get_current_quarter() -> int:
    """Get current quarter based on current month"""
    month = datetime.now().month
    if 4 <= month <= 6:
        return 1
    elif 7 <= month <= 9:
        return 2
    elif 10 <= month <= 12:
        return 3
    else:
        return 4


def get_quarter_name(quarter: int) -> str:
    """Get quarter display name"""
    quarter_names = {
        1: "Q1 (April - June)",
        2: "Q2 (July - September)",
        3: "Q3 (October - December)",
        4: "Q4 (January - March)"
    }
    return quarter_names.get(quarter, f"Q{quarter}")


def get_financial_year(date_obj: date = None) -> int:
    """Get financial year for a given date (April to March)"""
    if date_obj is None:
        date_obj = date.today()
    
    year = date_obj.year
    month = date_obj.month
    
    if month < 4:
        return year - 1
    return year


# ============================================
# CALCULATION UTILITIES
# ============================================

def calculate_progress(achieved: float, target: float) -> float:
    """Calculate progress percentage"""
    if target <= 0:
        return 0.0
    progress = (achieved / target) * 100
    return min(progress, 100.0)


def calculate_total_achievement(week1: float, week2: float, week3: float, week4: float) -> float:
    """Calculate total monthly achievement from weekly achievements"""
    return week1 + week2 + week3 + week4


def get_status_color(progress: float) -> str:
    """Get color based on progress percentage"""
    if progress >= 90:
        return "#10b981"
    elif progress >= 70:
        return "#3b82f6"
    elif progress >= 50:
        return "#f59e0b"
    else:
        return "#ef4444"


def format_number(value: float, decimals: int = 2) -> str:
    """Format number with specified decimal places"""
    return f"{value:.{decimals}f}"


# ============================================
# MODERN PROFESSIONAL THEME
# ============================================
def apply_theme():
    """Apply modern, clean, professional dashboard theme"""
    st.markdown("""
    <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* ROOT VARIABLES */
        :root {
        --primary-bg: #f1f5f9;
        --card-bg: #f8fafc;
        --sidebar-bg: #1e293b;
        --sidebar-hover: #334155;

        --text-primary: #0f172a;
        --text-secondary: #475569;
        --text-muted: #94a3b8;

        --border-color: #e2e8f0;

        --accent-blue: #3b82f6;
        --accent-green: #22c55e;
        --accent-orange: #f59e0b;
        --accent-red: #ef4444;
        --accent-purple: #8b5cf6;
    }


        /* GLOBAL STYLES */
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        html, body, .stApp {
            background-color: var(--primary-bg);
            color: var(--text-primary);
        }

        /* REMOVE DEFAULT STREAMLIT PADDING */
        .block-container {
            padding: 2rem 2rem 3rem 2rem;
            max-width: 100%;
        }

        /* HEADINGS */
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-primary);
            font-weight: 600;
            letter-spacing: -0.02em;
        }

        h1 {
            font-size: 28px;
            margin-bottom: 8px;
        }

        h2 {
            font-size: 22px;
            margin-bottom: 16px;
        }

        h3 {
            font-size: 18px;
            margin-bottom: 12px;
        }

        /* SIDEBAR STYLING */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
            border-right: 1px solid rgba(255,255,255,0.1);
        }

        section[data-testid="stSidebar"] > div:first-child {
            padding-top: 1rem;
        }

        /* Sidebar buttons */
        section[data-testid="stSidebar"] button {
            background-color: transparent;
            border: none;
            color: #e2e8f0;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.2s ease;
            width: 100%;
            text-align: left;
            margin: 2px 0;
        }

        section[data-testid="stSidebar"] button:hover {
            background-color: var(--sidebar-hover);
            color: white;
            transform: translateX(2px);
        }

        /* METRIC CARDS */
        [data-testid="stMetricValue"] {
            font-size: 32px;
            font-weight: 700;
            color: var(--text-primary);
        }

        [data-testid="stMetricLabel"] {
            font-size: 13px;
            font-weight: 500;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* CUSTOM CARD STYLES */
        .metric-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 28px 24px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
            height: 100%;
        }

        .metric-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
            border-color: #e0e7ff;
        }

        .metric-card-title {
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 16px;
            display: block;
        }

        .metric-card-value {
            font-size: 42px;
            font-weight: 700;
            color: #0f172a;
            margin: 0;
            line-height: 1;
            letter-spacing: -0.02em;
        }

        .metric-card-delta {
            font-size: 13px;
            color: var(--text-muted);
            margin-top: 12px;
            font-weight: 500;
        }

        /* ICON CONTAINER IN METRIC CARDS */
        .metric-icon {
            width: 48px;
            height: 48px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 16px;
        }

        .metric-icon svg {
            width: 24px;
            height: 24px;
        }

        /* CARDS - HIERARCHY, MONTH, GENERAL */
        .hierarchy-card,
        .month-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 24px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .hierarchy-card:hover,
        .month-card:hover {
            box-shadow: var(--shadow-lg);
            transform: translateY(-4px);
            border-color: var(--accent-blue);
        }

        .month-card {
            text-align: center;
        }

        /* PROGRESS BARS */
        .pms-progress-container {
            background-color: #e2e8f0;
            height: 8px;
            border-radius: 999px;
            overflow: hidden;
            margin: 12px 0;
        }

        .pms-progress-bar {
            height: 100%;
            border-radius: 999px;
            transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
        }

        /* TABLES & DATAFRAMES */
        [data-testid="stDataFrame"] {
            background: var(--card-bg);
            border-radius: 12px;
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-sm);
            overflow: hidden;
        }

        table {
            border-collapse: separate;
            border-spacing: 0;
        }

        thead tr th {
            background: #f8fafc !important;
            font-weight: 600 !important;
            font-size: 12px !important;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-secondary) !important;
            border-bottom: 2px solid var(--border-color) !important;
            padding: 16px 12px !important;
        }

        tbody tr {
            border-bottom: 1px solid var(--border-color);
            transition: background 0.2s ease;
        }

        tbody tr:hover {
            background: #f8fafc;
        }

        tbody td {
            padding: 16px 12px !important;
            font-size: 14px;
            color: var(--text-primary);
        }

        /* BUTTONS */
        .stButton button {
            background: var(--accent-blue);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 24px;
            font-weight: 500;
            font-size: 14px;
            transition: all 0.2s ease;
            box-shadow: var(--shadow-sm);
        }

        .stButton button:hover {
            background: #2563eb;
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }

        button[kind="primary"] {
            background: var(--accent-blue) !important;
        }

        button[kind="secondary"] {
            background: var(--card-bg) !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--border-color) !important;
        }

        /* INPUT FIELDS */
        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox select,
        .stNumberInput input {
            border-radius: 8px;
            border: 1px solid var(--border-color);
            padding: 10px 14px;
            font-size: 14px;
            transition: all 0.2s ease;
        }

        .stTextInput input:focus,
        .stTextArea textarea:focus,
        .stSelectbox select:focus,
        .stNumberInput input:focus {
            border-color: var(--accent-blue);
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        }

        /* EXPANDERS */
        .streamlit-expanderHeader {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            font-weight: 500;
            color: var(--text-primary);
            padding: 14px 18px;
        }

        .streamlit-expanderHeader:hover {
            border-color: var(--accent-blue);
        }

        /* ALERTS */
        .stAlert {
            border-radius: 8px;
            border-left: 4px solid;
            padding: 14px 18px;
            font-size: 14px;
        }

        [data-testid="stAlert"][data-baseweb="notification-info"] {
            background: #dbeafe;
            border-left-color: var(--accent-blue);
        }

        [data-testid="stAlert"][data-baseweb="notification-positive"] {
            background: #d1fae5;
            border-left-color: var(--accent-green);
        }

        [data-testid="stAlert"][data-baseweb="notification-warning"] {
            background: #fef3c7;
            border-left-color: var(--accent-orange);
        }

        [data-testid="stAlert"][data-baseweb="notification-error"] {
            background: #fee2e2;
            border-left-color: var(--accent-red);
        }

        /* TABS */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            border-bottom: 2px solid var(--border-color);
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 8px 8px 0 0;
            padding: 12px 24px;
            font-weight: 500;
            font-size: 14px;
            color: var(--text-secondary);
            border: none;
        }

        .stTabs [aria-selected="true"] {
            background: var(--card-bg);
            color: var(--accent-blue);
            border-bottom: 2px solid var(--accent-blue);
        }

        /* SCROLLBAR */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }

        ::-webkit-scrollbar-track {
            background: var(--primary-bg);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--border-color);
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: var(--text-muted);
        }

        /* DIVIDER */
        hr {
            border: none;
            border-top: 1px solid var(--border-color);
            margin: 24px 0;
        }
    </style>
    """, unsafe_allow_html=True)


# ============================================
# PROFESSIONAL UI COMPONENTS
# ============================================

def render_user_avatar(user: Dict):
    """Modern professional user avatar"""
    initial = user['name'][0].upper() if user.get('name') else "U"
    role = user.get('role', 'User')
    designation = user.get('designation', 'Employee')

    # Role color mapping
    role_colors = {
        'HR': '#8b5cf6',
        'Manager': '#3b82f6',
        'Employee': '#10b981'
    }
    role_color = role_colors.get(role, '#64748b')

    st.markdown(f"""
    <div style="padding: 24px 16px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1);">
        <div style="
            width: 72px;
            height: 72px;
            border-radius: 50%;
            background: linear-gradient(135deg, {role_color}, #1e293b);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 16px;
            font-size: 28px;
            font-weight: 700;
            color: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        ">
            {initial}
        </div>
        <div style="font-size: 16px; font-weight: 600; color: #f1f5f9; margin-bottom: 4px;">
            {user.get('name', '')}
        </div>
        <div style="font-size: 12px; color: #94a3b8; margin-bottom: 8px;">
            {designation}
        </div>
        <div style="
            display: inline-block;
            padding: 4px 12px;
            border-radius: 999px;
            background: {role_color};
            font-size: 11px;
            font-weight: 600;
            color: white;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        ">
            {role}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_metric_card(
    label: str,
    value: str,
    color: str = "#3b82f6",
    delta: Optional[str] = None,
):
    """Clean, professional metric card without icons"""
    
    delta_html = ""
    if delta:
        delta_color = "#10b981" if "+" in str(delta) else "#ef4444"
        delta_html = f"<div class='metric-card-delta' style='color: {delta_color};'>{delta}</div>"

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-card-title" style="color: {color};">{label}</div>
        <div class="metric-card-value">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)


def render_card(title: str, subtitle: str = "", icon: str = ""):
    """Professional standalone card component (fully reliable styling)"""

    # Icon HTML (optional)
    icon_html = (
        f"<span style='margin-right: 10px; color: #3b82f6; font-size: 20px;'>{icon}</span>"
        if icon else ""
    )

    st.markdown(f"""
    <div style="
        background: #f8fafc;
        border-radius: 12px;
        padding: 20px 24px;
        border: 1px solid #e2e8f0;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
        transition: all 0.2s ease-in-out;
        margin-bottom: 12px;
    "
        onmouseover="this.style.boxShadow='0px 6px 12px rgba(0,0,0,0.10)'; this.style.transform='translateY(-2px)';"
        onmouseout="this.style.boxShadow='0px 2px 4px rgba(0,0,0,0.05)'; this.style.transform='translateY(0px)';"
    >
        <!-- Title -->
        <div style="
            font-size: 18px;
            font-weight: 600;
            color: #0f172a;
            display: flex;
            align-items: center;
            margin-bottom: 8px;
        ">
            {icon_html}{title}
        </div>

        <!-- Subtitle -->
        <div style="
            font-size: 14px;
            color: #64748b;
            line-height: 1.6;
        ">
            {subtitle}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_progress_bar(progress: float, label: str = ""):
    """Professional, standalone progress bar component"""

    color = get_status_color(progress)

    st.markdown(f"""
    <div style="
        margin: 18px 0;
        width: 100%;
    ">

        <!-- Label + Percentage -->
        <div style="
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        ">
            <span style="
                font-size: 13px;
                font-weight: 600;
                color: #475569;
            ">{label}</span>

            <span style="
                font-size: 14px;
                font-weight: 700;
                color: {color};
            ">{progress:.1f}%</span>
        </div>

        <!-- Progress Bar Container -->
        <div style="
            width: 100%;
            height: 10px;
            background: #e2e8f0;
            border-radius: 12px;
            overflow: hidden;
        ">

            <!-- Actual Bar -->
            <div style="
                width: {progress}%;
                height: 100%;
                background: {color};
                border-radius: 10px;
                transition: width 0.4s ease-in-out;
            ">
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


def render_feedback_card(feedback: Dict, feedback_type: str):
    """Modern feedback card"""
    color_map = {
        'Manager': '#3b82f6',
        'HR': '#10b981',
        'Self Appraisal': '#f59e0b'
    }
    
    color = color_map.get(feedback_type, '#64748b')
    stars = '★' * feedback.get('rating', 3) + '☆' * (5 - feedback.get('rating', 3))
    
    user_name = feedback.get('users', {}).get('name', 'Unknown')
    date_str = feedback.get('date', '')
    comment = feedback.get('comment', '')
    
    st.markdown(f"""
    <div style='
        background: {color}08;
        border: 1px solid {color}30;
        border-left: 4px solid {color};
        border-radius: 12px;
        padding: 20px;
        margin: 12px 0;
        transition: all 0.3s ease;
    '>
        <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;'>
            <div>
                <div style='font-weight: 600; color: #0f172a; font-size: 15px;'>{user_name}</div>
                <div style='color: #64748b; font-size: 12px; margin-top: 2px;'>{date_str}</div>
            </div>
            <div style='color: {color}; font-size: 18px;'>{stars}</div>
        </div>
        <p style='margin: 0; color: #334155; font-size: 14px; line-height: 1.6;'>{comment}</p>
    </div>
    """, unsafe_allow_html=True)


# ============================================
# VALIDATION UTILITIES
# ============================================

def validate_email(email: str) -> bool:
    """Validate email format"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_date_range(start_date: date, end_date: date) -> bool:
    """Validate that end date is after start date"""
    return end_date >= start_date


def validate_goal_data(goal_data: Dict) -> tuple[bool, str]:
    """Validate goal data before submission"""
    required_fields = ['goal_title', 'start_date', 'end_date']
    
    for field in required_fields:
        if not goal_data.get(field):
            return False, f"Missing required field: {field}"
    
    if not validate_date_range(goal_data['start_date'], goal_data['end_date']):
        return False, "End date must be after start date"
    
    return True, ""


# ============================================
# DATA FORMATTING UTILITIES
# ============================================

def format_goal_table_data(goals: List[Dict]) -> List[Dict]:
    """Format goals data for table display"""
    table_data = []
    for goal in goals:
        table_data.append({
            'Vertical': goal.get('vertical', ''),
            'Title': goal['goal_title'],
            'KPI': goal.get('kpi', ''),
            'Monthly Target': goal.get('monthly_target', 0),
            'Start Date': goal['start_date'],
            'End Date': goal['end_date'],
            'W1 Target': goal.get('week1_target', 0),
            'W2 Target': goal.get('week2_target', 0),
            'W3 Target': goal.get('week3_target', 0),
            'W4 Target': goal.get('week4_target', 0),
            'W1 Achievement': goal.get('week1_achievement', 0),
            'W2 Achievement': goal.get('week2_achievement', 0),
            'W3 Achievement': goal.get('week3_achievement', 0),
            'W4 Achievement': goal.get('week4_achievement', 0),
            'Monthly Achievement': goal.get('monthly_achievement', 0)
        })
    return table_data


def export_to_csv(data: List[Dict], filename: str) -> str:
    """Export data to CSV format"""
    import pandas as pd
    df = pd.DataFrame(data)
    return df.to_csv(index=False)


# ============================================
# SESSION STATE UTILITIES
# ============================================

def init_session_state():
    """Initialize all session state variables"""
    defaults = {
        'user': None,
        'page': 'year_selection',
        'theme': 'light',
        'selected_year': datetime.now().year,
        'selected_quarter': None,
        'selected_month': None
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_navigation():
    """Reset navigation to home page"""
    st.session_state.page = 'year_selection'
    st.session_state.selected_year = datetime.now().year
    st.session_state.selected_quarter = None
    st.session_state.selected_month = None
    
