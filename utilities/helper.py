import pyperclip

def extract_code_section(md_content, code_url):
    start_pattern = f"[copy code]({code_url})"
    end_pattern = "```"

    start_index = md_content.find(start_pattern)
    if start_index == -1:
        return None  # URL not found

    start_index = md_content.find(end_pattern, start_index)
    if start_index == -1:
        return None  # Closing code block not found

    start_index += len(end_pattern)  # Move to the end of the first code block delimiter

    end_index = md_content.find(end_pattern, start_index)
    if end_index == -1:
        return None  # Second closing code block not found

    code_section = md_content[start_index:end_index]
    
    # Split the string into lines
    line = code_section.split('\n')
    return '\n'.join(line[1:]).strip()
	#return '\n'.join(lines[1:]).strip()
	

def copyToClipboard(text_to_copy):
	pyperclip.copy(text_to_copy)
    

def readSectionStringContent(file):
    content = ''
    with open(f'./mdfiles/{file}','r') as fp:
        data = fp.readlines()[2:]
        for string in data :
            content += string
    return content


def schemeOfWork():
    
    return {
        "1" : [
            {
                "topic":"introduction",
                "link":"",
                "file_name":"introduction.md",
                "question_link":"",
                "question_name":"introduction"
            },
            {
                "topic":"Setup",
                "link":"",
                "file_name":"setup.md",
                "question_link":"",
                "question_name":"setup"
            },
            {
                "topic":"JS Syntax & Data Types",
                "link":"",
                "file_name":"syntax.md",
                "question_link":"",
                "question_name":"syntax"
            }
        ],
        "2": [
            {
                "topic":"Variables",
                "link":"",
                "file_name":"variable.md",
                "question_link":"",
                "question_name":"variable"
            },
            {
                "topic":"Operators & Expression",
                "link":"",
                "file_name":"operators.md",
                "question_link":"",
                "question_name":"operators"
            }
        ],
        "3" : [
            {
                "topic":"Conditional Statement",
                "link":"",
                "file_name":"conditional.md",
                "question_link":"",
                "question_name":"conditional"
            },
            {
                "topic":"Loops",
                "link":"",
                "file_name":"loops.md",
                "question_link":"",
                "question_name":"loops"
            },
            {
                "topic":"Functions",
                "link":"",
                "file_name":"functions.md",
                "question_link":"",
                "question_name":"functions"
            },
        ],

        "4" : [
            {
                "topic":"Arrays",
                "link":"",
                "file_name":"arrays.md",
                "question_link":"",
                "question_name":"arrays"
            },
            {
                "topic":"Objects",
                "link":"",
                "file_name":"objects.md",
                "question_link":"",
                "question_name":"objects"
            }
        ],

        "5" : [
            {
                "topic":"Strings as Object",
                "link":"",
                "file_name":"strings.md",
                "question_link":"",
                "question_name":"strings"
            },
            {
                "topic":"Math",
                "link":"",
                "file_name":"math.md",
                "question_link":"",
                "question_name":"math"
            },
            {
                "topic":"Date",
                "link":"",
                "file_name":"date.md",
                "question_link":"",
                "question_name":"date"
            },
             {
                "topic":"Regular Expressions",
                "link":"",
                "file_name":"re.md",
                "question_link":"",
                "question_name":"regular_expression"
            }
        ],
        
        "6" : [
            {
                "topic":"Error Handling",
                "link":"",
                "file_name":"error_handling.md",
                "question_link":"",
                "question_name":None
            },
            {
                "topic":"Scope and Closures",
                "link":"",
                "file_name":"scope.md",
                "question_link":"",
                "question_name":"scope"
            }
        ],

        "7" : [
            {
                "topic":"ES6 and Modern JavaScript",
                "link":"",
                "file_name":"es6.md",
                "question_link":"",
                "question_name":"es6"
            },
            {
                "topic":"Advanced Arrays Methods",
                "link":"",
                "file_name":"array_iteration.md",
                "question_link":"",
                "question_name":"arrays"
            },
            {
                "topic":"Functional Programming",
                "link":"",
                "file_name":"f_programming.md",
                "question_link":"",
                "question_name":"functional_programming"
            },
            {
                "topic":"Functional Programming With Array",
                "link":"",
                "file_name":"array_in_fprogramming.md",
                "question_link":"",
                "question_name":None
            }
        ],

        "8" : [
            {
                "topic":"Asynchronous JavaScript",
                "link":"",
                "file_name":"asyncode.md",
                "question_link":"",
                "question_name":"asyncode"
            },
            {
                "topic":"Object Oriented Programming",
                "link":"",
                "file_name":"oop.md",
                "question_link":"",
                "question_name":"oop"
            },
            {
                "topic":"Modules and Modularization",
                "link":"",
                "file_name":"modular.md",
                "question_link":"",
                "question_name":None
            },
            {
                "topic":"Round Up",
                "link":"",
                "file_name":"section_roundup.md",
                "question_link":"",
                "question_name":None
            }
        ],


    }


def sectionalSummary():
    
    return {
    
        "1":{
            'file_name':"section1.md",
            "previous_file":None,
            "next_file": "introduction.md"
        },
        "2":{
            'file_name':"section2.md",
            "previous_file":"operators.md",
            "next_file": "conditional.md"
        },
        "3":{
            'file_name':"section3.md",
            "previous_file":"functions.md",
            "next_file": "arrays.md"
        },
        "4":{
            'file_name':"section4.md",
            "previous_file":"objects.md",
            "next_file": "strings.md"
        },
        "5":{
            'file_name':"section5.md",
            "previous_file":"date.md",
            "next_file": "re.md"
        },
        "6":{
            'file_name':"section6.md",
            "previous_file":"scope.md",
            "next_file": "es6.md"
        },
         "7":{
            'file_name':"section7.md",
            "previous_file":"array_in_fprogramming.md",
            "next_file": "asyncode.md"
        },
        "8":{
            'file_name':"section8.md",
            "previous_file":"modular.md",
            "next_file": None
        }
    }