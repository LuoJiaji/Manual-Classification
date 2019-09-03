import os
import shutil
from PIL import Image
import matplotlib.pyplot as plt 
import tkinter as tk

dataset_path = './data/'
dataset_path_yes = './类/'
dataset_path_no = './new_data2/'

filelist = os.listdir(dataset_path)

window = tk.Tk()
window.title('Manual Classification')
window.geometry('400x200')

i = 0
l = len(filelist)

plt.ion()
fp = open(dataset_path + filelist[i],'rb') 
img = Image.open(fp)
plt.imshow(img)
plt.show()
fp.close()

print('THe number of files:', l)
print(i, ';', filelist[i])

def yes():
    global i
    # print('yes')
    shutil.move(dataset_path + filelist[i], dataset_path_yes + filelist[i])
    i += 1
    plt.close()
    if i < l:
        print(i, ';', filelist[i])
        fp = open(dataset_path + filelist[i],'rb') 
        img = Image.open(fp)
        plt.imshow(img)
        plt.show()
        fp.close()

    elif i == l:
        quit()

def no():
    global i
    # print('yes')
    shutil.move(dataset_path + filelist[i], dataset_path_no + filelist[i])
    i += 1
    plt.close()
    if i < l:
        print(i, ';', filelist[i])
        # img = Image.open(dataset_path + filelist[i])
        fp = open(dataset_path + filelist[i],'rb') 
        img = Image.open(fp)
        # fp.close()
        plt.imshow(img)
        plt.show()
        fp.close()

    elif i == l:
        quit()

b1 = tk.Button(window, text='Yes', width=15, height=2, command=yes)
b1.pack()
b1.place(x=170, y=30)

b2 = tk.Button(window, text='No', width=15, height=2, command=no)
b2.pack()
b2.place(x=170, y=100)

window.mainloop()


# print(filelist)
# plt.ion()
# for i in filelist:
#     # shutil.copy(dataset_path + i, new_dataset_path + i)
#     shutil.move(dataset_path + i, new_dataset_path + i)
#     img = Image.open(new_dataset_path + i)
#     plt.imshow(img)
#     plt.show()
#     plt.pause(1)
#     plt.close()
