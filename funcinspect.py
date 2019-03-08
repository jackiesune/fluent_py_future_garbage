#funcinspect.py



def clip(text,max_len=30):
    length=len(text)
    end=None
    if length>max_len:
        ind=text.rfind(' ',0,max_len)
        if  ind<0:
            ind=text.rfind(' ',max_len)

    end=ind if ind >0 else max_len
    return text[:end].strip()
    
    


