
STOCK_PRICES = {
    "TCS": 3500,
    "INFOSYS": 1500,
    "WIPRO": 500,
    "RELIANCE": 2500,
    "HCL": 1200
}


def main():
    print("=" * 42)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 42)
    print("\nAvailable stocks and sample prices:")

    for stock, price in STOCK_PRICES.items():
        print(f"{stock}: Rs. {price:.2f} per share")

    total_investment = 0
    portfolio = []

    while True:
        stock_name = input(
            "\nEnter a stock name (or type 'done' to finish): "
        ).strip().upper()

        if stock_name == "DONE":
            break

        if stock_name not in STOCK_PRICES:
            print("Stock not found. Please choose a name from the list.")
            continue

        quantity_text = input(f"Enter quantity of {stock_name}: ").strip()

        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
        except ValueError:
            print("Please enter a valid whole-number quantity.")
            continue

        price = STOCK_PRICES[stock_name]
        investment = price * quantity
        total_investment += investment
        portfolio.append((stock_name, quantity, price, investment))

        print(f"{stock_name}: {quantity} x Rs. {price:.2f} = Rs. {investment:.2f}")

    print("\n" + "=" * 42)
    print("             YOUR PORTFOLIO")
    print("=" * 42)

    if not portfolio:
        print("No stocks were added.")
    else:
        print(f"{'Stock':<12}{'Quantity':>10}{'Price':>10}{'Investment':>14}")
        print("-" * 46)
        for stock, quantity, price, investment in portfolio:
            print(f"{stock:<12}{quantity:>10}{price:>10.2f}{investment:>14.2f}")
        print("-" * 46)
        print(f"{'TOTAL INVESTMENT':<32}Rs. {total_investment:.2f}")

    print("\nNote: The prices are sample values entered in the program, not live prices.")
    print("Thank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
