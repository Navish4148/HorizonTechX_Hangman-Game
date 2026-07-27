import csv

STOCK_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 140.0,
    "AMZN": 175.0,
    "MSFT": 400.0,
}

def run_portfolio_tracker():
    my_portfolio = []
    total_portfolio_value = 0.0

    print("\n--- Stock Portfolio Tracker ---")
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))

    while True:
        ticker = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()

        if ticker == "DONE":
            break

        if ticker not in STOCK_PRICES:
            print(f"Sorry, '{ticker}' isn't in our price database.")
            continue

        raw_quantity = input(f"How many shares of {ticker} do you own? ").strip()

        if not raw_quantity.isdigit() or int(raw_quantity) <= 0:
            print("Please enter a valid whole number greater than 0.")
            continue

        quantity = int(raw_quantity)
        price = STOCK_PRICES[ticker]
        position_value = price * quantity

        total_portfolio_value += position_value

        my_portfolio.append(
            {
                "symbol": ticker,
                "shares": quantity,
                "price": price,
                "total": position_value,
            }
        )
        print(f"Added {quantity} x {ticker} (${position_value:,.2f})")

    if not my_portfolio:
        print("\nNo holdings added. Goodbye!")
        return

    print("\n" + "=" * 45)
    print("             YOUR PORTFOLIO             ")
    print("=" * 45)
    print(f"{'Stock':<10}{'Shares':<10}{'Price':<12}{'Total Value':<10}")
    print("-" * 45)

    for item in my_portfolio:
        print(
            f"{item['symbol']:<10}{item['shares']:<10}${item['price']:<11.2f}${item['total']:<10.2f}"
        )

    print("-" * 45)
    print(f"TOTAL VALUE: ${total_portfolio_value:,.2f}")
    print("=" * 45)

    print("\nSave your portfolio summary?")
    choice = input("Type 'txt', 'csv', or press Enter to skip: ").strip().lower()

    if choice == "txt":
        save_as_text(my_portfolio, total_portfolio_value)
    elif choice == "csv":
        save_as_csv(my_portfolio, total_portfolio_value)
    else:
        print("Done! Have a great day.")

def save_as_text(portfolio, total_value):
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("PORTFOLIO SUMMARY\n")
        file.write("-" * 35 + "\n")
        for item in portfolio:
            file.write(
                f"{item['symbol']}: {item['shares']} shares @ ${item['price']:.2f} = ${item['total']:.2f}\n"
            )
        file.write("-" * 35 + "\n")
        file.write(f"Total Portfolio Value: ${total_value:,.2f}\n")
    print(f"Saved to {filename}!")

def save_as_csv(portfolio, total_value):
    filename = "portfolio_summary.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Symbol", "Shares Owned", "Price Per Share", "Total Value"])
        for item in portfolio:
            writer.writerow(
                [item["symbol"], item["shares"], item["price"], item["total"]]
            )
        writer.writerow([])
        writer.writerow(["Total Portfolio Value", "", "", total_value])
    print(f"Saved to {filename}!")

if __name__ == "__main__":
    run_portfolio_tracker()