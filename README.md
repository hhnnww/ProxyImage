```commandline
conda create -p ./env python=3.11
conda activate ./env
pip install -r requirement.txt
```

# 运行

```commandline
gunicorn main:app -c gunicorn.py -D
```
