
import openpyxl

file = openpyxl.load_workbook('inventory.xlsx')

product_details = file['Sheet1']

products_company = {}

for product_row in range(2, product_details.max_row + 1):
    company_name = product_details.cell(product_row, 4).value
    if company_name in products_company:
        products_company[company_name] = products_company.get(company_name) + 1
    else:
        products_company[company_name] = 1



print(products_company)



