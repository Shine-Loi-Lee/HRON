from my_parser import Parser

variables = {}
temp = 0

def is_declared(var_name): # Check if variable is declared
    return var_name in variables

def parse_command(command):
    parser = Parser(command)
    cmd = parser.next_token('command')

    # Variable
    if cmd == '해롱해롱': # Declare variable
        var_name = parser.next_token('variable')
        type = parser.next_token('type')
        value = parser.next_token(type)
        def declare():
            if not is_declared(var_name):
                variables[var_name] = value
            else:
                raise RuntimeError(f"Variable {var_name} is already declared.")
        parser.assert_end()
        return declare
    elif cmd == '해롱': # Initialize variable
        var_name = parser.next_token('variable')
        type = parser.next_token('type')
        value = parser.next_token(type)
        def initialize():
            if is_declared(var_name):
                variables[var_name] = value
            else:
                raise RuntimeError(f"Variable {var_name} is not declared.")
        parser.assert_end()
        return initialize
    
    # Input and Output
    elif cmd == '해해롱해롱': # Input
        var_name = parser.next_token('variable')
        def input_command():
            value = input()
            variables[var_name] = value
        parser.assert_end()
        return input_command
    elif cmd == '해롱해해롱': # Print
        var_name = parser.next_token('variable')
        def print_command():
            print(variables[var_name])
        parser.assert_end()
        return print_command
    
    # Arithmetic Operators
    elif cmd == '해롱해롱해': # Plus (+)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def plus():
            variables[var_name] = variables[var1] + variables[var2]
        parser.assert_end()
        return plus
    elif cmd == '해롱롱해': # Minus (-)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def minus():
            variables[var_name] = variables[var1] - variables[var2]
        parser.assert_end()
        return minus
    elif cmd == '해롱해롱해롱해': # Multiply (*)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def multiply():
            variables[var_name] = variables[var1] * variables[var2]
        parser.assert_end()
        return multiply
    elif cmd == '해롱롱해롱롱해': # Divide (//)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def divide():
            variables[var_name] = variables[var1] // variables[var2]
        parser.assert_end()
        return divide
    elif cmd == '해롱해롱해롱해롱해': # Power (**)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def power():
            variables[var_name] = variables[var1] ** variables[var2]
        parser.assert_end()
        return power
    elif cmd == '해롱롱해해롱해': # Modulus (%)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def modulus():
            variables[var_name] = variables[var1] % variables[var2]
        parser.assert_end()
        return modulus
    
    # Relational Operators
    elif cmd == '해해롱롱해해': # Equal (==)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def equal():
            variables[var_name] = variables[var1] == variables[var2]
        parser.assert_end()
        return equal
    elif cmd == '해해롱롱해롱': # Not equal (!=)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def not_equal():
            variables[var_name] = variables[var1] != variables[var2]
        parser.assert_end()
        return not_equal
    elif cmd == '해롱해롱롱해롱': # Greater than (>)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def greater_than():
            variables[var_name] = variables[var1] > variables[var2]
        parser.assert_end()
        return greater_than
    elif cmd == '해롱롱롱해롱해': # Less than (<)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def less_than():
            variables[var_name] = variables[var1] < variables[var2]
        parser.assert_end()
        return less_than
    elif cmd == '해롱해롱롱해해': # Greater than or equal to (>=)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def greater_than_or_equal_to():
            variables[var_name] = variables[var1] >= variables[var2]
        parser.assert_end()
        return greater_than_or_equal_to
    elif cmd == '해해롱롱해롱해': # Less than or equal to (<=)
        var1 = parser.next_token('variable')
        var2 = parser.next_token('variable')
        var_name = parser.next_token('variable')
        def less_than_or_equal_to():
            variables[var_name] = variables[var1] <= variables[var2]
        parser.assert_end()
        return less_than_or_equal_to
    
    # Conditional Statements
    elif cmd == '해롱해롱롱해': # if statement
        commands_block_list = []
        else_block = []
        
        def parse_if(condition_var):
            commands_block = []
            while True:
                code_block = input(">> ")
                if_parser = Parser(code_block)
                cmd = if_parser.next_token('command')
                if cmd=="롱롱":
                    if_parser.assert_end()
                    break
                elif cmd=="해롱해롱롱해롱": # elif statement
                    if_condition_var = if_parser.next_token('variable')
                    if_parser.assert_end()
                    parse_if(if_condition_var)
                    return
                elif cmd=="해롱해롱롱해롱해롱": # else statement
                    if_parser.assert_end()
                    while True:
                        code_block = input(">> ")
                        else_parser = Parser(code_block)
                        if else_parser.next_token('command')=="롱롱":
                            else_parser.assert_end()
                            break
                        else_block.append(parse_command(code_block))
                    return
                commands_block.append(parse_command(code_block))
            commands_block_list.append([condition_var,commands_block])
        
        if_condition_var = parser.next_token('variable')
        parse_if(if_condition_var)

        parser.assert_end()
        def if_statement():
            for condition_var, commands_block in commands_block_list:
                if variables[condition_var]:
                    for code_block in commands_block:
                        code_block()
                    break
            else:
                for code_block in else_block:
                    code_block()
        return if_statement
    elif cmd == '해롱해롱롱해롱': # elif statement
        raise RuntimeError("Unexpected command: elif should be inside if block")
    elif cmd == '해롱해롱롱해롱해롱': # else statement
        raise RuntimeError("Unexpected command: else should be inside if block")

    # Loop
    elif cmd == '해롱롱롱': # for loop
        commands_block = []

        i_var = parser.next_token('variable')
        start_var = parser.next_token('variable')
        end_var = parser.next_token('variable')
        step_var = parser.next_token('variable')

        while True:
            code_block = input(">> ")
            loop_parser = Parser(code_block)
            if loop_parser.next_token('command')=="롱롱":
                loop_parser.assert_end()
                break
            commands_block.append(parse_command(code_block))

        def for_loop():
            variables[i_var] = variables[start_var]
            while variables[i_var] < variables[end_var]:
                for code_block in commands_block:
                    code_block()

                variables[i_var] += variables[step_var]
        parser.assert_end()
        return for_loop
    else:
        raise RuntimeError(f"Unexpected command: {cmd}")



if __name__ == "__main__":
    while True:
        code = input("> ")
        parser = Parser(code)
        if parser.next_token('command')=="해로온이라": # Quit command
            parser.assert_end()
            break

        try:
            cmd = parse_command(code)
            cmd()

        except Exception as e:
            print(f"Error: {e}")
