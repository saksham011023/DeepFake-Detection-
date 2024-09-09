import os
from youtube import video_pred
from image import image_pred
from PIL import Image
import streamlit as st
import traceback
import sys

ALLOWED_VIDEO_EXTENSIONS = {'mp4'}
ALLOWED_IMAGE_EXTENSIONS = {'jpg', 'jpeg', 'png'}


def allowed_file(filename, accepted_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in accepted_extensions


import os
from PIL import Image

def process_image(image, model, dataset, threshold):
    image_path = "uploads/check.jpg"
    
    try:
        # Open the image and save it to the specified path
        Image.open(image).convert("RGB").save(image_path, "JPEG")
        print("Image saved successfully.")
        
        # Perform image prediction
        output_string, pred = image_pred(
            image_path=image_path, model=model, dataset=dataset, threshold=threshold
        )
        return output_string, pred

    except Exception as e:
        # Handle any errors during processing
        return str(e), -1

    finally:
        # Ensure the temporary image file is deleted if it exists
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Temporary file {image_path} deleted.")
        else:
            print(f"Temporary file {image_path} does not exist.")


def process_video(video_path, model, dataset, threshold, frames):

    try:
        output_string, pred = video_pred(video_path=video_path, model=model,
                                         dataset=dataset, threshold=threshold, frames=frames)

        return output_string,pred

    except Exception as e:
        # Handle any errors during processing
        return traceback.print_exception(*sys.exc_info()) ,-1

    finally:
        # Ensure the temporary video file is deleted
        if video_path and os.path.exists(video_path):
            os.remove(video_path)
