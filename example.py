import src.markdownipy.markdownipy as markdownipy

md = markdownipy.markdownipy()

md << ("Markdownipy" | md.h1)
md < ("markdownipy_logo.png" | md.image)
md < "Markdownipy is a simple Python library to generate fast markdown files using only two operators and some helpers"
md < " `<` writes text to markdown file, `|` just gives property to the text" | md.h2
md < "Even this README file is genereted by markdownipy!"
md < "./example.py" | md.link("Checkout example file")

md < "Motivation" | md.h2
md < md.hline
md < """
Lately, I'm trying to write markdown documentations for different codes and I needed to put
some specs, numbers etc. so just copy-paste some tables, links.
I was trying to change some predefined strings to speed up my writing process, yet
instead of text manipulation I just wanted to make it as a library.

Sometimes I also forget markdown syntax, so this library requires no memory (I hope so) :)
Only requirement is remember properties of markdown and the rest will be handled
"""

md < md.hline
md < "Install" | md.h3
md < "pip install markdownipy" | md.code
md < md.hline
#Quick start
md < "Quick start" | md.h3
c = """
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
md < "markdownipy_logo.png" | md.image

#Writing to a file, README or README.md both works!
md >> "README"
"""
md < c | md.codeb("python")
md < md.hline
md < md.hline





#We will call this function for each section
def add_section(section_name,section_note,code):
	md < section_name | md.h3
	md < section_note
	md < code | md.codeb("python")
	md < "Output :" | md.italic
	md < md.hline
	exec(code)
	md < md.hline
	md < md.hline	


#Headers
add_section("Headers","",
"""
md < "This is a chapter" | md.chapter
md < "This is header1" | md.h1
md < "This is header2" | md.h2
md < "This is header3" | md.h3
md < "This is header4" | md.h4
md < "This is header5" | md.h5
md < "This is header6" | md.h6
"""
)



#Text props
add_section("Bold, italic, strikethrough texts","",
"""
md < "This should be a bold text" | md.bold
md < "This is an italic text" | md.italic
md < "Strikethrough is banned"  | md.strike
""")

#Lists
add_section("Lists","","""
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
""")


#Table
add_section("Table","",
"""
md < {
	"Name" : ["Albert", "Paul" | md.bold, "Richard"],
	"Surname" : ["Einstein" | md.italic, "Dirac" , "Feynman" | md.italic],
}
""")


#Link
add_section("Links","",
"""
md < "https://github.com/fbgencer/markdownipy" | md.link("Markdownipy website")
""")

#Image
add_section("Image","","""
md < ("markdownipy_logo.png" | md.image("Image name"))
""")

#Quote
add_section("Single line Quote","","""
md << ("With Great Power Comes Great Responsibility" | md.quote)
""")



#Task lists
add_section("Task lists","",
"""
md < ["-", 
	"Take the key" | md.bold | md.task,
	"Cat food" | md.bold | md.task_check
]
""")


md >> "README"
