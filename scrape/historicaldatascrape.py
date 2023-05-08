import os
import requests
import pandas as pd
from datetime import datetime
from tabulate import tabulate

def get_financial_data(api_key, function, ticker):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": function,
        "symbol": ticker,
        "apikey": api_key,
    }
    response = requests.get(base_url, params=params)
    return response.json()

def filter_last_five_years(data):
    if 'annualReports' not in data:
        return {}

    current_year = datetime.now().year
    five_years_ago = current_year - 5
    filtered_data = [report for report in data['annualReports'] if int(report['fiscalDateEnding'].split("-")[0]) >= five_years_ago]
    return filtered_data

# Example usage

api_key = '6G6DT6CCRO8UWZ39'


def display_valuation(income_statement_data, balance_sheet_data, cash_flow_data):
    
    # Reverse the income statement data, balance sheet data, and cash flow data
    income_statement_data = list(reversed(income_statement_data))
    balance_sheet_data = list(reversed(balance_sheet_data))
    cash_flow_data = list(reversed(cash_flow_data))

    headers = ["Metric"] + [report['fiscalDateEnding'].split("-")[0] for report in income_statement_data] + [f"Forecast {i+1}" for i in range(2)]
    metrics = ["Total Revenue", "Gross Profit", "Operating Income", "Net Income"]
    balance_sheet_metrics = ["Total Assets", "Total Liabilities", "Current Assets", "Non-Current Assets", "Current Liabilities", "Non-Current Liabilities"]
    cash_flow_metrics = [
        "Operating Cash Flow",
        "Cash Flow from Financing",
        "Cash Flow from Investment",
        "Free Cash Flow",
    ]

    # Mapping dictionary for accessing values from the reports
    metric_to_key = {
        "Total Revenue": "totalRevenue",
        "Gross Profit": "grossProfit",
        "Operating Income": "operatingIncome",
        "Net Income": "netIncome",
    }

    balance_sheet_metric_to_key = {
        "Total Assets": "totalAssets",
        "Total Liabilities": "totalLiabilities",
        "Current Assets": "totalCurrentAssets",
        "Non-Current Assets": "totalNonCurrentAssets",
        "Current Liabilities": "totalCurrentLiabilities",
        "Non-Current Liabilities": "totalNonCurrentLiabilities",
    }

    cash_flow_metric_to_key = {
        "Operating Cash Flow": "operatingCashflow",
        "Cash Flow from Financing": "cashflowFromFinancing",
        "Cash Flow from Investment": "cashflowFromInvestment",
    }

    # Extract the financial data from the income statement
    past_data = {metric: [] for metric in metrics}
    for report in income_statement_data:
        for metric in metrics:
            past_data[metric].append(float(report[metric_to_key[metric]]))

    # Extract the balance sheet data
    balance_sheet_past_data = {metric: [] for metric in balance_sheet_metrics}
    for report in balance_sheet_data:
        for metric in balance_sheet_metrics:
            key = balance_sheet_metric_to_key[metric]
            value = float(report[key]) if key in report else 0
            balance_sheet_past_data[metric].append(value)

     # Extract the financial data for the cash flow statement
    cash_flow_past_data = {metric: [] for metric in cash_flow_metrics[:-1]}  # Exclude "Free Cash Flow"
    for report in cash_flow_data:
        for metric in cash_flow_metrics[:-1]:  # Exclude "Free Cash Flow"
            cash_flow_past_data[metric].append(float(report[cash_flow_metric_to_key[metric]]))

    # Calculate Free Cash Flow
    cash_flow_past_data["Free Cash Flow"] = [
        cash_flow_past_data["Operating Cash Flow"][i] +
        cash_flow_past_data["Cash Flow from Financing"][i] +
        cash_flow_past_data["Cash Flow from Investment"][i]
        for i in range(len(cash_flow_past_data["Operating Cash Flow"]))
    ]
    # Calculate forecasted future valuations using CAGR for the income statement
    for metric in metrics:
        num_years = len(past_data[metric]) - 1
        start_value = past_data[metric][0] if past_data[metric] else 0
        end_value = past_data[metric][-1] if metric in past_data and past_data[metric] else None
        if start_value == 0:
            cagr = 0
        else:
            cagr = (end_value / start_value) ** (1 / num_years) - 1

        forecasted_values = [end_value * (1 + cagr) ** (i + 1) for i in range(2)] if end_value is not None else [None] * 2
        past_data[metric].extend(forecasted_values)
        
     # Calculate forecasted future valuations using CAGR for the balance sheet
    for metric in balance_sheet_metrics:
        num_years = len(balance_sheet_past_data[metric]) - 1
        start_value = balance_sheet_past_data[metric][0] if balance_sheet_past_data[metric] else 0
        end_value = balance_sheet_past_data[metric][-1] if balance_sheet_past_data[metric] else None
        if start_value == 0:
            cagr = 0
        else:
            cagr = (end_value / start_value) ** (1 / num_years) - 1

        forecasted_values = [end_value * (1 + cagr) ** (i + 1) for i in range(2)]if end_value is not None else [None] * 2
        balance_sheet_past_data[metric].extend(forecasted_values)

    # Calculate forecasted future valuations using CAGR for the cash flow statement
    for metric in cash_flow_metrics:
        num_years = len(cash_flow_past_data[metric]) - 1
        start_value = cash_flow_past_data[metric][0] if cash_flow_past_data[metric] else 0
        end_value = cash_flow_past_data[metric][-1] if cash_flow_past_data[metric] else None
        if start_value == 0:
            cagr = 0
        else:
            cagr = (end_value / start_value) ** (1 / num_years) - 1

        forecasted_values = [end_value * (1 + cagr) ** (i + 1) for i in range(2)]if end_value is not None else [None] * 2
        cash_flow_past_data[metric].extend(forecasted_values)
    # Transpose the income statement data
    transposed_data = [[metric] + values for metric, values in past_data.items()]
    print("Income Statement Transposed Data:", transposed_data)

    # Transpose the balance sheet data
    transposed_balance_sheet_data = [[metric] + values for metric, values in balance_sheet_past_data.items()]
    print("Balance Sheet Transposed Data:", transposed_balance_sheet_data)

    # Transpose the cash flow statement data
    transposed_cash_flow_data = [[metric] + values for metric, values in cash_flow_past_data.items()]
    print("Cash Flow Statement Transposed Data:", transposed_cash_flow_data)

    # Display the income statement data in a tabulated format
    print("Income Statement:")
    #print(tabulate(transposed_data, headers=headers, tablefmt="grid"))


    # Display the balance sheet data in a tabulated format
    print("\nBalance Sheet:")
    #print(tabulate(transposed_balance_sheet_data, headers=headers, tablefmt="grid"))


    # Display the cash flow statement data in a tabulated format
    print("\nCash Flow Statement:")
    print("Headers length:", len(headers))
    print("Transposed data length:", len(transposed_data[0]))
    print("Transposed balance sheet data length:", len(transposed_balance_sheet_data[0]))
    print("Transposed cash flow data length:", len(transposed_cash_flow_data[0]))

    #print(tabulate(transposed_cash_flow_data, headers=headers, tablefmt="grid"))
    income_statement_str = "Income Statement:\n" + tabulate(transposed_data, headers=headers, tablefmt="grid")
    balance_sheet_str = "\nBalance Sheet:\n" + tabulate(transposed_balance_sheet_data, headers=headers, tablefmt="grid")
    cash_flow_str = "\nCash Flow Statement:\n" + tabulate(transposed_cash_flow_data, headers=headers, tablefmt="grid")
    # Create DataFrames for each financial statement
    income_statement_df = pd.DataFrame(transposed_data, columns=headers)
    balance_sheet_df = pd.DataFrame(transposed_balance_sheet_data, columns=headers)
    cash_flow_df = pd.DataFrame(transposed_cash_flow_data, columns=headers)

    return income_statement_df, balance_sheet_df, cash_flow_df

