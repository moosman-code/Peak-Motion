from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
import requests

app = FastAPI()

# Your PlantNet API key and URL configuration (update as needed)
key = '2b10mD9ZagycYz5vQn0or5viQ'
url = (
        "https://my-api.plantnet.org/v2/identify/all?"
        "include-related-images=false&no-reject=false&nb-results=1&lang=en&api-key=" + key
)
headers = {"accept": "application/json"}


# Serve a simple HTML page that opens a file dialog
@app.get("/", response_class=HTMLResponse)
async def main():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Plant Classifier Upload</title>
    </head>
    <body>
        <h2>Upload an Image for Plant Classification</h2>
        <!-- Hidden file input element -->
        <input type="file" id="fileInput" style="display: none;" accept="image/*"/>
        <!-- Button that triggers the file dialog -->
        <button id="uploadButton">Upload Image</button>
        <pre id="output"></pre>
        <script>
            // When the button is clicked, open the file dialog
            document.getElementById("uploadButton").addEventListener("click", function() {
                document.getElementById("fileInput").click();
            });

            // When a file is selected, send it to the /classify/ endpoint
            document.getElementById("fileInput").addEventListener("change", function() {
                const file = this.files[0];
                const formData = new FormData();
                formData.append("image", file);

                fetch("/classify/", {
                    method: "POST",
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById("output").textContent = JSON.stringify(data, null, 2);
                })
                .catch(error => console.error("Error:", error));
            });
        </script>
    </body>
    </html>
    """
    return html_content


# API endpoint that handles the file upload and classification
@app.post("/classify/")
async def classify_plant(image: UploadFile = File(...)):
    # Read image file bytes
    image_bytes = await image.read()

    # Prepare the file for the external API call
    files = {"images": (image.filename, image_bytes, image.content_type)}

    # Call the PlantNet API
    response = requests.post(url, headers=headers, files=files)
    result = response.json()

    # Extract best match (modify based on actual API response structure)
    best_match = result.get('bestMatch', "No match found")

    return JSONResponse(content={"bestMatch": best_match})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
