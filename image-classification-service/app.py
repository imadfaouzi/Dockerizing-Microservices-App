from flask import Flask, jsonify, request
import numpy as np
import tensorflow as tf
# Example code (requires Pillow):
from PIL import Image

app = Flask(__name__)

# Load the TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input image from the request
    imagefile = request.files['imagefile']
    image = process_image(imagefile)

    # Perform inference
    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Post-process the output if needed
    prediction = np.argmax(output_data)

    # Return the prediction as JSON response
    return jsonify({'prediction': int(prediction)})

def process_image(imagefile):
    # Add your image preprocessing code here
    # Example: Read the image, resize it to the required input size, normalize, etc.
    # You may need additional libraries like Pillow or OpenCV for image processing
    # Make sure the input shape matches the model's input shape

    

    image = Image.open(imagefile)
    image = image.resize((224, 224))  # Adjust size according to your model's input shape
    image = np.array(image)
    image = image.astype(np.float32)  # Convert to FLOAT32
    image = image / 255.0  # Normalize to [0, 1]

    # Expand dimensions to match the model's expected shape
    image = np.expand_dims(image, axis=0)

    return image

if __name__ == '__main__':
    app.run(port=3000, debug=True)
