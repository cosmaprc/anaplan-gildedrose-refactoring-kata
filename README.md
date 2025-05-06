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

3 - Replace test constants with class constants
4 - Move big code blocks in functions
5 - Move item processing into _update_item_quality fn
6 - Start breaking out individual per item functionalityin own functions, startign with sulfuras
7 - Break out age brie
8 - break out backstage passes - here is wherre I realize the coverage ahs cahnged and there is now 1 function not covered - But it's ok since it's only in the sulfuras stage. 
9 - This refactoring has shown that when broken down there are paths that might have been mnissed by tests otherwise. Let's add it in.