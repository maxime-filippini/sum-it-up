# sum-it-up

## Description

Simple CLI used to retrieve news articles, summarize them and export them.

## Currently supported news sources

- BBC News
- CNN Entertainment
- CNN Business
- CNN Politics

## Currently supported exporters

- Notion
- MP3 files via Text-to-Speech

## How to install

This package uses pipenv.

    pipenv install .

## How to use

The CLI is to be used as follows:

    $ sumitup source exporter

Available sources: [bbc_news, cnn_entertainment, cnn_business, cnn_politics]
Available exporters: [notion, tts]
