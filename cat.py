# import tempfile
# 
# 6. creating cat function
# Am I supposed to create a file and fill it up with data on-the-go?
# If I am, what type of data should I fill the file?
# filepath_one = "C:/Users/ashapkin/Documents/Training/sin.txt"
# filepath_two = "C:/Users/ashapkin/Documents/Training/bread.txt"
# 
# def cat(*args):
#     with tempfile.TemporaryFile() as tmp:
#         for every in args:
#             tmp.writelines(line if '\n' in line else "%s\n" % line for line in open(every, 'r'))
#         tmp.seek(0)
#         print tmp.read()
# 
# cat(filepath_one, filepath_two)
