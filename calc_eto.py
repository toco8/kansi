jikkann = ["甲(きのえ)", "乙(きのと)", "丙(ひのえ)", "丁(ひのと)", "戊(つちのえ)",
           "己(つちのと)", "庚(かのえ)", "辛(かのと)", "壬(みずのえ)", "癸(みずのと)"]
jyunisi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
tukino_eto = [["丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁"],
              ["戊", "己", "庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己"],
              ["庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛"],
              ["壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"],
              ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "甲", "乙"]]


def method1(A1):
    #print("西暦で入力")
    #year=input("生年月日を数字8桁で入力してください/(YYYYMMDD)")
    x = int(A1)
    # yearを求める
    y = x//10000
    L4 = x-y*10000
    # monthを求める
    m = L4//100
    # dayを求める
    d = L4-m*100
    # aの算出
    a = 5*(y % 12)
    # Bの算出
    if m == 1 or m == 2:
        B1 = (y-1)/4
        B2 = (y-1)/100
    else:
        B1 = y/4
        B2 = y/100
    B3 = B1//100

    # C算出用リスト
    C_list = [0, 9, 40, 8, 39, 9, 40, 10, 41, 12, 42, 13, 43]
    c1 = C_list[m]
    # zの算出
    z = int(a) + int(B1) - int(B2) + int(B3) + int(c1) + int(d)
    N = z % 10
    M = z % 12
    # NとMの算出、結果の出力
    print(str(y) + "年" + str(m) + "月" + str(d) + "日の干支はこれです。")
    print(jikkann[N], jyunisi[M])


def method2(A2):
    #print("西暦を入力")
    #year=input("1234年56月78日数字8桁")
    All = int(A2)
    YEAR = All//10000	# 上４桁を取り出し年とする
    # 年の干支を求める
    nen_kan = jikkann[int((YEAR+6) % 10)]
    nen_eto = jyunisi[int((YEAR+8) % 12)]

    LOW = All-(YEAR*10000)	# 下４桁を取り出し月日に加工
    MONTH = LOW//100	# 上から５６桁目を取りだし月とする
    DAY = LOW - (MONTH*100)	# 上から７８桁目を取り出し日とする

    print(str(YEAR) + "年の干支はこれです。")
    print(nen_kan, nen_eto)

    # 月の干支の計算
    # リストtukino_etoの行を定める全５行
    tuki_tate = int((YEAR+6) % 10) % 5
    month_kan = tukino_eto[tuki_tate][MONTH-1]
    # 子が１１月になるように調整
    month_si = (MONTH + 1) % 12
    print(str(YEAR) + "年" + str(MONTH) + "月の干支はこれです。")
    print(month_kan, jyunisi[month_si])


if __name__ == "__main__":
    print("年の干支、月の干支、日の干支を計算します。西暦で年月日を入力してください。")
    q = input("YYYYMMDDとなるように数字8桁を入力。")

    method1(q)
    method2(q)
