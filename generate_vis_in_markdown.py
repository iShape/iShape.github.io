from boxx import *
from generate_html import *

img_names = ["antenna/4165.jpg", "branch/30.jpg", "fence/103.jpg", "hanger/366.jpg", "log/103.jpg", "wire/212.jpg"]

methods = ["gt", "maskrcnn", "solov2", "asis"]

with table(style="overflow: hidden;") as d,tbody():
    with tr(style="padding:0px;"):
        for method in methods:
            th(method_names[method])
    for img_name in img_names:
        with tr(cls="content"):
            for method in methods:
                imgp = pathjoin(img_path, method, img_name)
                with td(style="padding:0px;"),a(href=imgp):
                    img(src=imgp, style="")


openwrite(d.render(), "tmp_vis-in-md.md")
