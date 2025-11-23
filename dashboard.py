import streamlit as st
import requests
import json
import base64
import os

# Configuration
API_BASE_URL = 'https://jobsearch.api.jobtechdev.se'
SEARCH_ENDPOINT = f"{API_BASE_URL}/search"

# Role Definitions with Image Assets
ROLES = {
    "Product Manager": "assets/product_manager.png",
    "Frontend Web Developer": "assets/frontend_developer.png",
    "Business Analyst": "assets/business_analyst.png",
    "Team Lead": "assets/team_lead.png",
    "Engineering Manager": "assets/engineering_manager.png"
}

# --- Compatibility Helpers ---
def safe_rerun():
    """Reruns the script in a way compatible with older Streamlit versions."""
    if hasattr(st, "rerun"):
        st.rerun()
    elif hasattr(st, "experimental_rerun"):
        st.experimental_rerun()
    else:
        st.warning("Please manually refresh the page.")

# --- API Functions ---
@st.experimental_memo(ttl=3600) # Cache for 1 hour
def _get_ads(params):
    """
    Fetches job ads from the JobTech Dev JobSearch API.
    Cached to improve performance.
    """
    headers = {'accept': 'application/json'}
    response = requests.get(SEARCH_ENDPOINT, headers=headers, params=params)
    response.raise_for_status()
    return json.loads(response.content.decode('utf8'))

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_custom_css():
    st.markdown("""
        <style>
        /* General Card Styling for Columns */
        [data-testid="stColumn"] {
            background-color: #f8f9fa;
            border-radius: 15px;
            padding: 15px;
            transition: all 0.3s ease;
            border: 1px solid #e0e0e0;
        }
        
        [data-testid="stColumn"]:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            border-color: #0D8ABC;
        }

        /* Image Styling */
        [data-testid="stImage"] img {
            border-radius: 10px;
            transition: transform 0.3s ease;
        }
        
        /* Button Styling */
        .stButton button {
            width: 100%;
            border-radius: 8px;
            font-weight: 600;
            border: none;
            background-color: #0D8ABC;
            color: white;
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #0b76a0;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        /* Remove default padding from top of columns to make cards look tighter */
        .block-container {
            padding-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

def render_dashboard():
    st.title("🚀 Job Hunt Dashboard")
    st.write("Select a role to view current opportunities.")

    # Create a grid layout
    cols = st.columns(3) # 3 columns per row
    
    for i, (role, image_path) in enumerate(ROLES.items()):
        col = cols[i % 3]
        with col:
            # Fetch hit count
            count = 0
            try:
                params = {'q': role, 'limit': 0}
                response = _get_ads(params)
                count = response['total']['value']
            except Exception:
                count = "N/A"

            # Display Card
            # Image
            if os.path.exists(image_path):
                # FIX: use_container_width -> use_column_width for older Streamlit
                st.image(image_path, use_column_width=True) 
            else:
                st.warning(f"Image not found: {image_path}")

            # Metric
            st.metric(label="Open Positions", value=count)

            # Button
            if st.button(f"Explore {role}", key=f"btn_{role}"):
                st.session_state.selected_role = role
                st.session_state.page = 'listings'
                safe_rerun()
            
            st.markdown("---") # Spacer

def render_listings():
    role = st.session_state.selected_role
    
    # Header with Back Button
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back"):
            st.session_state.page = 'home'
            st.session_state.selected_role = None
            safe_rerun()
    with col2:
        st.title(f"Listings for: {role}")

    # Search Interface (Pre-filled)
    query = st.text_input("Refine Search", value=role)
    
    if query:
        with st.spinner(f"Searching for '{query}'..."):
            try:
                # Get actual ads
                search_params = {'q': query, 'limit': 50}
                response = _get_ads(search_params)
                hits = response['hits']
                total = response['total']['value']
                
                st.markdown(f"**Found {total} matches**")

                if hits:
                    for hit in hits:
                        with st.expander(f"{hit['headline']} - {hit['employer']['name']}"):
                            st.write(f"**Employer:** {hit['employer']['name']}")
                            if 'description' in hit and 'text' in hit['description']:
                                st.write(hit['description']['text'][:300] + "...")
                            if 'webpage_url' in hit:
                                st.markdown(f"[Read Full Ad]({hit['webpage_url']})")
                else:
                    st.info("No ads found.")
            except Exception as e:
                st.error(f"Error: {e}")

def main():
    st.set_page_config(page_title="Alexander's Job Hunt", page_icon="💼", layout="wide")
    set_custom_css()

    # Sidebar Profile
    with st.sidebar:
        st.image("https://ui-avatars.com/api/?name=Alexander+Härenstam&background=0D8ABC&color=fff&size=200", width=150)
        st.title("Alexander Härenstam")
        st.markdown("**Product Manager**")
        st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/alehar/)")
        st.markdown("---")
        if st.button("Reset Dashboard"):
            st.session_state.page = 'home'
            st.session_state.selected_role = None
            safe_rerun()

    # State Management
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    if 'selected_role' not in st.session_state:
        st.session_state.selected_role = None

    # Routing
    if st.session_state.page == 'home':
        render_dashboard()
    elif st.session_state.page == 'listings':
        render_listings()

if __name__ == '__main__':
    main()
