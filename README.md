# Geo_Image

This tool uses Picarta to find an estimate location of an image using AI software. A Picarta account is needed to optain the API key. The free account will work but does limit searches to 3 per day. https://picarta.ai

It is a very simple program to install. Just ensure python is installed. See Transcription_Tool repo for more on python.

STEP 1: Creat a Virtual Environment When creating a new program, it is a good idea to make a virtual enviornment to run the program. This environment is where all of the libraries and dependencies will be installed. It Keep things seperate from other programs so dependencies are not impacted by other tools. Dependencies/Libraries: Simply put these are tools that other programers and coders have developed to run sertain things with the code. These help you do a wide variety of things so you do not have to do all the coding yourself.

STEP 1A: Set up a virtual environment (venv)

Create a new folder on your C: drive labled "GeoImage" (or something like that)

Right click within that new folder, and "OPEN IN TERMINAL" (You can also open PowerShell and type: cd "C:file\path\to\your\new\folder"). "cd" is the command to open a folder directory path.

cd "C:file\path\to\your\new\folder"
Now create the virtual environment by typing in terminal:

    python -m venv NAME_YOUR_VENV
Example:

    python -m venv GeoImage_venv
Once the venv is created in your directory, you need to activate the venv. This opens the venv and will store all of your dependencies within the venv. You will know you are in the venv when you see the name of your venv in green before your directory file path. Acttivate your venv:

    YOUR_VENV\Scripts\activate
Example:

    GeoImage_venv\Scripts\activate
STEP 3) Now that your venv is active, you can install Whisper within this venv. NOTE: if you close the terminal you will need to reactivate the venv. Make sure that you have downloaded the file "requirements.txt" and place it in your directory Installing dependencies:

    pip install -r requirements.txt
"pip" is the code you will use to install most python libraries and dependencies.

Verify that all the dependencies installed correctly. This list should have all the same things as the requierments.txt

    pip list

Step 2: This will create the user interface using your web browser
In your GeoImage directory, create a folder labled:

    templates

Index.html
With in "templates" create a .html files by opening up Notepad and pasting:

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Upload Image</title>
    </head>
    <body>
        <h1>Upload an Image to GeoImage Search ***Limit 10mb***</h1>
        <form action="/upload" method="POST" enctype="multipart/form-data">
            <label for="image">Select an image:</label>
            <input type="file" name="image" required>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    
Save the file as:
      
    index.htlm

Result.html
With in "templates" create a .html files by opening up Notepad and pasting:
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Localization Result</title>
    </head>
    <body>
        <h1>Image GeoSearch Result (Top 10 Results)</h1>
        <p>{{ result }}</p>
        <a href="/">Back to upload page</a>
    </body>
    </html>

Save the file as: 

    result.htlm

API KEY
Once you get your API KEY from Picarta paste it into the python script. 

Running the program

In your GeoImage_venv:

    python Geo_Image.py
