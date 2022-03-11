
from owlApiv2 import *

# the first example

# define domainName and owlPath
domainName = "testKG"
owlPath = ".\owlDataSet\Personage.owl"

# dismantling owl
header, opList, dpList, classesList, indsList, footer = readOwl(owlPath, domainName)

# example of classse
# add class
oneClass = OneClass(domainName, "中国民主促进会", None)
oneClass.addSuperClass("人物")
classesList.append(oneClass)

# add dataProperty
oneDP = DP(domainName, "特别身份", None)
dpList.append(oneDP)

# add object Property
oneOP = DP(domainName, "哥哥", None)
dpList.append(oneDP)

# add entity
oneEntity = Individual(domainName, "周建人", None)
oneEntity.addComment("周建人（1888年11月12日-1984年7月29日），生于浙江绍兴都昌坊口，初名松寿，乳名阿松，后改名建人，字乔峰，浙江绍兴人。笔名克士、高山、李正、孙鲠等，鲁迅三弟。（即《风筝》中的小弟。）")
oneEntity.addType("中国民主促进会")
oneEntity.addDataProperty("特别身份", "鲁迅的三弟")
oneEntity.addObjectProperty("哥哥", "鲁迅")
indsList.append(oneEntity)

# assemble owl
# generateOwl(header, opList, dpList, classesList, indsList, footer, domainName)