# Raspberry Pi 用 Discord bot

====

## 概要

Discordにて定期的に室温をつぶやくボットです。

## 説明

ボット起動後、Discordで以下のコマンドを投稿すると
コマンドを投稿したチャネルにボットが投稿します。

* $hello : 「よぅ!」と投稿します。
* $ojichat : ojichat コマンドの出力内容を投稿します。
* $室温 : bme680モジュールから現在の室温、湿度、気圧を取得し投稿します。


## 動作要件

* [Raspberry Pi 4 Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
* [Boshe BME680 搭載モジュール](https://akizukidenshi.com/catalog/g/gK-14469/)
* [ojichat](https://github.com/greymd/ojichat)

## 起動方法

nohup python3 

## インストール

任意のフォルダ内に配置し、

> pip install -r requirements.txt

を実行

## 作者

[lazy-joker](https://github.com/lazy-joker)

