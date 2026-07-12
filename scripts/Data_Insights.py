import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import psycopg2
import streamlit as st

st.set_page_config(page_title="PhonePe Data Insights Engine", page_icon=":bar_chart:", layout="wide")

if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

def set_page(page_name: str) -> None:
    st.session_state.selected_page = page_name

def get_top_10_Lower_district_insurance_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            select region_name, sum(transaction_count) as total_count
            from insurance_map
            group by region_name
            order by total_count ASC
            limit 10;
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["region_name", "total_count"])
    except Exception as e:
        st.error(f"Unable to load insurance data: {e}")
        return pd.DataFrame(columns=["region_name", "total_count"])

def get_top_10_district_insurance_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            select region_name, sum(transaction_count) as total_count
            from insurance_map
            group by region_name
            order by total_count DESC
            limit 10;
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["region_name", "total_count"])
    except Exception as e:
        st.error(f"Unable to load insurance data: {e}")
        return pd.DataFrame(columns=["region_name", "total_count"])

def get_top_10_state_lower_insurance_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            select state, sum(transaction_count) as total_count
            from insurance_map
            group by state
            order by total_count ASC
            limit 10;
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["state", "total_count"])
    except Exception as e:
        st.error(f"Unable to load insurance data: {e}")
        return pd.DataFrame(columns=["state", "total_count"]) 

def get_top_10_state_insurance_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            select state, sum(transaction_count) as total_count
            from insurance_map
            group by state
            order by total_count DESC
            limit 10;
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["state", "total_count"])
    except Exception as e:
        st.error(f"Unable to load insurance data: {e}")
        return pd.DataFrame(columns=["state", "total_count"]) 

def get_top_3_payment_category_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            SELECT transaction_type,
            SUM(transaction_count) AS total_count
            FROM transaction_agg
            GROUP BY transaction_type
            ORDER BY total_count DESC
            Limit 3;
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["transaction_type", "total_count"])
    except Exception as e:
        st.error(f"Unable to load transaction data: {e}")
        return pd.DataFrame(columns=["transaction_type", "total_count"]) 
    
def get_top_3_payment_category_Merchant_transactions_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            SELECT  state, SUM(transaction_count) AS total_count
            FROM transaction_agg
            where transaction_type='Merchant Payments'
            GROUP BY state
            ORDER BY total_count DESC
            Limit 3;
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["state", "total_count"])
    except Exception as e:
        st.error(f"Unable to load transaction data: {e}")
        return pd.DataFrame(columns=["state", "total_count"]) 

def get_lower_3_state_transactions_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            SELECT  state, SUM(transaction_count) AS total_count
            FROM transaction_agg
            GROUP BY state
            ORDER BY total_count ASC
            Limit 3;
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["state", "total_count"])
    except Exception as e:
        st.error(f"Unable to load transaction data: {e}")
        return pd.DataFrame(columns=["state", "total_count"])

def get_top_3_year_quarter_transactions_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            SELECT  year,quarter, SUM(transaction_count) AS total_count
                FROM transaction_agg
                GROUP BY year,quarter
                ORDER BY total_count DESC
                Limit 3;
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["year", "quarter", "total_count"])
    except Exception as e:
        st.error(f"Unable to load transaction data: {e}")
        return pd.DataFrame(columns=["year", "quarter", "total_count"])         


def get_top_3_state_transaction_amount_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            SELECT state,
            SUM(transaction_amount) AS total_amount
            FROM transaction_agg
            GROUP BY state
            ORDER BY total_amount DESC
            Limit 3;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["state", "total_amount"])
    except Exception as e:
        st.error(f"Unable to load transaction data: {e}")
        return pd.DataFrame(columns=["state", "total_amount"])    

def get_top_10_state_transaction_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            SELECT state,
            SUM(transaction_count) AS total_transactions
            FROM transaction_agg
            GROUP BY state
            ORDER BY total_transactions DESC
            limit 10;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["state", "total_transactions"])
    except Exception as e:
        st.error(f"Unable to load transaction data: {e}")
        return pd.DataFrame(columns=["state", "total_transactions"])


def get_state_transaction_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
           SELECT state,
            SUM(transaction_count) AS total_transactions
            FROM transaction_agg
            GROUP BY state
        ORDER BY total_transactions DESC
        limit 50;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["state", "total_transactions"])
    except Exception as e:
        st.error(f"Unable to load transaction data: {e}")
        return pd.DataFrame(columns=["state", "total_transactions"])

