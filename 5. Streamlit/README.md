# Streamlit — Quick Overview

This folder contains simple Streamlit example apps and widgets demonstrating core concepts.

## What is Streamlit

Streamlit is a Python library for building interactive, data-driven web apps with minimal code. It is designed for data scientists and ML engineers to quickly create UIs for visualizing data, building demos, and creating simple dashboards.

## Important concepts

- **Script-based apps:** Streamlit apps are plain Python scripts that run from top to bottom on each user interaction (widget change), triggering a rerun.
- **Widgets:** Input controls like `st.slider`, `st.text_input`, `st.selectbox`, and `st.file_uploader` allow users to provide input. Widget values are available as Python variables.
- **Layout & sidebar:** Use `st.sidebar` to place controls in a sidebar and `st.columns`, `st.container` etc. for layouts.
- **Caching:** Use `@st.cache_data` or `@st.cache_resource` to cache expensive computations or loaded data to avoid recomputation across reruns.
- **State:** Use `st.session_state` to persist small pieces of state (like counters, user selections) across reruns.
- **Reruns & determinism:** Every widget interaction reruns the script from top to bottom. Keep side effects minimal and perform expensive work inside cached functions.

## Files in this folder

- `classification.py`: Simple ML demo using `sklearn` and Streamlit widgets for inputs and prediction display.
- `streamlit.py`: Minimal example showing `st.write`, DataFrame display and a line chart.
- `widget.py`: Examples of common input widgets and file upload.

## How to run

1. Create and activate a Python virtual environment.
2. Install dependencies:

```
pip install streamlit pandas scikit-learn
```

3. Run an app:

```
streamlit run "5. Streamlit/streamlit.py"
```

Replace with `classification.py` or `widget.py` to try other examples.

## Notes

- This README is a quick reference — see inline comments in the Python files for explanations of each concept used.
