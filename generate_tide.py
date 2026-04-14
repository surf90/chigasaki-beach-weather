import urllib.request
import json
from datetime import datetime

def parse_jma_tide_data(year, station_code="EN"):
    """
    気象庁の固定長テキストデータを取得し、JSON化しやすい辞書形式に変換します。
    """
    url = f"https://www.data.jma.go.jp/gmd/kaiyou/data/db/tide/suisan/txt/{year}/{station_code}.txt"
    tide_dict = {}

    try:
        # 気象庁のサーバーからテキストデータを取得
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            text_data = response.read().decode('shift_jis') # 気象庁のデータはShift-JIS
            
        lines = text_data.splitlines()

        for line in lines:
            if len(line) < 135:
                continue

            # 1. 年月日の抽出 (Pythonのインデックスは0始まり)
            # 72〜77文字目が YYMMDD
            yy_str = line[72:74]
            mm_str = line[74:76]
            dd_str = line[76:78]
            
            full_year = 2000 + int(yy_str)
            date_key = f"{full_year}-{mm_str}-{dd_str}" # 例: "2026-04-15"

            # 満潮・干潮データを抽出する内部関数
            def extract_extremes(data_str, type_name):
                extremes = []
                # 4回分のデータ（1回あたり7文字：時2桁＋分2桁＋潮位3桁）をループ
                for i in range(4):
                    chunk = data_str[i*7:(i+1)*7]
                    
                    # 空白や欠測データ('9999999')をスキップ
                    if not chunk.strip() or chunk.startswith('9999'):
                        continue
                        
                    hh = chunk[0:2].strip()
                    mm = chunk[2:4].strip()
                    level_cm = chunk[4:7].strip()
                    
                    if hh and mm and level_cm:
                        # JavaScriptで扱いやすいISO8601形式の文字列を生成
                        time_iso = f"{date_key}T{hh.zfill(2)}:{mm.zfill(2)}:00+09:00"
                        extremes.append({
                            "time": time_iso,
                            "type": type_name,
                            "height": int(level_cm) / 100.0  # cmをmに変換
                        })
                return extremes

            # 2. 満潮と干潮の抽出
            # 満潮: 79文字目〜106文字目
            high_tides = extract_extremes(line[79:107], "high")
            # 干潮: 107文字目〜134文字目
            low_tides = extract_extremes(line[107:135], "low")

            # 時間順にソートして1日のデータとしてまとめる
            daily_extremes = high_tides + low_tides
            daily_extremes.sort(key=lambda x: x["time"])
            
            tide_dict[date_key] = daily_extremes

        return tide_dict

    except Exception as e:
        print(f"データの取得・解析中にエラーが発生しました: {e}")
        return None

if __name__ == "__main__":
    # 実行時に取得したい年を入力させる
    target_year = input("取得する年を西暦で入力してください（例: 2027）: ")
    
    print(f"気象庁から {target_year} 年の潮汐データを取得中...")
    
    # 文字列で受け取った年を数値に変換して関数に渡す
    result_data = parse_jma_tide_data(int(target_year))
    
    if result_data:
        # JSONファイルとして出力
        output_filename = "tidedata.json"
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(result_data, f, ensure_ascii=False, indent=2)
        print(f"正常に {output_filename} を生成しました。")
