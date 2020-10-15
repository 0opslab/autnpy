#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import unittest
<<<<<<< HEAD
from monsoon import Autn


class TEST_monsoon(unittest.TestCase):
    # def test_zip_dir(self):
    #     monsoon.zip_dir("c:/tools", "c:/tools.zip")
    #
    # def test_unzip_file(self):
    #     monsoon.unzip_file( "c:/tools.zip","c:/toolsback")


    # def test_path(self):
    #     print(monsoon.trim_path("c:\\files\\\\file2//files"))
    #     print(monsoon.base_path("c:\\files\\\\file2//files"))
    #
    # def test_commonsoon(self):
    #     print(monsoon.base_path())
    #     print(monsoon.base_path("/str/test.txt"))
    #     # print(date_time_str())
    #     print(monsoon.date_now())
    #     print(monsoon.load_keyvalue("127.0.0.1", "root", "123456", "datas", "WEIBOLOGIN"))
    #
    # def test_listfile(self):
    #     monsoon.list_file('c:/workspace/', print, '*.java')

    def test_removepunctuation(self):
        text = """
            导语：沙皇是俄罗斯人最早用来称拜帝国皇帝的名号，俄罗斯末代在沙皇尼古拉二世统治期间，整个皇室始终弥漫着荒淫无道、富奢华贵的风气。在俄国十月革命后，由沙俄海军上将哥萨克押送一批黄金，据说这批黄金是沙皇尼古拉二世从民间搜刮得来的，有人说这批黄金最后沉入贝加尔湖畔，还有人说这批黄金被埋藏在世界的某个秘密基地。那么这批黄金到底去哪里了呢?接下来就由探秘志小编为大家揭秘沙皇500吨黄金之谜吧!
            据有关资料记载，俄国在十月革命胜利后，在1919年11月13日由沙俄海军上将阿历克赛·瓦西里维奇·哥萨克率领一支部队，护送着一列28节车厢的装甲列车，从鄂木斯克沿西伯利亚大铁路向中国东北边境撤退。就在这趟戒备森严的列车上装载着沙皇的500吨黄金。据有关人士透露说，这批黄金斗士沙皇尼古拉二世从民间搜刮来的民脂民膏。
            这队人马经过3个月的艰难跋涉，来到了贝加尔湖的湖畔，由于饥寒交迫，有许多人死去了。哥萨克将军发现铁路已经彻底被破坏了，无法通行，只好命令部队改乘雪橇穿过贝加尔湖去中国边境。冰面上积了厚厚的雪，在刺人肌骨得得暴风雪中500吨黄金装上了雪橇，在武装人员的押送下，在80公里宽的湖面上，像蜗牛一样边扫着积雪边前进。到了1920年3月初，贝加尔湖面上的冰突然出现了裂缝。据说，哥萨克的所有部队和500吨黄金全都沉入一百多米的湖底。
            有人考证，这500吨黄金，全部是来自俄国底层的民脂民膏。在尼古拉二世年轻的时候，就因为多情而闻名，当年他在奥地利参加外事活动，与英国女王之女亚历山德拉邂逅生情，从此坠入爱河。不久之后，尼古拉继承俄国沙皇之位，然后迅速举行了盛大的婚礼，将亚历山德拉迎娶进门，封为皇后，度过了一段快乐而甜蜜的时光。1904年8月，尼古拉二世和亚历山德拉的孩子亚历克亚出生，这是四个孩子之中唯一的男孩，按照俄国皇室的习俗，亚历克亚将是俄国皇室唯一的王位继承人。整个皇室上下一片欣喜。
            可是这种欣喜持续了没过多久，人们便发现，“小王子亚历克亚身体非常奇怪，稍一擦伤便血流不止，原来皇后亚历山德拉继承了英国王室的基因，导致自己的王子从诞生开始便患上了血友病，这给周围的人们心头带来一片阴影。
            这批黄金是在1920年由高尔察克将军押送到日本的。俄罗斯观察家西罗特金在他所着的4本书中说，这批黄金是用来购买武器的，不过高尔查克从未获得任何军事硬体。高尔察克出生于1874年11月16日的俄罗斯圣彼得堡，年幼时期的高尔察克就表现出了对大海的浓厚兴趣，他常常称自己在海上比在陆地上更有安全感。在他13岁的时候，就考入了圣彼得堡海军学校，成为了这所学校的高材生，并最终以优异的成绩毕业。
            1919年10月，高尔察克的军队在托博尔斯克被红军击败，同时他和盟友安东·伊万诺维奇·邓尼金之间的联系，也被红军切断，高尔察克不得不选择撤退。当时的高尔察克身在鄂木斯克，他要指挥自己的军队陆续撤退，最主要的是，他还要押运从喀山的国库运来的500吨黄金到东方去。这些黄金是沙皇拨给高尔察克的资费，高尔察克打算将其用作他日东山再起的资金。
            高尔察克从鄂木斯克出发，打算到太平洋沿岸地区，去寻求日本舰队的协助。而那500吨黄金，则分别藏在28辆武装押运车里。当他们抵达托木斯克时，天气突然变得极其寒冷，而押运车的染料也逐渐耗尽。他们不得不把黄金搬下来，放到马拉雪橇上。但是天气依然在持续变冷，不多久，拉雪橇的马匹也开始死亡，最后，他们不得不把这500吨黄金，丢弃在荒野上。
            90多年来，这批黄金始终没有人找到过，至今成为了一个历史的谜团。2013年，俄罗斯政府在贝加尔湖底找到了一个火车的残骸，被初步认定与当年的高尔察克黄金有关。但事实究竟如何，依然无法找到有力的证据。西罗特金估计，这些黄金连本带息今日价值高达800亿美元。他声称，这批黄金现在还保存在日本三菱银行的地下金库。西罗特金还说，日本从高尔查克手共计收到200吨黄金，1917年3月还从在运往英国途中的沙皇的私人金库 “偷了”5.5吨。
            1994年，俄罗斯公开文件证明，於1920年被布尔什维克处决的高尔查克至少运送了22箱金条到日本。然而，由於缺乏确凿证据，俄罗斯没能把沙皇黄金问题提到外交层面解决。俄罗斯媒体报道称，东京已承认价值27亿美元的“沙皇黄金”依然存放在日本，但日本没有就该问题正式发表评论。
            事情过去了18年，有一个生活在美国的沙俄军官斯拉夫·贝克达诺夫公开了身份，并对人讲：”沙皇的这批财宝并没有沉入贝加尔湖，早在大部队抵达伊尔库茨克之前就已经被转移走了，并且早已被秘密埋藏了起来。因为当时的形式已经很明朗了，大部队不可能撤退到满洲，不论从哪个方面来考虑，最好的做法就是把这比黄金秘密埋在一个地方。当时我跟一个名叫德兰科维奇的军官奉命负责指挥了这次埋藏黄金的行动。我俩带上45个士兵，把黄金转移出来之后，就把它们埋在一座已倒塌的教堂的地下室里。这事办完之后，我们把这45名士兵带到了一个采石场上，我和德兰科维奇用机枪把他们统统枪决了。在返回的路上，我发现德兰科维奇想暗算我，于是，我抢先一步掏出手枪把他打死了。这46个人的死亡根本不会引起注意，因为当时每天都要失踪一百多人。就这样，我成了现在唯一掌握沙皇金宝秘密的知情人。
            1959年，贝克达诺夫曾利用一次大赦的机会返回苏联，并在马格尼托戈尔斯克碰上了在美国加尼福利亚认识的美国工程师。此人始终没有透露真实姓名，他只用假名，叫约翰·史密斯。史密斯了解贝克达诺夫的情况，建议与他共同去当年埋藏沙皇金宝的地方。于是他们在一个名叫达妮娅的年轻姑娘陪伴下，一起找到了在离西伯利亚大铁路3公里处的原教堂地下室里找到了仍然完整无损的沙皇金宝。他们只取走了部分黄金。随后，当他们开着吉普车，正要通过格鲁吉亚闯过边境时，突然一阵密集的子弹扫来，在弹雨中，贝克达诺夫被当场打死，而史密斯和达妮娅则扔下了车子和黄金，惊恐万分地逃出了苏联。
            沙皇500吨黄金之谜至今仍然找不到任何踪迹，也许就深埋在贝加尔湖底部，也许就埋藏在世界的某一个角落当中，要想找到沙皇500吨黄金不是一件容易的事情。真相到底如何，或许还需要史密斯或达妮娅出来证实才能解开谜底，至今无人得知。
            """.strip().replace("\s+", "")
        print(Autn.remove_punctuation(text))

        print(Autn.replace_punctuation(text))
if __name__ == '__main__':
    print("==============>start test")
    #log = monsoon.logger(__name__, "c:/run.log")
=======
import monsoon as  Mon



class TEST_MONSOON(unittest.TestCase):

    # def test_zip_dir(self):
    #     Mon.zip_dir("c:/tools", "c:/tools.zip")
    #
    # def test_unzip_file(self):
    #     Mon.unzip_file( "c:/tools.zip","c:/toolsback")


    def test_path(self):
        print(Mon.trim_path("c:\\files\\\\file2//files"))
        print(Mon.base_path("c:\\files\\\\file2//files"))
    def test_common(self):
        print(Mon.base_path())
        print(Mon.base_path("/str/test.txt"))
        # print(date_time_str())
        print(Mon.date_now())
        print(Mon.load_keyvalue("127.0.0.1", "root", "123456", "datas", "WEIBOLOGIN"))


    def test_listfile(self):
        Mon.list_file('c:/workspace/', print, '*.java')

if __name__ == '__main__':
    print("==============>start test")
    log = Mon.logger(__name__,"c:/run.log")
    log.info("info")
    log.debug("debug")
    log.error("error")
>>>>>>> 81319360620ffa27ee5932b094978cc4e1ddb302
    unittest.main()
