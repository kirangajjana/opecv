from fastapi import FastAPI,UploadFile, File
import cv2
app=FastAPI()

@app.post("/process_image")
async def process_image(image: UploadFile = File(...)):
    try:
        # Read the image data
        image_data = await image.read()

        # Create a NumPy array from the image data
        img = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

        # Perform image processing
        imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgblur = cv2.GaussianBlur(imggray, (7, 7), 0)
        imgcanny = cv2.Canny(img, 100, 150)

        # Return the processed images (or save them to a file)
        return {
            "grayscale": imggray,
            "blurred": imgblur,
            "canny": imgcanny
        }
    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e)}