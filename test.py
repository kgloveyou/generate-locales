import re

# 不想保留分隔符，以（?:...）的形式指定
# linePat = r"'(.+)':(?: +)'(.+)'"
# splitPat = r":(?: +)"
linePattern = re.compile(r"'(.+)':(?: +)'(.+)'(?:,?)")
# splitPattern = re.compile(r":(?: +)")

# str = r"'app.pwa.serviceworker.updated.ok': '刷新'"
# str = r"'Undo: ${undoAction} ${undoShortcut}': '撤销: {{undoAction}} {{undoShortcut}}'"
str = r"'404.tips.error': '抱歉，您访问的页面不存在',"

# if re.search(linePat, str):
#   print(re.split(linePat, str))

if linePattern.search(str):
  print(linePattern.split(str))