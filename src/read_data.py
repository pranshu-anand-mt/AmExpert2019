# Load the Pandas libraries with alias 'pd'
import pandas as pd
import os


def load_data():
    current_file = os.path.abspath(os.path.dirname(__file__))

    csv_filename = os.path.join(current_file, '../training_data/campaign_data.csv')
    campaign_data = pd.read_csv(csv_filename)

    csv_filename = os.path.join(current_file, '../training_data/coupon_item_mapping.csv')
    coupon_item_mapping_data = pd.read_csv(csv_filename)

    csv_filename = os.path.join(current_file, '../training_data/customer_demographics.csv')
    customer_demographics_data = pd.read_csv(csv_filename)

    csv_filename = os.path.join(current_file, '../training_data/customer_transaction_data.csv')
    customer_transaction_data = pd.read_csv(csv_filename)

    csv_filename = os.path.join(current_file, '../training_data/item_data.csv')
    item_data = pd.read_csv(csv_filename)

    csv_filename = os.path.join(current_file, '../training_data/train.csv')
    train_data = pd.read_csv(csv_filename)

    return campaign_data, coupon_item_mapping_data, customer_demographics_data, \
           customer_transaction_data, item_data, train_data


def main():
    campaign_data, coupon_item_mapping_data, customer_demographics_data, \
    customer_transaction_data, item_data, train_data = load_data()
    campaign_data.columns.values


    # # Preview the first 5 lines of the loaded test_data
    # print(campaign_data.head())
    # print(coupon_item_mapping_data.head())
    # print(customer_demographics_data.head())
    # print(customer_transaction_data.head())
    # print(item_data.head())
    # print(train_data.head())


if __name__ == '__main__':
    main()
    import matplotlib.pyplot as plt

    plt.scatter([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()

