import cv2
import numpy as np
from matplotlib import pyplot as plt
mavi=[255,0,0]
img = cv2.imread("logo.png")
replicate=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101)
wrap=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
costant=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=mavi)


plt.subplot(231),plt.imshow(img,"gray"),plt.title("orijinal")
plt.subplot(231),plt.imshow(replicate,"gray"),plt.title("replicate")
plt.subplot(231),plt.imshow(reflect,"gray"),plt.title("reflect")
plt.subplot(231),plt.imshow(reflect101,"gray"),plt.title("reflect101")
plt.subplot(231),plt.imshow(wrap,"gray"),plt.title("wrap")

plt.subplot(231),plt.imshow(costant,"gray"),plt.title("costant")

plt.show()

"""
cv2.imshow("orinal",img)
cv2.imshow("replicate",replicate)
cv2.imshow("reflect",reflect)
cv2.imshow("reflect101",reflect101)
cv2.imshow("wrap",wrap)
cv2.imshow("costant",costant)


"""
cv2.waitKey(0)
cv2.destroyAllWindows()




