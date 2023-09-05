#Ishita Garg
#e22cseu1045
class EmployeeTable:
    def __init__(self):
        self.records = [
            {'Employee ID': '161E90', 'Name': 'Raman', 'Age': 41, 'Salary (PM)': 56000},
            {'Employee ID': '161F91', 'Name': 'Himadri', 'Age': 38, 'Salary (PM)': 67500},
            {'Employee ID': '161F99', 'Name': 'Jaya', 'Age': 51, 'Salary (PM)': 82100},
            {'Employee ID': '171E20', 'Name': 'Tejas', 'Age': 30, 'Salary (PM)': 55000},
            {'Employee ID': '171G30', 'Name': 'Ajay', 'Age': 45, 'Salary (PM)': 44000}
        ]

    def search_records(self, parameter, value):
        results = []
        for record in self.records:
            if parameter == '1':
                if record['Age'] == value:
                    results.append(record)
            elif parameter == '2':
                if value.lower() in record['Name'].lower():
                    results.append(record)
            elif parameter == '3':
                operator = input("Enter the operator (>, <, >=, <=): ")
                if operator == '>' and record['Salary (PM)'] > value:
                    results.append(record)
                elif operator == '<' and record['Salary (PM)'] < value:
                    results.append(record)
                elif operator == '>=' and record['Salary (PM)'] >= value:
                    results.append(record)
                elif operator == '<=' and record['Salary (PM)'] <= value:
                    results.append(record)
        return results

# data
    def print_records(self, records):
        if not records:
            print("No records found.")
        else:
            print("Search Results:")
            for record in records:
                print(f"Employee ID: {record['Employee ID']}, Name: {record['Name']}, Age: {record['Age']}, Salary (PM): {record['Salary (PM)']}")

def main():
    table = EmployeeTable()
    print("Employee Table Data:")
    table.print_records(table.records)

    while True:
        print('ISHITA GARG')
        print('E22CSEU1045')

        print("\nSearch Options:")
        print("1. Age")
        print("2. Name")
        print("3. Salary")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '4':
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please select a valid option.")
            continue

        search_param = choice
        search_value = input("Enter the search value: ")

        search_results = table.search_records(search_param, search_value)
        table.print_records(search_results)

if __name__ == "__main__":
    main()
    
