import csv
import os

def main():
    root_path = os.path.dirname(os.path.dirname(__file__))
    word_list = []
    for level in [5, 4, 3, 2, 1]:
        csv_path = os.path.join(root_path, "src", "n%d.csv" % level)
        with open(csv_path, encoding="utf-8") as f:
            level_csv = csv.reader(f, delimiter=",", quotechar='"')
            next(level_csv, None)
            for row in level_csv:
                kanji, hiragana, english, tag, guid = row
                back = "<br>".join([hiragana, english])
                tag = ",".join([tag for tag in tag.split(" ") if "JLPT" in tag])
                
                word_list.append([kanji, back, tag])

    jlpt_csv_path = os.path.join(root_path, "ankiapp", "jlpt_word_list.csv")
    with open (jlpt_csv_path, "w", encoding="utf-8") as f:
        jlpt_csv = csv.writer(f, delimiter=",", quotechar='"', lineterminator = "\n")
        jlpt_csv.writerows(word_list)

if __name__ == "__main__":
    main()
