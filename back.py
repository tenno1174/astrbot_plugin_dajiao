def time_long(time):
    if time < 3.00:
      return "唉唉唉，杂鱼，耐力杂鱼，射得太快了吧，真是个杂鱼小jb"
    if time < 20.00:
      return "嘻嘻嘻，小杂鱼，这么快就撑不住？真是太逊了"
    if time < 40.00:
      return "哎呀，你jb有点杂鱼唉，但短短的也很可爱了"
    if time < 80.00:
      return "嘻嘻,jb还能坚持一下吗，还有很大进步空间哦"
    if time < 150.00:
      return "嘿嘿，jb有点水准了，下次再多坚持一会把"
    if time < 300.00:
      return "嚯嚯，坚持得挺久嘛，已经不是杂鱼jb了哦"
    if time < 500.00:
      return "不错哦，能坚持这么久，你这家伙一定是有在偷偷锻炼了吧"
    else:
      return "假的吧，坚持了这么久，好厉害！ 简直是鬼畜级别的jb了" 

def volume(V):    
    if V < 1.00:
      return "好稀薄哦，杂鱼，杂鱼，最近偷偷打了不少吧"
    if V < 3.00:
      return "杂鱼，只出来少少的，嘛也很可爱啦"
    if V < 10.00:
      return "啊呀呀，怎么快就被榨干了，杂鱼"
    if V < 20.00:
      return "嘻嘻,这个量也一般般嘛，下次再多攒点吧"
    if V < 50.00:
      return "嘿嘿，好多浓浓的哦，下次争取再多产点吧"
    if V < 80.00:
      return "好厉害，这么多，我满手都是了"
    else:
      return "诶诶欸，假的吧，这个量，你这家伙已经不是人类了" 