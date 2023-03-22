# Anime Face Generation with StyleGAN-XL

This repo simply used StyleGAN-XL to generate anime faces

## Environments

- Python 3.8.10

Specify CUDA_VER in `setup_environments.sh` and run

``` bash
bash setup_environments.sh
```

## Data Preparation

> Follow instruction [here](https://github.com/autonomousvision/stylegan-xl#data-preparation)

Create 256x256 dataset

``` bash
python dataset_tool.py --source=./data/animeface256cleaner_combine \
                       --dest=./data/animeface256.zip \
                       --resolution=256x256 \
                       --transform=center-crop
```

Create 64x64 dataset (For training stem)

``` bash
python dataset_tool.py --source=./data/animeface256cleaner_combine \
                       --dest=./data/animeface64.zip \
                       --resolution=64x64 \
                       --transform=center-crop
```

## Training

> Strategy from [here](https://github.com/autonomousvision/stylegan-xl#training)

### Training the stem

``` bash
python train.py --outdir=./training-runs/af --cfg=stylegan3-t --data=./data/animeface64.zip \
    --gpus=1 --batch=1 --mirror=1 --snap 10 --batch-gpu 1 --kimg 10000 --cbase 16384 --cmax 256 --syn_layers 7
```

## Citation

``` bibtex
@InProceedings{Sauer2021ARXIV,
  author    = {Axel Sauer and Katja Schwarz and Andreas Geiger},
  title     = {StyleGAN-XL: Scaling StyleGAN to Large Diverse Datasets},
  journal   = {arXiv.org},
  volume    = {abs/2201.00273},
  year      = {2022},
  url       = {https://arxiv.org/abs/2201.00273},
}
```

## Acknowledgement

This repo builds on the codebase of [stylegan-xl](https://github.com/autonomousvision/stylegan-xl)

## ORIGINAL README FILE [HERE](./original_README.md)
