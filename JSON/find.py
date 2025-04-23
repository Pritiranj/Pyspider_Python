import pickle
d={'a':[12,23,34],'b':[20,34,55]}
with open('test2.txt','wb') as fobj:
    content=pickle.dumps(d)
    fobj.write(content)