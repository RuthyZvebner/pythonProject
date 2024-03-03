import pandas as ps
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime

class MyError(Exception):
    def __init__(self, error_text, name, date, time):
        self.error_text = error_text
        self.name = name
        self.date = date
        self.time = time

    def __str__(self):
        return f"<{self.name}, {self.date}, {self.time}> {self.error_text} <{self.name}>"



class SalesData(object):
    def __init__(self, dataSet):
        self._dataSet = ps.DataFrame(dataSet)

    @property
    def dataSet(self):
        return  self._dataSet

    @dataSet.setter
    def dataSet(self, dataSet):
        self._dataSet = dataSet

    def handle_error(self, error_text):
        current_datetime = datetime.datetime.now()
        formatted_date = current_datetime.strftime('%d.%m.%y')
        formatted_time = current_datetime.strftime('%H:%M')
        error_instance = MyError(error_text, "Ruthy", formatted_date, formatted_time)
        print(error_instance)
        return error_instance

    def eliminate_duplicates(self):
        try:
            newData = self._dataSet.drop_duplicates().dropna()

            print('---eliminate_duplicates---')
            print(newData)
            return newData
        except Exception as e:
            self.handle_error(f"type error: {str(e)}")

    def calculate_total_sale(self):
        try:
            total_sales = self._dataSet.groupby("Product")["Total"].sum()
            print("---calculate_total_sale---")
            print(total_sales)
            return total_sales
        except Exception as e:
            self.handle_error(f"type error: {str(e)}")

    def calculate_total_sales_per_month(self):
        try:
            monthSum = self._dataSet.copy()
            monthSum['Date'] = ps.to_datetime(monthSum['Date'], dayfirst=True)
            monthSum['Month'] = monthSum['Date'].dt.month
            monthSum['Year'] = monthSum['Date'].dt.year
            monthSum = monthSum.groupby(['Year', 'Month'])['Total'].sum()
            print("---calculate_total_sales_per_month---")
            print(monthSum)
            return monthSum
        except Exception as e:
            self.handle_error(f"type error: {str(e)}")

    def identify_best_selling_product(self):
        try:
            best_selling_product = self._dataSet.groupby('Product')['Total'].sum().idxmax()
            print("---method_identify_best_selling_product---")
            print(best_selling_product)
            return best_selling_product
        except Exception as e:
            self.handle_error(f"type error: {str(e)}")

    def identify_month_with_highest_sales(self):
        monthly_sales = self._dataSet.copy()
        monthly_sales['Date'] = ps.to_datetime(monthly_sales['Date'], dayfirst=True)
        monthly_sales['Month'] = monthly_sales['Date'].dt.month
        max_month_sales = monthly_sales.groupby('Month')['Total'].sum()
        month_with_highest_sales = max_month_sales.idxmax()
        plt.figure(figsize=(8, 6))
        sns.barplot(x=max_month_sales.index, y=max_month_sales.values, palette='viridis')
        plt.title('Total Sales by Month')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.show()
        print("---identify_month_with_highest_sales---")
        print(month_with_highest_sales)
        return month_with_highest_sales

    def calculate_minimum_selling_product(self):
        min_selling_product = self._dataSet.groupby('Product')['Total'].sum().idxmin()
        return min_selling_product

    def calculate_average_sales(self):
        average_sales = self._dataSet['Total'].mean()
        return average_sales

    def analyze_sales_data(self):
        best_selling_product = self.identify_best_selling_product()
        month_with_highest_sales = self.identify_month_with_highest_sales()
        min_selling_product = self.calculate_minimum_selling_product()
        mean_selling_product = self.calculate_mean_quantity()
        analysis_result = {
            'best_selling_product': best_selling_product,
            'month_with_highest_sales': month_with_highest_sales,
            'min_selling_product': min_selling_product,
            'average_sales': mean_selling_product
        }
        print("---analyze_sales_data---")
        print(analysis_result)
        return analysis_result

    def calculate_cumulative_sales(self):
        data_per_product_month = self._dataSet.copy()
        data_per_product_month['Date'] = ps.to_datetime(data_per_product_month['Date'], dayfirst=True)
        data_per_product_month['Month'] = data_per_product_month['Date'].dt.month
        data_per_product_month = data_per_product_month.groupby(['Product', 'Month'])['Total'].sum()
        plt.figure(figsize=(12, 8))
        sns.lineplot(data=data_per_product_month.reset_index(), x='Month', y='Total', hue='Product', marker='o')
        plt.title('Cumulative Sales per Month')
        plt.xlabel('Month')
        plt.ylabel('Cumulative Sales')
        plt.legend(title='Product')
        plt.show()
        print("---calculate_cumulative_sales---")
        print(data_per_product_month)
        return  data_per_product_month

    def add_90_values_column(self):
        new_data = self._dataSet.copy()
        new_data['Date'] = ps.to_datetime(new_data['Date'], dayfirst=True)
        new_data['Discount'] = 0.9*new_data['Quantity']
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=new_data, x='Quantity', y='Discount', hue='Product', palette='Set2', s=100)
        plt.title('Scatter Plot of Quantity vs Discount')
        plt.xlabel('Quantity')
        plt.ylabel('Discount')
        plt.legend(title='Product')
        plt.show()
        print("---add_90_values_column---")
        print(new_data)
        return new_data

    def bar_chart_category_sum(self):
        category_sum = self._dataSet.groupby('Product')['Quantity'].sum()
        category_sum.plot(kind='bar', color='red')
        plt.title('sum of quantity per product')
        plt.xlabel('product')
        plt.ylabel('sum of quantity')
        plt.show()
        print("---bar_chart_category_sum---")

    def calculate_mean_quantity(self):
        total_array = np.array(self._dataSet['Total'])
        mean_value = np.mean(total_array)
        median_value = np.median(total_array)
        second_max_value = np.partition(total_array, -2)[-2]
        print(f"mean of total: {mean_value}")
        print(f"median of total:{median_value}")
        print(f"second max of total:{second_max_value}")
        results_dict = {
            'mean': mean_value,
            'median': median_value,
            'second max': second_max_value
        }
        sns.pairplot(self._dataSet[['Total', 'Quantity', 'Price']])
        plt.suptitle('Pair Plot of Total, Quantity, and Price', y=1.02)
        plt.show()
        print("---calculate_mean_quantity---")
        print(results_dict)
        return results_dict

    def filter_by_selling_or_and(self):
        condition_1 = (self._dataSet['Quantity'] > 5) | (self._dataSet['Quantity'] == 0)
        condition_2 = (self._dataSet['Price'] > 300) & (self._dataSet['Quantity'] < 2)
        filtered_data = self._dataSet[condition_1|condition_2]
        plt.figure(figsize=(10, 6))
        sns.countplot(data=filtered_data, x='Product', hue='Quantity', palette='viridis')
        plt.title('Count Plot of Products based on Quantity')
        plt.xlabel('Product')
        plt.ylabel('Count')
        plt.legend(title='Quantity')
        plt.show()
        print("---filter_by_selling_or_and---")
        print(filtered_data)
        return filtered_data

    def divide_by_2(self):
        new_data = self._dataSet.copy()
        new_data['BlackFridayPrice'] = new_data['Price']/2
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=new_data, x='Product', y='BlackFridayPrice', palette='pastel')
        plt.title('Box Plot of Black Friday Price per Product')
        plt.xlabel('Product')
        plt.ylabel('Black Friday Price')
        plt.show()
        print("---divide_by_2---")
        print(new_data)
        return new_data

    def calculate_stats(self, columns=None):
        if columns is None:
            columns = self._dataSet.columns
        stats = {}
        for col in columns:
            if (col in self._dataSet.columns):
                col_data = self._dataSet[col]
                if col_data.dtype.kind in 'biufc':  # Check if data type is numeric
                    col_stats = {
                        'max': col_data.max(),
                        'sum': col_data.sum(),
                        'abs': col_data.abs().sum(),
                        'cumulative_max': col_data.cummax()
                    }
                    stats[col] = col_stats
        sns.pairplot(self._dataSet[['Total', 'Quantity', 'Price']])
        plt.suptitle('Pair Plot of Total, Quantity, and Price', y=1.02)
        plt.show()
        print("---calculate_stats---")
        print(stats)
        return stats

    def generate_random_sales_and_amount(self, product_name):
        try:
            sales_count = self._dataSet[self.dataSet['Product'] == product_name]['Quantity'].sum()
            random_sales = random.randint(0, sales_count)
            max_amount = self._dataSet[(self.dataSet['Product'] == product_name) &
                                       (self._dataSet['Quantity'] == random_sales)]['Total'].max()
            print("---generate_random_sales_and_amount---")
            print(random_sales)
            print(max_amount)
            return random_sales, max_amount
        except Exception as e:
            self.handle_error(f"type error: {str(e)}")

    def print_table_info_internal(self):
        print("Original Table:")
        print(self._dataSet)
        print("First Three Rows:")
        print(self._dataSet.head(3))
        print("Last Two Rows:")
        print(self._dataSet.tail(2))
        random_row_index = random.randint(0, len(self._dataSet) - 1)
        print(f"Random Row ({random_row_index}):")
        print(self._dataSet.iloc[random_row_index])

    def iterate_numeric_values(self):
        for value in self._dataSet.select_dtypes(include='number').values.flatten():
            print(value)