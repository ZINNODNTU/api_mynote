from flask import Flask, jsonify, request

app = Flask(__name__)

# Danh sách ghi chú
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
    }
    {
        "id": 2,
        "userId": 102,
        "username": "user",
        "password": "Abc@123",
        "status": "active",
        "lastLogin": "2025-04-01T10:30:00Z",
        "createdAt": "2025-04-01T09:00:00Z"
    },
    # Các ghi chú khác...
]

# Danh sách tài khoản
accounts = [
    {
        "id": 1,
        "userId": 101,
        "username": "user1",
        "password": "password123",
        "status": "active",
        "lastLogin": "2025-04-01T10:30:00Z",
        "createdAt": "2025-04-01T09:00:00Z"
    },
    # Các tài khoản khác...
]

# Endpoint cho Notes

@app.route('/notes', methods=['GET'])
def get_all_notes():
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

# Endpoint cho Accounts

@app.route('/accounts', methods=['GET'])
def get_all_accounts():
    return jsonify(accounts)

@app.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
    account = next((acc for acc in accounts if acc["id"] == account_id), None)
    if account:
        return jsonify(account)
    return jsonify({"error": "Account not found"}), 404

@app.route('/accounts', methods=['POST'])
def create_account():
    new_account = request.get_json()
    new_account['id'] = max(acc["id"] for acc in accounts) + 1 if accounts else 1
    accounts.append(new_account)
    return jsonify(new_account), 201

@app.route('/accounts/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    account = next((acc for acc in accounts if acc["id"] == account_id), None)
    if account:
        data = request.get_json()
        account.update(data)
        return jsonify(account)
    return jsonify({"error": "Account not found"}), 404

@app.route('/accounts/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    global accounts
    account = next((acc for acc in accounts if acc["id"] == account_id), None)
    if account:
        accounts = [acc for acc in accounts if acc["id"] != account_id]
        return jsonify({"message": "Account deleted"})
    return jsonify({"error": "Account not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
