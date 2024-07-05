from instruction_runner import execute_instruction as exe

cmd = input().split(':')

while cmd[0] != 'exit':
    data = exe(*cmd)
    print(data)

    cmd = input().split(':')