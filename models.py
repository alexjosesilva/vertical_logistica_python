from datetime import datetime
import json

def process_file(file):
    lines = file.readlines()
    users = {}
    
    for line in lines:
        line_str = line.decode('utf-8')
        user_id = int(line[0:10].strip())
        user_name = line[10:55].strip()
        order_id = int(line[55:65].strip())
        product_id = int(line[65:75].strip())
        product_value = float(line[75:87].strip())
       ## purchase_date_str = line_str[87:95].strip()      
       ## purchase_date = datetime.strptime(purchase_date_str, '%Y%m%d')
        
        if user_id not in users:
            users[user_id] = {
                "user_id": user_id,
                "name": user_name,
                "orders": []
            }
        
        orders = users[user_id]['orders']
        order = next((o for o in orders if o['order_id'] == order_id), None)
        
        if not order:
            order = {
                "order_id": order_id,
                "total": 0.0,
             ##   "date": purchase_date.strftime('%Y-%m-%d'),
                "products": []
            }
            orders.append(order)
        
        order['total'] += product_value
        order['products'].append({
            "product_id": product_id,
            "value": f"{product_value:.2f}"
        })
    
    result = [user for user in users.values()]
    return result
