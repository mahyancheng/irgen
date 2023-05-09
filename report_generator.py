import subprocess
import sys
import pdfkit
import base64

subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4", "lxml", "tabulate", "openai", "pdfkit", "weasyprint"])

import os
import streamlit as st
from scrape.yahoo_finance_scrape import *
from scrape.google_scrape import *
from scrape.historicaldatascrape import *
from prod.report_section import *


api_key = '6G6DT6CCRO8UWZ39'

def generate_investment_report(ticker, generate_report_section, income_statement_data, balance_sheet_data, cash_flow_data, mosaic_analysis, model):
    report_parts = []  # Initialize the report_parts list
    st.write("Company Overview")
    st.write(company_overview(generate_report_section, ticker, mosaic_analysis, model))
    st.write("Industry Analysis")
    st.write(industry_analysis(generate_report_section, ticker, mosaic_analysis, model))
    print("Valuation")
    income_statement_df, balance_sheet_df, cash_flow_df = display_valuation(income_statement_data, balance_sheet_data, cash_flow_data)

    st.write("Income Statement:")
    st.table(income_statement_df)

    st.write("Balance Sheet:")
    st.table(balance_sheet_df)

    st.write("Cash Flow Statement:")
    st.table(cash_flow_df)
    st.write("Financial Analysis")
    st.write(financial_analysis(generate_report_section, ticker, income_statement_data, balance_sheet_data, model))
    st.write("Investment Thesis")
    st.write(investment_thesis(generate_report_section, ticker, mosaic_analysis, model))
    st.write("Risk Analysis")
    st.write(risk_analysis(generate_report_section, ticker, mosaic_analysis, model))
    st.write("SWOT Analysis")
    st.write(SWOT_analysis(generate_report_section, ticker, mosaic_analysis, model))
    st.write("Investment Recommendations")
    st.write(investment_recommendations_messages(generate_report_section, ticker, mosaic_analysis, model))

    report = "\n".join(report_parts)

    # Convert report to PDF
    pdfkit.from_string(report, 'out.pdf')

    # Create download link
    with open('out.pdf', 'rb') as f:
        pdf = f.read()

    b64 = base64.b64encode(pdf).decode()

    href = f'<a href="data:application/octet-stream;base64,{b64}">Download PDF File</a>'
    st.markdown(href, unsafe_allow_html=True)

    return report


def main():
    st.title("Investment Report Generator")
    openai.api_key = st.text_input("Enter the openai api key:")
    ticker = st.text_input("Enter the stock ticker:").upper()
    model = "gpt-4"
    
    # Scrape Yahoo Finance and Google analysis data
    yahoo_analysis = scrape_yahoo_finance_news(ticker)
    google_analysis = scrape_google_news(ticker)

    income_statement_data = filter_last_five_years(get_financial_data(api_key, "INCOME_STATEMENT", ticker))
    balance_sheet_data = filter_last_five_years(get_financial_data(api_key, "BALANCE_SHEET", ticker))
    cash_flow_data = filter_last_five_years(get_financial_data(api_key, "CASH_FLOW", ticker))

   
    # Generate the investment report
    generate_investment_report(ticker, generate_report_section, income_statement_data, balance_sheet_data, cash_flow_data, mosaic_analysis, model)
    

if__name__ == '__main__':
    main()

