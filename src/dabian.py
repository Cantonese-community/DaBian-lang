###########################################
#        Generated by Cantonese           #
###########################################
# Run it by 'cantonese src/dabian.py -build' 
import re
class Lexer(object):
	def __init__(self, 代码, 关键字):
		self. code = 代码
		self. keywords = 关键字
		self. line = 1
		self.re_number = r"^0[xX][0-9a-fA-F]*(\.[0-9a-fA-F]*)?([pP][+\-]?[0-9]+)?|^[0-9]*(\.[0-9]*)?([eE][+\-]?[0-9]+)?"
		self.re_new_line = re.compile(r"\r\n|\n\r|\n|\r")
		self.re_id = r"^[_\d\w]+|^[\u4e00-\u9fa5]+"
		self.re_str = r"(?s)(^'(\\\\|\\'|\\\n|\\z\s*|[^'\n])*')|(^\"(\\\\|\\\"|\\\n|\\z\s*|[^\"\n])*\")"
		self.re_expr = r"[(](.*?)[)]"
	def 跳过(self, n):
		self. code = self. code[n:]
	def 识别空格(self, c):
		return c in ('\t', '\n', '\v', '\f', '\r', ' ')
	def 识别换行(self, c):
		return c in ('\r', '\n')
	def 识别中文字(self, word):
		for i in range(0,word .__len__()):
			if  '\u4e00' <= word[i] <= '\u9fff' :
				return 啱
		return 唔啱
	def 扫描(self, 模式):
		m = re.match(模式, self. code)
		if m:
			Token = m.group()
			self. 跳过(Token .__len__())
			return Token
	def 扫描标识符(self):
		return self. 扫描(self. re_id)
	def 扫描数字(self):
		return self. 扫描(self. re_number)
	def 扫描字符串(self):
		return self. 扫描(self. re_str)
	def 扫描表达式(self):
		return self. 扫描(self. re_expr)
	def 检查(self, s):
		return self. code.startswith(s)
	def 跳过空格换行(self):
		while not (self. code .__len__() <= 0):
			if self. 检查('\r\n') or self. 检查('\n\r'):
				self. 跳过(2)
				self. line = self. line + 1
			elif self. 识别换行(self. code[0]):
				self. 跳过(1)
				self. line = self. line + 1
			elif self. 检查('?') or self. 检查(':') or self. 检查('：') or \
            self. 检查('？') or self. 检查('!') or self. 检查('！') or \
            self. 检查(','):
				self. 跳过(1)
			elif self. 识别空格(self. code[0]):
				self. 跳过(1)
			else:
				break
	def 获取token(self):
		self. 跳过空格换行()
		if self. code .__len__() == 0:
			return [self. line, ['EOF', 'EOF']]
		c = self. code[0]
		if c == '-':
			if self. 检查('->'):
				self. 跳过(2)
				return [self. line, ['keyword', '->']]
		if c == '{':
			self. 跳过(1)
			return [self. line, ['keyword', '{']]
		if c == '}':
			self. 跳过(1)
			return [self. line, ['keyword', '}']]
		if c in ('\'', "\""):
			return [self. line, ['string', self. 扫描字符串()]]
		if c == '(':
			return [self. line, ['expr', self. 扫描表达式()]]
		if self. 识别中文字(c) or c == '_' or c.isalpha():
			token = self. 扫描标识符()
			if token in self. keywords:
				return [self. line, ['keyword', token]]
			return [self. line, ['identifier', token]]
		if c == '.' or c.isdigit():
			token = self. 扫描数字()
			return [self. line, ['num', token]]
class AST(object):
	pass
class PrintAST(AST):
	def __init__(self, args):
		self.args = args
	def 生成代码(self):
		if 身位(self. args, 0) == 'string' or 身位(self. args, 0) == 'num' or \
          身位(self. args, 0) == 'identifier':
			return "print(" + 身位(self. args, 1) + ")" + "\n"
		elif 身位(self. args, 0) == 'expr':
			return "print" + 身位(self. args, 1) + "\n"
class InputAST(AST):
	def __init__(self, value, str):
		self.value = value
		self.str = str
	def 生成代码(self):
		return self. value + "=input(" + self. str + ")" + "\n"
