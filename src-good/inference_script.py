# %%

from ultralytics import YOLO
import torch

model = YOLO("../src-good/best.pt")

source = "../dataset/images/5.jpg"

results = model(source)  # list of Results objects

print(f"In this image we found: {len(results[0].boxes)} craters")


# %%
