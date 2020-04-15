import re
def camel_case_split(CamelCaseStr):
    strlist = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', CamelCaseStr)
    class_name = ""
    lower_class_name = ""
    for item in strlist:
    	class_name +=" " + item
    	lower_class_name += item.lower() + "_"
    return class_name, lower_class_name

res,res1 = camel_case_split("Subject")
print(res,res1)



