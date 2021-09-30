# README of iShape dataset 

A dataset designed for irregular Shape instance segmentation. Our dataset consists of six sub-datasets, namely iShape-Antenna, iShape-Branch, iShape-Fence, iShape-Log, iShape-Hanger, and iShape-Wire. As shown in picture below, each sub-dataset represents scenes of a typical irregular shape, for example, strip shape, hollow shape, and mesh shape.

![](https://ishape.github.io/image/ishape_img/ishape.png)

Project page: https://ishape.github.io/

Paper: iShape: A First Step Towards Irregular Shape Instance Segmentation

**Basic information of iShape**: 
- Contains six sub-datasets, each sub-dataset has a foreground class.
- Contains 12,870 images with 175,840 instances. 
- All images are 1024$\times$1024 pixels.

**File struct:** 
```bash
ishape_dataset
├── antenna
│   ├── train
│   │   ├── coco_format  # include soft links
│   │   |   ├── instances_train2017.json -> ../coco*2017.json
│   │   |   └── train2017 -> ../image
│   │   ├── coco_format-mask_encoding=rle-instances_2017.json
│   │   ├── image
│   │   └── instance_map
│   └── val
│       ├── coco_format
│       |   ├── instances_train2017.json -> ../coco*2017.json
│       |   └── train2017 -> ../image
│       ├── coco_format-mask_encoding=rle-instances_2017.json
│       ├── image
│       └── instance_map
├── branch ...
├── fence ...
├── hanger ...
├── log ...
└── wire ...
```


**Dataset format:** iShape provides both Cityscapes and COCO style instance segmentation annotations.
- Cityscapes style: store as `*.png` files under directory `instance_map`. Similar to `*_instanceIds.png` in Cityscapes dataset, those png file are Height * Width * 16bit. Each pixel value `x` means that the pixel belongs to the instance ID is `x`.
- COCO style: It should be pointed out that the COCO style annotations encode masks by [Run-Length Encoding(RLE)](https://en.wikipedia.org/wiki/Run-length_encoding), because polygon can not represent hollow-shaped masks.

**Source code about the dataset:**
- [**`build_synthetic_ishape`**](https://github.com/iShape/build_synthetic_ishape): Source code of building iShape synthetic data.
- [**`bpycv`**](https://github.com/DIYer22/bpycv): Computer vision utils for open-source CG software [Blender](https://www.blender.org/).
  
**Dataset license:** [Public domain (CC0)](https://creativecommons.org/publicdomain/zero/1.0/)    


