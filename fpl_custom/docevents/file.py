import frappe

# Get users in which supplier role is not assigned
@frappe.whitelist()
def get_users():
    # check supplier role users
    data = frappe.db.sql('''select u.name from `tabUser` u 
                        inner join `tabHas Role` hr 
                        on hr.parent = u.name 
                        where hr.role = 'Supplier' ''',as_list=1)

    user_list = sum(data,[])
    user_list.append('Guest')
    
    # filter the Users from above user_list
    if user_list:
        return frappe.db.sql("""select user.name
                from
                    `tabUser` user
                inner join
                    `tabHas Role` user_role
                on user_role.role != "Supplier"
                and user_role.parent = user.name 
                where
                    user.name not in %(users)s
                    group by user.name""",{"users":tuple(user_list)})