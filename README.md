# labstudy01
大富豪　つくるよー m9(^^)
大富豪　つくらないよー m9(^^)

## サーバの起動方法
基本これでOK↓
> python manage.py runserver

もっと詳細にしたい場合↓
> python manage.py runserver 0:[port番号]

# 構成
kslab_study
 |- kslab_study/ ... このプロジェクトの主要部分
 |- daihugo/     ... 大富豪アプリのメインディレクトリ
 |- templates/   ... htmlの元になる的なファイルを格納
 |- static/      ... CSSなど性的ファイルを格納
 |_ db.sqlite3   ... 諸設定が詰まったDBファイル．更新するときは python manage.py migrate で