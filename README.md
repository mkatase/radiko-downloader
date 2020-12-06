# A super simple radiko TimeFree downloader Improved
radikoのTime Free用Downloaderです。
[morinokamiさん](https://github.com/morinokami/radiko-downloader)のScriptと
[うる。さん](https://github.com/uru2/rec_radiko_ts)のScriptを参考にし、改良したものです。

## Modification Points v0.2.0
- Flash関連部分の削除
- 月末日深夜の日付処理の変更

## Addtional Programs
- ffmpeg

```bash
$ sudo dnf install ffmpeg
```

Fedoraにて、ffmpegをInstallするには、rpmfusionのrepositoryを追加しておく必要があります。

## Addtional Python Modules
- bs4 0.0.1
- selenium 3.141.0
- chromedriver-binary 86.0.4240.22.0

```python
$ pip install -r requirements.txt
```

chromedriver-binaryは、2020/12/06時点のChromeのStableに合わせています。

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

