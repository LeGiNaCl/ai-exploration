import win32ui as wui
import win32gui as wgui
from ctypes import windll
from PIL import Image
from PIL import ImageFilter

class ScreenRead:
    
    def __init(self):
        print("Screen Handler")
    
    def get_framebuffer(self,handle):
        left, top, right, bot = wgui.GetWindowRect(handle)
        w = right - left
        h = bot - top
        handleDC = wgui.GetWindowDC(handle)
        mfcDC = wui.CreateDCFromHandle(handleDC)
        saveDC = mfcDC.CreateCompatibleDC()
        
        saveBitMap = wui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        
        saveDC.SelectObject(saveBitMap)
        
        result = windll.user32.PrintWindow(handle, saveDC.GetSafeHdc(), 0)
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)

        wgui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        wgui.ReleaseDC(handle, handleDC)
        im.save ("Test.png")
        imconv1 = im.convert("L")
        
        imfil1 = imconv1.filter(ImageFilter.CONTOUR)
        imfil2 = imconv1.filter(ImageFilter.EDGE_ENHANCE)
        imfil3 = imconv1.filter(ImageFilter.EDGE_ENHANCE_MORE)
        imfil4 = imconv1.filter(ImageFilter.EMBOSS)
        imfil5 = imconv1.filter(ImageFilter.EMBOSS)
        
        imfil1.save ("testfilter1.png")
        imfil2.save ("testfilter2.png")
        imfil3.save ("testfilter3.png")
        imfil4.save ("testfilter4.png")
        imfil5.save ("testfilter5.png")
        imconv1.save ("testcon1.png")
        
        return result, im
    
    def get_minimap (self,handle):
        left, top, right, bot = wgui.GetWindowRect(handle)
        w = right - left
        h = bot - top
        handleDC = wgui.GetWindowDC(handle)
        mfcDC = wui.CreateDCFromHandle(handleDC)
        saveDC = mfcDC.CreateCompatibleDC()
        
        saveBitMap = wui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
            
        saveDC.SelectObject(saveBitMap)
            
        result = windll.user32.PrintWindow(handle, saveDC.GetSafeHdc(), 0)
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        im = Image.frombuffer(
                'RGB',
                (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
                bmpstr, 'raw', 'BGRX', 0, 1)

        wgui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        wgui.ReleaseDC(handle, handleDC)
            
        cleft= 812
        cright= 912
        ctop= 67
        cbottom= 154
        minimap = im.crop((cleft,ctop,cright,cbottom))
        
        minimap.save ("minimap.png")
        
        return result, minimap
