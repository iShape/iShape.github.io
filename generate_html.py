import dominate
from dominate.tags import *
from dominate.util import text
import glob

dataset_names = {
    "antenna": "iShape-Antenna",
    "branch": "iShape-Branch",
    "fence": "iShape-Fence",
    "hanger": "iShape-Hanger",
    "log": "iShape-Log",
    "wire": "iShape-Wire",
}
method_names = {
    "input": "Input",
    "solov2": "SOLOv2",
    "polarmask": "PolarMask",
    "se": "SE",
    "maskrcnn": "Mask RCNN",
    "detr": "DETR",
    "asis": "Ours",
    "gt": "Ground Truth",
}
img_path = "image/vis_tmp"


def get_img_list(img_path):
    img_list = glob.glob(img_path + "/*/*/*.jpg")
    return img_list


def creat_html():
    h = dominate.document(title="ishape")
    img_list = []
    img_list = get_img_list(img_path)

    with h.head:
        style(".title{display:inline-block;width:100px;text-align:center;")
        style("li {list-style:none;display:inline-block;width:100px;}")
        style("li img{width:100%;}")
        style(".img-box img {position:relative;width:100%;top:100%;}")
        style(".content {width:100%;text-align:center;}")
        style(".headline {font-size:20px;text-align:center;}")
        style(".title-box {text-align:center;}")
        style(".ul-img {font-size:1;}")

    with h:
        for dataset_name in dataset_names:
            a_line_img = []
            img_id_list_tmp = []
            for method_name in method_names:
                for item in img_list:
                    if dataset_name in item and method_name in item:
                        a_line_img.append(item)
                        img_name = item.split("_new", -1)[-1]
                        img_id_list_tmp.append(img_name)

            img_id_list = []
            [img_id_list.append(i) for i in img_id_list_tmp if not i in img_id_list]
            with div(cls="headline"):
                p()
                text(dataset_names[dataset_name])
                p()
            with div(cls="title-box"):
                for method_name in method_names:
                    with div(cls="title"):
                        text(method_names[method_name])

            for i in range(5):
                i_list = img_id_list[i::5]
                with div(cls="content"):
                    for a_img in i_list:
                        for img_ in img_list:
                            if a_img in img_:
                                with li(), a(href=img_):
                                    img(src=img_)
                                break

    with open("ishape_experiment.html", "w") as f:
        f.write(h.render())


if __name__ == "__main__":
    creat_html()
