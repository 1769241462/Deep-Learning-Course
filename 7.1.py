import matplotlib. pyplot as plt
from PIL import Image
plt.rcParams['font.sans-serif']=['SimHei']
img=Image.open("D:\Vscode\project1\lena.tiff")
plt.figure()
img_r,img_g,img_b = img.split()

plt.subplot(221)
img_R=img_r.resize((50,50))
plt.axis("off")
plt.imshow(img_R,cmap="gray")
plt.title("R-缩放",fontsize=14)

plt.subplot(222)
img_G=img_g.transpose(Image.FLIP_LEFT_RIGHT)
img_G=img_G.rotate(90)
plt.axis("on")
plt.imshow(img_G,cmap="gray")
plt.title("G-镜像+旋转",fontsize=14)

plt.subplot(223)
img_B=img_b.crop((0,0,300,300))
plt.axis("off")
plt.imshow(img_B,cmap="gray")
plt.title("B-裁剪",fontsize=14)

plt.subplot(224)
img_rgb=Image.merge("RGB",[img_r,img_g,img_b])
plt.axis("off")
plt.imshow(img_rgb,cmap="gray")
plt.title("RGB",fontsize=14)
img_rgb.save("test.png")

plt.suptitle("图像基本操作",color="blue",fontsize=20)
# plt.tight_layout(rect=[0,0,0,0.9])
plt.show()