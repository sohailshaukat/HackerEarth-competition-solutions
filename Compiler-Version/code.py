'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def text_parser(text):
    comment_flag = False
    position = 0
    while comment_flag != True and position < len(text)-1:
        if text[position]=='-' and text[position + 1]=='>':
            text = list(text)
            text[position] = '.'
            del text[position + 1]
            text = ''.join(text)
        if text[position]=='/' and text[position + 1]=='/':
            comment_flag = True
        position += 1
    return text
line = ''
code = []
while line != 'return 0;':
    try:
        line = input()
        code.append(line)
        new_line = text_parser(line)
        print(new_line)
    except:
        break;
    
