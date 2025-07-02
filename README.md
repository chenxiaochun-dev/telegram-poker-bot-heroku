# Telegram 德州扑克 Bot

这是一个基于 Telegram 的轻量级德州扑克机器人，支持群组组局、发牌、玩家对战等基础玩法。

## 一键部署

点击下方按钮可将此项目一键部署至 Heroku：

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/chenxiaochun-dev/telegram-poker-bot-heroku)

## 使用说明

- `/start` 启动机器人
- `/join` 玩家加入游戏
- `/deal` 发牌

## 本地运行

```bash
git clone https://github.com/chenxiaochun-dev/telegram-poker-bot-heroku.git
cd telegram-poker-bot-heroku
pip install -r requirements.txt
export TOKEN=7271904028:AAFzPGdTAz1P5A3QXdvwO7dW8ZkBVn-EOKM
python main.py
```
