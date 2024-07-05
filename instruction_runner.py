from console_dict import add_word as add, update_meaning as upd, find_word as fnd, words

def execute_instruction(cmd, *args):
    if cmd == "add":
        return add(word=args[0], meaning=args[1])
    
    elif cmd == "update":
        return upd(word=args[0], meaning=args[1])

    elif cmd == "find":
        return fnd(args[0])
    


print(execute_instruction("add", "keyword", "word with special meaning in a language"))

print(execute_instruction("add", "while", "keyword that repeats code"))

print(execute_instruction("update", "while", "keyword that repeats code until condition is true"))

print(execute_instruction("find", "keyword"))

print(execute_instruction("find", "while"))

print(execute_instruction("find", "for"))