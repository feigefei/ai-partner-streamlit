#读文件
# with open("./resources/望庐山瀑布.txt","w",encoding="utf-8") as f:
#     f.write("望庐山瀑布（李白）\n")
#     f.write("日照香炉生紫烟，\n")
#     f.write("遥看瀑布挂前川。\n")
#     f.write("飞流直下三千尺，\n")
#     f.write("疑是银河落九天。")
# with open("./resources/望庐山瀑布.txt","r",encoding="utf-8") as f:
#     # content_list = f.readlines()
#     # for line in content_list:
#     #     print(line.strip())
#     content = f.read()
#     print(content)

# f = open("resources/静夜思.txt","w",encoding='utf-8')
# f.write("静夜思（李白）\n\n")
# f.write("床前明月光，\n")
# f.write("疑是地上霜。\n")
# f.write("举头望明月，\n")
# f.write("低头思故乡。")
# f.close()

#===========================================================
#繁琐的文件读写
# f = open("resources/静夜思.txt","w",encoding='utf-8')
# try:
#     f.write("静夜思（李白）\n\n")
#     f.write("床前明月光，\n")
#     f.write("疑是地上霜。\n")
#     f.write("举头望明月，\n")
#     f.write("低头思故乡。")
# finally:
#     f.close()

with open("resources/静夜思.txt","r",encoding='utf-8') as f:
    f.write("静夜思（李白）\n\n")
    f.write("床前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")
