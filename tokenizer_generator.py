import re
grammar_file = open("grammar.txt", "r")

grammar = dict()

#Grammar: {RULE: [[OPTION1], [OPTION2]]}
pattern = re.compile("<.*?>")
for line in grammar_file:
	split = [x.strip() for x in line.split(":")]
	if len(split) < 2: continue
	
	if(split[0] != ''):
		rule_name = split[0]
		grammar[rule_name] = []
	rule_body = split[1].split()#[x.strip() for x in pattern.findall(split[1])]
	
	print("rule name"+str(rule_name))
	print("RULe_body"+str(rule_body))
	
	grammar[rule_name].append(rule_body)
	
print(grammar)