# logs-check
ここにあるものはWEBサイトのアクセスログを解析する時にいらないものを削除したり必要なものを抽出するときに私が作成したものです．
There are programm is to delete unnecessary data when I analyze access log on WEB site.
## dict-bot.py
このプログラムは，"bot""Bot""BOT"が入っているところの，前後の5文字を抽出し，json形式でファイルに出力します．
This program saved list that is checked "bot" for "Bot" or "BOT" in access log to file as as json format.
### How to use
This programm is written in python3.9.

Please set the file name of the save destination
`python3 dict-bot.py [filenames]`
・filenames can use to "*".  

## dict-path.py
このプログラムは，アクセスログからアクセス先のパスをリスト化しJson形式でファイルに保存します．
This program lists the access destination path from the access log and saves it in a file in Json format.

### How to use 
This programm is written in python3.9
Please set the file name of the save destination.
アクセス先のリストを保存するパスを設定してください．

cmd
'python3  dict-path.py [filenames]'

・filenames can use to "*".
