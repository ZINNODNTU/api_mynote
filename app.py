from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize the notes data
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
        "color": "#008000"
    },
    # Add the rest of your notes here...
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

    # Validate incoming data
    if not new_note.get('title') or not new_note.get('content'):
        return jsonify({"error": "Title and content are required"}), 400

    new_note['id'] = max(note["id"] for note in notes) + 1 if notes else 1
    notes.append(new_note)
    return jsonify(new_note), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        data = request.get_json()

        # Update only fields that exist in the data
        note.update(data)
        return jsonify(note)
    return jsonify({"error": "Note not found"}), 404

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = next((note for note in notes if note["id"] == note_id), None)
    if note:
        notes.remove(note)  # Removing the note directly
        return jsonify({"message": "Note deleted"})
    return jsonify({"error": "Note not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
