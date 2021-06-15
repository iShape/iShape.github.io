
<head>
    <meta charset="UTF-8">
    <title>iShape datasets Project Page</title>
    <meta name="description" content="Irregular Shape Instance Segmentation">
    <meta name="keywords" content="irregular Shape, instance segmentation, overlap, connected components">
    <link rel="shortcut icon" href="./favicon.ico">
</head>

<div align="center">

# Irregular Shape Instance Segmentation

**[Lei Yang<sup>1</sup>](https://github.com/DIYer22) &nbsp;&nbsp;&nbsp; Ziwei Yan<sup>2</sup> &nbsp;&nbsp;&nbsp; Wei Sun<sup>1</sup>&nbsp;&nbsp;&nbsp; Yisheng He<sup>3</sup> &nbsp;&nbsp;&nbsp; Zhenhang Huang<sup>4</sup> &nbsp;&nbsp;&nbsp; Haibin Huang<sup>5</sup> Haoqiang Fan<sup>1</sup>**

<sup>1</sup>Megvii Research Beijing, Megvii Technology Ltd., Beijing, China    
<sup>2</sup>School of Software, Beihang University, Beijing, China    
<sup>3</sup>Hong Kong University of Science and Technology, Hong Kong, China   
<sup>4</sup>Beijing University of Chemical Technology, Beijing, China  
<sup>5</sup>Kuaishou Technology, Beijing, China  
<!-- <sup>3</sup>School of Computer Science, The University of Adelaide, Adelaide, Australia -->


<div align="center">

<br>

  <img style="width:200px" src="image/ishape_img/wire5.png">
  <img style="width:200px" src="image/ishape_img/wire-inst.png">


<p style="width:670px; text-align: justify">A typical scene of objects with irregular shape and similar appearance. It has many characteristics that challenge instance segmentation algorithms, including the large overlaps between bounding boxes of objects, extreme aspect ratios (bounding box of the grey mask), and large numbers of connected components in one instance (green and blue masks).</p>

<br>

</div>


---

 ### [Abstract](#1-abstract) | [Paper](#2-paper) | [Dataset](#3-our-ishape-dataset) | [Baselines](#4-our-baseline-arbitrary-shape-instance-segmentation) | [Benchmark](#5-benchmark) | [Misc](#6-misc)
 
  <!-- | [Leaderboard](#5-Leaderboard) | [iShape-tool](#6-rpc-tool)  -->

</div>

## 1. Abstract

<p style="text-align: justify"><em>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this paper, we introduce a brand new dataset to promote the study of instance segmentation for objects with irregular shapes. Our key observation is that though irregularly shaped objects widely exist in daily life and industrial scenarios, they received little attention in the instance segmentation field due to the lack of corresponding datasets. To fill this gap, we propose iShape, an irregular shape dataset for instance segmentation. Unlike most existing instance segmentation datasets of regular objects, iShape has many characteristics that challenge existing instance segmentation algorithms, such as large overlaps between bounding boxes of instances, extreme aspect ratios, and large numbers of connected components per instance. We benchmark popular instance segmentation methods on iShape and find their performance drop dramatically. Hence, we propose an affinity-based instance segmentation algorithm, called ASIS, as a stronger baseline. ASIS explicitly combines perception and reasoning to solve <b>A</b>rbitrary <b>S</b>hape <b>I</b>nstance <b>S</b>egmentation including irregular objects. Experimental results show that ASIS outperforms the state-of-the-art on iShape.</em></p>

## 2. Paper

<div align="center">

<a href="https://openreview.net/forum?id=48CBzhshpcS">
    <img style="width:200px" src="image/ishape_img/paper.png">
</a>   


[**Paper on OpenReview.net => "Irregular Shape Instance Segmentation"**](https://openreview.net/forum?id=48CBzhshpcS)
</div>

## 3. Our iShape dataset 

In this work, we present iShape, a new dataset designed for **i**rregular **Shape** instance segmentation. Our dataset consists of six sub-datasets, namely iShape-Antenna, iShape-Branch, iShape-Fence, iShape-Log, iShape-Hanger, and iShape-Wire. As shown in  picture below, each sub-dataset represents scenes of a typical irregular shape, for example, strip shape,  hollow shape, and mesh shape.

<div align="center">

![](image/ishape_img/ishape.png)

</div>

### Download iShape dataset (4.5GB):
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://47.103.201.240:9000/ishape/ishape_dataset.tar</p>

### Browse iShape dataset online: => [ishape_dataset](http://47.103.201.240:9000/ishape/ishape_dataset)

**Dataset format:** iShape provides both Cityscapes and COCO style instance segmentation annotations.
- Cityscapes style: store as `*.png` files under directory `instance_map`. Similar to `*_instanceIds.png` in Cityscapes dataset, those png file are Height * Width * 16bit. Each pixel value `x` means that the pixel belongs to the instance ID is `x`.
- COCO style: It should be pointed out that the COCO style annotations encode masks by [Run-Length Encoding(RLE)](https://en.wikipedia.org/wiki/Run-length_encoding), because polygon can not represent hollow-shaped masks.
  
**Dataset license:** [Public domain (CC0)](https://creativecommons.org/publicdomain/zero/1.0/)    

<img style="width:200px" src="https://blogs.uakron.edu/dds/files/2014/07/Public-Domain.jpg">

**Overview infomation of the iShape dataset:** 

<div align="center">

| **# sub-datasets** | **# imgages** | **# instances** | **# instance/image** |
| ------------------ | ------------: | --------------: | -------------------: |
| iShape-Antenna     | 370           | 3,036           | 8.20                 |
| iShape-Branch      | 2,500         | 26,046          | 10.14                |
| iShape-Fence       | 2,500         | 7,870           | 3.15                 |
| iShape-Hanger      | 2,500         | 49,275          | 19,71                |
| iShape-Log         | 2,500         | 72,144          | 28.86                |
| iShape-Wire        | 2,500         | 17,469          | 6.99                 |

</div>

## 4. Our Baseline: Arbitrary Shape Instance Segmentation

<p style="text-align: justify"> We introduce a stronger baseline considering irregular shape in this paper, which explicitly combines perception and reasoning. Our key insight is to simulate how a person identifies an irregular object. Taking the wire shown in Figure 1 for example, one natural way is to start from a local point and gradually expand by following the wire contour and figure out the entire object. The behavior of such ``following the contour'' procedure is a process of <b>continuous iterative reasoning based on local clues</b>, which is similar to the recent affinity-based approaches . Under such observation, we propose a novel affinity-based instance segmentation baseline, called ASIS, which includes principles of generating effective and efficient affinity kernel based on dataset property to solve <b>A</b>rbitrary <b>S</b>hape <b>I</b>nstance  <b>S</b>egmentation. Experimental results show that the proposed baseline outperforms existing state-of-the-art methods by a large margin on iShape.</p>


<div align="center">

<br>

  <img style="width:700px" src="image/ishape_img/overview.png">


<p style="width:700px; text-align: justify"><b>Overview of ASIS</b>. In the training stage, the network learns to predict the semantic segmenation as well as the affinity map where the ground truth of affinity can be generated by affinity kernel and instance ground truth. In the inference stage, the predicted affinity map will be used to construct a sparse and undirected graph, with pixel as node and affinity map as edge. The final instance label then can be generated by applying a class assign module on top of the constructed graph and semantic segmentation map.</p>

<br>

</div>

**Baseline code will release soon.**

## 5. Benchmark
We also benchmark existing instance segmentation algorithms on iShape and find their performance degrades significantly.

#### 5.1 Experimental results

<div align="center" >

| Method            | Backbone  | Antenna | Branch | Fence | Hanger | Log  | Wire | Average |
| ----------------- | --------: | ------: | -----: | ----: | -----: | ---: | ---: | ------: |
| SOLOv2            | ResNet-50 | 6.6     | 27.5   | 0.0   | 28.8   | 22.2 | 0.0  | 14.07   |
| PolarMask         | ResNet-50 | 0.0     | 0.0    | 0.0   | 0.0    | 18.6 | 0.0  | 3.10    |
| SpatialEmbeddings | -         | 38.3    | 0.0    | 0.0   | 49.8   | 20.9 | 0.0  | 18.17   |
| Mask RCNN         | ResNet-50 | 16.9    | 4.2    | 0.0   | 22.1   | 32.6 | 0.0  | 12.63   |
| DETR              | ResNet-50 | 2.1     | 2.6    | 0.0   | 32.2   | 46.2 | 0.0  | 13.85   |
| ASIS(ours)        | ResNet-50 | 77.5    | 25.1   | 37.1  | 53.1   | 69.3 | 64.9 | 54.50   |

</div>

#### 5.2 Qualitative results 

Qualitative results are [=> **here**](ishape_experiment.html)

<div align="center" style="width:300px">

[![](image/ishape_img/result.png)](ishape_experiment.html)

</div>

<!-- 
## 5. Leaderboard


<div style="text-align: justify">

[**iShape-Leaderboard**]()

If you have been successful in creating a model based on the training set and it performs well on the validation set, we encourage you to run your model on the test set. The  [`rpctool`]() (in the next section in this project page) will contribute to return the corresponding results of the evaluation metrics. You can submit your results on the RPC leaderboard by creating a new issue. Your results will be ranked in the leaderboard and to benchmark your approach against that of other machine learners. We are looking forward to your submission. Please click [here]() to submit.

</div> -->


## 6. Misc

If you have any questions about iShape, feel free to submit an issue here: [issues](https://github.com/iShape/iShape.github.io/issues).

<!-- ## 6. ATTN

<div style="text-align: justify">

This dataset and code packages are free for academic usage. You can run them at your own risk. For other purposes, please contact the corresponding author Lei Yang (yanglei@megvii.com).

</div> -->


<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NGRJZ0J17J"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-NGRJZ0J17J');
</script>
