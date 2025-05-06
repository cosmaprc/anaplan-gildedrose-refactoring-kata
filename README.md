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
9 - After careful refactoring of the affected fn, turns out the sulfuric item udpate stage did not need to use _update_quality_nagative_sell_in at all, so removed and code coverage is back at 100%.

10 - Upon inspection of shared _update_quality_all between sulfuric and all other items expect the other special ones, I found that sulfuric does not need any update at all, which is in line with it's requirements and test so removing the function. Test still passing 100% and full coverage.