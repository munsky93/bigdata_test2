import matplotlib.pyplot as plt
from matplotlib import font_manager
import pytagcloud
import webbrowser

# matplotlib 그래프

def show_graph_bar(dictwords, pagename) :

    # 한글처리
    font_filename = 'c:/Windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_filename).get_name()
    print(font_name)
    plt.rc('font', family=font_name)

    # 라벨처리
    plt.xlabel('주요단어')
    plt.xlabel('빈도수')
    plt.xlabel(True)

    # 데이타 대입
    dict_keys = dictwords.keys()
    dict_values = dictwords.values()
    plt.bar(range(len(dictwords)), dict_values, align='center')
    plt.xticks(range(len(dictwords)), list(dict_keys), rotation=70)
    plt.show()
    save_filename = "D:/javaStudy/fb/%s_bar_graph.png" % pagename
    plt.savefig(save_filename, dpi=400, bbox_inches='tight')

    save_filename = "D:\javastudy\facebook\%s_bar_graph.png" % pagename




    ## 워드크라우드
    def wordcloud(dictWords, pagename):
        print(type(dictWords))
        print(dictWords)
        taglist = pytagcloud.make_tags(dictWords.items(), maxsize=80)
        save_filename = "D:/javaStudy/fb/%s_wordcloud.jpg" % pagename
        pytagcloud.create_tag_image(
        taglist,
        save_filename,
        size=(800, 600),
        fontname='korean',
        rectangular=False
        )
    webbrowser.open(save_filename)