import streamlit as st
import requests
import json

url = 'https://jobsearch.api.jobtechdev.se'
url_for_search = f"{url}/search"

def _get_ads(params):
    headers = {'accept': 'application/json'}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()  # check for http errors
    return json.loads(response.content.decode('utf8'))

def main():
    st.title("JobTech Dev Job Search")
    st.write("Enter a search query to find job ads.")

    query = st.text_input("Search Query", value="lärare uppsala")

    if st.button("Search"):
        with st.spinner("Searching..."):
            try:
                # Get total hits
                search_params_count = {'q': query, 'limit': 0}
                json_response_count = _get_ads(search_params_count)
                number_of_hits = json_response_count['total']['value']
                st.success(f"Found {number_of_hits} hits")

                # Get actual ads (limit 100 for this example)
                search_params_hits = {'q': query, 'limit': 100}
                json_response_hits = _get_ads(search_params_hits)
                hits = json_response_hits['hits']

                if hits:
                    st.subheader("Results")
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
