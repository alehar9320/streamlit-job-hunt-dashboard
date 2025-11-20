# JobTech Dev Job Search Dashboard

This project is a simple Streamlit dashboard that interfaces with the [JobTech Dev JobSearch API](https://jobsearch.api.jobtechdev.se/) to search for job advertisements.

## Architecture

The application follows a simple client-server architecture where:

-   **Frontend**: [Streamlit](https://streamlit.io/) provides the web interface (UI). It handles user input (search queries) and renders the results.
-   **Backend Logic**: Python is used to handle the business logic. It makes HTTP requests to the external API.
-   **External API**: The [JobSearch API](https://jobsearch.api.jobtechdev.se/) is the source of truth for job data.

### Data Flow
1.  User enters a query in the Streamlit UI.
2.  Python script sends a GET request to `https://jobsearch.api.jobtechdev.se/search`.
3.  API responds with JSON data containing job hits.
4.  Python script parses the JSON.
5.  Streamlit updates the UI to display the results.

## Configuration

The project is configured to use the JobSearch API.

-   **API Endpoint**: `https://jobsearch.api.jobtechdev.se`
-   **Search Endpoint**: `/search`

## Prerequisites

-   Python 3.9+
-   `pip`

## Installation

1.  Install the required packages:
    ```bash
    pip install streamlit requests
    ```
    *(Note: `altair<5` might be required if you encounter version compatibility issues with Streamlit)*

## Usage

Run the dashboard using Streamlit:

```bash
streamlit run dashboard.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.
