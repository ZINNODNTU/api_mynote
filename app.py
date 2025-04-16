from flask import Flask, jsonify, request

app = Flask(__name__)

notes = [
    {
        "id": 1,
        "title": "Học Flutter cơ bản của căn bản",
        "content": "Học các widget cơ bản như Text, Column, Row, ListView...",
        "priority": 3,
        "createdAt": "2025-04-01T10:30:00Z",
        "modifiedAt": "2025-04-03T12:00:00Z",
        "tags": ["flutter", "học tập", "mobile"],
        "color": "#FFB74D"
    },
    {
        "id": 2,
        "title": "Đi chợ",
        "content": "Mua rau, thịt, trái cây và nước mắm.",
        "priority": 1,
        "createdAt": "2025-04-05T08:00:00Z",
        "modifiedAt": "2025-04-05T08:15:00Z",
        "tags": ["cá nhân", "việc nhà"],
        "color": "#008000"  # Green in hex
    },
    {
        "id": 3,
        "title": "Gặp mặt đối tác",
        "content": "Chuẩn bị slide thuyết trình và in hợp đồng.",
        "priority": 2,
        "createdAt": "2025-04-06T09:00:00Z",
        "modifiedAt": "2025-04-06T09:30:00Z",
        "tags": ["công việc", "gặp gỡ"],
        "color": "#4FC3F7"
    },
    {
        "id": 4,
        "title": "Tập thể dục",
        "content": "Chạy bộ 30 phút, hít đất, plank.",
        "priority": 2,
        "createdAt": "2025-04-04T06:00:00Z",
        "modifiedAt": "2025-04-04T06:45:00Z",
        "tags": ["sức khỏe"],
        "color": "#81C784"
    },
    {
        "id": 5,
        "title": "Lập kế hoạch tuần",
        "content": "Xem lại mục tiêu và sắp xếp lịch làm việc.",
        "priority": 3,
        "createdAt": "2025-04-07T20:00:00Z",
        "modifiedAt": "2025-04-07T20:10:00Z",
        "tags": ["kế hoạch", "tuần"],
        "color": "#BA68C8"
    },
    {
        "id": 6,
        "title": "Nấu cơm tối",
        "content": "Nấu canh chua cá, trứng chiên và rau xào.",
        "priority": 1,
        "createdAt": "2025-04-03T17:00:00Z",
        "modifiedAt": "2025-04-03T17:45:00Z",
        "tags": ["cá nhân", "nấu ăn"],
        "color": "#F06292"
    },
    {
        "id": 7,
        "title": "Đọc sách",
        "content": "Đọc xong chương 5 cuốn 'Thiết kế hệ thống'",
        "priority": 2,
        "createdAt": "2025-04-02T21:00:00Z",
        "modifiedAt": "2025-04-02T21:30:00Z",
        "tags": ["học tập", "giải trí"],
        "color": "#FFD54F"
    },
    {
        "id": 8,
        "title": "Viết blog",
        "content": "Viết bài về trải nghiệm học Flutter",
        "priority": 3,
        "createdAt": "2025-04-06T22:00:00Z",
        "modifiedAt": "2025-04-06T23:00:00Z",
        "tags": ["viết lách", "chia sẻ"],
        "color": "#90CAF9"
    },
    {
        "id": 9,
        "title": "Xem phim",
        "content": "Xem phần mới nhất của series yêu thích",
        "priority": 1,
        "createdAt": "2025-04-05T20:00:00Z",
        "modifiedAt": "2025-04-05T22:00:00Z",
        "tags": ["giải trí"],
        "color": "#E0E0E0"
    },
    {
        "id": 10,
        "title": "Backup dữ liệu",
        "content": "Sao lưu toàn bộ tài liệu và ảnh lên cloud",
        "priority": 3,
        "createdAt": "2025-04-01T08:00:00Z",
        "modifiedAt": "2025-04-01T08:30:00Z",
        "tags": ["công nghệ", "bảo mật"],
        "color": "#A1887F"
    },
    {
        "id": 11,
        "title": "Đi khám răng",
        "content": "Khám tổng quát định kỳ",
        "priority": 2,
        "createdAt": "2025-04-07T09:00:00Z",
        "modifiedAt": "2025-04-07T09:45:00Z",
        "tags": ["sức khỏe", "cá nhân"],
        "color": "#FFAB91"
    }
]

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        return jsonify(note)
    return jsonify({"error": "Note not found"}), 404

@app.route('/notes', methods=['POST'])
def create_note():
    new_note = request.get_json()
    new_note['id'] = max(note["id"] for note in notes) + 1 if notes else 1
    notes.append(new_note)
    return jsonify(new_note), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        data = request.get_json()
        note.update(data)
        return jsonify(note)
    return jsonify({"error": "Note not found"}), 404

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        notes = [n for n in notes if n["id"] != note_id]
        return jsonify({"message": "Note deleted"})
    return jsonify({"error": "Note not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)