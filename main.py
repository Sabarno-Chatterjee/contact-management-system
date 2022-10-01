#def rolodex()

name = []
contact = []
postal_address = []
email = []
company = []
membership_status = []

is_continue = 1

while is_continue:
    name.append(input("Name: "))
    contact.append(input("Contact Number: "))
    postal_address.append(input("Address: "))
    email.append(input("Email: "))
    company.append(input("Company: "))
    membership_status.append(input("Membership status: "))

    if (input("Do you want to enter more data, Type 'Y' or 'N'").lower()) == "n":
        is_continue = 0

print(name, contact, postal_address, email, company, membership_status)