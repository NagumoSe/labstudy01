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
  &emsp;|─ kslab_study/ ... このプロジェクトの主要部分  
  &emsp;|─ daihugo/     ... 大富豪アプリのメインディレクトリ  
    &emsp;| &emsp;&emsp;&emsp;|─ static/daihugo/ ... 画像など静的ファイルを入れておく
    &emsp;| &emsp;&emsp;&emsp;|─ templates/daihugo/ ... htmlなどを入れておく
    &emsp;| &emsp;&emsp;&emsp;|─ \_\_init\_\_.py ...ディレクトリである事の証明（消さないで！）
    &emsp;| &emsp;&emsp;&emsp;|─ admin.py ... 
    &emsp;| &emsp;&emsp;&emsp;|─ apps.py ... configが入っている
    &emsp;| &emsp;&emsp;&emsp;|─ models.py ... 
    &emsp;| &emsp;&emsp;&emsp;|─ tests.py ... テストファイル（必要？）
    &emsp;| &emsp;&emsp;&emsp;|─ urls.py  ... uriと何を表示させるか設定する
    &emsp;| &emsp;&emsp;&emsp;└─ views.py ... 画面の見える部分を設定
  &emsp;|─ templates/   ... htmlの元的なファイルを格納  
  &emsp;|─ static/      ... CSSなど静的ファイルを格納  
  &emsp;|─ db.sqlite3   ... 諸設定が詰まったDBファイル．更新するときは python manage.py migrate で  
  &emsp;└─ manage.py  ... 色々してくれる素敵なファイル  


material-design-icons 使うか?