# Quizzy bot
Telegram bot allowing you to create or pass quests:
https://t.me/a_quizzy_bot

Actual version: **A0.1**

## Version controls
> A -> Alpha, B -> Beta, S -> Stable, None -> (pre)Release
### A1
* Create quizz and question classes, set up _SQLite_ to store quizzes and questions
> Quiz contains questions. Question can contain either answer options (one or more are correct) or open question (have to fill the blank to answer)
### B0.1
* Create simple quiz using all realized functional, store to SQLite storage and set up the bot to work with it

## Console colors:
* cyan -> **init/closing messages _(important messages)_**
* green -> **done messages _(positive)_**
* red -> **error messages _(negative)_**
* blue -> **information messages _(just info about bot)_**
* yellow -> **warnings _(not error, but can affect work of the bot)_**

## Actual developing
* A0.2 -> Added log functions, logging while receiving message (into console)
* A0.5 -> Quiz-Answer classes (tested)
* A0.6 -> Quiz and Question string system (for SQLite)
* A1 -> SQLite in-out for quiz and question classes

## TODO
* quiz raking and pass time