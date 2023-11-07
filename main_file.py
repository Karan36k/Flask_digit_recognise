# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to compare two images and predict if they represent the same digit
def compare_images(image_path_1, image_path_2):
    # Placeholder logic (replace this with actual image comparison logic)
    return image_path_1 == image_path_2

@app.route('/compare_images', methods=['POST'])
def compare_images_route():
    data = request.get_json()
    image_1 = data.get('image_1')
    image_2 = data.get('image_2')

    result = compare_images(image_1, image_2)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