class AssignAST(AST):
	def __init__(self, KeyList, ValueList):
		self.KeyList = KeyList
		self.ValueList = ValueList
	def 生成代码(self):
		ret = ""
		for i in range(0,self. KeyList .__len__()):
			ret = ret + 身位(self. KeyList, i) + '=' + 身位(self. ValueList, i) + '\n'
		return ret
class FunctionDefAST(AST):
	def __init__(self, FuncName, Args, Body):
		self.FuncName = FuncName
		self.Args = Args
		self.Body = Body
	def 生成代码(self):
		if self. Args .__len__() == 0:
			return "def " + self. FuncName + "():" + '\n'
		else:
			return "def " + self. FuncName + self. Args + ":\n"
class FunctionCallAST(AST):
	def __init__(self, FuncName, Args):
		self.FuncName = FuncName
		self.Args = Args
	def 生成代码(self):
		if self. Args .__len__() == 0:
			return self. FuncName + "()" + '\n'
		else:
			return self. FuncName + self. Args + "\n"
class ReturnAST(AST):
	def __init__(self, val):
		self.val = val
	def 生成代码(self):
		return "return " + self. val + "\n"
class WhileAST(AST):
	def __init__(self, Cond, Body):
		self.Cond = Cond
		self.Body = Body
	def 生成代码(self):
		return "while " + self. Cond + ":" + "\n"
class IfAST(AST):
	def __init__(self, Cond, Body):
		self.Cond = Cond
		self.Body = Body
	def 生成代码(self):
		return "if " + self. Cond + ":" + "\n"
class ElifAST(AST):
	def __init__(self, Cond, Body):
		self.Cond = Cond
		self.Body = Body
	def 生成代码(self):
		return "elif " + self. Cond + ":" + "\n"
class ElseAST(AST):
	def __init__(self, Body):
		self.Body = Body
	def 生成代码(self):
		return "else:\n"
def get_token_list(code, keywords):
	lex = Lexer(code, keywords)
	tokens = []
	while not (唔啱):
		token = lex.获取token()
		tokens.append(token)
		if token[1] == ['EOF', 'EOF']:
			break
	return tokens
class Parser(object):
	def __init__(self, tokens, Node):
		self. tokens = tokens
		self. pos = 0
		self. Node = Node
	def get(self, offset, get_line = 唔啱):
		if self. pos + offset >= self. tokens .__len__():
			return ["", ""]
		if get_line:
			return 身位(self. tokens, self. pos + offset, 0)
		return 身位(self. tokens, self. pos + offset, 1)
	def skip(self, offset):
		self. pos = self. pos + offset
	def match(self, name):
		if self. get(0)[1] in name:
			self. pos = self. pos + 1
			return 啱
		return 唔啱
	def match_type(self, name):
		if self. get(0)[0]  in  name:
			self. skip(1)
			return 啱
		return 唔啱
	def parse(self):
		while not (唔啱):
			if self. match(["捅了老挝", "没想到捅了老挝"]):
				if not self. match(['->']):
					raise "Excepted '->' in print statement."
				self. Node.append(PrintAST(self. get(0)))
				self. skip(1)
			elif self. match(["抓个小贼", "本以为抓个小贼"]):
				if not self. match(['->']):
					raise "Excepted '->' in input statement."
				AssignExpr = self. get(0)[1]
				if not (',' in AssignExpr):
					self. Node.append(InputAST(self. AssignExpr[1:-1], ""))
				else:
					self. Node.append(InputAST(AssignExpr[1 : AssignExpr.index(',')], 
                                             AssignExpr[AssignExpr.index(',') + 1 : -1]))
				self. skip(1)
			elif self. match(["答辩", "依托答辩"]):
				if not self. match(['{']):
					raise "Excepted '{' in assign statement."
				KeyList = []
				ValueList = []
				t = 0
				while not (self. get(0)[1] == '}'):
					t = t + 1
					if t & 1:
						KeyList.append(self. get(0)[1])
					else:
						ValueList.append(self. get(0)[1])
					self. skip(1)
				self. skip(1)
				self. Node.append(AssignAST(KeyList, ValueList))
			elif self. match(["功夫是这样的"]):
				if not self. match_type('identifier'):
					raise "Excepted identifier type in function define statement."
				FuncName = self. get(-1)[1]
				FuncArgs = ""
				if self. get(0)[0] == 'expr':
					FuncArgs = self. get(0)[1]
					self. skip(1)
				self. skip(1)
				FuncBody = []
				FuncBodyNode = []
				while not (身位(self. get(0), 1) == "任何邪恶终将绳之以法"):
					FuncBody.append([self. get(0, 啱), self. get(0)])
					self. skip(1)
				self. skip(1)
				p = Parser(FuncBody, FuncBodyNode)
				p.parse()
				self. Node.append(FunctionDefAST(FuncName, FuncArgs, p.Node))
			elif self. match(["绳之以法"]):
				if not self. match(['->']):
					raise "Excepted '->' in Functin call statement."
				FuncName = self. get(0)[1]
				self. skip(1)
				FuncArgs = ""
				if self. get(0)[0] == 'expr':
					FuncArgs = self. get(0)[1]
					self. skip(1)
				self. Node.append(FunctionCallAST(FuncName, FuncArgs))
			elif self. match(["此地答辩"]):
				val = ""
				if self. get(0)[0] == 'expr':
					val = self. get(0)[1]
					self. skip(1)
				self. Node.append(ReturnAST(val))
			elif self. match(["不是"]):
				Cond = self. get(0)[1]
				self. skip(1)
				if not self. match("的我不吃"):
					raise "Excepted '的我不吃' in while statement. "
				if not self. match("->"):
					raise "Excepted '->' in while statement. "
				WhileBody = []
				WhileBodyNode = []
				while not (self. get(0)[1] == "因为是良心的中国制造"):
					WhileBody.append([self. get(0, 啱), self. get(0)])
					self. skip(1)
				self. skip(1)
				p = Parser(WhileBody, WhileBodyNode)
				p.parse()
				self. Node.append(WhileAST(Cond, p.Node))
			else:
				break
