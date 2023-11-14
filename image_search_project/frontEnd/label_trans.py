import pandas as pd
import re
class keyword_search():
    def __init__(self):
        self.df = pd.read_excel('frontEnd//assets/data_label.xlsx')
        self.df["DisplayName"] = self.df["DisplayName"].str.lower()
        
        self.eng_dict = dict(zip(self.df["DisplayName"],self.df["LabelName"]))
        self.zh_dict = dict(zip(self.df["ChineseName"],self.df["LabelName"]))
    def search(self, keyword):
        if re.search(u'[\u4e00-\u9fff]+',keyword):
            try:
                return self.zh_dict[keyword]
            except KeyError:
                raise KeyError("關鍵字不存在!")
        elif re.search(r'[a-z]+',keyword):
            try:
                return self.eng_dict[keyword]
            except KeyError:
                raise KeyError("Keyword does not exist.")
        else:
            raise KeyError("輸入格式錯誤")

