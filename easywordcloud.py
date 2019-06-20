

from wordcloud import WordCloud
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']


# この下の部分にワードクラウドにしたい原文コピペするとできるよ!

text = """ここにワードクラウドにしたいテキストをいれてね！"""


#ここに除外したいワードをいれるとよいよ！
stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
             u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
             u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
             u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう',u'とか', u'でも', u'なら', u'']

wordcloud = WordCloud(background_color="white",
    font_path="/usr/library/fonts/ヒラギノ丸ゴ ProN W4.ttc",
    width=800,height=600, stopwords=set(stop_words)).generate(text)


wordcloud.to_file("./wordcloud_sample.png")
