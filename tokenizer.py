current = ''
currentIndex = 0
input = ""
def tokenize(t_file):
	print("hi")

def tokenize(t_string):
	print("HI")

def increment():
	current = input[currentIndex]
	currentIndex += 1	
	
#{COMMENT}
def COMMENT():
	#: ; [{all subsequent characters up to a line ending}]
	match_string = ";"
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		#[{all subsequent characters up to a line ending}]		return True

	#: {NESTED_COMMENT}
	if(NESTED_COMMENT()):
		return True

	#: #; {INTERTOKEN_SPACE} {DATUM}
	match_string = "#;"
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		if(INTERTOKEN_SPACE()):
			if(DATUM()):
				return True

	return False

#{COMMENT_CONT}
def COMMENT_CONT():
	#: {NESTED_COMMENT} {COMMENT_TEXT}
	if(NESTED_COMMENT()):
		if(COMMENT_TEXT()):
			return True

	return False

#{COMMENT_TEXT}
def COMMENT_TEXT():
	#: [{character sequence not containing #| or |#}]
	#[{character sequence not containing #| or |#}]	return True

	return False

#{DELIMITER}
def DELIMITER():
	#: {WHITESPACE}
	if(WHITESPACE()):
		return True

	#: {VERTICAL_LINE}
	if(VERTICAL_LINE()):
		return True

	#: (
	match_string = "("
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#: )
	match_string = ")"
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#: "
	match_string = "\\""
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#:
	return True

	return False

#{DIRECTIVE}
def DIRECTIVE():
	#: #!fold-case
	match_string = "#!fold-case"
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#: #!no-fold-case
	match_string = "#!no-fold-case"
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	return False

#{INTRALINE_WHITESPACE}
def INTRALINE_WHITESPACE():
	#: {SPACE_OR_TAB}
	if(SPACE_OR_TAB()):
		return True

	return False

#{LINE_ENDING}
def LINE_ENDING():
	#: {NEWLINE}
	if(NEWLINE()):
		return True

	#: {RETURN} {NEWLINE}
	if(RETURN()):
		if(NEWLINE()):
			return True

	#: {RETURN}
	if(RETURN()):
		return True

	return False

#{NESTED_COMMENT}
def NESTED_COMMENT():
	#: [#| {COMMENT_TEXT} {COMMENT_CONT}* |#]
	#[#| {COMMENT_TEXT} {COMMENT_CONT}* |#]	return True

	return False

#{SPACE_OR_TAB}
def SPACE_OR_TAB():
	#: [\n]
	#[\n]	return True

	#: [\t]
	#[\t]	return True

	return False

#{TOKEN}
def TOKEN():
	#: {IDENTIFIER}
	if(IDENTIFIER()):
		return True

	#: {BOOLEAN}
	if(BOOLEAN()):
		return True

	#: {NUMBER}
	if(NUMBER()):
		return True

	#: {CHARACTER}
	if(CHARACTER()):
		return True

	#: {STRING}
	if(STRING()):
		return True

	#: (
	match_string = "("
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#: )
	match_string = ")"
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#: #\(
	match_string = "#\\("
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#: #u8(
	match_string = "#u8("
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#: '
	match_string = "'"
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#: `
	match_string = "`"
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#: ,
	match_string = ","
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#: ,@
	match_string = ",@"
	match = True
	for i in range(len(match_string)):
		if(current != match_string[i]):
			match = False
			continue
	if(match):
		return True

	#:
	return True

	return False

#{VERTICAL_LINE}
def VERTICAL_LINE():
	#: [|]
	#[|]	return True

	return False

#{WHITESPACE}
def WHITESPACE():
	#: {INTRALINE_WHITESPACE}
	if(INTRALINE_WHITESPACE()):
		return True

	#: {LINE_ENDING}
	if(LINE_ENDING()):
		return True

	return False

