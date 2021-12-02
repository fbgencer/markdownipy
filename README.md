# Markdownipy

![](markdownipy_logo.png)

Markdownipy is a simple library to create fast markdown files using only two operators

 '<' sends text to markdown file, '|' just gives property to the text

Even this README file is written with markdownipy!

## Motivation

---


Lately, I'm trying to generate markdown documentations for different codes and I needed to put
some specs, numbers etc. Instead of text manipulation I just wanted to make it as a library.
Sometimes I also forget markdown syntax, so this library is intended as easy as its suppose to be.


```python
md = markdownipy.markdownipy()
```

### Headers

```python
md < "This is header1" | md.h1
md < "This is header2" | md.h2
md < "This is header3" | md.h3
md < "This is header4" | md.h4
md < "This is header5" | md.h5
md < "This is header6" | md.h6
```

_Running the above code gives:_

# This is header1

## This is header2

### This is header3

#### This is header4

##### This is header5

###### This is header6

---

### Bold, italic, strikethrough texts

```python
md < "This should be a bold text" | md.bold
md < "This is an italic text" | md.italic
md < "Strikethrough is banned"  | md.strike
```

_Running the above code gives:_

__This should be a bold text__

_This is an italic text_

~~Strikethrough is banned~~

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
				"Oh this is getting serious" | md.strike
			],
		],
		"Quantum statistical mechanics"
	],
	"Optics and acoustics",
	"Condensed matter physics",
	"High-energy particle physics and nuclear physics",
]
```

_Running the above code gives:_

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

	* Quantum statistical mechanics

8. Optics and acoustics

9. Condensed matter physics

10. High-energy particle physics and nuclear physics

---

### Table

```python
md < {
	"Name" : ["Albert", "Paul" | md.bold, "Richard"],
	"Surname" : ["Einstein" | md.italic, "Dirac" , "Feynman" | md.italic],
}
```

_Running the above code gives:_

|Name|Surname|
|:---:|:---:|
|Albert|_Einstein_|
|__Paul__|Dirac|
|Richard|_Feynman_|

---

### Links

```python
md < "https://github.com/fbgencer/markdownipy" | md.link("Markdownipy website")
```

_Running the above code gives:_

[Markdownipy website](https://github.com/fbgencer/markdownipy)

---

### Image

```python
md < ("markdownipy_logo.png" | md.image("Image name"))
```

_Running the above code gives:_

![Image name](markdownipy_logo.png)

---

### Single line Quote

```python
md << ("With Great Power Comes Great Responsibility" | md.quote)
```

_Running the above code gives:_

> With Great Power Comes Great Responsibility

---

### Task lists

```python
md < ["-", 
	"Take the key" | md.bold | md.task,
	"Cat food" | md.bold | md.task_check
]
```

_Running the above code gives:_

- [ ] __Take the key__

- [x] __Cat food__

---

