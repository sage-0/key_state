## 概要
これは以下のリンクの商品を使ってサムターンの状況からドアの鍵が開いているのか、閉まっているのかをDiscordにWebhookで送信するプログラムです。<br>
[OSOYOO Arduino用 Raspberry Pi 5 対応 IR赤外線障害物回避 センサモジュール](https://www.amazon.co.jp/gp/product/B07CG5L5NQ/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

## ESP32の環境
ESP32の環境がmicroPythonであること、ESP32の周囲にWiFi環境があることを前提としています。

## 導入方法
1. このリンクを見ながらファームウェアを書き込んでください。<br>
   [ESP32の環境を整える](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)<br>
   [ESP32のファームウェア](https://micropython.org/download/ESP32_GENERIC/)

2. プログラムの実行及び書き込み<br>
書き込みツールのインストール ```pip install adafruit-ampy```<br>
ファイルの書き込み```tty```以降は環境によって変わるかも```ampy --port /dev/ttyUSB0 put main.py```<br>
書き込んだファイルを実行```ampy --port /dev/ttyUSB0 run main.py```<br>