# shopping_list = []
# add_item = str(input("L"))
# remove_item = str(input("i"))
def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View item")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Add your item: ").strip()
            shopping_list.append(item)
        elif choice == '2':
            item = input("Remove an item: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Not found")
        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your Shopping List is Empty")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()