import csv
from datetime import datetime

class Tool:
    def __init__(self, name, quantity, location, last_maintenance, serial_number, category):
        self.name = name
        self.quantity = quantity
        self.location = location
        self.last_maintenance = last_maintenance
        self.serial_number = serial_number
        self.category = category
    
    def __str__(self) -> str:
        """Returns a string representation of the tool."""
        return f"{self.name}({self.category}): {self.quantity} in {self.location}, Serial: {self.serial_number},Last Maintenance: {self.last_maintenance}"

class Inventory:
    def __init__(self):
        """Initializes an empty inventory with a dictionary for efficient lookup by serial number."""
        self.tools = {}
    
    def add_tool(self, tool):
        """Adds a new tool to the inventory."""
        self.tools[tool.serial_number] = tool  # Use serial number as the key in the dictionary
        print(f"Added tool: {tool.name}")

    def remove_tool(self, serial_number):
        """Removes a tool from the inventory by its serial number."""
        if serial_number in self.tools:
            del self.tools[serial_number]
            print(f"Removed tool with serial number: {serial_number}")
        else:
            print(f"Tool with serial number {serial_number} not found.")

    def update_tool(self, serial_number, name=None, quantity=None, location=None, last_maintenance=None, category=None):
        """Updates the details of an existing tool by its serial number."""
        tool = self.tools.get(serial_number)
        if tool:
            if name:
                tool.name = name
            if quantity:
                tool.quantity = quantity
            if location:
                tool.location = location
            if last_maintenance:
                tool.last_maintenance = last_maintenance
            if category:
                tool.category = category
            print(f"Updated tool with serial number: {serial_number}")
        else:
            print(f"Tool with serial number {serial_number} not found.")

    def generate_report(self):
        """Generates a CSV report of all tools in the inventory."""
        with open('inventory_report.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Quantity', 'Location', 'Last Maintenance', 'Serial Number', 'Category'])
            for tool in self.tools.values():
                writer.writerow([tool.name, tool.quantity, tool.location, tool.last_maintenance, tool.serial_number, tool.category])
        print("Report generated: inventory_report.csv")

class InventoryManager:
    def __init__(self):
        """Initializes the inventory manager."""
        self.inventory = Inventory()

    def run(self):
        """Runs the inventory management system."""
        while True:
            print("\nOptions: 1) Add Tool 2) Remove Tool 3) Update Tool 4) Generate Report 5) Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_tool()
            elif choice == '2':
                self.remove_tool()
            elif choice == '3':
                self.update_tool()
            elif choice == '4':
                self.inventory.generate_report()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please try again.")
    
    
    def add_tool(self):
        """Prompts the user to add a new tool."""
        name = input("Enter tool name: ")
        quantity = int(input("Enter quantity: "))
        location = input("Enter location: ")
        last_maintenance = input("Enter last maintenance date (YYYY-MM-DD): ")
        serial_number = input("Enter serial number: ")
        category = input("Enter category: ")
        new_tool = Tool(name, quantity, location, last_maintenance, serial_number, category)
        self.inventory.add_tool(new_tool)

    def remove_tool(self):
        """Prompts the user to remove a tool by its serial number."""
        serial_number = input("Enter serial number of the tool to remove: ")
        self.inventory.remove_tool(serial_number)

    def update_tool(self):
        """Prompts the user to update an existing tool's details."""
        serial_number = input("Enter serial number of the tool to update: ")
        name = input("Enter new name (leave blank for no change): ")
        quantity = input("Enter new quantity (leave blank for no change): ") or None
        if quantity is not None:
            quantity = int(quantity) if quantity.isdigit() else None  # Convert to int if valid
        location = input("Enter new location (leave blank for no change): ") or None
        last_maintenance = input("Enter new last maintenance date (leave blank for no change): ") or None
        category = input("Enter new category (leave blank for no change): ") or None
        self.inventory.update_tool(serial_number, name, quantity, location, last_maintenance, category)

    
if __name__ == "__main__":
    manager = InventoryManager()
    manager.run()

    


      
      
        





       



    
    
