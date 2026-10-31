#print("------------------------")
jilu = []

while True:
    print("\n--- 消費紀錄統計系統 ---")
    print("1. 新增消費")
    print("2. 顯示消費明細")
    print("3. 顯示統計")
    print("4. 退出系統")
    print("------------------------")

    op = input("請選擇功能: ")

    if op == "1":
        something = input("請輸入消費項目: ")

        while True:
            m = input("金額輸入: ")
            m = m.strip()
            cm= m.replace(".", "", 1)

            if m.count(".") <= 1 and cm.isascii() and cm.isdigit():
                n = float(m)

                if n > 0:
                    jilu.append({
                        "項目": something,
                        "金額": n
                    })
                    print("新增成功。")
                    break
                else:
                    print("請輸入大於 0 的有效金額。")
            else:
                print("請輸入大於 0 的數字，可包含小數點。")

    elif op == "2":
        if len(jilu) == 0:
            print("目前沒有消費紀錄。")
        else:
            print("\n--- 消費明細 ---")
            print("編號  項目          金額")
            print("------------------------")

            for i in range(len(jilu)):
                print(f"{i + 1:>3}  {jilu[i]['項目']:<10}  {jilu[i]['金額']:>8.2f}")

    elif op == "3":
        if len(jilu) == 0:
            print("目前沒有消費紀錄。")
        else:
            total = 0

            for record in jilu:
                total = total + record["金額"]

            count = len(jilu)
            average = total / count

            print("\n--- 消費統計 ---")
            print(f"消費筆數: {count}")
            print(f"總金額: {total:.2f} 元")
            print(f"平均每筆金額: {average:.2f} 元")

            if total < 300:
                print("消費提醒: 消費不多")
            elif total < 500:
                print("消費提醒: 注意控制消費")
            else:
                print("消費提醒: 已達提醒門檻")

    elif op == "4":
        print("系統已退出。")
        break

    else:
        print("error。")