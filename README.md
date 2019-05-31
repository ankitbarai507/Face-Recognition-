

```
git clone https://github.com/kitsook/face
cd face
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Face detection

`detect.py`

## Face recognizer training

`train.py`

* `imgdb/Barack Obama/image1.jpg`
* `imgdb/Barack Obama/image2.jpg`
* ...
* `imgdb/Donald Trump/anotherimage.png`
* `imgdb/Donald Trump/yetanotherimage.jpg`
* ...
* `imgdb/Justin Trudeau/faces.jpg`

Note that each image can contain multiple faces of the same person.

## Face recognition

`recognize.py`


