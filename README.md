# 🚀 Job Hunt Dashboard

A personalized, interactive dashboard to streamline the job search process. This application interfaces with the [JobTech Dev JobSearch API](https://jobsearch.api.jobtechdev.se/) to aggregate, filter, and display job advertisements for specific roles.

**Live Demo:** [https://swe-job-hunt-dash.streamlit.app/](https://swe-job-hunt-dash.streamlit.app/)

## ✨ Features

-   **Role-Based Filtering**: Quickly view opportunities for pre-defined roles (e.g., Product Manager, Frontend Developer).
-   **Real-Time Data**: Fetches live job listings directly from the JobTech Dev API.
-   **Interactive UI**: Clean, responsive interface built with Streamlit.
-   **Job Details**: View key details including employer, description preview, and direct links to full ads.
-   **Smart Caching**: Implements caching to reduce API calls and improve performance.

## 🛠️ Architecture

The application follows a simple client-server architecture:

-   **Frontend**: [Streamlit](https://streamlit.io/) handles the UI, user input, and rendering.
-   **Backend**: Python logic manages API requests, data parsing, and state management.
-   **Data Source**: [JobTech Dev JobSearch API](https://jobsearch.api.jobtechdev.se/) serves as the source of truth for job data.

## 📂 Project Structure

```text
streamlit-dash-pm-example/
├── assets/                 # Static assets (images, icons)
├── dashboard.py            # Main application logic
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── agent_instructions.md   # Guidelines for AI assistance
```

## 🚀 Getting Started

### Prerequisites

-   Python 3.9+
-   pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/alehar9320/streamlit-job-hunt-dashboard.git
    cd streamlit-job-hunt-dashboard
    ```

2.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the dashboard locally:

```bash
streamlit run dashboard.py
```

The app will open in your default browser at `http://localhost:8501`.

## ⚙️ Configuration

The application is configured to use the JobSearch API:

-   **API Endpoint**: `https://jobsearch.api.jobtechdev.se`
-   **Search Endpoint**: `/search`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
