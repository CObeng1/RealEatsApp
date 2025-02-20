# Simple simulation of RealEats barcode scanner

# Simulating a small database of products with their barcode and classification
product_db = {
    '123456789012': {'name': 'Packaged Chips', 'classification': 'UPF', 'alternative': 'Homemade Roasted Potatoes'},
    '987654321098': {'name': 'Canned Soup', 'classification': 'UPF', 'alternative': 'Homemade Vegetable Soup'},
    '543216789012': {'name': 'Fresh Apple', 'classification': 'Whole Food', 'alternative': 'None'},
    '112233445566': {'name': 'Soda Drink', 'classification': 'UPF', 'alternative': 'Sparkling Water with Lemon'}
}

def scan_product(barcode):
    product = product_db.get(barcode)
    
    if product:
        print(f"Product: {product['name']}")
        print(f"Classification: {product['classification']}")
        
        if product['classification'] == 'UPF':
            print(f"Suggested Alternative: {product['alternative']}")
        else:
            print("This is a healthy choice!")
    else:
        print("Product not found in database.")

def main():
    print("Welcome to the RealEats barcode scanner simulation!")
    
    while True:
        barcode = input("\nEnter a barcode (or type 'exit' to quit): ")
        
        if barcode.lower() == 'exit':
            print("Exiting... Thank you for using RealEats!")
            break
        
        scan_product(barcode)

if __name__ == '__main__':
    main()
