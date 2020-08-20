# QuantGuide

An online, open-source guide to quantitative methods, mathematics, statistics, and finance.
Knowledge is phrased in a question and answer style which makes this useful for both learning and testing. 

## Accessing the Guide

The guide is available online [here](https://andrewmellor.co.uk/quantguide).

## Building

Building the project requires two steps:

1. Constructing the markdown files using ```python generate_guide.py```.
2. Building the guide using ```jupyter-book build guide```.

## Content Style

Content is added as XML, examples of which can be found in `/source`.

```xml
<entry>
<title>Title</title>
<slug>slug_name</slug>
<category>Category</category>
<subcategory>Subcategory</subcategory>
<difficulty>Difficulty</difficulty>
<date>01/01/200</date>
<interview>Interview Location (Interview Type)</interview>
<link name="Link description">HTML Link</link>
<question>
Question (written in markdown)
</question>
<answer>
Answer (written in markdown)
</answer>
<include>True</include>
</entry>
```
You can specify multiple interview and link rows.
Questions and answers should be written in markdown with no need to worry about possible escape characters, which are accounted for in the parsing engine.


## Contributing

To contribute to the guide submit a pull request. 
Please make sure to follow the coding/writing style set out otherwise your requests may be rejected.