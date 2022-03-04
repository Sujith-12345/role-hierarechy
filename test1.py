root_role_name = str(input("Enter root role name : "))
all_sub_role = []
all_user_details = []
def hyrachyFunc():
    global reporting_role,sub_role,del_rol,user_name,user_role
    if root_role_name == "CEO" or "ceo":
        print("Opretions : \n1. Add Sub Role.\n2. Display Roles.\n3. Delete Role.\n4. Add Users.\n5. Display Users.")
    operation_num = input("Operation to be performed : ")
    if operation_num == "1":
        sub_role = input("Enter sub role name : ")
        all_sub_role.append(sub_role)
        reporting_role = input("Enter reporting to role name : ")
    if operation_num == "2":
        print(root_role_name ," ".join(all_sub_role))
    if operation_num == "3":
        del_rol = input("Enter the role to be deleted❗ : ")
        all_sub_role.remove(del_rol)
    if operation_num == "4":
        user_name = input("Enter User Name : ")
        user_role = input("Enter Role : ")
        all_user_details.append(user_name+ " - " +user_role)
    if operation_num == "5":
        print("\n".join(all_user_details))    

for x in range(6):
    hyrachyFunc()
