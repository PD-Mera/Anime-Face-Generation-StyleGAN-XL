"""
Original structure:
.
└── animeface256cleaner/
    ├── animefaces256cleaner_Filtered_Set0/
    │   ├── 000000.jpg
    │   └── ...
    └── ...

Combined structure:
.
└── animeface256cleaner_combine/
    ├── animefaces256cleaner_Filtered_Set0_000000.jpg
    └── ...
"""

import os
from tqdm import tqdm

ROOT_DIR = "./data/animeface256cleaner/"
TARGET_DIR = "./data/animeface256cleaner_combine/"

os.makedirs(TARGET_DIR, exist_ok=True)

for subset in tqdm(os.listdir(ROOT_DIR)):
    subfolder = os.path.join(ROOT_DIR, subset)
    for image in os.listdir(subfolder):
        image_path = os.path.join(subfolder, image)
        save_path = subfolder + image
        save_path = save_path.replace(ROOT_DIR, TARGET_DIR)
        # os.rename(image_path, save_path)