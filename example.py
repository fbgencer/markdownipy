import markdownipy

md = markdownipy.markdownipy()


md << ("Markdownipy" | md.h1)
md < ("markdownipy_logo.png" | md.image)
md < "Markdownipy is a simple library to create fast markdown files using only two operators"
md < " '<' sends text to markdown file, '|' just gives property to the text"
md < "Even this README file is written with markdownipy!"

md < "Motivation" | md.h2
md < md.hline
md < """
Lately, I'm trying to generate markdown documentations for different codes and I needed to put
some specs, numbers etc. Instead of text manipulation I just wanted to make it as a library.
Sometimes I also forget markdown syntax, so this library is intended as easy as its suppose to be.
"""

md < """
md = markdownipy.markdownipy()
""" | md.codeb("python")


#Headers
md < "Headers" | md.h3
c = """
md < "This is header1" | md.h1
md < "This is header2" | md.h2
md < "This is header3" | md.h3
md < "This is header4" | md.h4
md < "This is header5" | md.h5
md < "This is header6" | md.h6
"""
md < c | md.codeb("python")
md < "Running the above code gives:" | md.italic
exec(c)
md < md.hline

#Text props
md < "Bold, italic, strikethrough texts" | md.h3
c = """
md < "This should be a bold text" | md.bold
md < "This is an italic text" | md.italic
md < "Strikethrough is banned"  | md.strike
"""
md < c | md.codeb("python")
md < "Running the above code gives:" | md.italic
exec(c)
md < md.hline

#Lists
md < "Lists" | md.h3
c = """
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
"""
md < c | md.codeb("python")
md < "Running the above code gives:" | md.italic
exec(c)
md < md.hline


# md.table()

#Table
md < "Table" | md.h3
c = """
md < {
	"Name" : ["Albert", "Paul" | md.bold, "Richard"],
	"Surname" : ["Einstein" | md.italic, "Dirac" , "Feynman" | md.italic],
}
"""
md < c | md.codeb("python")
md < "Running the above code gives:" | md.italic
exec(c)
md < md.hline



#Link
md < "Links" | md.h3
c = """
md < "https://github.com/fbgencer/markdownipy" | md.link("Markdownipy website")
"""
md < c | md.codeb("python")
md < "Running the above code gives:" | md.italic
exec(c)
md < md.hline


#Image
md < "Image" | md.h3
c = """
md < ("markdownipy_logo.png" | md.image("Image name"))
"""
md < c | md.codeb("python")
md < "Running the above code gives:" | md.italic
exec(c)
md < md.hline


#Quote
md < "Single line Quote" | md.h3
c = """
md << ("With Great Power Comes Great Responsibility" | md.quote)
"""
md < c | md.codeb("python")
md < "Running the above code gives:" | md.italic
exec(c)
md < md.hline


#Task lists
md < "Task lists" | md.h3
c = """
md < ["-", 
	"Take the key" | md.bold | md.task,
	"Cat food" | md.bold | md.task_check
]
"""
md < c | md.codeb("python")
md < "Running the above code gives:" | md.italic
exec(c)
md < md.hline



md >> "README"







# md < "quote" | md.quote

# md < "fbgencer" | md.chapter




# # Table of Contents
# # ==

# # - [Overview](#overview)
# # - [Features](#features)
# #     - [Writing and Reading Files](#writing-and-reading-files)
# #     - [Markdown](#markdown)    
# # - [Installation](#installation)
# # - [Markdown File Example](#markdown-file-example)
