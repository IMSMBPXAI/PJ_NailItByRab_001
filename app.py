from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# อนุญาตให้ Frontend (HTML) ข้ามโดเมนมาดึงข้อมูลจาก Backend ได้
CORS(app)

# จำลองฐานข้อมูล (ในของจริงจะเชื่อมกับ MySQL, PostgreSQL ฯลฯ)
mock_database_bookings = [
    {
        "id": 1,
        "customer_name": "คุณสมหญิง",
        "phone": "081-123-4567",
        "service": "ทาสีเจล + เพ้นท์ลาย",
        "datetime": "15 ต.ค. 67 - 13:00 น.",
        "status": "รอการยืนยัน"
    },
    {
        "id": 2,
        "customer_name": "น้องมายด์",
        "phone": "089-987-6543",
        "service": "ต่อขนตา + สปามือ",
        "datetime": "15 ต.ค. 67 - 15:30 น.",
        "status": "รอการยืนยัน"
    }
]

# สร้าง API Endpoint ให้ Frontend เรียกใช้
@app.route('/api/bookings', methods=['GET'])
def get_all_bookings():
    # ส่งข้อมูลการจองกลับไปให้หน้าเว็บ
    return jsonify(mock_database_bookings)

if __name__ == '__main__':
    # รันเซิร์ฟเวอร์
    app.run(debug=True, port=5000)