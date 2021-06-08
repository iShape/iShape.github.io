
<head>
    <meta charset="UTF-8">
    <title>iShape datasets Project Page</title>
    <meta name="description" content="Irregular Shape Instance Segmentation: Dataset and Baseline">
    <meta name="keywords" content="irregular Shape, instance segmentation, overlap, connected components">
    <link rel="shortcut icon" href="./favicon.ico">
</head>

<div align="center">

# Irregular Shape Instance Segmentation: Dataset and Baseline

**[Lei Yang<sup>1</sup>](https://github.com/DIYer22) &nbsp;&nbsp;&nbsp; Ziwei Yan<sup>2</sup> &nbsp;&nbsp;&nbsp; Wei Sun<sup>1</sup>&nbsp;&nbsp;&nbsp; Yisheng He<sup>1</sup> &nbsp;&nbsp;&nbsp; Zhenhang Huang<sup>3</sup> &nbsp;&nbsp;&nbsp; Haibin Huang<sup>4</sup> Haoqiang Fan<sup>1</sup>**

<sup>1</sup>Megvii Research Beijing, Megvii Technology Ltd., Beijing, China    
<sup>2</sup>School of Software, Beihang University, Beijing, China    
<sup>3</sup>Beijing University of Chemical Technology, Beijing, China  
<sup>4</sup>Kuaishou Technology, Beijing, China  
<!-- <sup>3</sup>School of Computer Science, The University of Adelaide, Adelaide, Australia -->

---

 ### [Abstract](#1-abstract) | [Paper](#2-paper) | [Dataset](#3-our-iShape-dataset) | [Baselines](#4-proposed-baseline-method-on-the-iShape-dataset) | [Leaderboard](#5-Leaderboard) | [iShape-tool](#6-rpc-tool) 
</div>

## 1. Abstract

<p style="text-align: justify"><em>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this paper, we introduce a brand new dataset to promote the study of instance segmentation for objects with irregular shapes. Our key observation is that though irregularly shaped objects widely exist in daily life and industrial scenarios, they received little attention in the instance segmentation field due to the lack of corresponding datasets. To fill this gap, we propose iShape, an irregular shape dataset for instance segmentation. Unlike most existing instance segmentation datasets of regular objects, iShape has many characteristics that challenge existing instance segmentation algorithms, such as large overlaps between bounding boxes of instances, extreme aspect ratios, and large numbers of connected components per instance. We benchmark popular instance segmentation methods on iShape and find their performance drop dramatically. Hence, we propose an affinity-based instance segmentation algorithm, called ASIS, as a stronger baseline. ASIS explicitly combines perception and reasoning to solve <b>A</b>rbitrary <b>S</b>hape <b>I</b>nstance <b>S</b>egmentation including irregular objects. Experimental results show that ASIS outperforms the state-of-the-art on iShape.</em></p>

## 2. Paper

<div align="center">

<a href="image/ishape_img/paper.png">
    <img style="width:200px" src="image/ishape_img/paper.png">
</a>   


[**Paper on github => "Irregular Shape Instance Segmentation: Dataset and Baseline"**](https://github.com/iShape/)
</div>

## 3. Our iShape dataset 

<div align="center">

![](image/ishape_img/ishape.png)

[**Dataset on Kaggle => "iShape dataset"**]
(15GB)

</div>

#### 3.1 Dataset license:  
[![](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)    
CC BY-NC-SA 4.0

#### 3.2 Overview infomation of the RPC dataset 

<div align="center">

| **# sub-datasets** | **# imgages** | **# instances** | **# instance/image** |
| ------------------ | ------------- | --------------- | -------------------- |
| iShape-Antenna     | 370           | 3,036           | 8.20                 |
| iShape-Branch      | 2,500         | 26,046          | 10.14                |
| iShape-Fence       | 2,500         | 7,870           | 3.15                 |
| iShape-Hanger      | 2,500         | 49,275          | 19,71                |
| iShape-Log         | 2,500         | 72,144          | 28.86                |
| iShape-Wire        | 2,500         | 17,469          | 6.99                 |

</div>

## 4. Proposed baseline method on the iShape dataset

#### 4.1 Experimental results

<div align="center">

| Method            | Backbone  | Antenna | Branch | Fence | Hanger | Log  | Wire | Average |
| ----------------- | --------- | ------- | ------ | ----- | ------ | ---- | ---- | ------- |
| SOLOv2            | ResNet-50 | 6.6     | 27.5   | 0.0   | 28.8   | 22.2 | 0.0  | 14.07   |
| PolarMask         | ResNet-50 | 0.0     | 0.0    | 0.0   | 0.0    | 18.6 | 0.0  | 3.10    |
| SpatialEmbeddings | -         | 38.3    | 0.0    | 0.0   | 49.8   | 20.9 | 0.0  | 18.17   |
| Mask RCNN         | ResNet-50 | 16.9    | 4.2    | 0.0   | 22.1   | 32.6 | 0.0  | 12.63   |
| DETR              | ResNet-50 | 2.1     | 2.6    | 0.0   | 32.2   | 46.2 | 0.0  | 13.85   |
| ASIS(ours)        | ResNet-50 | 77.5    | 25.1   | 37.1  | 53.1   | 69.3 | 64.9 | 54.50   |

</div>

#### 4.1 Qualitative results 

<div align="center">

[![](image/ishape_img/result.png)](ishape_experiment.html)

</div>

## 5. Leaderboard


<div style="text-align: justify">

[**iShape-Leaderboard**]()

If you have been successful in creating a model based on the training set and it performs well on the validation set, we encourage you to run your model on the test set. The  [`rpctool`]() (in the next section in this project page) will contribute to return the corresponding results of the evaluation metrics. You can submit your results on the RPC leaderboard by creating a new issue. Your results will be ranked in the leaderboard and to benchmark your approach against that of other machine learners. We are looking forward to your submission. Please click [here]() to submit.

</div>


## 6. ATTN

<div style="text-align: justify">

This dataset and code packages are free for academic usage. You can run them at your own risk. For other purposes, please contact the corresponding author Lei Yang (yanglei@megvii.com).

</div>


<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-133191784-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-133191784-1');
</script>
