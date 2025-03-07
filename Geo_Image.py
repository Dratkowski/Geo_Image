import webbrowser
from flask import Flask, render_template, request, redirect, url_for
from picarta import Picarta

# Initialize Flask app
app = Flask(__name__)

# Initialize Picarta with API token
api_token = "7Y3BMGXEUAZBDB80H15R"
localizer = Picarta(api_token)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file part", 400

    image = request.files['image']
    
    if image.filename == '':
        return "No selected file", 400

    # Save the uploaded image temporarily
    img_path = "uploaded_image.jpg"
    image.save(img_path)

    # Geolocate the uploaded image
    result = localizer.localize(img_path=img_path)
    
    # Return the result to the user
    return render_template('result.html', result=result)

if __name__ == '__main__':
    # Open the browser automatically when starting the server
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)
