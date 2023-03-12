#!/usr/bin/env python
# coding: utf-8

#written by 𝙽3𝙾𝙱_𝙷4𝙲𝙺𝙴𝚁

import pyfiglet
print ('𝙉 𝙏 𝘼𝙡𝙞𝙛 𝙎𝙝𝙚𝙞𝙠𝙝')
name=input("Enter Your Text: ")
name=str(name)
while True:
    try:
        style=input("Enter Your Style: ")
        style=str(style)
        word=pyfiglet.figlet_format(name,font=style)
        print(word)
    except Exception as e:
    	print("Wrong Font Style")
    	style=input("Enter Your Style: ")
    	style=str(style)
    	word=pyfiglet.figlet_format(name,font=style)
    	print(word)
