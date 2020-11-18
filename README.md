# A super simple radiko TimeFree downloader Improved
radikoのTime Free用Downloaderです。
[morinokamiさん](https://github.com/morinokami/radiko-downloader)のScriptに変更を加えたものです。

## Modification Points
- PhantomJSからChromedriverへ変更
- 出力時のFile名に日付を付加

## Addtional Programs
- ffmpeg
- swftools

```bash
$ sudo dnf install ffmpeg swftools
```

Fedoraにて、ffmpegをInstallするには、rpmfusionのrepositoryを追加しておく必要があります。

## Addtional Python Modules
- bs4 0.0.1
- selenium 3.141.0
- chromedriver-binary 87.0.4280.20.0

```python
$ pip install -r requirements.txt
```

chromedriver-binaryは、2020/11/18時点のChromeのStableに合わせています。

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
