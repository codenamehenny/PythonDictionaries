#2. Python Programming Challenges for Customer Service Data Handling
#Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.
#Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#Implement functions to:
#-Open a new service ticket.
#-Update the status of an existing ticket.
#-Display all tickets or filter by status.
#Initialize with some sample tickets and include functionality for additional ticket entry.

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# open new service ticket section
def add_ticket(customer_value, issue_value):
    ticket_key = max(service_tickets.keys())
    ticket_number = int(ticket_key.replace("Ticket",'')) # removing string so we can update the ticket number once added
    new_ticket_number = ticket_number + 1
    new_ticket_number = f"Ticket00{new_ticket_number}"
    status_open = "open"
    service_tickets.update({new_ticket_number: {"Customer": customer_value, "Issue": issue_value, "Status": status_open}})
    return print(f"\n{new_ticket_number} successfully added. Returning to main menu")

#this function iterates over the outer and inner dictionaries
def display_tickets():
    for outer_dictionary, inner_dictionary in service_tickets.items():
        print(f"\nDetails of {outer_dictionary}:")
        for key, value in inner_dictionary.items():
            print(f"{key}: {value}")
    #print("\nReturning to menu")

#ticket tracker function
def data_handling_menu():
    while True:
        print("Welcome to the customer service ticket tracker! Choose an option to get started.")
        print("1. Open a new service ticket")
        print("2. Update the status of an existing ticket")
        print("3. Display all tickets")
        print("4. Quit")
        option = int(input("Enter option number: "))
        try:
            if option == 1:
                customer_value = input("What's the customer's name? ")
                issue_value = input("What's the issue? ")
                add_ticket(customer_value, issue_value)
            elif option == 2:  # updates a status to closed
                ticket_input = input("Enter ticket number to update status in the format 'TicketXXX': ")
                service_tickets[ticket_input].update({"Status": "closed"})
                print(f"\n{ticket_input} status has is now closed. Returning to menu")
            elif option == 3:
                display_tickets()
            elif option == 4:
                print("Quitting...")
                break
        except ValueError:
            print("Looks like a valid option number wasn't selected. Please enter number a number between 1-4.\n")
        except KeyError:
            print("Invalid format. Please enter the ticket number as 'TicketXXX'")
        finally:
            print("\nThanks for using the ticket tracker\n")

data_handling_menu()