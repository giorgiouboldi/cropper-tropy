import os
import json
from PIL import Image

def crop_and_save_selections(data):
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    for item in data["@graph"]:
        title = item["title"]
        if "photo" in item:
            photo = item["photo"][0]
            img_path = photo["path"]
            img = Image.open(img_path)
            if "selection" in photo:
                selections = photo["selection"]
                for i, selection in enumerate(selections):
                    x = selection["x"]
                    y = selection["y"]
                    width = selection["width"]
                    height = selection["height"]
                    label = selection["title"]["@value"]
                    cropped_img = img.crop((x, y, x + width, y + height))
                    filename = f"{label}-{title}.png"
                    output_path = os.path.join(output_folder, filename)
                    cropped_img.save(output_path)
                    print(f"Cropped and saved {filename} in {output_folder}")

if __name__ == "__main__":
    json_file = "data.json"  # Replace with the path to your JSON file
    with open(json_file, "r") as f:
        json_data = json.load(f)
    crop_and_save_selections(json_data)
