# Irregular Shape Instance Segmentation GitHub Pages

</br>
</br>
</br>
</br>

### How to render `.md` to `.html` and release to github page

1. Install `Markdown Viewer` extension in Chrome, and allow `Markdown Viewer` to access local file in Chrome setting

2. Press F12 , and click Elements tab in debug panel. Right click on `<html><h....` , click `copy => copy outerHTML`, copy the raw HTML code 

3. Paste raw HTML code to VS code, then using `Ctrl+Shift+I` to format the document

4. Paste formatted HTML code in `./index.html`, remove all `chrome-extension://.../`, e.g. `href="chrome-extension://.../github.css"` to `href="github.css"`

5. `git add *;git commit; git push`

### How to apply update from `.md` to `.html`

1. Press F12 , and click Elements tab in debug panel. Right click on `<html><h....` , click `copy => copy outerHTML`, copy the raw HTML code 

2. Replace body in `index.html`, remove all `chrome-extension://.../`.

3. `git add *;git commit; git push`