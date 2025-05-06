# Guildedrose solution

## Install python and virtualenv

Install python notes

```
python3 -m venv ~/.virtualenvs/guildedrose
source ~/.virtualenvs/guildedrose/bin/activate
pip install -r requirements.txt
```

Initial unit test coverage starting from requirement file

```
python test_gilded_rose.py
coverage run -m unittest discover
coverage html
```