import streamlit as st
import requests
import json

# Configuration
API_BASE_URL = 'https://jobsearch.api.jobtechdev.se'
SEARCH_ENDPOINT = f"{API_BASE_URL}/search"

def _get_ads(params):
    """
    Fetches job ads from the JobTech Dev JobSearch API.
    
    Args:
        params (dict): Query parameters for the API search.
        
    Returns:
        dict: JSON response from the API.
    """
    headers = {'accept': 'application/json'}
    response = requests.get(SEARCH_ENDPOINT, headers=headers, params=params)
    response.raise_for_status()  # check for http errors
    return json.loads(response.content.decode('utf8'))

def main():
    st.set_page_config(page_title="Alexander's Job Hunt", page_icon="💼", layout="wide")

    # Sidebar Profile
    with st.sidebar:
        st.image("https://ui-avatars.com/api/?name=Alexander+Härenstam&background=0D8ABC&color=fff&size=200", width=150)
        st.title("Alexander Härenstam")
        st.markdown("**Product Manager**")
        st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/alehar/)")
        
        st.markdown("### Target Roles")
        roles = [
            "Product Manager", 
            "Frontend Web Developer", 
            "Business Analyst", 
            "Team Lead", 
            "Engineering Manager"
        ]
        for role in roles:
            st.markdown(f"- {role}")

    st.title("🚀 Job Hunt Dashboard")
    st.write("Welcome to your personalized job search assistant. Click a role below to quick-search or enter a custom query.")

    # Quick Search Buttons
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    
    selected_role = None
    
    for i, role in enumerate(roles):
        with columns[i % 5]:
            if st.button(role):
                selected_role = role

    st.markdown("---")

    # Search Interface
    if selected_role:
        query = st.text_input("Search Query", value=selected_role)
        # Auto-trigger search if a button was clicked
        run_search = True
    else:
        query = st.text_input("Search Query", value="Product Manager")
        run_search = st.button("Search")

    if run_search:
        with st.spinner(f"Searching for '{query}'..."):
            try:
                # Get total hits
                search_params_count = {'q': query, 'limit': 0}
                json_response_count = _get_ads(search_params_count)
                number_of_hits = json_response_count['total']['value']
                st.success(f"Found {number_of_hits} hits for '{query}'")

                # Get actual ads (limit 100 for this example)
                search_params_hits = {'q': query, 'limit': 100}
                json_response_hits = _get_ads(search_params_hits)
                hits = json_response_hits['hits']

                if hits:
                    st.subheader("Job Listings")
                    for hit in hits:
                        with st.expander(f"{hit['headline']} - {hit['employer']['name']}"):
                            st.write(f"**Employer:** {hit['employer']['name']}")
                            st.write(f"**Headline:** {hit['headline']}")
                            # Add more details if available and relevant
                            if 'description' in hit and 'text' in hit['description']:
                                st.write(hit['description']['text'][:200] + "...") # Preview
                            
                            if 'webpage_url' in hit:
                                st.markdown(f"[Read more]({hit['webpage_url']})")

                else:
                    st.warning("No ads found for this query.")

            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
