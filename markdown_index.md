
<head>
    <meta charset="UTF-8">
    <title>iShape datasets Project Page</title>
    <meta name="description" content="Irregular Shape Instance Segmentation: Dataset and Baseline">
    <meta name="keywords" content="irregular Shape, instance segmentation, overlap, connected components">
    <link rel="shortcut icon" href="./favicon.ico">
</head>

<div align="center">

# Irregular Shape Instance Segmentation: Dataset and Baseline

**[Lei Yang<sup>1*</sup>](https://github.com/DIYer22) &nbsp;&nbsp;&nbsp; Ziwei Yan<sup>2</sup> &nbsp;&nbsp;&nbsp; Wei Sun<sup>1</sup>&nbsp;&nbsp;&nbsp; Yisheng He<sup>1</sup> &nbsp;&nbsp;&nbsp; Zhenhang Huang<sup>3</sup> &nbsp;&nbsp;&nbsp; Haibin Huang<sup>4</sup> Haoqiang Fan<sup>1</sup>**

<sup>1</sup>Megvii Research Beijing, Megvii Technology Ltd., Beijing, China    
<sup>2</sup>School of Software, Beihang University, Beijing, China    
<sup>3</sup>Beijing University of Chemical Technology, Beijing, China  
<sup>4</sup>Kuaishou Technology, Beijing, China  
<!-- <sup>3</sup>School of Computer Science, The University of Adelaide, Adelaide, Australia -->

---

 ### [Abstract](#1-abstract) | [Paper](#2-paper) | [Dataset](#3-our-rpc-dataset) | [Baselines](#4-proposed-baseline-method-on-the-rpc-dataset) | [Leaderboard](#5-Leaderboard) | [iShape-tool](#6-rpc-tool) 
</div>

## 1. Abstract

<p style="text-align: justify"><em>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this paper, we introduce a brand new dataset to promote the study of instance segmentation for objects with irregular shapes. Our key observation is that though irregularly shaped objects widely exist in daily life and industrial scenarios, they received little attention in the instance segmentation field due to the lack of corresponding datasets. To fill this gap, we propose iShape, an irregular shape dataset for instance segmentation. Unlike most existing instance segmentation datasets of regular objects, iShape has many characteristics that challenge existing instance segmentation algorithms, such as large overlaps between bounding boxes of instances, extreme aspect ratios, and large numbers of connected components per instance. We benchmark popular instance segmentation methods on iShape and find their performance drop dramatically. Hence, we propose an affinity-based instance segmentation algorithm, called ASIS, as a stronger baseline. ASIS explicitly combines perception and reasoning to solve <b>A</b>rbitrary <b>S</b>hape <b>I</b>nstance <b>S</b>egmentation including irregular objects. Experimental results show that ASIS outperforms the state-of-the-art on iShape.</em></p>

## 2. Paper

<div align="center">

<a href="https://github.com/iShape/">
    <img style="width:200px" src="/home/yanziwei/PycharmProjects/RPC/RPC-Dataset.github.io/ishape_img/paper.png">
</a>   


[**Paper on github => "Irregular Shape Instance Segmentation: Dataset and Baseline"**](https://github.com/iShape/)
</div>

## 3. Our iShape dataset 

<div align="center">

![](/home/yanziwei/PycharmProjects/RPC/RPC-Dataset.github.io/ishape_img/ishape.png)
<!-- (https://www.kaggle.com/diyer22/retail-product-checkout-dataset)      -->

[**Dataset on Kaggle => "iShape dataset"**]
(1GB)

</div>

\***Notice**: If downloading from Kaggle is not accessable, you can alternatively download the dataset using [Baidu Drive](https://pan.baidu.com/s/1vrrLaSpJe5JxT3zhYfOaog).

#### 3.1 Dataset license:  
[![](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)    
CC BY-NC-SA 4.0

#### 3.2 Overview infomation of the RPC dataset 

<div align="center">

| **# sub-datasets** | **# imgages** | **# instances** | **# instance/image** |
| ------------------ | ------------- | --------------- | -------------------- |
| iShape-Antenna     | 370           | 3,036           | 8.20                 |
| iShape-Branch      | 2,500         | 16,300          | 6.52                 |
| iShape-Fence       | 2,500         | 7,115           | 2.84                 |
| iShape-Hanger      | 2,500         | 25,371          | 10.14                |
| iShape-Log         | 2,500         | 68,025          | 27.21                |
| iShape-Wire        | 2,500         | 14,802          | 5.92                 |

</div>

## 4. Proposed baseline method on the iShape dataset

#### 4.1 Experimental results

<div align="center">

| Method            | Backbone  | Antenna | Branch | Fence | Hanger | Log  | Wire | Average |
| ----------------- | --------- | ------- | ------ | ----- | ------ | ---- | ---- | ------- |
| SOLOv2            | ResNet-50 | 1.7     | 31.1   | 0.0   | 51.7   | 0.1  | 8.07 | 15.45   |
| PolarMask         | ResNet-50 | 0.0     | 0.0    | 0.0   | 0.0    | 13.7 | 0.0  | 2.28    |
| SpatialEmbeddings | -         | 2.3     | 0.0    | 0.0   | 47.4   | 17.0 | 0.5  | 11.20   |
| Mask RCNN         | ResNet-50 | 16.9    | 9.2    | 0.0   | 34.6   | 28.9 | 1.4  | 15.16   |
| ASIS(ours)        | ResNet-50 | 77.5    | 33.7   | 60.4  | 70.1   | 67.9 | 67.8 | 62.90   |

</div>

#### 4.1 Qualitative results 

<div align="center">

[![](/home/yanziwei/PycharmProjects/RPC/ishape/ishape_img/results.png)](/home/yanziwei/PycharmProjects/RPC/ishape/ishape_experiment.html)

</div>

## 5. Leaderboard


<div style="text-align: justify">

[**iShape-Leaderboard**](https://github.com/RPC-Dataset/RPC-Leaderboard)

If you have been successful in creating a model based on the training set and it performs well on the validation set, we encourage you to run your model on the test set. The  [`rpctool`](https://github.com/DIYer22/retail_product_checkout_tools) (in the next section in this project page) will contribute to return the corresponding results of the evaluation metrics. You can submit your results on the RPC leaderboard by creating a new issue. Your results will be ranked in the leaderboard and to benchmark your approach against that of other machine learners. We are looking forward to your submission. Please click [here](https://github.com/RPC-Dataset/RPC-Leaderboard/issues) to submit.

</div>

## 6. iShape-tool

<div style="text-align: justify">

[`rpctool`](https://github.com/DIYer22/retail_product_checkout_tools): A Python package for evaluating your methods on the RPC dataset. It can return several evaluation metrics (listed in the aforementioned table in Sec. 4.2). More information can be found in [`rpctool`](https://github.com/DIYer22/retail_product_checkout_tools).

</div>

## 7. ATTN

<div style="text-align: justify">

This dataset and code packages are free for academic usage. You can run them at your own risk. For other purposes, please contact the corresponding author Dr. Xiu-Shen Wei (weixs.gm [at] gmail.com).

</div>


<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-133191784-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-133191784-1');
</script>
