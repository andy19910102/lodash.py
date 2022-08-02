# Note for publish

Package folder structure

```
packaging_lodash_py
├── lodash_py
│   └── __init__.py
└── setup.py
```

Build dist

```
$ python setup.py sdist bdist_wheel
```

Publish

```shell
$ python -m twine upload dist/*
```

