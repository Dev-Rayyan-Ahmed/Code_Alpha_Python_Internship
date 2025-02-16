import yfinance as yf
import tkinter as tk
from tkinter import ttk

#DIct: (Ticker: [Shares, Buy Price])
portfolio = {
    "AAPL": [10, 220],
    "GOOGL": [5, 200],
    "TSLA": [8, 330],
    "MSFT": [7, 390]
}

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")["Close"].iloc[-1]

def update_portfolio():
    for row in tree.get_children():
        tree.delete(row)

    total_value = 0
    total_profit_loss = 0

    for ticker, (shares, buy_price) in portfolio.items():
        current_price = get_stock_price(ticker)
        value = current_price * shares
        profit_loss = (current_price - buy_price) * shares
        total_value += value
        total_profit_loss += profit_loss

        status = "Gain" if profit_loss > 0 else "Loss"
        tree.insert("", "end", values=(ticker, shares, f"${buy_price:.2f}", f"${current_price:.2f}", f"${value:.2f}", f"${profit_loss:.2f}", status))

    total_label.config(text=f"Total Portfolio Value: ${total_value:.2f}")
    if total_profit_loss > 0:
        profit_label.config(bg = "Light Green")
    else:
        profit_label.config(bg = "lightcoral")
    profit_label.config(text=f"Total Profit/Loss: ${total_profit_loss:.2f} ({'Gain' if total_profit_loss > 0 else 'Loss'})")

# Create GUI window
root = tk.Tk()
root.title("Portfolio Tracker")
root.geometry("700x400")

# Table Headers
columns = ("Ticker", "Shares", "Buy Price", "Current Price", "Total Value", "Profit/Loss", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)
tree.pack(pady=10)

# Labels for total portfolio value and profit/loss
total_label = tk.Label(root, text="Total Portfolio Value: $0.00", font=("Arial", 12, "bold"))
total_label.pack()
profit_label = tk.Label(root, text="Total Profit/Loss: $0.00", font=("Arial", 12, "bold"))
profit_label.pack(pady = 5)

# Refresh Button
refresh_button = tk.Button(root, text="Refresh Data", command=update_portfolio, font=("Arial", 12, "bold"))
refresh_button.pack(pady=10)

# Initial Data Load
update_portfolio()

# Run GUI
root.mainloop()
