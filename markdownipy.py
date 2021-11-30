import os,sys



class markdownipy:

	class emphasis:
		def __init__(self,start,end):
			self.start = start
			self.end = end
		
		def __or__(self,m):
			return self.start + m + self.end
		def __ror__(self,m):
			return self.start + m + self.end

	bold = emphasis("__","__")
	italic = emphasis("_","_")
	code = emphasis('`','`')
	codeb = emphasis('```','```')
	h1 = emphasis('#'*1+' ','')
	h2 = emphasis('#'*2+' ','')
	h3 = emphasis('#'*3+' ','')
	h4 = emphasis('#'*4+' ','')
	h5 = emphasis('#'*5+' ','')
	h6 = emphasis('#'*6+' ','')

	def __init__(self):
		print("Hello you have created me")
		self.doc = ""
	
	def __lshift__(self,x):
		if(isinstance(x,str)):
			self.doc += x + "\n\n"
		elif(isinstance(x,list)):
			for ln in range(len(x)):
				line = f"{ln+1}. {x[ln]}\n"
				self.doc += line + "\n\n"
	
	def __rshift__(self,file_name:str):
		if(not file_name.endswith(".md")):
			file_name += ".md"
		with open(file_name,"w+") as f:
			f.write(self.doc)

	def put(self,x):
		self << x

	def bullets(self,str_list,bullet_type='-'):
		for ln in str_list:
			line = f"{bullet_type} {ln}\n"
			self.put(line)

	def lists(self,str_list):
		for ln in range(len(str_list)):
			line = f"{ln+1}. {str_list[ln]}\n"
			self.put(line)

	def image(self,img_path):
		line = f"![foo]({img_path})"
		self.put(line)






md = markdownipy()

md << ("This is an header" | md.h1)
md << ("fbg" | md.italic)
md << ("This should be a code" | md.codeb)
md << """
	this is just a line :)
"""

md << [
	"Fbg1",
	"fbg2",
	"fbg3"
]


md.image("example_logo.png")
md >> "myexample"
 