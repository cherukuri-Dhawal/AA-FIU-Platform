import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="AA FIU Platform",
    layout="wide"
)

BASE_URL = "http://127.0.0.1:8000"

st.title("AA FIU Platform")

st.sidebar.title("AA FIU Platform")
st.sidebar.markdown("---")
st.sidebar.write("Financial Information User")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Dashboard",
        "Consents",
        "FI Requests",
        "Financial Data",
        "Audit Logs",
        "Create Consent",
        "Create FI Request",
        "Create Financial Data"
    ]
)

if menu == "Dashboard":

    st.header("Dashboard Summary")

    try:

        response = requests.get(
            f"{BASE_URL}/dashboard/dashboard/summary"
        )

        data = response.json()

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Consents",
                data["total_consents"]
            )

        with col2:
            st.metric(
                "Total FI Requests",
                data["total_fi_requests"]
            )

        with col3:
            st.metric(
                "Total Financial Data",
                data["total_financial_data"]
            )

        with col4:
            st.metric(
                "Total Audit Logs",
                data["total_audit_logs"]
            )

        st.divider()

        chart_df = pd.DataFrame(
            {
                "Category": [
                    "Consents",
                    "FI Requests",
                    "Financial Data",
                    "Audit Logs"
                ],
                "Count": [
                    data["total_consents"],
                    data["total_fi_requests"],
                    data["total_financial_data"],
                    data["total_audit_logs"]
                ]
            }
        )

        st.subheader("Platform Activity Overview")

        st.bar_chart(
            chart_df.set_index("Category")
        )

        csv = chart_df.to_csv(
            index=False
        )

        st.download_button(
            "Download Summary CSV",
            csv,
            file_name="dashboard_summary.csv",
            mime="text/csv"
        )

        st.success(
            "Backend Connected Successfully"
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

elif menu == "Consents":

    st.header("Consent Records")

    try:

        response = requests.get(
            f"{BASE_URL}/consents/consents/list"
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

elif menu == "FI Requests":

    st.header("FI Requests")

    try:

        response = requests.get(
            f"{BASE_URL}/fi-requests/fi-requests/list"
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

elif menu == "Financial Data":

    st.header("Financial Data")

    try:

        response = requests.get(
            f"{BASE_URL}/financial-data/financial-data/list"
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

elif menu == "Audit Logs":

    st.header("Audit Logs")

    try:

        response = requests.get(
            f"{BASE_URL}/audit-logs/audit-logs/list"
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

elif menu == "Create Consent":

    st.header("Create Consent")

    consent_request_id = st.text_input(
        "Consent Request ID"
    )

    customer_name = st.text_input(
        "Customer Name"
    )

    customer_mobile = st.text_input(
        "Customer Mobile"
    )

    status = st.selectbox(
        "Status",
        [
            "PENDING",
            "ACTIVE"
        ]
    )

    gateway_token_id = st.text_input(
        "Gateway Token ID"
    )

    if st.button("Create Consent"):

        payload = {
            "consent_request_id": consent_request_id,
            "customer_name": customer_name,
            "customer_mobile": customer_mobile,
            "status": status,
            "gateway_token_id": gateway_token_id
        }

        try:

            response = requests.post(
                f"{BASE_URL}/consents/consents/create",
                json=payload
            )

            if response.status_code == 200:

                st.success(
                    "Consent Created Successfully"
                )

                st.json(
                    response.json()
                )

            else:

                st.error(
                    response.text
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )
elif menu == "Create FI Request":

    st.header("Create FI Request")

    fi_request_id = st.text_input(
        "FI Request ID"
    )

    consent_request_id = st.text_input(
        "Consent Request ID"
    )

    fi_start_date = st.text_input(
        "Start Date"
    )

    fi_end_date = st.text_input(
        "End Date"
    )

    status = st.selectbox(
        "Status",
        [
            "PENDING",
            "COMPLETED"
        ]
    )

    if st.button("Create FI Request"):

        payload = {
            "fi_request_id": fi_request_id,
            "consent_request_id": consent_request_id,
            "fi_start_date": fi_start_date,
            "fi_end_date": fi_end_date,
            "status": status
        }

        response = requests.post(
            f"{BASE_URL}/fi-requests/fi-requests/create",
            json=payload
        )

        if response.status_code == 200:
            st.success(
                "FI Request Created Successfully"
            )
        else:
            st.error(
                response.text
            )
elif menu == "Create Financial Data":

    st.header("Create Financial Data")

    fi_data_id = st.text_input(
        "FI Data ID"
    )

    fi_request_id = st.text_input(
        "FI Request ID"
    )

    account_id = st.text_input(
        "Account ID"
    )

    account_number = st.text_input(
        "Account Number"
    )

    fi_type = st.text_input(
        "FI Type"
    )

    fip_id = st.text_input(
        "FIP ID"
    )

    if st.button("Create Financial Data"):

        payload = {
            "fi_data_id": fi_data_id,
            "fi_request_id": fi_request_id,
            "account_id": account_id,
            "account_number": account_number,
            "fi_type": fi_type,
            "fip_id": fip_id
        }

        try:

            response = requests.post(
                f"{BASE_URL}/financial-data/financial-data/create",
                json=payload
            )

            if response.status_code == 200:

                st.success(
                    "Financial Data Created Successfully"
                )

                st.json(
                    response.json()
                )

            else:

                st.error(
                    response.text
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )