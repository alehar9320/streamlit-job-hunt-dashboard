# Antigravity Agent Instructions

These instructions are designed to guide Antigravity in maintaining high accuracy and adhering to best practices when working on this project.

## 1. Streamlit Best Practices
-   **Source of Truth**: Always refer to the official [Streamlit Documentation](https://docs.streamlit.io/) for the most accurate and up-to-date information.
-   **Version Compatibility**: Be mindful of the installed Streamlit version. Avoid using features that are not supported by the current version (e.g., `st.divider` or `use_container_width` in older versions).
-   **State Management**: Use `st.session_state` for managing state across reruns, especially for interactive elements like buttons and inputs.
-   **Performance**: Use `st.cache_data` or `st.cache_resource` (or `st.experimental_memo`/`st.experimental_singleton` for older versions) to optimize expensive computations or data fetching.
-   **Layout**: Utilize `st.columns`, `st.sidebar`, and `st.expander` effectively to create clean and organized layouts.

## 2. Code Quality & Style
-   **Clarity**: Write clear, readable code with meaningful variable names.
-   **Modularity**: Break down complex logic into helper functions.
-   **Error Handling**: Implement robust error handling (try-except blocks) to prevent the app from crashing and to provide user-friendly error messages.
-   **Type Hinting**: Use Python type hints to improve code maintainability.

## 3. Project Specifics
-   **API Usage**: When interacting with the JobTech Dev API, ensure proper error handling for HTTP requests and validate JSON responses.
-   **Configuration**: Keep configuration values (like API URLs) in constants or a separate config file.
-   **Documentation**: Maintain the `README.md` and ensure it accurately reflects the current state of the project.

## 4. Verification
-   **Browser Testing**: Always verify changes by running the app and interacting with it in the browser.
-   **Screenshot Verification**: Use screenshots to confirm that UI elements are rendered correctly and that the app is in the expected state.
