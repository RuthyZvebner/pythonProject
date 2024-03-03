import numpy as np
import pandas as ps
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from abc import ABC, abstractmethod
from docx import Document
import sys
import random
import re


class FileReaderInterface(ABC):
    @abstractmethod
    def read_file(self, file_path: str):
        pass


class CSVReader(FileReaderInterface):
    def read_file(self, file_path: str):
        try:
            return ps.read_csv(file_path)
        except Exception as e:
            print(f"Error reading CSV file {file_path}: {str(e)}")
            return None


class ExcelReader(FileReaderInterface):
    def read_file(self, file_path: str):
        try:
            return ps.read_excel(file_path)
        except Exception as e:
            print(f"Error reading Excel file {file_path}: {str(e)}")
            return None


class WordReader(FileReaderInterface):
    def read_file(self, file_path: str):
        try:
            doc = Document(file_path)
            text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
            return ps.DataFrame({'Text': [text]})
        except Exception as e:
            print(f"Error reading Word file {file_path}: {str(e)}")
            return None

class FileOperation(object):
    def __init__(self): pass

    def read_excel(self, path: str):
        x = ps.read_csv(path)
        print("---read_excel---")
        print(x)
        return x

    def save_to_excel(self, data, file_name: str):
        x = ps.DataFrame(data)
        x.to_excel(file_name)


class MyError(Exception):
    def __init__(self, error_text, name, date, time):
        self.error_text = error_text
        self.name = name
        self.date = date
        self.time = time

    def __str__(self):
        return f"<{self.name}, {self.date}, {self.time}> {self.error_text} <{self.name}>"





def print_python_version():
    print("Python version")
    print(sys.version)
    print("Version info.")
    print(sys.version_info)


def process_parameters(*args, **kwargs):
    result_dict = {}
    print("---process_parameters---")
    for arg in args:
        if isinstance(arg, (int, float)):
            print(arg)
        elif isinstance(arg, str) and arg.startswith("VALUE"):
            key, value = arg.split(" ")
            result_dict[key] = value
    print(result_dict)
    return result_dict

def read_users_to_array():
    usernames_file_path = "UsersName.txt"
    usernames = []
    if os.path.exists(usernames_file_path):
        with open(usernames_file_path, 'r') as file:
            usernames = [line.strip() for line in file]
    return usernames

def read_usernames_to_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


def get_emails(file_path):
    with open(file_path, 'r') as file:
        emails = [line.strip() for line in file.readlines()]
    return emails

class SmartArray:
    def __init__(self):
        self.usernames = read_users_to_array()

    def get_subset(self):
        total_users = len(self.usernames)
        subset_size = int(total_users * 10 / 100)
        return self.usernames[subset_size:]


def get_usernames_generator():
    usernames_generator = read_usernames_to_generator('UserName.txt')
    return usernames_generator


def get_users_without_10_percent():
    users = SmartArray()
    usernames_array = users.get_subset()
    print(usernames_array)
    return usernames_array


def get_even_lines_users():
    users_to_even=read_users_to_array()
    even_users = [user for index, user in enumerate(users_to_even, 1) if index % 2 == 0]
    print(even_users)
    return even_users

def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_pattern, email):
        return True
    else:
        return False


def read_and_validate_emails(file_path):
    with open(file_path, 'r') as file:
        emails = [line.strip() for line in file.readlines()]
    isallvalid = True
    for email in emails:
        if not validate_email(email):
            print(f'Invalid Email: {email}')
            isallvalid =False
    return isallvalid


def filter_gmail_emails(emails):
    gmail_emails = [email for email in emails if email.endswith('@gmail.com')]
    print(gmail_emails)
    return gmail_emails


def is_username_in_mail(emails, usernames):
    email_info_list = []
    for email, username in zip(emails, usernames):
        has_username = username.lower() in email.lower().split('@')[0]
        email_info = {
            'email': email,
            'has_username': has_username
        }
        email_info_list.append(email_info)
    print(email_info_list)
    return email_info_list


def check_name_and_count_A(name,users):
        ascii_value = [ord(char) for char in name]
        binary_value = ' '.join(format(ord(char), 'b') for char in name)
        decimal_value = ' '.join(str(ord(char)) for char in name)

        ascii_string = ''.join(chr(ascii_val) for ascii_val in ascii_value)
        binary_string = ''.join(chr(int(binary_val, 2)) for binary_val in binary_value.split())
        decimal_string = ''.join(chr(int(decimal_val)) for decimal_val in decimal_value.split())
        is_appear= name in users
        count_A = name.count('A')
        print(f"countA: {count_A}")
        print(f"is user name appear: {is_appear}")
        return is_appear,count_A


def convert_to_upper(users):
    upper_list=[user[0].upper()+user[1:] for user in users]
    print(upper_list)
    return upper_list


def calculate_payment(team_members):
    total_payment = 0
    for i, member in enumerate(team_members):
        if (i + 1) % 8 == 0:
            total_payment += 200
        elif i > 7 and (i + 1) % 8 == len(team_members) % 8:
            total_payment += 50
    return total_payment
    return total_payment
    print("Total payment:", total_payment)



if __name__ == '__main__':
    file_operaion = FileOperation()
    read = file_operaion.read_excel("YafeNof.csv")
    data = {'name': ['ruthy', 'tami', 'dassi', 'chaya', 'shulamit', 'bati', 'ruthy'], 'age': [19, 12, 12, 12, 12, 13, 34]}
    #file_operaion.save_to_excel("YafeNof.csv","newExcel.xlsx")
    sales_data = SalesData(read)
    '''
    print(sales_data)
    
    sales_data.calculate_total_sale()
    sales_data.identify_best_selling_product()
    sales_data.calculate_total_sales_per_month()
    sales_data.identify_month_with_highest_sales()
    sales_data.analyze_sales_data()
    sales_data.calculate_cumulative_sales()
    sales_data.add_90_values_column()
    sales_data.bar_chart_category_sum()
    sales_data.calculate_mean_quantity()
    sales_data.filter_by_selling_or_and()
    sales_data.divide_by_2()
    sales_data.calculate_stats()
    sales_data.generate_random_sales_and_amount('Chumash')
    file_path='UsersEmail.txt'
    users= read_users_to_array()
    emails=get_emails(file_path)
    print(read_users_to_array())
    get_users_without_10_percent()
    get_even_lines_users()
    read_and_validate_emails('UsersEmail.txt')
    filter_gmail_emails(get_emails(file_path))
    is_username_in_mail(emails,users)
    #name=input("enter your name")
    check_name_and_count_A('Chana',users)
    convert_to_upper(users)
    print_python_version()
    process_parameters(42, "Hello", "VALUE_NAME John", 3.14, "VALUE_AGE 25", "World")
    sales_data.print_table_info_internal()
    sales_data.iterate_numeric_values()
    '''
    sales_data.eliminate_duplicates()
