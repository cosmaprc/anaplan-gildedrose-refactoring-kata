# Guildedrose refactoring solution

```
Exercise 2:

Using the Guilded Rose Refactoring Kata we would like you to approach the Kata as described in the readme:

    https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/README.md
```

## Problem statement and requirements
- [GildedRose-Refactoring-Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata)
- [GildedRoseRequirements.md](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md)

## Pre-requisites

Install [python](https://www.python.org/downloads/)

Clone this repo

Createa a virtualenv:

```
# Create the venv
python3 -m venv ~/.virtualenvs/guildedrose

# Activate it
source ~/.virtualenvs/guildedrose/bin/activate

# Install project requirements
pip install -r requirements.txt
```

## Refactoring steps

### Notes

Rerun the following command after each step to verify coverage is still at 100% and initial tests are passing

```
python test_gilded_rose.py
coverage run -m unittest discover
coverage html
```

1 - Add initial unit test coverage starting from [GildedRoseRequirements.md](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md) file, achieving 100% coverage. [commit](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/4cbf037cdf66f2ea0d9870ff18782d710e3fa04b)

2 - The test class passes 100% and has all values used expressed as constants which we can now move into the class under test and centralize these common values. [commit1](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/df902663d03bea2234cfbc86e4b900c75b58a1c4) , [commit2](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/3da1b6a41d762234fe44c31ee66c961298c04927)

3 - Replace test constants with class constants. [commit](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/0f187edc6c42d883fa32713e390415e5200eeff9)

4 - Move big code blocks in functions. [commits](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/5dfd3c07414a17c92fbaa29185d2446ed046059b)

5 - Move item processing into _update_item_quality fn. [commit](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/002322d4cc0895923698d6562974de83e1e61732)

6 - Start breaking out individual per item functionalityin own functions, starting with sulfuras. [commit](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/338c3a4cdc610ec844d43293daf7638e62529aa5)

7 - Break out age brie item. [commit](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/33e164a5b5208ed4ad934ab9345c3e028631f90c)

8 - Break out backstage passes. Here is wherre I realize the coverage has changed and there is now 1 function not covered, but it's ok since it's only in the sulfuras stage and I will investigate on my next step. [commit](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/eb81fe6c12cd17a9be4228a14ed63e3f697c85eb) 

9 - Determined sulfuring item udpate does not need _update_quality_nagative_sell_in or any update at all, which is in line with it's requirements and test so removing the function. Test still passing 100% and full coverage. [commit1](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/1588c6d133230997c311468d8c33ad7c74988861) , [commit2](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/0ea7a4e419dd10931dbd2d37f8591b2a6e478296)

10 - Upon another code review I find that _update_quality_aged_brie_and_backstage_passes still has a lot of logic in it that might be broken down or removed. Let's refactor it and other functions at this point. So at this point I've done a final refacroting where I've removed unused constants, renamed some functions whose purpose is more clear now and we have a final refactoring project except for the last piece of new functionality we had to introduce. [commit](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/ace56e29931a4eb870c9e7e5381d9f76360859c2)

11 - Add new Conjured item test, with the requirement that '"Conjured" items degrade in Quality twice as fast as normal items' so the test is initially failing because it's not treating it as a special case yet. [commit](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/17fad9334e176e0b56086d1b1bf3335f0aec646b) , 

12 - Add the missing logic to the class under test and the test will now pass. [commit1](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/c0b5b6a6d81e739fba95c5fc3d18092417e39534) , [commit2](https://github.com/cosmaprc/anaplan-gildedrose-refactoring-kata/commit/427fa9c318ca58ab32f094f7a460eb2873e1c193)
