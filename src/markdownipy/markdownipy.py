__version__ = "1.0.0"
__VERSION__ = __version__

class markdownipy:

	class lineprop:
		def __init__(self,format,callable_format=None,on_text=lambda f:f):
			self.line_format = format
			self.line_format_c = callable_format
			self.line_format_c_temp = None
			self.on_text=on_text
		
		def __or__(self,t):
			t = self.on_text(t)
			if(self.line_format_c_temp != None):
				s = self.line_format_c_temp
				self.line_format_c_temp = None
				return s.replace('{t}',str(t))
			return self.line_format.replace('{t}',str(t))
		def __ror__(self,t):
			t = self.on_text(t)
			if(self.line_format_c_temp != None):
				s = self.line_format_c_temp
				self.line_format_c_temp = None
				return s.replace('{t}',str(t))
			return self.line_format.replace('{t}',str(t))

		def __call__(self, *args, **kwargs):
			assert(len(args) > 0 or self.line_format_c == None)
			self.line_format_c_temp = self.line_format_c
			for i in range(len(args)):
				s = '{' + f'args[{i}]' + '}'
				arg = args[i]
				self.line_format_c_temp = self.line_format_c_temp.replace(s,str(arg))
			return self
			

	bold = lineprop("__{t}__")
	b = bold
	italic = lineprop("_{t}_")
	i = italic
	strike = lineprop("~~{t}~~")

	code = lineprop('`{t}`')
	codeb = lineprop('```{t}```','```{args[0]}{t}```')
	h1 = lineprop('#'*1+' {t}')
	h2 = lineprop('#'*2+' {t}')
	h3 = lineprop('#'*3+' {t}')
	h4 = lineprop('#'*4+' {t}')
	h5 = lineprop('#'*5+' {t}')
	h6 = lineprop('#'*6+' {t}')

	chapter = lineprop('{t}\n===')

	hline = lineprop('---')
	link = lineprop('<{t}>','[{args[0]}]({t})')
	image = lineprop('![]({t})','![{args[0]}]({t})')

	#lineprop('','')
	ref = lineprop('','[{args[0]}]({t})',on_text=lambda t:t.lower().replace(' ','-'))

	_list = lineprop('','{args[0]}{args[1]} {t}')

	para = lineprop('{t}\n\n','')
	task = lineprop('[ ] {t}')
	task_check = lineprop('[x] {t}')

	quote = lineprop("> {t}")

	available_bullets = ['*','-']

	def __init__(self):
		self.doc = ""
		self.indent = 0
	
	def __lshift__(self,x):
		"""
			<< operator on md
			Puts stuff on string document
		"""
		if(isinstance(x,str)):
			self.put(x | self.para)
		elif(isinstance(x,list)):
			self.lists(x)
		elif(isinstance(x,self.lineprop)):
			self << str(x.line_format) # careful for recursive
		elif(isinstance(x,dict)):
			self.table(x)
		else:
			assert(0)

	def __rshift__(self,file_name):
		"""
			Filename can be string with md or just a name
			sys.stdout is also allowed for printing
		"""
		import sys
		if(isinstance(file_name,str)):
			if(not file_name.endswith(".md")):
				file_name += ".md"
			with open(file_name,"w+") as f:
				f.write(self.doc)
		elif(file_name == sys.stdout):
			file_name.write(self.doc)
		else:
			raise Exception("file_name can be string or sys.stdout")

	def __lt__(self,x):
		"""
			< operator on md
			just calls the main operator '<<'
		"""
		return self << x
	
	def __gt__(self,x):
		"""
			> operator on md
			just calls the main operator '>>'
		"""
		return self >> x

	def put(self,x):
		"""
			Just adds items to string doc
		"""
		self.doc += x
	
	def print(self):
		"""
			Returns the doc
		"""
		return self.doc

	def bullets(self,str_list,bullet_type='-'):
		ls = [bullet_type,*str_list]
		return self << ls

	def lists(self,str_list):
		x = str_list
		assert(len(x))
		#if(not isinstance(x[0],str)):
		bullet_type = None
		if(x[0] in self.available_bullets):
			#This is bullet'in header, don't put number
			bullet_type = x[0]
			x = x[1:]
		for ln in range(0,len(x)):
			if(isinstance(x[ln],list)):
				f = x[ln]
				self.indent += 1
			else:
				if(bullet_type != None):
					f = x[ln] | self._list("\t"*self.indent,bullet_type)
				else:
					f = x[ln] | self._list("\t"*self.indent,str(ln+1)+".")

			self << f
		if(self.indent > 0):
			self.indent -= 1

	def img(self,img_path):
		return self << (img_path | self.img)

	def table(self, table_dict):
		values = list(table_dict.values())
		n_rows = len(values[0])
		n_cols = len(table_dict.keys())
		
		form = "|%s"
		form = (form * n_cols) + "|"
		#Now we only support centeral alignment
		hypens = ":---:"

		header_line = ( form ) % tuple(table_dict.keys()) 
		hypens_line = ( form ) % tuple([hypens]*n_cols)

		self.put(header_line+'\n')
		self.put(hypens_line+'\n')

		for i in range(n_rows):
			rowline = []
			for j in range(n_cols):
				#print(values[j][i])
				rowline.append(str(values[j][i]))
			self.put(form % tuple(rowline) + '\n')

		self.put("\n")

	def clear(self):
		"""
			Clears the document
		"""
		self.doc = ""
