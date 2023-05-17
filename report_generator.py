import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "openai","beautifulsoup4","numpy","tabulate", "pdfkit", "weasyprint","wkhtmltopdf","yfinance"])
import pdfkit
import base64
#import matplotlib.pyplot as plt
import numpy as np
#import plotly.graph_objects as go
#from plotly.io import to_image

import os
import streamlit as st
from scrape.yahoo_finance_scrape import *
from scrape.google_scrape import *
from scrape.historicaldatascrape import *
from prod.report_section import *


api_key = '6G6DT6CCRO8UWZ39'

def generate_investment_report(ticker, generate_report_section, income_statement_data, balance_sheet_data, cash_flow_data, mosaic_analysis, model ,get_price_change, get_financial_data, api_key):
    report_parts = []  # Initialize the report_parts list
    # Plot the price change
    st.write(f"Stock price of {ticker} performance compared to S&P500")
    price_change_data = get_price_change(ticker)
    st.line_chart(price_change_data)
    #st.write("Company Overview")
    #st.write(company_overview(generate_report_section, ticker, mosaic_analysis, model))
    #report_parts.append(company_overview(generate_report_section, ticker, mosaic_analysis, model))
    #st.write("Industry Analysis")
    #st.write(industry_analysis(generate_report_section, ticker, mosaic_analysis, model))
    #report_parts.append(industry_analysis(generate_report_section, ticker, mosaic_analysis, model))
    st.write("Valuation")
    income_statement_df, balance_sheet_df, cash_flow_df = display_valuation(income_statement_data, balance_sheet_data, cash_flow_data)

    st.write("Income Statement:")
    st.table(income_statement_df)
    report_parts.append(income_statement_df.to_html())

    st.write("Balance Sheet:")
    st.table(balance_sheet_df)
    report_parts.append(balance_sheet_df.to_html())

    st.write("Cash Flow Statement:")
    st.table(cash_flow_df)
    report_parts.append(cash_flow_df.to_html())
    st.write("Financial Analysis")
    st.write(financial_analysis(generate_report_section, ticker, income_statement_data, balance_sheet_data, model, get_financial_data, api_key))
    report_parts.append(financial_analysis(generate_report_section, ticker, income_statement_data, balance_sheet_data, model, get_financial_data, api_key))
    #st.write("Investment Thesis")
    #st.write(investment_thesis(generate_report_section, ticker, mosaic_analysis, model))
    #report_parts.append(investment_thesis(generate_report_section, ticker, mosaic_analysis, model))
    #st.write("Risk Analysis")
    #st.write(risk_analysis(generate_report_section, ticker, mosaic_analysis, model))
    #report_parts.append(risk_analysis(generate_report_section, ticker, mosaic_analysis, model))
    #st.write("SWOT Analysis")
    #st.write(SWOT_analysis(generate_report_section, ticker, mosaic_analysis, model))
    #report_parts.append(SWOT_analysis(generate_report_section, ticker, mosaic_analysis, model))
    #st.write("Investment Recommendations")
    #st.write(investment_recommendations_messages(generate_report_section, ticker, mosaic_analysis, model))
    #report_parts.append(investment_recommendations_messages(generate_report_section, ticker, mosaic_analysis, model))
    report = "\n".join(report_parts)
    
    # Convert report to PDF
    try:
        pdfkit.from_string(report, 'report.pdf')
    except Exception as e:
        st.write(f"Error creating PDF: {e}")

    # Check the current working directory
    cwd = os.getcwd()
    st.write(f"Current working directory: {cwd}")

    # Read the PDF file as bytes
    try:
        with open("report.pdf", "rb") as f:
            pdf_content = f.read()
    except FileNotFoundError:
        st.write("File 'report.pdf' not found")

    # Display a download button for the PDF file
    st.download_button('Download PDF', pdf_content,  'report.pdf')


def main():
    st.title("Investment Report Generator")
    openai.api_key = st.text_input("Enter the openai api key (gpt-4):")
    ticker = st.text_input("Enter the stock ticker:").upper()
    model = "gpt-4"
    
    if st.button('Generate Report'):
        
        # Scrape Yahoo Finance and Google analysis data
        yahoo_analysis = scrape_yahoo_finance_news(ticker)
        google_analysis = scrape_google_news(ticker)

        
        
        income_statement_data = pd.DataFrame(filter_last_five_years(get_financial_data(api_key, "INCOME_STATEMENT", ticker)))
        balance_sheet_data = pd.DataFrame(filter_last_five_years(get_financial_data(api_key, "BALANCE_SHEET", ticker)))
        cash_flow_data = pd.DataFrame(filter_last_five_years(get_financial_data(api_key, "CASH_FLOW", ticker)))

   
        # Generate the investment report
        report = generate_investment_report(ticker, generate_report_section, income_statement_data, balance_sheet_data, cash_flow_data, mosaic_analysis, model ,get_price_change, get_financial_data, api_key)

if __name__ == '__main__':
    main()
