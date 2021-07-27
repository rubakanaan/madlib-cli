import re

def read_template(filepath: str):
    with open(filepath,'r') as file:
      file_content=file.read()
      file.close()
    return file_content.strip()



def parse_template(text :str):
    
    parts=[]
    strippedText= text.format(Adjective='{}' ,Noun='{}')
    res = re.findall(r'\{.*?\}', text)
    for i in res:
        parts.append(i.strip("{ }"))
    parts=tuple(parts)
    return strippedText,parts
   
def merge(text: str , parts :tuple):
    mergedText=text.format(*parts)
    return mergedText

if __name__ == "__main__":
    print("Welcome to Madlib Game")
    print("Please enter some words to play the game!")
wordLst=[]
