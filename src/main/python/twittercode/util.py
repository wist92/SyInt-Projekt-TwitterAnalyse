import os


# Deletes Twitter Result Files
def delete_txt_and_png():
    for item in os.listdir('.'):
        if item.endswith(".png") or item.endswith(".txt"):
            os.remove(os.path.join(item))