class Product:
    def __init__(self, name):
        self.name = name
        self.next = None
       

class ProductList:
    def __init__(self):
        self.head = None
       
    def add(self, product):
        product=Product(name)
        if self.head is None:
            self.head = product
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = product

    def sort_alphabetically(self):
        """Sort the products alphabetically by name."""
        sorted_list = None
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sorted_insert(self, head, product):
        """Insert the product into the sorted list."""
        if head is None or head.name >= product.name:
            product.next = head
            head = product
        else:
            current = head
            while current.next is not None and current.next.name < product.name:
                current = current.next
            product.next = current.next
            current.next = product
        return head

    def PrintList(self):
        """Print the names of all products in the list.Display msg if user fails to enter correct product list format and exits."""
        current = self.head
        if current is None:
            print(f"\n Product List is empty. Run the app and try again.")
        else:
            print(f"\nThe following products are registered(sorted alphabetically):\n")
            while current is not None:           
                print(f"* {current.name.upper()}")
                current = current.next

# Create an empty product list
pl = ProductList()

# Continuously prompt the user for product names 
while True:
    name = input("Enter product name and number (Type 'exit' to quit): ")
    if name.lower() == "exit":
        break
    
    if name.strip() == "":
        print("ERROR: Product list can not be empty.")
    if "-" in name:
        product_name,product_number=name.split("-")
        try:    
            product_number=int(product_number)
        except ValueError:
            print("ERROR: Type only product numbers. ")
            continue
        if 200 <= product_number <= 500 and product_name.isalpha():
                pl.add(Product(name))
        else:
            print("ERROR: Product number must be between 200 and 500.And product name must be only letters.")
    if "-" not in name:
        print("ERROR: Enter product name and number separated by '-'.")
       
   # else:
    #    pl.add(Product(name))

# Sort the product list alphabetically
pl.sort_alphabetically()

# print the list of products
pl.PrintList()
