#coding=utf-8
'''
Created on 2015年7月8日

@author: Administrator
'''


from pytesser import *
import os
import sys  
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw
# 二值化

#由于都是数字
#对于识别成字母的 采用该表进行修正
class getVerCode:
    
    rep={'O':'0',
        'g':'9',
        '?':'7',
        'z':'2',
        'Q':'9',
        'T':'7',
        'b':'6',
        '$':'5'
        }
    
    

    def getPixel(self,image,x,y,G,N):  
        L = image.getpixel((x,y))  
        if L > G:  
            L = True  
        else:  
            L = False  
      
        nearDots = 0  
        if L == (image.getpixel((x - 1,y - 1)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x - 1,y)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x - 1,y + 1)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x,y - 1)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x,y + 1)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x + 1,y - 1)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x + 1,y)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x + 1,y + 1)) > G):  
            nearDots += 1  
      
        if nearDots < N:  
            return image.getpixel((x,y-1))  
        else:  
            return None  
  
# 降噪   
# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点   
# G: Integer 图像二值化阀值   
# N: Integer 降噪率 0 <N <8   
# Z: Integer 降噪次数   
# 输出   
#  0：降噪成功   
#  1：降噪失败   
    def clearNoise(self,image,G,N,Z):  
        draw = ImageDraw.Draw(image)  
      
        for i in xrange(0,Z):  
            for x in xrange(1,image.size[0] - 1):  
                for y in xrange(1,image.size[1] - 1):  
                    color = self.getPixel(image,x,y,G,N)  
                    if color != None:  
                        draw.point((x,y),color)  

    

    def getverify(self,jpg):
        

        '''
        threshold = 140  
        table = []  
        for i in range(256):  
            if i < threshold:  
                table.append(0)  
            else:  
                table.append(1)
        '''
        
        
        os.chdir('E:\python\Lib\site-packages\pytesser')
        #打开图片
        im = Image.open(jpg).convert('RGB')
        
        im = im.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(im)
        im = enhancer.enhance(2)
        
        imgry = im.convert('L')
        
        
        #out = imgry.point(table,'1')
        
        self.clearNoise(imgry,50,4,4)
        imgry.save("D:/result.jpg")
        
        text=image_to_string(imgry)
        print text
        for r in self.rep:
            text = text.replace(r,self.rep[r])
        
        print text
        verCode=filter(str.isdigit,text)
        #print verCode
        
        return verCode
    
#getVerCode().getverify('codePhoto.tif')

