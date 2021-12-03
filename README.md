# Markdownipy

![](markdownipy_logo.png)

Markdownipy is a Python library to generate markdown files using only two operators and some helpers

Markdownipy can be used in jupyter notebooks to generate markdown outputs in python cells or inside any .py file, see below for examples

##  `<`(lower than operator) writes text to markdown file, `|`(pipe operator) just gives property to the text

Even this README file is genereted by markdownipy!

[Checkout example file](./example.py)

## Motivation

---


Lately, I'm trying to write markdown documentations for different codes and I needed to put
some specs, numbers etc. so just copy-paste some tables, links.
I was trying to change some predefined strings to speed up my writing process, yet
instead of text manipulation I just wanted to make it as a library.

Sometimes I also forget markdown syntax, so this library requires no memory (I hope so, there is even no function calls) :)

Only requirement is remembering the properties of markdownipy and the rest will be handled


---

### Install

`pip install markdownipy`

---

### Quick start - example Jupyter cell

```python
from markdownipy import markdownipy
from IPython.display import display,Markdown

md = markdownipy.markdownipy()

md < "hello there" | md.bold

md < "This should be a italic text" | md.italic
display(Markdown(md.print()))
```

__See the example jupter notebook output:__ [Example jupyter file](jupyter_example.ipynb)

---

### Quick start - example Python code

```python
from markdownipy import markdownipy
md = markdownipy.markdownipy()

#Simple line
md < "Hello there!"

#Bold text, numbers are also allowed
md < 3.14159 | md.bold

#Italic text
md < "Above bold text is just some digits of pi" | md.italic

#One line code and codeblock

md < "One line code " | md.code
md < '''
void markdownipy_helper(int x, int y, int z):
	return x*y*z
''' | md.codeb("cpp")


#Lists 
md < ["Item1","Item2","Item3"]

#Tables
md < {
	"Country":["Fran","Kate","Ivan"],
	"Age" : [30,48,73]
}

#E-mail, links
md < "fbgencer8@gmail.com" | md.link
md < "fbgencer8@gmail.com" | md.link("My mail")

#Image
md < "./markdownipy_logo.png" | md.image

#Writing to a file, README or README.md both works!
#Even md >> sys.stdout prints the whole markdown document
md >> "README"
```

---

### Library keywords

This table is the whole documentation of markdownipy! (Assuming md is the markdown object in python)

|Keywords|Explanation|Markdown equivalent|
|:---:|:---:|:---:|
|md.bold|Bold text|`__text__`|
|md.italic|Italic text|`_text_`|
|md.strike|Strikethrough text|`~~text~~`|
|md.code|For single line code|` `code` `|
|md.codeb|Code fence, takes optional arg as language name|` ```code``` `|
|md.link or md.link(link_name)|Link text|`[link_name(optional)](link)`|
|md.hline|Horizontal line|`---`|
|md.chapter|Chapter|`Chapter_name\n===`|
|md.h1|Header level 1|`# Header1`|
|md.h2|Header level 2|`## Header2`|
|md.h3|Header level 3|`### Header3`|
|md.h4|Header level 4|`#### Header4`|
|md.h5|Header level 5|`##### Header5`|
|md.h6|Header level 6|`###### Header6`|
|md.image or md.image(image_name)|Image insertion|`![image_name(optional)](image_path)`|
|md.task|Task entry in a list|`[ ] text`|
|md.task_check|Checked task entry in a list|`[x] text`|
|`object` \| md.`keyword`|Pipes the above defined line property keywords to the object||
|md < `object`|Adds any object to document (str,dict,list,numbers etc.)||
|md > `file_name`|Writes document to a file||
|md > `stdout`|Prints the document to console||
|md.print()|Returns the markdown document as string||
|md.clear()|Clears the markdown document||

---

---

### Headers



```python
md < "This is a chapter" | md.chapter
md < "This is header1" | md.h1
md < "This is header2" | md.h2
md < "This is header3" | md.h3
md < "This is header4" | md.h4
md < "This is header5" | md.h5
md < "This is header6" | md.h6
```

_Output :_

---

This is a chapter
===

# This is header1

## This is header2

### This is header3

#### This is header4

##### This is header5

###### This is header6

---

---

### Bold, italic, strikethrough texts



```python
md < "This should be a bold text" | md.bold
md < "This is an italic text" | md.italic
md < "Strikethrough is banned"  | md.strike
```

_Output :_

---

__This should be a bold text__

_This is an italic text_

~~Strikethrough is banned~~

---

---

### Lists



```python
md < [
	"Classical mechanics" | md.bold,
	[
		"Newton's law of motion",
		"Lagrangian Mechanics"
	],
	"Thermodynamics and statistical mechanics" | md.italic,
	"Electromagnetism and photonics",
	"Relativistic mechanics",
	"Quantum mechanics, atomic physics, and molecular physics",
	[
		"*", #For dot bullet put bullet type
		"Schrödinger equation",
		"Quantum field theory",
		[
			"Lists can be nested :)",
			"This is another liner",
			[
				"Oh this is getting serious" | md.strike,
				"And now bunch of numbers",
				[
					3.1415,
					2.7176,
					99999,
					88888
				],
				"Now another item"
			],
		],
		"Quantum statistical mechanics"
	],
	"Optics and acoustics",
	"Condensed matter physics",
	"High-energy particle physics and nuclear physics",
]
```

_Output :_

---

1. __Classical mechanics__

	1. Newton's law of motion

	2. Lagrangian Mechanics

3. _Thermodynamics and statistical mechanics_

4. Electromagnetism and photonics

5. Relativistic mechanics

6. Quantum mechanics, atomic physics, and molecular physics

	* Schrödinger equation

	* Quantum field theory

		1. Lists can be nested :)

		2. This is another liner

			1. ~~Oh this is getting serious~~

			2. And now bunch of numbers

				1. 3.1415

				2. 2.7176

				3. 99999

				4. 88888

			4. Now another item

	* Quantum statistical mechanics

8. Optics and acoustics

9. Condensed matter physics

10. High-energy particle physics and nuclear physics

---

---

### Table



```python
md < {
	"Name" : ["Albert", "Paul" | md.bold, "Richard"],
	"Surname" : ["Einstein" | md.italic, "Dirac" , "Feynman" | md.italic],
}
```

_Output :_

---

|Name|Surname|
|:---:|:---:|
|Albert|_Einstein_|
|__Paul__|Dirac|
|Richard|_Feynman_|

---

---

### Links



```python
md < "https://github.com/fbgencer/markdownipy" | md.link("Markdownipy website")
```

_Output :_

---

[Markdownipy website](https://github.com/fbgencer/markdownipy)

---

---

### Image



```python
md < ("markdownipy_logo.png" | md.image("Image name"))
```

_Output :_

---

![Image name](markdownipy_logo.png)

---

---

### Single line Quote



```python
md << ("With Great Power Comes Great Responsibility" | md.quote)
```

_Output :_

---

> With Great Power Comes Great Responsibility

---

---

### Task lists



```python
md < ["-", 
	"Take the key" | md.bold | md.task,
	"Cat food" | md.bold | md.task_check
]
```

_Output :_

---

- [ ] __Take the key__

- [x] __Cat food__

---

---