TO_PY_CODE = ""
def trans(Nodes, TAB = '', label = ''):
	global TO_PY_CODE
	TAB = '' if (label != "if" and label != "func" and label != "while") else TAB
	for i in range(0,Nodes .__len__()):
		if Nodes[i].__class__.__name__ == "PrintAST":
			TO_PY_CODE = TO_PY_CODE + TAB + Nodes[i].生成代码()
		elif Nodes[i].__class__.__name__ == "InputAST":
			TO_PY_CODE = TO_PY_CODE + TAB + Nodes[i].生成代码()
		elif Nodes[i].__class__.__name__ == "AssignAST":
			TO_PY_CODE = TO_PY_CODE + TAB + Nodes[i].生成代码()
		elif Nodes[i].__class__.__name__ == "FunctionDefAST":
			TO_PY_CODE = TO_PY_CODE + TAB + Nodes[i].生成代码()
			trans(Nodes[i].Body, TAB + '\t', label = "func")
		elif Nodes[i].__class__.__name__ == "WhileAST":
			TO_PY_CODE = TO_PY_CODE + TAB + Nodes[i].生成代码()
			trans(Nodes[i].Body, TAB + '\t', label = "while")
		elif Nodes[i].__class__.__name__ == "FunctionCallAST":
			TO_PY_CODE = TO_PY_CODE + TAB + Nodes[i].生成代码()
		elif Nodes[i].__class__.__name__ == "ReturnAST":
			TO_PY_CODE = TO_PY_CODE + TAB + Nodes[i].生成代码()
关键字 = {
  "捅了老挝", "没想到捅了老挝",
  "抓个小贼", "本以为抓个小贼",
  "依托答辩", "答辩", "功夫是这样的", "此地答辩",
  "任何邪恶终将绳之以法", "绳之以法",
  "要是", "跟我zs", "你这是违法行为",
  "不是", "的我不吃", "因为是良心的中国制造"
}
import sys
try:
	ctx = 读取(开份文件(身位(sys.argv, 2), 解码 = 'utf-8'))
	print(身位(sys.argv, 2))
except FileNotFoundError:
	print("Can not find the path: " + sys.argv[2])
tk_list = get_token_list(ctx, 关键字)
print(tk_list)
parse = Parser(tk_list, [])
parse.parse()
trans(parse.Node)
print(TO_PY_CODE)
exec(TO_PY_CODE)