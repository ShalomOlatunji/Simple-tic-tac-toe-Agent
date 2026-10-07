"""Create the Matplotlib visualizations required by the assignment."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_FILE = Path(__file__).with_name("company_sales_data.csv")


def create_visualizations():
    """Read the sales data and create the required charts."""
    sales_data = pd.read_csv(DATA_FILE)

    months = sales_data["month_number"]
    total_profit = sales_data["total_profit"]

    # Exercise 1: total profit for every month using a line plot.
    plt.figure(figsize=(8, 5))
    plt.plot(
        months,
        total_profit,
        color="red",
        marker="o",
        linestyle="--",
        linewidth=2,
        label="Total profit"
    )
    plt.title("Company Profit by Month")
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit")
    plt.xticks(months)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("total_profit_by_month.png")
    plt.show()

    # Exercise 2: bathing soap and facewash using two subplots.
    figure, axes = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

    axes[0].plot(
        months,
        sales_data["bathingsoap"],
        color="black",
        marker="o",
        linewidth=2
    )
    axes[0].set_title("Bathing Soap Sales")
    axes[0].set_ylabel("Units Sold")
    axes[0].grid(True, linestyle=":", alpha=0.6)

    axes[1].plot(
        months,
        sales_data["facewash"],
        color="blue",
        marker="o",
        linewidth=2
    )
    axes[1].set_title("Facewash Sales")
    axes[1].set_xlabel("Month Number")
    axes[1].set_ylabel("Units Sold")
    axes[1].grid(True, linestyle=":", alpha=0.6)

    figure.suptitle("Bathing Soap and Facewash Sales")
    figure.tight_layout()
    figure.savefig("bathing_soap_facewash_subplots.png")
    plt.show()


if __name__ == "__main__":
    create_visualizations()
