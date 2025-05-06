# Guildedrose solution

## Install python and virtualenv

Install python notes

```
python3 -m venv ~/.virtualenvs/guildedrose
source ~/.virtualenvs/guildedrose/bin/activate
pip install -r requirements.txt
```

1 - Initial unit test coverage starting from requirement file, 100% coverage in this case

```
python test_gilded_rose.py
coverage run -m unittest discover
coverage html
```

2 - The test class passes 100% and has all values used expressed as constants which we can now move into the calss under test and centralize these common values as well as give meaning to them.
- Check coverage has not changed nor test resutls

