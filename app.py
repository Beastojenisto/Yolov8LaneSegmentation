from PIL import Image,ImageDraw,ImageFont
import numpy as np
from ultralytics import YOLO
import streamlit as st

model = YOLO('LaneSegmentation.pt')
img = st.file_uploader('Choose an Image')

if img is not None:
    img = Image.open(img).resize((640,640)).convert('RGB')
    results = model(img)
    st.image(img,'Input')
    for result in results:
        for mask in result.masks.data:
            mask = mask.numpy()
            st.image(mask,'Mask')
