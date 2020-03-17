import pyperclip
from opencc import OpenCC
import time

cc=OpenCC('s2t')
while 1:
    a1= pyperclip.paste()

    print('复制了:{}'.format(a1))
    res = cc.convert(a1)

    pyperclip.copy(res)
    print("转化: {}==>{}".format(a1,res))
    time.sleep(0.2)
