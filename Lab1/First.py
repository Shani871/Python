

product_names = ["MicroPhone", "Upgrades", "Limited"]
sk =[]
for product in product_names:
    sk.append(len(product))
print(sk)

product_names = ["dell", "apple", "powerbi"]
productName = []

for prod in product_names:
    productName.append(prod.upper())
print(productName)
# Product descriptions
product_description = "Amazing sales in this season"
product_description2 = "Clearance of sales"
product_description3 = "Today sales is good"

# Combine all product descriptions into a single string
all_products_des = product_description + " " + product_description2 + " " + product_description3

# Count occurrences of the word 'sales' (case insensitive)
cout_sales = all_products_des.lower().count("sales")
print(cout_sales)

product_des1= "This shirt comes in red and blue"
product_des2 = "Red roes for your love"

product_des1 = product_des1.replace("red","Green")
product_des2  = product_des2.replace("Red","Green")

print(product_des1)
print(product_des2)