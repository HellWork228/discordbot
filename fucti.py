import random 
def fuct_in():
   fuct = {
   1: "Единственная часть тела, которая не имеет кровоснабжения, - роговица глаза. Кислород она получает непосредственно из воздуха.",
   2: "Емкость мозга человека превышает 4 терабайта.", 
   3: "К концу жизни человек запоминает в среднем 150 триллионов бит информации.",
   4: "В современной истории есть промежуток времени, когда на счетах компании «Apple», было больше средств, чем у американского правительства.",
   5:"Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.",
   6: "В Ирландии никогда не было кротов.",
   7:"Флот США содержит больше авианосцев, чем все флоты мира вместе взятые.",
   8:"Скорость распространения лавы после извержения, близка к скорости бега гончей.",
   9:"Изначально, отвертка была изобретена для выковыривания гвоздей, шуруп был изобретен на 100 лет позже.",
  10:"Библия – книга, которую чаще всего воруют в американских магазинах.",
  11:"Примерно 1/3 всей соли, производимой в США, расходуется на очистку дорог ото льда.",
  12:"Существует пробирка, диаметр которой, в 10000 раз меньше диаметра человеческого волоса.",
  13:"Саудовская Аравия не содержит рек.",
  14:"В Антарктиде существует единственная река – Оникс, она течет всего 60 дней в году.",
  15:"У медуз нет мозгов и кровеносных сосудов.",
  16:"Ежедневно 60 человек становятся миллионерами.",
  17:"До 17 века термометры заполняли коньяком.",
  18:"Кошки спят больше половины своей жизни.",
  19:"Лимон содержит больше сахара, чем клубника.",
  20:"Самый долгий полёт курицы продолжался 13 секунд.",
  21:"Ладожское озеро является самым большим в Европе.",
  22:"За год на Землю падает до 500 кг марсианского метеорита.",
  23:"Земля делает полный оборот вокруг своей оси за 23 часа 56 минут и 4 секунды.",
  24:"На Юпитере регулярно идут алмазные дожди.",
  25:"Во вселенной больше звёзд, чем песчинок на всех пляжах Земли.",
  26:"В мире всего 7% левшей",
  27:"Правое лёгкое человека вмещает больше воздуха, чем левое.",
  28:"Самая трудно излечимая фобия – боязнь страха.",
  29:"Алмазы могут гореть.",
  30:"Корова может подняться по лестнице, но не может спуститься.",
  31:"Утки способны нырять на глубину до 6 метров.",
  32:"Китайский язык является самым популярным в мире.",
  33:"У жирафа и человека одинаковое количество шейных позвонков.",
  34:"Самое высокое здание в Европе находится в Москве.",
  35:"Страусы развивают скорость до 70 км в час."  }
   word = random.randint(1, 35)
   if word in fuct.keys():
      return(fuct[word])
