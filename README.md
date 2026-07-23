# data-insights-engine

This project provides a Python-based analytics dashboard and reporting engine for transaction, device, and user engagement data.

The current Streamlit dashboard is implemented in `scripts/Data_Insights.py` and connects to a PostgreSQL database for live transaction and user metrics.

## Project structure
- `.env.example`: example environment variables file
- `env/`: Python virtual environment and Streamlit dashboard entrypoint
- `notebooks/`: Jupyter notebooks for analysis and visualization
- `README.md`: project documentation
- `requirements.txt`: Python dependency list

## Setup
1. Create or activate the Python virtual environment:
   - `python -m venv env`
   - `env\Scripts\activate`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Configure database connection settings in `config/settings.py` or the appropriate connection file.
4. Ensure the PostgreSQL database is running and accessible.

## Run the Streamlit dashboard
From the repository root, start the app with:

```bash
streamlit run scripts/Data_Insights.py
```
For example - streamlit run "D:\GITHUB REPO\data-insights-engine\scripts\Data_Insights.py"

Then open the local URL displayed by Streamlit in your browser.

## Development notes
- The dashboard uses Plotly Express for charts and Streamlit for page navigation.
- SQL query helpers are defined in `scripts/Data_Insights.py` and currently connect to the `smart_pay` PostgreSQL database.
- The app includes sections for:
  - `Transaction Dynamics`
  - `Transaction Analysis`
  - `Device Dominance`
  - `User Engagement`
  - `Insurance Analysis`

## Notes
- If you change the database credentials, update the connection settings in the dashboard script or configuration files.

