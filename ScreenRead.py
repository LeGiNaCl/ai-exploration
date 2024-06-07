import win32ui as wui
import win32gui as wgui
from ctypes import windll
from PIL import Image
from PIL import ImageFilter

class ScreenRead:
    
    def __init(self):
        print("Screen Handler")
    
    def process_image(self, handle):
        result, image = self.get_image(handle)
        minimap = self.extract_minimap(image)
        grayscale_img = self.grayscale_conversion(image)
        filtered_imgs = self.apply_filters(grayscale_img, [
            ImageFilter.CONTOUR,
            ImageFilter.EDGE_ENHANCE,
            ImageFilter.EDGE_ENHANCE_MORE,
            ImageFilter.EMBOSS,
            ImageFilter.EMBOSS
        ])
        i = 0
        for img in filtered_imgs:
            img.save(f"test{i}.png")
            i+=1
        return result, image
    
    def grayscale_conversion(self, image: Image):
        return image.convert("L")
    
    def apply_filters(self, image:Image, filters: list)->list:
        filtered_img = []
        for filter in filters:
            filtered_img.append(image.filter(filter))
        return filtered_img
    
    def get_image(self, handle):
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
          
        return result, im
    
    def extract_minimap(self, image):
        cleft= 812
        cright= 912
        ctop= 67
        cbottom= 154
        minimap = image.crop((cleft,ctop,cright,cbottom))
                
        return minimap
