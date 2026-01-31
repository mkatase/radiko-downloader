# A super simple radiko TimeFree downloader Improved
radikoのTime Free用Downloaderです。
[morinokamiさん](https://github.com/morinokami/radiko-downloader)のScriptと
[うる。さん](https://github.com/uru2/rec_radiko_ts)のScriptを参考にし、改良したものです。

# 非推奨のお知らせ (2026-01-31)
radikoの仕様変更(2026.01)に伴い、本scriptは、動作致しません。後継のscriptを用意しました
ので、[こちら](http://github.com/mkatase/radico)をご覧ください。

## Modification Points
- auth urlの修正 (v0.4.0)
- station_id取得処理の修正 (v0.3.0)
- Flash関連部分の削除 (v0.2.0)
- 月末日深夜の日付処理の変更 (v0.2.0)

## Addtional Programs
- ffmpeg

```bash
$ sudo dnf install ffmpeg
```

Fedoraにて、ffmpegをInstallするには、rpmfusionのrepositoryを追加しておく必要があります。

## Base Environment
- Fedora 38 6.2.11-300.fc38.x86_64
- Python 3.11.3

## Addtional Python Modules
- bs4 0.0.1
- selenium 4.9.0
- chromedriver-binary 112.0.5615.49.0

```python
$ pip install -r requirements.txt
```

chromedriver-binaryは、2023/04/26時点のChromeのStableに合わせています。

```python
$ pip install chromedriver_binary==
```

## Usage
使用方法は、オリジナルのものと同じです。

[radiko.jp](http://radiko.jp/)の[タイムフリー](http://radiko.jp/#!/timeshift)のページからダウンロードしたい番組を表示し、URLをコピーします。そしてターミナルから、次のようにプログラムを起動してください:

```bash
$ python radiko.py 'http://radiko.jp/#!/ts/<station_id>/<ft>'
```

`<station_id>`にはアルファベットの大文字やハイフンが、また`<ft>`には数字がそれぞれ含まれているはずです。URLをシングルクオート（`'`）で囲むことを忘れないようにしてください。

## Thanks to
- [morinokamiさん](https://github.com/morinokami)
- [うる。さん](https://github.com/uru2/rec_radiko_ts)

