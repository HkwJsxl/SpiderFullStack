from lxml import etree

html_page = """
<!DOCTYPE html>
<html lang="zh">
<head>
    <script type="text/javascript" src="https://ip.ws.126.net/ipquery"></script>
    <script src="https://img.shicimingju.com/newpage/js/all.js"></script>
    <meta charset="UTF-8">
    <title>《三国演义》全集在线阅读_史书典籍_诗词名句网</title>
    <meta name="viewport" content="width=device-width,user-scalable=no"/>
    <meta name="description" content=""/>
    <link rel="stylesheet" href="https://img.shicimingju.com/public/css/www_v3.css">
    <link rel="stylesheet" href="https://img.shicimingju.com/public/css/font_576092_m2icqcebp7evzpvi.css">
    <script src="https://img.shicimingju.com/public/js/device.js"></script>
    <script src="https://img.shicimingju.com/public/js/jq.js"></script>
    <script src="https://img.shicimingju.com/public/js/www_v3.js"></script>
</head>
<body>
<div id="top_bar">
    <div id="top_bar_main">
        <div id="top_left">
            <a href="/"><img src="https://img.shicimingju.com/public/image/logo.png" id="logo"/></a>
            <div id="top_left_menu">
                <ul>
                    <li><a href="/">首页</a></li>
                    <li><a href="/shicimark">分类</a></li>
                    <li><a href="/category/all">作者</a></li>
                    <li><a href="/paiming">排行榜</a></li>
                    <li><a href="/cate?cate_id=4">课本古诗</a></li>
                    <li><a href="/cipai/index.html">词牌名</a></li>
                    <li><a href="/cangtoushi/index.html">藏头诗</a></li>
                    <li><a href="/hecheng/index.html">合称</a></li>
                    <li><a href="/book/">古籍</a></li>
                    <li><a href="/app/">安卓下载</a></li>
                </ul>
            </div>
            <div style="clear: both"></div>
        </div>
        <div id="top_right">
            <div id="top_right_nav">
                <ul>
                    <li><a href="javascript:void(0)" data-cate="all">综合</a></li>
                    <li><a href="javascript:void(0)" data-cate="zuozhe">作者</a></li>
                    <li><a href="javascript:void(0)" data-cate="title">标题</a></li>
                    <li><a href="javascript:void(0)" data-cate="shiju">诗句</a></li>
                    <li><a href="javascript:void(0)" data-cate="first">句首</a></li>
                    <li><a href="javascript:void(0)" data-cate="end">句尾</a></li>
                    <li><a href="javascript:void(0)" data-cate="book">古籍</a></li>
                    <li><a href="javascript:void(0)" data-cate="chengyu">成语</a></li>
                </ul>
            </div>
            <div id="input_div">
                <input type="text" name="kw" id="search_input" placeholder="" autocomplete="off" value="">
                <a href="javascript:doSearch();"><img src="https://img.shicimingju.com/public/image/web_search.png"
                                                      class="www-icon"></a>
                <div style="clear: both"></div>
            </div>
            <div id="tip_result" class="card">
                <ul>
                </ul>
                <div id="tip_content">
                </div>
            </div>
        </div>
        <div style="clear: both;"></div>
    </div>
</div>

<div id="nav-top"><a href="/">主页</a><span class="nav-arrow"></span><a href="/book/index.html">史书典籍</a><span
        class="nav-arrow"></span><a href="/book/sidamingzhu.html">四大名著</a></div>

<div id="main">
    <div id="main_left">
        <div class="card bookmark-list">
            <h1>《三国演义》</h1>
            <div>
                <img src="https://img.shicimingju.com/public/image/book/sanguoyanyi.jpg" class="book-img">
                <p>年代：元末明初</p>
                <p>作者：罗贯中</p>
                <p class="des">
                    《三国演义》中国古典四大名著之一。元末明初小说家罗贯中所著，是中国第一部长篇章回体历史演义的小说。描写了从东汉末年到西晋初年之间近100年的历史风云。全书反映了三国时代的政治军事斗争，反映了三国时代各类社会矛盾的渗透与转化，概括了这一时代的历史巨变，塑造了一批叱咤风云的英雄人物。</p>
                <div style="clear: both"></div>
            </div>
            <div>
                <form method="get" action="/book/chaxun/" style="float: right;">
                    <input type="hidden" name="book_id" value="1">
                    <input type="text" name="kw" placeholder="全文检索" autocomplete="off">
                </form>
                <div style="clear: both"></div>
            </div>
            <div class="line"></div>
            <div class="book-mulu">
                <ul>
                    <li><a href="/book/sanguoyanyi/1.html">第一回·宴桃园豪杰三结义 斩黄巾英雄首立功</a></li>
                    <li><a href="/book/sanguoyanyi/2.html">第二回·张翼德怒鞭督邮 何国舅谋诛宦竖</a></li>
                    <li><a href="/book/sanguoyanyi/3.html">第三回·议温明董卓叱丁原 馈金珠李肃说吕布</a></li>
                    <li><a href="/book/sanguoyanyi/4.html">第四回·废汉帝陈留践位 谋董贼孟德献刀</a></li>
                    <li><a href="/book/sanguoyanyi/5.html">第五回·发矫诏诸镇应曹公 破关兵三英战吕布</a></li>
                    <li><a href="/book/sanguoyanyi/6.html">第六回·焚金阙董卓行凶 匿玉玺孙坚背约</a></li>
                    <li><a href="/book/sanguoyanyi/7.html">第七回·袁绍磐河战公孙 孙坚跨江击刘表</a></li>
                    <li><a href="/book/sanguoyanyi/8.html">第八回·王司徒巧使连环计 董太师大闹凤仪亭</a></li>
                    <li><a href="/book/sanguoyanyi/9.html">第九回·除暴凶吕布助司徒 犯长安李傕听贾诩</a></li>
                    <li><a href="/book/sanguoyanyi/10.html">第一十回·勤王室马腾举义 报父仇曹操兴师</a></li>
                    <li><a href="/book/sanguoyanyi/11.html">第十一回·刘皇叔北海救孔融 吕温侯濮阳破曹操</a></li>
                    <li><a href="/book/sanguoyanyi/12.html">第十二回·陶恭祖三让徐州 曹孟德大战吕布</a></li>
                    <li><a href="/book/sanguoyanyi/13.html">第十三回·李傕郭汜大交兵 杨奉董承双救驾</a></li>
                    <li><a href="/book/sanguoyanyi/14.html">第十四回·曹孟德移驾幸许都 吕奉先乘夜袭徐郡</a></li>
                    <li><a href="/book/sanguoyanyi/15.html">第十五回·太史慈酣斗小霸王 孙伯符大战严白虎</a></li>
                    <li><a href="/book/sanguoyanyi/16.html">第十六回·吕奉先射戟辕门 曹孟德败师淯水</a></li>
                    <li><a href="/book/sanguoyanyi/17.html">第十七回·袁公路大起七军 曹孟德会合三将</a></li>
                    <li><a href="/book/sanguoyanyi/18.html">第十八回·贾文和料敌决胜 夏侯惇拔矢啖睛</a></li>
                    <li><a href="/book/sanguoyanyi/19.html">第十九回·下邳城曹操鏖兵 白门楼吕布殒命</a></li>
                    <li><a href="/book/sanguoyanyi/20.html">第二十回·曹阿瞒许田打围 董国舅内阁受诏</a></li>
                    <li><a href="/book/sanguoyanyi/21.html">第二十一回·曹操煮酒论英雄 关公赚城斩车胄</a></li>
                    <li><a href="/book/sanguoyanyi/22.html">第二十二回·袁曹各起马步三军 关张共擒王刘二将</a></li>
                    <li><a href="/book/sanguoyanyi/23.html">第二十三回·祢正平裸衣骂贼 吉太医下毒遭刑</a></li>
                    <li><a href="/book/sanguoyanyi/24.html">第二十四回·国贼行凶杀贵妃 皇叔败走投袁绍</a></li>
                    <li><a href="/book/sanguoyanyi/25.html">第二十五回·屯土山关公约三事 救白马曹操解重围</a></li>
                    <li><a href="/book/sanguoyanyi/26.html">第二十六回·袁本初败兵折将 关云长挂印封金</a></li>
                    <li><a href="/book/sanguoyanyi/27.html">第二十七回·美髯公千里走单骑 汉寿侯五关斩六将</a></li>
                    <li><a href="/book/sanguoyanyi/28.html">第二十八回·斩蔡阳兄弟释疑 会古城主臣聚义</a></li>
                    <li><a href="/book/sanguoyanyi/29.html">第二十九回·小霸王怒斩于吉 碧眼儿坐领江东</a></li>
                    <li><a href="/book/sanguoyanyi/30.html">第三十回·战官渡本初败绩 劫乌巢孟德烧粮</a></li>
                    <li><a href="/book/sanguoyanyi/31.html">第三十一回·曹操仓亭破本初 玄德荆州依刘表</a></li>
                    <li><a href="/book/sanguoyanyi/32.html">第三十二回·夺冀州袁尚争锋 决漳河许攸献计</a></li>
                    <li><a href="/book/sanguoyanyi/33.html">第三十三回·曹丕乘乱纳甄氏 郭嘉遗计定辽东</a></li>
                    <li><a href="/book/sanguoyanyi/34.html">第三十四回·蔡夫人隔屏听密语 刘皇叔跃马过檀溪</a></li>
                    <li><a href="/book/sanguoyanyi/35.html">第三十五回·玄德南漳逢隐沧 单福新野遇英主</a></li>
                    <li><a href="/book/sanguoyanyi/36.html">第三十六回·玄德用计袭樊城 元直走马荐诸葛</a></li>
                    <li><a href="/book/sanguoyanyi/37.html">第三十七回·司马徽再荐名士 刘玄德三顾草庐</a></li>
                    <li><a href="/book/sanguoyanyi/38.html">第三十八回·定三分隆中决策 战长江孙氏报仇</a></li>
                    <li><a href="/book/sanguoyanyi/39.html">第三十九回·荆州城公子三求计 博望坡军师初用兵</a></li>
                    <li><a href="/book/sanguoyanyi/40.html">第四十回·蔡夫人议献荆州 诸葛亮火烧新野</a></li>
                    <li><a href="/book/sanguoyanyi/41.html">第四十一回·刘玄德携民渡江 赵子龙单骑救主</a></li>
                    <li><a href="/book/sanguoyanyi/42.html">第四十二回·张翼德大闹长坂桥 刘豫州败走汉津口</a></li>
                    <li><a href="/book/sanguoyanyi/43.html">第四十三回·诸葛亮舌战群儒 鲁子敬力排众议</a></li>
                    <li><a href="/book/sanguoyanyi/44.html">第四十四回·孔明用智激周瑜 孙权决计破曹操</a></li>
                    <li><a href="/book/sanguoyanyi/45.html">第四十五回·三江口曹操折兵 群英会蒋干中计</a></li>
                    <li><a href="/book/sanguoyanyi/46.html">第四十六回·用奇谋孔明借箭 献密计黄盖受刑</a></li>
                    <li><a href="/book/sanguoyanyi/47.html">第四十七回·阚泽密献诈降书 庞统巧授连环计</a></li>
                    <li><a href="/book/sanguoyanyi/48.html">第四十八回·宴长江曹操赋诗 锁战船北军用武</a></li>
                    <li><a href="/book/sanguoyanyi/49.html">第四十九回·七星坛诸葛祭风 三江口周瑜纵火</a></li>
                    <li><a href="/book/sanguoyanyi/50.html">第五十回·诸葛亮智算华容 关云长义释曹操</a></li>
                    <li><a href="/book/sanguoyanyi/51.html">第五十一回·曹仁大战东吴兵 孔明一气周公瑾</a></li>
                    <li><a href="/book/sanguoyanyi/52.html">第五十二回·诸葛亮智辞鲁肃 赵子龙计取桂阳</a></li>
                    <li><a href="/book/sanguoyanyi/53.html">第五十三回·关云长义释黄汉升 孙仲谋大战张文远</a></li>
                    <li><a href="/book/sanguoyanyi/54.html">第五十四回·吴国太佛寺看新郎 刘皇叔洞房续佳偶</a></li>
                    <li><a href="/book/sanguoyanyi/55.html">第五十五回·玄德智激孙夫人 孔明二气周公瑾</a></li>
                    <li><a href="/book/sanguoyanyi/56.html">第五十六回·曹操大宴铜雀台 孔明三气周公瑾</a></li>
                    <li><a href="/book/sanguoyanyi/57.html">第五十七回·柴桑口卧龙吊丧 耒阳县凤雏理事</a></li>
                    <li><a href="/book/sanguoyanyi/58.html">第五十八回·马孟起兴兵雪恨 曹阿瞒割须弃袍</a></li>
                    <li><a href="/book/sanguoyanyi/59.html">第五十九回·许诸裸衣斗马超 曹操抹书问韩遂</a></li>
                    <li><a href="/book/sanguoyanyi/60.html">第六十回·张永年反难杨修 庞士元议取西蜀</a></li>
                    <li><a href="/book/sanguoyanyi/61.html">第六十一回·赵云截江夺阿斗 孙权遗书退老瞒</a></li>
                    <li><a href="/book/sanguoyanyi/62.html">第六十二回·取涪关杨高授首 攻雒城黄魏争功</a></li>
                    <li><a href="/book/sanguoyanyi/63.html">第六十三回·诸葛亮痛哭庞统 张翼德义释严颜</a></li>
                    <li><a href="/book/sanguoyanyi/64.html">第六十四回·孔明定计捉张任 杨阜借兵破马超</a></li>
                    <li><a href="/book/sanguoyanyi/65.html">第六十五回·马超大战葭萌关 刘备自领益州牧</a></li>
                    <li><a href="/book/sanguoyanyi/66.html">第六十六回·关云长单刀赴会 伏皇后为国捐生</a></li>
                    <li><a href="/book/sanguoyanyi/67.html">第六十七回·曹操平定汉中地 张辽威震逍遥津</a></li>
                    <li><a href="/book/sanguoyanyi/68.html">第六十八回·甘宁百骑劫魏营 左慈掷杯戏曹操</a></li>
                    <li><a href="/book/sanguoyanyi/69.html">第六十九回·卜周易管辂知机 讨汉贼五臣死节</a></li>
                    <li><a href="/book/sanguoyanyi/70.html">第七十回·猛张飞智取瓦口隘 老黄忠计夺天荡山</a></li>
                    <li><a href="/book/sanguoyanyi/71.html">第七十一回·占对山黄忠逸待劳 据汉水赵云寡胜众</a></li>
                    <li><a href="/book/sanguoyanyi/72.html">第七十二回·诸葛亮智取汉中 曹阿瞒兵退斜谷</a></li>
                    <li><a href="/book/sanguoyanyi/73.html">第七十三回·玄德进位汉中王 云长攻拔襄阳郡</a></li>
                    <li><a href="/book/sanguoyanyi/74.html">第七十四回·庞令明抬榇决死战 关云长放水淹七军</a></li>
                    <li><a href="/book/sanguoyanyi/75.html">第七十五回·关云长刮骨疗毒 吕子明白衣渡江</a></li>
                    <li><a href="/book/sanguoyanyi/76.html">第七十六回·徐公明大战沔水 关云长败走麦城</a></li>
                    <li><a href="/book/sanguoyanyi/77.html">第七十七回·玉泉山关公显圣 洛阳城曹操感神</a></li>
                    <li><a href="/book/sanguoyanyi/78.html">第七十八回·治风疾神医身死 传遗命奸雄数终</a></li>
                    <li><a href="/book/sanguoyanyi/79.html">第七十九回·兄逼弟曹植赋诗 侄陷叔刘封伏法</a></li>
                    <li><a href="/book/sanguoyanyi/80.html">第八十回·曹丕废帝篡炎刘 汉王正位续大统</a></li>
                    <li><a href="/book/sanguoyanyi/81.html">第八十一回·急兄仇张飞遇害 雪弟恨先主兴兵</a></li>
                    <li><a href="/book/sanguoyanyi/82.html">第八十二回·孙权降魏受九锡 先主征吴赏六军</a></li>
                    <li><a href="/book/sanguoyanyi/83.html">第八十三回·战猇亭先主得仇人 守江口书生拜大将</a></li>
                    <li><a href="/book/sanguoyanyi/84.html">第八十四回·陆逊营烧七百里 孔明巧布八阵图</a></li>
                    <li><a href="/book/sanguoyanyi/85.html">第八十五回·刘先主遗诏托孤儿 诸葛亮安居平五路</a></li>
                    <li><a href="/book/sanguoyanyi/86.html">第八十六回·难张温秦宓逞天辩 破曹丕徐盛用火攻</a></li>
                    <li><a href="/book/sanguoyanyi/87.html">第八十七回·征南寇丞相大兴师 抗天兵蛮王初受执</a></li>
                    <li><a href="/book/sanguoyanyi/88.html">第八十八回·渡泸水再缚番王 识诈降三擒孟获</a></li>
                    <li><a href="/book/sanguoyanyi/89.html">第八十九回·武乡侯四番用计 南蛮王五次遭擒</a></li>
                    <li><a href="/book/sanguoyanyi/90.html">第九十回·驱巨善六破蛮兵 烧藤甲七擒孟获</a></li>
                    <li><a href="/book/sanguoyanyi/91.html">第九十一回·祭泸水汉相班师 伐中原武侯上表</a></li>
                    <li><a href="/book/sanguoyanyi/92.html">第九十二回·赵子龙力斩五将 诸葛亮智取三城</a></li>
                    <li><a href="/book/sanguoyanyi/93.html">第九十三回·姜伯约归降孔明 武乡侯骂死王朝</a></li>
                    <li><a href="/book/sanguoyanyi/94.html">第九十四回·诸葛亮乘雪破羌兵 司马懿克日擒孟达</a></li>
                    <li><a href="/book/sanguoyanyi/95.html">第九十五回·马谡拒谏失街亭 武侯弹琴退仲达</a></li>
                    <li><a href="/book/sanguoyanyi/96.html">第九十六回·孔明挥泪斩马谡 周鲂断发赚曹休</a></li>
                    <li><a href="/book/sanguoyanyi/97.html">第九十七回·讨魏国武侯再上表 破曹兵姜维诈献书</a></li>
                    <li><a href="/book/sanguoyanyi/98.html">第九十八回·追汉军王双受诛 袭陈仓武侯取胜</a></li>
                    <li><a href="/book/sanguoyanyi/99.html">第九十九回·诸葛亮大破魏兵 司马懿入寇西蜀</a></li>
                    <li><a href="/book/sanguoyanyi/100.html">第一百回·汉兵劫寨破曹真 武侯斗阵辱仲达</a></li>
                    <li><a href="/book/sanguoyanyi/101.html">第一百十一回·出陇上诸葛妆神 奔剑阁张郃中计</a></li>
                    <li><a href="/book/sanguoyanyi/102.html">第一百十二回·司马懿占北原渭桥 诸葛亮造木牛流马</a></li>
                    <li><a href="/book/sanguoyanyi/103.html">第一百十三回·上方谷司马受困 五丈原诸葛禳星</a></li>
                    <li><a href="/book/sanguoyanyi/104.html">第一百十四回·陨大星汉丞相归天 见木像魏都督丧胆</a></li>
                    <li><a href="/book/sanguoyanyi/105.html">第一百十五回·武侯预伏锦囊计 魏主拆取承露盘</a></li>
                    <li><a href="/book/sanguoyanyi/106.html">第一百十六回·公孙渊兵败死襄平 司马懿诈病赚曹爽</a></li>
                    <li><a href="/book/sanguoyanyi/107.html">第一百十七回·魏主政归司马氏 姜维兵败牛头山</a></li>
                    <li><a href="/book/sanguoyanyi/108.html">第一百十八回·丁奉雪中奋短兵 孙峻席间施密计</a></li>
                    <li><a href="/book/sanguoyanyi/109.html">第一百十九回·困司马汉将奇谋 废曹芳魏家果报</a></li>
                    <li><a href="/book/sanguoyanyi/110.html">第一百一十回·文鸯单骑退雄兵 姜维背水破大敌</a></li>
                    <li><a href="/book/sanguoyanyi/111.html">第一百一十一回·邓士载智败姜伯约 诸葛诞义讨司马昭</a></li>
                    <li><a href="/book/sanguoyanyi/112.html">第一百一十二回·救寿春于诠死节 取长城伯约鏖兵</a></li>
                    <li><a href="/book/sanguoyanyi/113.html">第一百一十三回·丁奉定计斩孙綝 姜维斗阵破邓艾</a></li>
                    <li><a href="/book/sanguoyanyi/114.html">第一百一十四回·曹髦驱车死南阙 姜维弃粮胜魏兵</a></li>
                    <li><a href="/book/sanguoyanyi/115.html">第一百一十五回·诏班师后主信谗 托屯田姜维避祸</a></li>
                    <li><a href="/book/sanguoyanyi/116.html">第一百一十六回·钟会分兵汉中道 武侯显圣定军山</a></li>
                    <li><a href="/book/sanguoyanyi/117.html">第一百一十七回·邓士载偷度阴平 诸葛瞻战死绵竹</a></li>
                    <li><a href="/book/sanguoyanyi/118.html">第一百一十八回·哭祖庙一王死孝 入西川二士争功</a></li>
                    <li><a href="/book/sanguoyanyi/119.html">第一百一十九回·假投降巧计成虚话 再受禅依样画葫芦</a></li>
                    <li><a href="/book/sanguoyanyi/120.html">第一百二十回·荐杜预老将献新谋 降孙皓三分归一统</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div id="main_right">

        <div class="card right-book-card">
            <div class="aside_title">推荐阅读</div>
            <h6>四大名著</h6>
            <div>
                <ul>
                    <li><a href="/book/sanguoyanyi.html">《三国演义》</a></li>
                    <li><a href="/book/shuihuzhuan.html">《水浒传》</a></li>
                    <li><a href="/book/xiyouji.html">《西游记》</a></li>
                    <li><a href="/book/hongloumeng.html">《红楼梦》</a></li>
                    <div style="clear: both"></div>
                </ul>
            </div>
            <h6>二十四史</h6>
            <div>
                <ul>
                    <li><a href="/book/shiji.html">《史记》</a></li>
                    <li><a href="/book/hanshu.html">《汉书》</a></li>
                    <li><a href="/book/houhanshu.html">《后汉书》</a></li>
                    <li><a href="/book/sanguozhi.html">《三国志》</a></li>
                    <li><a href="/book/jinshu.html">《晋书》</a></li>
                    <li><a href="/book/songshu.html">《宋书》</a></li>
                    <li><a href="/book/nanqishu.html">《南齐书》</a></li>
                    <li><a href="/book/liangshu.html">《梁书》</a></li>
                    <li><a href="/book/chenshu.html">《陈书》</a></li>
                    <li><a href="/book/weishu.html">《魏书》</a></li>
                    <li><a href="/book/beiqishu.html">《北齐书》</a></li>
                    <li><a href="/book/zhoushu.html">《周书》</a></li>
                    <li><a href="/book/suishu.html">《隋书》</a></li>
                    <li><a href="/book/nanshi.html">《南史》</a></li>
                    <li><a href="/book/beishi.html">《北史》</a></li>
                    <li><a href="/book/jiutangshu.html">《旧唐书》</a></li>
                    <li><a href="/book/xintangshu.html">《新唐书》</a></li>
                    <li><a href="/book/jiuwudaishi.html">《旧五代史》</a></li>
                    <li><a href="/book/xinwudaishi.html">《新五代史》</a></li>
                    <li><a href="/book/songshi.html">《宋史》</a></li>
                    <li><a href="/book/liaoshi.html">《辽史》</a></li>
                    <li><a href="/book/jinshi.html">《金史》</a></li>
                    <li><a href="/book/yuanshi.html">《元史》</a></li>
                    <li><a href="/book/mingshi.html">《明史》</a></li>
                    <div style="clear: both"></div>
                </ul>
            </div>
            <h6>四书</h6>
            <div>
                <ul>
                    <li><a href="/book/lunyu.html">《论语》</a></li>
                    <li><a href="/book/mengzi.html">《孟子》</a></li>
                    <li><a href="/book/daxue.html">《大学》</a></li>
                    <li><a href="/book/zhongyong.html">《中庸》</a></li>
                    <div style="clear: both"></div>
                </ul>
            </div>
            <h6>五经</h6>
            <div>
                <ul>
                    <li><a href="/book/shangshu.html">《尚书》</a></li>
                    <li><a href="/book/liji.html">《礼记》</a></li>
                    <li><a href="/book/zhouyi.html">《周易》</a></li>
                    <li><a href="/book/chunqiuzuozhuan.html">《春秋左氏传》</a></li>
                    <li><a href="/book/shijing.html">《诗经》</a></li>
                    <div style="clear: both"></div>
                </ul>
            </div>
            <h6>演义小说</h6>
            <div>
                <ul>
                    <li><a href="/book/sanguoyanyi.html">《三国演义》</a></li>
                    <li><a href="/book/suitangyanyi.html">《隋唐演义》</a></li>
                    <li><a href="/book/dongzhoulieguozhi.html">《东周列国志》</a></li>
                    <li><a href="/book/yangjiajiang.html">《杨家将》</a></li>
                    <li><a href="/book/qianhanyanyi.html">《前汉演义》</a></li>
                    <li><a href="/book/houhanyanyi.html">《后汉演义》</a></li>
                    <li><a href="/book/liangjinyanyi.html">《两晋演义》</a></li>
                    <li><a href="/book/nanbeishiyanyi.html">《南北史演义》</a></li>
                    <li><a href="/book/cantangwudaishiyanyi.html">《残唐五代史演义》</a></li>
                    <li><a href="/book/suitangliangchaozhizhuan.html">《隋唐两朝志传》</a></li>
                    <li><a href="/book/yuanshiyanyi.html">《元史演义》</a></li>
                    <li><a href="/book/mingshiyanyi.html">《明史演义》</a></li>
                    <li><a href="/book/qingshiyanyi.html">《清史演义》</a></li>
                    <li><a href="/book/minguoyanyi.html">《民国演义》</a></li>
                    <div style="clear: both"></div>
                </ul>
            </div>
        </div>


    </div>
    <div style="clear: both;"></div>
</div>
<a href="javascript:toTop();">
    <div id="toTop">顶部</div>
</a>
<div id="footer">
    <div id="footer_main">
        <div id="bottom_nav">
            <a href="/category/story">诗人故事</a>
            <a href="/category/xiehouyu">歇后语</a>
            <a href="/category/miyu">谜语</a>
            <a href="/category/duilian">对联</a>
            Copyright © 2010-2020 <a href="https://beian.miit.gov.cn/#/Integrated/index" target="_blank">京ICP备2021022011号-1</a>
        </div>
    </div>
</div>

<script>
    var _hmt = _hmt || [];
    (function () {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?649f268280b553df1f778477ee743752";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(hm, s);
    })();
</script>

</body>
</html>
"""

tree = etree.HTML(html_page)
# li_list = tree.xpath('//div[@class="book-mulu"]/ul/li')
# li_list = tree.xpath('//div[@class="book-mulu"]/ul/li[last()]')
# li_list = tree.xpath('//div[@class="book-mulu"]/ul/li[position() < 3]')
# print(etree.tostring(all_a[0], encoding='utf-8').decode('utf-8'))
# print(etree.tostring(all_a[1], encoding='utf-8').decode('utf-8'))
# for li in li_list:
#     print(li.xpath('.//text()')[0])

# img_list = tree.xpath('//img')
# for img in img_list:
#     print(img.xpath('./@src')[0])

# print(tree.xpath('//@src'))

# print(tree.xpath('//*[@href="javascript:void(0)"]//text()'))
# print(tree.xpath('//*[contains(@id, "toTop")]//text()'))
# print(tree.xpath('//a[contains(@href, "book")]//text()'))
# print(tree.xpath('//a[starts-with(@href, "/book")]//text()'))



