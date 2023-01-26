
import openpyxl

file = openpyxl.load_workbook('inventory.xlsx')

product_details = file['Sheet1']

products_company = {}
products_cost_per_company = {}
unit_product_price = {}


for product_row in range(2, product_details.max_row + 1):
    # Total Company
    company_name = product_details.cell(product_row, 4).value
    if company_name in products_company:
        products_company[company_name] = products_company.get(company_name) + 1
    else:
        products_company[company_name] = 1

    # Total Cost per Company
    product_quantity = product_details.cell(product_row, 2).value
    product_price = product_details.cell(product_row, 3).value

    if company_name in products_cost_per_company:
        products_cost_per_company[company_name] = products_cost_per_company.get(company_name) +\
                                                  (product_quantity * product_price)
    else:
        products_cost_per_company[company_name] = product_quantity * product_price

    # unit_price = product_price / product_quantity
    unit_product_price[product_row] = product_price / product_quantity


print(products_company)
print(products_cost_per_company)
print(sum(products_cost_per_company.values()))
print(unit_product_price)


