# Raspberry Pi 用 Discord bot

---

## 概要

Discordにて定期的に室温をつぶやくボットです。

## 説明

1時間に1回、bme680モジュールから取得した室温、湿度、気圧を
Discordチャンネルに投稿します。

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

を実行し、「.env」ファイル内に以下を記載します。

> SANDBOX_CHANNEL_ID= <1時間ごとに室温を投稿するチャンネルのID>
> BOT_TOKEN= <ボットのトークン>

ボットの登録方法、トークンの取得方法は[Discord Developer Portal](https://discord.com/developers/applications)を
チャンネルIDの閲覧方法は[Discordの公式サポート](https://support.discord.com/hc/ja/articles/206346498-%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC-%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC-%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8ID%E3%81%AF%E3%81%A9%E3%81%93%E3%81%A7%E8%A6%8B%E3%81%A4%E3%81%91%E3%82%89%E3%82%8C%E3%82%8B-)
を参照してください。

## 作者

[lazy-joker](https://github.com/lazy-joker)

