import pandas as reader

class CustomerDataReader:
    
    def __init__(self, resource_path):
        self.resource_path = resource_path

    def read_customer_data(self):
        print("Reading data...")
        customer_data = reader.read_excel(self.resource_path, engine="openpyxl")
        return customer_data