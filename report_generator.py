import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4", "lxml", "tabulate","openai"])

import os
import streamlit as st
from scrape.yahoo_finance_scrape import *
from scrape.google_scrape import *
from scrape.historicaldatascrape import *
from prod.report_section import *


api_key = '6G6DT6CCRO8UWZ39'

def generate_investment_report(ticker, generate_report_section, income_statement_data, balance_sheet_data, cash_flow_data, mosaic_analysis, model):
    report_parts = []  # Initialize the report_parts list

    st.write(company_overview(generate_report_section, ticker, mosaic_analysis, model))
    st.write(industry_analysis(generate_report_section, ticker, mosaic_analysis, model))
    print("Valuation")
    income_statement_df, balance_sheet_df, cash_flow_df = display_valuation(income_statement_data, balance_sheet_data, cash_flow_data)

    st.write("Income Statement:")
    st.table(income_statement_df)

    st.write("Balance Sheet:")
    st.table(balance_sheet_df)

    st.write("Cash Flow Statement:")
    st.table(cash_flow_df)
    st.write(financial_analysis(generate_report_section, ticker, income_statement_data, balance_sheet_data, model))
    st.write(investment_thesis(generate_report_section, ticker, mosaic_analysis, model))
    st.write(risk_analysis(generate_report_section, ticker, mosaic_analysis, model))
    st.write(SWOT_analysis(generate_report_section, ticker, mosaic_analysis, model))
    st.write(investment_recommendations_messages(generate_report_section, ticker, mosaic_analysis, model))

    report = "\n".join(report_parts)
    return report


def main():
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
    

if __name__ == '__main__':
    main()
