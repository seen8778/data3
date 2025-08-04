products = {
    "หมูสับกิโล": 150.00,
    "เนื้ออกไก่": 105.00,
    "ไก่บ้าน(ตัว)": 120.00,
    "ข้าวสาร": 150.00,
    "มาม่าต้มยำ": 6.50,
    "น้ำตาล": 20.00,
    "ปลากะป๋องสามแม่ครัว": 10.00,
    "ซอสน้ำมันหอย": 18.00,
    "ผงชูรส": 10.25,
    "ไข่แผงคละเบอร์": 120.25,
    "ชาเขียว": 21.50,
    "Pepsi": 29.50,
    "กาแฟ": 15.75,
    "ขนมปังอบเนย": 19.00,
    "ชาไทย": 11.50,
    "น้ำเปล่า": 15.15,
    "น้ำแข็ง": 10.00
}

budget = 1000
selected_items = list(products.items())[:15]
total_spent = sum(price for _, price in selected_items)
change = budget - total_spent

print("รายการสินค้าที่ซื้อ:")
for item, price in selected_items:
    print(f"- {item}: {price:.2f} บาท")
print("\nราคารวมทั้งหมด:", f"{total_spent:.2f} บาท")
print("เงินที่จ่าย:", f"{budget:.2f} บาท")
print("เงินทอน:", f"{change:.2f} บาท")