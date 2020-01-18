from tkinter import filedialog
import os
import sys
import tkinter as tk  # 使用Tkinter前需要先导入
#def choose_video():
# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('My Window')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
# 第4步，在图形界面上设定标签
var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False

def choose_v():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('选择文件')
        global file_path     #chosen_video为选中的视频文件名
        file_path = filedialog.askdirectory(initialdir='F:/Adachuang/folder/dongzuo')
        os.system('convert_video_to_images.sh ' + file_path + ' 10')
        print(file_path)
    else:
        on_hit = False
        var.set('')


def check_result():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('切割')
        global chosen_video     #chosen_video为选中的视频文件名
        chosen_video = filedialog.askdirectory(initialdir='F:\Adachuang\folder1\dongzuo')
        print(chosen_video)
        os.system('convert_images_to_list.sh ' + chosen_video + ' 10')
        print('hello')
    else:
        on_hit = False
        var.set('')


def test():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('测试')
        run_test()
        print('hello')
    else:
        on_hit = False
        var.set('')
# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='选择文件', font=('Arial', 12), width=10, height=1, command=choose_v)
b.pack()
b2 = tk.Button(window, text='查看结果', font=('Arial', 12), width=10, height=1, command=check_result)
b2.pack()
# 第6步，主窗口循环显示
window.mainloop()

