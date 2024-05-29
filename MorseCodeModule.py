class morseCode():
  
  def morse_dict(self):
    return {
    'a' : ". _" ,
    'b' : "_ . . .",
    'c' : "_ . _ .",
    'd' : "_ . .",
    'e' : ".",
    'f' : ". . _ .",
    'g' : "_ _ .",
    'h' : ". . . .",
    'i' : ". .",
    'j' : ". _ _ _",
    'k' : "_ . _",
    'l' : ". _ . .",
    'm' : "_ _",
    'n' : "_ .",
    'o' : "_ _ _",
    'p' : ". _ _ .",
    'q' : "_ _ . _",
    'r' : ". _ .",
    's' : ". . .",
    't' : "_",
    'u' : ". . _",
    'v' : ". . . _",
    'w' : ". _ _",
    'x' : "_ . . _",
    'y' : '_ . _ _',
    'z' : "_ _ . .",
    #Numbers
    '1' : ". _ _ _ _",
    '2' : ". . _ _ _",
    '3' : ". . . _ _",
    '4' : ". . . . _",
    '5' : ". . . . .",
    '6' : "_ . . . .",
    '7' : "_ _ . . .",
    '8' : "_ _ _ . .",
    '9' : "_ _ _ _ .",
    '0' : "_ _ _ _ _",
    #Special Characters
    ',' : "_ _ . . _ _",
    '?' : ". . _ _ . .",
    ':' : "_ _ _ . . .",
    '-' : "_ . . . . _",
    '"' : ". _ . . _ .",
    '(' : "_ . _ _ .",
    '=' : "_ . . . _",
    '*' : "_ . . _",
    '.' : ". _ . _ . _",
    ';' : "_ . _ . _ .",
    '/' : "_ . . _ .",
    "'" : ". _ _ _ _ .",
    '_' : ". . _ _ . _",
    ')' : "_ . _ _ . _",
    '+' : ". _ . _ .",
    '@' : ". _ _ . _ .",
    '!' : "_ . _ . _ .",
    #Space
    ' ' : "//"
    }
  
  def morseStringToInt(self,morseText):
    temp_arr = []

    for i in morseText:
      if i == ".":
        temp_arr.append(0)
      elif i == "_":
        temp_arr.append(1)
      else :
        pass

    return temp_arr
  
  def morseIntDict(self,morseText):
    newDict ={key : self.morseStringToInt(value) for key,value in morseText.items()}
    
    return newDict

if __name__ == '__main__':
  morseCode()