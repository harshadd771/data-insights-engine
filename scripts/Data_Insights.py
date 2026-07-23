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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
            password="",
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
        transaction_df = get_transaction_all_region_data().sort_values(
            by="total_transactions", ascending=True
        )
        fig = px.bar(
            transaction_df,
            x="total_transactions",
            y="region_name",
            orientation="h",
            title="Top 10 Regions by Transaction Volume",
            text="total_transactions",
            color="region_name",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="#1D4ED8",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Transactions",
            yaxis_title="Region",
            title_x=0.5,
            margin=dict(l=120, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s"),
            yaxis={"categoryorder": "total ascending"},
            showlegend=False,
            autosize=True,
        )

        st.plotly_chart(fig, use_container_width=True)

    elif options == "Top 10 State Wise Maximum Transactions":
        st.write("Showing State Wise Analysis")
        transaction_df = get_transaction_state_data().sort_values(
            by="total_transactions", ascending=True
        )
        fig = px.bar(
            transaction_df,
            x="total_transactions",
            y="state",
            orientation="h",
            title="Top 10 States by Transaction Volume",
            text="total_transactions",
            color="state",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="#A21CAF",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Transactions",
            yaxis_title="State",
            title_x=0.5,
            margin=dict(l=120, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s"),
            yaxis={"categoryorder": "total ascending"},
            showlegend=False,
            autosize=True,
        )
        st.plotly_chart(fig, use_container_width=True)  

    elif options == "Quarter and year Wise Maximum Transactions":
        st.write("Showing Quarter and Year Wise Analysis")
        transaction_df = get_transaction_quarter_year_wise_data().sort_values(
            by=["year", "quarter"], ascending=True
        )
        transaction_df["Period"] = (
            transaction_df["year"].astype(str)
            + " Q"
            + transaction_df["quarter"].astype(str)
        )
        fig = px.line(
            transaction_df,
            x="Period",
            y="total_transactions",
            markers=True,
            title="Quarterly Transaction Trend",
        )

        fig.update_traces(
            mode="lines+markers",
            marker=dict(size=8, color="#059669"),
            line=dict(width=3, color="#059669"),
        )
        fig.update_layout(
            xaxis_title="Quarter",
            yaxis_title="Total Transactions",
            title_x=0.5,
            margin=dict(l=60, r=40, t=70, b=60),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(showgrid=False),
            yaxis=dict(tickformat="~s", gridcolor="#E5E7EB"),
        )

        st.plotly_chart(fig, use_container_width=True)

    elif options == "Payment Category wise Transactions":
        st.write("Showing Payment Category Wise Analysis")
        transaction_df = get_transaction_payment_category_wise_data().sort_values(
            by="total_transactions", ascending=True
        )

        fig = px.bar(
            transaction_df,
            x="total_transactions",
            y="transaction_type",
            orientation="h",
            text="total_transactions",
            title="Payment Category Distribution",
            color="transaction_type",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            marker_line_color="#064E3B",
            marker_line_width=1,
            texttemplate="%{x:~s}",
            textposition="outside",
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Transactions",
            yaxis_title="Payment Category",
            title_x=0.5,
            margin=dict(l=120, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s", showgrid=True, gridcolor="#E5E7EB"),
            yaxis={"categoryorder": "total ascending"},
            showlegend=False,
            autosize=True,
        )

        st.plotly_chart(fig, use_container_width=True)
    
elif st.session_state.selected_page == "Transaction Analysis":
    st.write("Showing Transaction Analysis for Market Expansion")
    st.subheader("Transaction Analysis")
    options = st.selectbox(
        "Select Transaction Data Analysis as:",
        (
            "-- Select Analysis --",
            "Top 10 State Wise Maximum Transactions Count",
            "Top 3 State Wise Maximum Transactions Amount",
            "Top 3 Payment Category",
            "Top 3 States by Payment Category Merchant Transactions",
            "Lower 3 States by Transaction Count",
            "Top 3 Quarter and Year Wise Maximum Transactions"
        )
    )
    if options == "-- Select Analysis --":
        st.info("Please select an analysis option from the dropdown.")  
        st.stop()

    elif options == "Top 10 State Wise Maximum Transactions Count":

        st.write("Showing State Wise Analysis")
        transaction_df = get_top_10_state_transaction_data().sort_values(
            by="total_transactions", ascending=True
        )
        fig = px.bar(
            transaction_df,
            x="total_transactions",
            y="state",
            orientation="h",
            title="Top 10 States by Transaction Volume",
            text="total_transactions",
            color="total_transactions",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="#1D4ED8",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Transactions",
            yaxis_title="state",
            title_x=0.5,
            margin=dict(l=120, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s"),
            yaxis={"categoryorder": "total ascending"},
            showlegend=False,
            autosize=True,
        )

        st.plotly_chart(fig, use_container_width=True)

    elif options == "Top 3 State Wise Maximum Transactions Amount":
        st.write("Showing State Wise Analysis")
        transaction_df = get_top_3_state_transaction_amount_data().sort_values(
            by="total_amount", ascending=True
        )
        fig = px.bar(
            transaction_df,
            x="total_amount",
            y="state",
            orientation="h",
            title="Top 3 States by Transaction Volume",
            text="state",
            color="state",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="#1D4ED8",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Amount",
            yaxis_title="State",
            title_x=0.5,
            margin=dict(l=120, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s"),
            yaxis={"categoryorder": "total ascending"},
            showlegend=False,
            autosize=True,
        )

        st.plotly_chart(fig, use_container_width=True)

    elif options == "Top 3 Payment Category":
        st.write("Showing Payment Category Analysis")
        transaction_df = get_top_3_payment_category_data().sort_values(
            by="total_count", ascending=True
        )
        fig = px.bar(
            transaction_df,
            x="total_count",
            y="transaction_type",
            orientation="h",
            title="Top 3 Payment Categories by Transaction Volume",
            text="total_count",
            color="transaction_type",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="white",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Transactions",
            yaxis_title="Payment Category",
            title_x=0.5,
            margin=dict(l=160, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s", showgrid=True, gridcolor="#E5E7EB"),
            yaxis={"categoryorder": "total ascending"},
            showlegend=False,
            autosize=True,
        )
        st.plotly_chart(fig, use_container_width=True)

    elif options == "Top 3 States by Payment Category Merchant Transactions":
        st.write("Showing Merchant Transaction State Analysis")
        transaction_df = get_top_3_payment_category_Merchant_transactions_data().sort_values(
            by="total_count", ascending=True
        )
        fig = px.bar(
            transaction_df,
            x="total_count",
            y="state",
            orientation="h",
            title="Top 3 States by Merchant Transactions",
            text="total_count",
            color="state",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="white",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Transactions",
            yaxis_title="State",
            title_x=0.5,
            margin=dict(l=120, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s", showgrid=True, gridcolor="#E5E7EB"),
            yaxis={"categoryorder": "total ascending"},
            showlegend=False,
            autosize=True,
        )
        st.plotly_chart(fig, use_container_width=True)

    elif options == "Lower 3 States by Transaction Count":
        st.write("Showing State Wise Analysis")
        transaction_df = get_lower_3_state_transactions_data().sort_values(
            by="total_count", ascending=True
        )
        fig = px.bar(
            transaction_df,
            x="total_count",
            y="state",
            orientation="h",
            title="Lower 3 States by Transaction Count",
            text="total_count",
            color="state",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="white",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Transactions",
            yaxis_title="State",
            title_x=0.5,
            margin=dict(l=120, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s", showgrid=True, gridcolor="#E5E7EB"),
            yaxis={"categoryorder": "total descending"},
            showlegend=False,
            autosize=True,
        )
        st.plotly_chart(fig, use_container_width=True)

    elif options == "Top 3 Quarter and Year Wise Maximum Transactions":
        st.write("Showing State Wise Analysis")
        transaction_df = get_top_3_year_quarter_transactions_data().sort_values(
            by="total_count", ascending=True
        )

        transaction_df["Period"] = (
        transaction_df["year"].astype(str) +
            " Q" +
            transaction_df["quarter"].astype(str)
        )
        fig = px.bar(
            transaction_df,
            x="Period",
            y="total_count",
            text="total_count",
            color="total_count",
            color_continuous_scale="Purples",
            title="Quarter-wise Total Transactions"
        )

        fig.update_traces(
            texttemplate="%{y:.2s}",   # Shows values like 2.5M, 3.2B
            textposition="outside"
        )

        fig.update_layout(
            title_x=0.5,
            xaxis_title="Year & Quarter",
            yaxis_title="Total Transactions",
            xaxis_tickangle=-45,
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)
        
elif st.session_state.selected_page == "Device Dominance":
    st.write("Showing Device Dominance Analysis")
    device_df = get_device_with_registered_users_wise_data().sort_values(
        by="number_of_registered_user", ascending=False
    )
    device_df = device_df[device_df["brand"].notna()].copy()
    device_df["brand"] = device_df["brand"].astype(str).str.strip()
    device_df = device_df[~device_df["brand"].str.lower().isin(["unknown", "unknown brand", "n/a", "na", "")] )

    total_users = device_df["number_of_registered_user"].sum()
    device_df["share_pct"] = (device_df["number_of_registered_user"] / total_users * 100).round(1)

    st.markdown("### Key device brand insights")
    top_devices = device_df.head(3).copy()
    bottom_devices = device_df.tail(3).copy()

    st.markdown("#### Top 3 Brands Registered Users")
    top_cols = st.columns(len(top_devices))
    for col_idx, row in enumerate(top_devices.itertuples(index=False)):
        top_cols[col_idx].metric(
            label=row.brand,
            value=f"{row.number_of_registered_user:,}",
            delta=f"{row.share_pct}% share",
        )

    st.markdown("#### Bottom 3 Brands Registered Users")
    bottom_cols = st.columns(len(bottom_devices))
    for col_idx, row in enumerate(bottom_devices.itertuples(index=False)):
        bottom_cols[col_idx].metric(
            label=row.brand,
            value=f"{row.number_of_registered_user:,}",
            delta=f"{row.share_pct}% share",
        )

elif st.session_state.selected_page == "User Engagement":

    st.subheader("User Engagement Analysis")
    user_df = get_appopens_with_registered_users_wise_data().sort_values(
        by="total_app_opens", ascending=False
    )
    user_df = user_df[user_df["brand"].notna()].copy()
    user_df["brand"] = user_df["brand"].astype(str).str.strip()
    user_df = user_df[~user_df["brand"].str.lower().isin(["unknown", "unknown brand", "n/a", "na", "")] )

    user_df["number_of_registered_user"] = pd.to_numeric(
        user_df["number_of_registered_user"], errors="coerce"
    ).fillna(0)
    user_df["total_app_opens"] = pd.to_numeric(
        user_df["total_app_opens"], errors="coerce"
    ).fillna(0)

    if user_df.empty:
        st.info("No user engagement data is available yet.")
    else:
        user_df["avg_app_opens_per_user"] = (
            user_df["total_app_opens"]
            .where(user_df["number_of_registered_user"] != 0, 0)
            .div(user_df["number_of_registered_user"].replace(0, 1))
        ).round(2)

        active_brands = len(user_df)
        total_registered = int(user_df["number_of_registered_user"].sum())
        total_app_opens = int(user_df["total_app_opens"].sum())
        average_opens = round(total_app_opens / total_registered, 2) if total_registered else 0

        st.markdown("### Engagement summary")
        summary_cols = st.columns(3)
        summary_cols[0].metric("Active Brands", active_brands)
        summary_cols[1].metric("Total Registered Users", f"{total_registered:,}")
        summary_cols[2].metric("Avg App Opens/User", f"{average_opens:.2f}")

        chart_df = user_df.sort_values("avg_app_opens_per_user", ascending=False).head(10)
        st.markdown("### Top brands by average app opens per user")
        engagement_chart = px.bar(
            chart_df.sort_values("avg_app_opens_per_user"),
            x="avg_app_opens_per_user",
            y="brand",
            orientation="h",
            text="avg_app_opens_per_user",
            title="Brand Engagement Strength",
            color="avg_app_opens_per_user",
            color_continuous_scale="Blues",
            labels={
                "avg_app_opens_per_user": "Avg App Opens/User",
                "brand": "Device Brand",
            },
        )
        engagement_chart.update_traces(
            texttemplate="%{x:.2f}",
            textposition="outside",
            marker_line_color="white",
            marker_line_width=1,
            showlegend=False,
        )
        engagement_chart.update_layout(
            title_x=0.5,
            margin=dict(l=180, r=20, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(showgrid=True, gridcolor="#E5E7EB"),
            yaxis={"categoryorder": "total ascending"},
        )
        st.plotly_chart(engagement_chart, use_container_width=True)

        top_users = user_df.sort_values("avg_app_opens_per_user", ascending=False).head(3).copy()
        bottom_users = user_df.sort_values("avg_app_opens_per_user", ascending=True).head(3).copy()

        st.markdown("### Top 3 / Bottom 3 Brands")
        insight_cols = st.columns(6)
        for idx, row in enumerate(top_users.itertuples(index=False)):
            insight_cols[idx].metric(
                label=f"Top {idx + 1}: {row.brand}",
                value=f"{row.avg_app_opens_per_user:.2f}",
                delta=f"{row.total_app_opens:,} app opens",
            )
        for idx, row in enumerate(bottom_users.itertuples(index=False)):
            insight_cols[idx + 3].metric(
                label=f"Bottom {idx + 1}: {row.brand}",
                value=f"{row.avg_app_opens_per_user:.2f}",
                delta=f"{row.total_app_opens:,} app opens",
            )

elif st.session_state.selected_page == "Home":

    st.write("Welcome to the PhonePe Data Insights Engine!")
    st.markdown("""
### Welcome!

The **PhonePe Data Insights Engine** is an interactive analytics dashboard that transforms PhonePe Pulse data into meaningful business insights.

### 🎯 Objectives
- Analyze state-wise transaction performance
- Track quarter-wise transaction trends
- Explore payment category distribution
- Understand user preferences across device brands
- Identify growth opportunities across regions

### 📊 Visualizations Included
- 📈 Line Charts
- 📊 Bar Charts
- 🍩 Donut Charts

Use the **sidebar** to navigate through different analyses and explore the insights.
""")

elif st.session_state.selected_page == "Insurance":
    st.write("Showing Insurance Analysis")
    st.subheader("Insurance Analysis")
    options = st.selectbox(
        "Select Insurance Data Analysis as:",
        (
            "-- Select Analysis --",
            "Top 10 State Wise Maximum Insurance Count",
            "Top 10 State Wise Lower Insurance Count",
            "Top 10 District Wise Maximum Insurance Count",
            "Top 10 District Wise Lower Insurance Count",
            
        )
    )
    if options == "-- Select Analysis --":
        st.info("Please select an analysis option from the dropdown.")  
        st.stop()

    elif options == "Top 10 State Wise Maximum Insurance Count":

        st.write("Showing State Wise Analysis")
        insurance_df = get_top_10_state_insurance_data().sort_values(
            by="total_count", ascending=True
        )
        fig = px.bar(
            insurance_df,
            x="total_count",
            y="state",
            orientation="h",
            title="Top 10 States by Insurance Volume",
            text="total_count",
            color="total_count",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="#1D4ED8",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Insurance",
            yaxis_title="State",
            title_x=0.5,
            margin=dict(l=120, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s"),
            yaxis={"categoryorder": "total ascending"},
            showlegend=False,
            autosize=True,
        )

        st.plotly_chart(fig, use_container_width=True)

    elif options == "Top 10 State Wise Lower Insurance Count":
        st.write("Showing State Wise Analysis")
        insurance_df = get_top_10_state_lower_insurance_data().sort_values(
            by="total_count" , ascending=True
        )
        fig = px.bar(
            insurance_df,
            x="total_count",
            y="state",
            orientation="h",
            title="Top 10 States by Lower Insurance Count",
            text="total_count",
            color="total_count",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="#1D4ED8",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Insurance",
            yaxis_title="State",
            title_x=0.5,
            margin=dict(l=120, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s"),
            yaxis={"categoryorder": "total descending"},
            showlegend=False,
            autosize=True,
        )

        st.plotly_chart(fig, use_container_width=True)

    elif options == "Top 10 District Wise Maximum Insurance Count":
        st.write("Showing Payment Category Analysis")
        transaction_df = get_top_10_district_insurance_data().sort_values(
            by="total_count", ascending=True
        )
        fig = px.bar(
            transaction_df,
            x="total_count",
            y="region_name",
            orientation="h",
            title="Top 10 Districts by Maximum Insurance Count",
            text="total_count",
            color="region_name",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="white",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Transactions",
            yaxis_title="District",
            title_x=0.5,
            margin=dict(l=160, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s", showgrid=True, gridcolor="#E5E7EB"),
            yaxis={"categoryorder": "total ascending"},
            showlegend=False,
            autosize=True,
        )
        st.plotly_chart(fig, use_container_width=True)

    elif options == "Top 10 District Wise Lower Insurance Count":
        st.write("Showing Lower Insurance Count by District Analysis")
        insurance_df = get_top_10_Lower_district_insurance_data().sort_values(
            by="total_count", ascending=True
        )
        fig = px.bar(
            insurance_df,
            x="total_count",
            y="region_name",
            orientation="h",
            title="Top 10 Districts by Lower Insurance Count",
            text="total_count",
            color="region_name",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )

        fig.update_traces(
            texttemplate="%{x:~s}",
            textposition="outside",
            marker_line_color="white",
            marker_line_width=1,
            showlegend=False,
        )
        fig.update_layout(
            xaxis_title="Total Transactions",
            yaxis_title="District",
            title_x=0.5,
            margin=dict(l=120, r=40, t=70, b=40),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(tickformat="~s", showgrid=True, gridcolor="#E5E7EB"),
            yaxis={"categoryorder": "total descending"},
            showlegend=False,
            autosize=True,
        )
        st.plotly_chart(fig, use_container_width=True)
