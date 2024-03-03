import unittest
import pandas as pd
from SalesData import SalesData


class TestSalesData(unittest.TestCase):

    def test_eliminate_duplicates(self):
        data = {
            'Product': ['A', 'A', 'B', 'C', 'B'],
            'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-02'],
            'Quantity': [10, 5, 15, 8, 20],
            'Price': [100, 100, 120, 90, 120]
        }
        df = pd.DataFrame(data)
        sales_data = SalesData(df)
        sales_data.eliminate_duplicates()
        expected_df = df.drop_duplicates().dropna()
        self.assertTrue(sales_data.data.equals(expected_df))

    def test_calculate_total_sales(self):
        data = {
            'Product': ['A', 'A', 'B', 'C'],
            'Quantity': [10, 5, 15, 8],
            'Price': [100, 100, 120, 90]
        }
        df = pd.DataFrame(data)
        sales_data = SalesData(df)
        sales_data.calculate_total_sales()
        expected_df = df.assign(Total_Sales=df['Quantity'] * df['Price'])
        self.assertTrue(sales_data.data.equals(expected_df))
        with self.assertRaises(NotImplementedError):
            sales_data.calculate_total_sales()  # Simulate plotting error

    def test_analyze_sales_data(self):
        data = {
            'Product': ['A', 'A', 'B', 'C'],
            'Quantity': [10, 5, 15, 8],
            'Price': [100, 100, 120, 90]
        }
        df = pd.DataFrame(data)

        sales_data = SalesData(df)
        analysis_results = sales_data.analyze_sales_data()

        expected_best_selling_product = 'A'  # Modify as needed based on your data
        expected_month_with_highest_sales = 1  # Modify as needed based on your data
        self.assertEqual(analysis_results['best_selling_product'], expected_best_selling_product)
        self.assertEqual(analysis_results['month_with_highest_sales'], expected_month_with_highest_sales)
        with self.assertRaises(NotImplementedError):
            sales_data.analyze_sales_data()  # Simulate analysis or plot error

    def test_add_additional_values(self):
        data = {
            'Product': ['A', 'A', 'B', 'C'],
            'Quantity': [10, 5, 15, 8],
            'Price': [100, 100, 120, 90]
        }
        df = pd.DataFrame(data)
        sales_data = SalesData(df)
        analysis_results = sales_data.add_additional_values()

        # Assert expected results
        expected_minimest_selling_product = 'C'  # Modify as needed based on your data
        expected_average_sales = 95  # Modify as needed based on your data
        self.assertEqual(analysis_results['minimest_selling_product'], expected_minimest_selling_product)
        self.assertEqual(analysis_results['average_sales'], expected_average_sales)

        with self.assertRaises(NotImplementedError):
            sales_data.add_additional_values()  # Simulate analysis or plot error
