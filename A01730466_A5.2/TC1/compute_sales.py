"""Program that receives two JSON files as parameters:
a catalogue of prices of products and a record for all sales,
to calculate the total cost of all sales.
"""

import sys
import json
import time


def load_json_file(file_path):
    """Load JSON data from file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as exception:
        print(f"Error loading {file_path}: {exception}")
        return None


def compute_total_cost(price_catalogue, sales_record):
    """Compute the total cost of all sales."""
    total_cost = 0
    for sale in sales_record:
        product_name = sale["Product"]
        quantity = sale["Quantity"]

        # Search for the product in the price catalogue list of dictionaries
        found = False
        for product in price_catalogue:
            if product["title"] == product_name:
                total_cost += product["price"] * quantity
                found = True
                break
        if not found:
            print(f"Product: {product_name}, not found in price catalogue.")
    return total_cost


def main():
    """Main function."""
    if len(sys.argv) != 3:
        print("python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    prices_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    # Load JSON data from corresponding files
    price_catalogue = load_json_file(prices_catalogue_file)
    if price_catalogue is None:
        sys.exit(1)

    sales_record = load_json_file(sales_record_file)
    if sales_record is None:
        sys.exit(1)

    # Compute total cost of all sales in company
    total_cost = compute_total_cost(price_catalogue, sales_record)

    # Compute time elapsed
    end_time = time.time()
    execution_time = end_time - start_time

    # Print results (total cost and execution time)
    print(f"Total cost of all sales: ${total_cost:.2f}")
    print(f"Execution time: {execution_time:.10f} seconds")

    # Write results to file SalesResults.txt
    with open("SalesResults.txt", "w", encoding='utf-8') as results_file:
        results_file.write(f"Total cost of all sales: ${total_cost:.2f}\n")
        results_file.write(f"Execution time: {execution_time:.10f} seconds\n")


if __name__ == "__main__":
    main()