def get_transaction_quarter_year_wise_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
           SELECT year, quarter,  SUM(transaction_count) AS total_transactions
            FROM transaction_agg
            GROUP BY year, quarter
            ORDER BY year, quarter DESC
            Limit 10;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["year", "quarter", "total_transactions"])
    except Exception as e:
        st.error(f"Unable to load transaction data: {e}")
        return pd.DataFrame(columns=["year", "quarter", "total_transactions"])
    
def get_transaction_payment_category_wise_data() -> pd.DataFrame:
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="smart_pay",
                user="postgres",
                password="HareKrishna@143",
            )
            conn.autocommit = True
            cur = conn.cursor()
            sql = """
               select transaction_type, sum(transaction_count) as total_transactions from transaction_agg
                group by transaction_type
                order by total_transactions desc;
            """
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            conn.close()
            return pd.DataFrame(rows, columns=["transaction_type", "total_transactions"])
        except Exception as e:
            st.error(f"Unable to load transaction data: {e}")
            return pd.DataFrame(columns=["transaction_type", "total_transactions"]) 

def get_device_with_registered_users_wise_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
           select brand, sum(count) as number_of_registered_user 
            from user_agg
            GROUP BY brand
            Order BY number_of_registered_user desc;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["brand", "number_of_registered_user"])
    except Exception as e:
        st.error(f"Unable to load device data: {e}")
        return pd.DataFrame(columns=["brand", "number_of_registered_user"])   

def get_appopens_with_registered_users_wise_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
           SELECT brand,
       SUM(count) AS registered_users,
       SUM(app_opens) AS total_app_opens
        FROM user_agg
        GROUP BY brand
        ORDER BY registered_users DESC;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["brand", "number_of_registered_user", "total_app_opens"])
    except Exception as e:
        st.error(f"Unable to load device data: {e}")
        return pd.DataFrame(columns=["brand", "number_of_registered_user", "total_app_opens"])


def get_transaction_state_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            SELECT state, SUM(transaction_count) AS total_transactions
            FROM transaction_agg
            GROUP BY state
            ORDER BY total_transactions DESC
            limit 10;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["state", "total_transactions"])
    except Exception as e:
        st.error(f"Unable to load state transaction data: {e}")
        return pd.DataFrame(columns=["state", "total_transactions"])


def get_transaction_all_region_data() -> pd.DataFrame:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="smart_pay",
            user="postgres",
            password="HareKrishna@143",
        )
        conn.autocommit = True
        cur = conn.cursor()
        sql = """
            SELECT region_name, SUM(transaction_count) AS total_transactions
            FROM transaction_map 
            GROUP BY region_name
            ORDER BY total_transactions DESC
            Limit 10;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(rows, columns=["region_name", "total_transactions"])
    except Exception as e:
        st.error(f"Unable to load transaction data: {e}")
        return pd.DataFrame(columns=["region_name", "total_transactions"])

# Header
st.title("PhonePe Data Insights Engine")

st.sidebar.header("Navigation")
if st.sidebar.button("📊 Home ", use_container_width=True):
    set_page("Home")
if st.sidebar.button("📊 Transaction Analysis for Market Expansion", use_container_width=True):
    set_page("Transaction Analysis")
if st.sidebar.button("📊 Transaction Dynamics Analysis", use_container_width=True):
    set_page("Transaction Dynamics")
if st.sidebar.button("📱 Device Dominance Analysis", use_container_width=True):
    set_page("Device Dominance")
if st.sidebar.button("👤 User Engagement Analysis", use_container_width=True):
    set_page("User Engagement")
if st.sidebar.button("📊 Insurance Analysis", use_container_width=True):
    set_page("Insurance")    

if st.session_state.selected_page == "Transaction Dynamics":
    st.subheader("Transaction Dynamics Analysis")
    options = st.selectbox(
        "Select Transaction Data Analysis as:",
        (
            "-- Select Analysis --",
            "Top 10 Region Wise Maximum Transactions",
            "Top 10 State Wise Maximum Transactions",
            "Quarter and year Wise Maximum Transactions",
            "Payment Category wise Transactions"

        )
    )
    if options == "-- Select Analysis --":
        st.info("Please select an analysis option from the dropdown.")  
        st.stop()

    elif options == "Top 10 Region Wise Maximum Transactions":
        st.write("Showing Region Wise Analysis")
        transaction_df = get_transaction_all_region_data().sort_values(}
