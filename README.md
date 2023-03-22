# Anime Face Generation with StyleGAN-XL

This repo simply used StyleGAN-XL to generate anime faces

## Environments

- Python 3.8.0

Install libraries

``` bash
bash setup_environments.txt
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

Create 64x64 dataset

``` bash
python dataset_tool.py --source=./data/animeface256cleaner_combine \
                       --dest=./data/animeface64.zip \
                       --resolution=64x64 \
                       --transform=center-crop
```

## Citation

```
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
