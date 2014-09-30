import sqlite3
import re
import datetime
from forms import foorms
class models():
    
    def gen(self,ur):
        
        con=sqlite3.connect('surl.db')
        q=''
        u=con.execute('select HEX,OURL from urls where OURL=?',(ur,))
        
        for i,j in u:
            d=str(j)
            if len(d)>1:
                return str(i)
        time=datetime.datetime.now()
        match=re.search('([\d]+)-([\d]+)-([\d]+)\s([\d]+):([\d]+):([\d]+).([\d]+)',str(time))
        if match:
            x=0
            for each in match.group(7):
                x=x+int(each)
            y1,x=incr(match.group(2),x)
            for each in match.group(6):
                x=x+int(each)
            y2,x=incr(match.group(1),x)
            y3,x=incr(match.group(3),x)
            y4,x=incr(match.group(4),x)
            y5,x=incr(match.group(5),x)
        h=dup(x+1,y1+y2+y3+y4+y5)
        x=x+1
        con.execute("INSERT INTO urls(HEX,OURL) \
                VALUES(?,?)",(h,ur));
        con.commit()
        return h
    def ret(self,un):
        con=sqlite3.connect('surl.db')
        v=con.execute('select OURL from urls where HEX=?',(un,))
        for each in v:
            f=each[0]
            break
        return str(f)
def incr(mg,y):
    a='abcdefghijklmnopqrstuvwxyz'
    for each in mg:
        y=y+int(each)
    while y>25:
        x=0
        for each in str(y):
            x=x+int(each)
            y=x
    n=a[y]
    return n,y
def dup(c,h):
    a='abcdefghijklmnopqrstuvwxyz'
    con=sqlite3.connect('surl.db')
    v=con.execute('select HEX from urls where HEX=?',(h,))
    for each in v:
        y1=a[c%25]
        y2=a[(c+1)%25]
        y3=a[(c+2)%25]
        y4=a[(c+3)%25]
        y5=a[(c+4)%25]
        return dup(c+1,y1+y2+y3+y4+y5)
    return h    
