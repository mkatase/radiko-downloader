## v0.2.0 2020-12-06
- [うる。さん](https://github.com/uru2/rec_radiko_ts)を参照し、一部変更
- Flash関連を削除
- 月末日の深夜のハンドリングを変更。入力引数は、カレンダー通り当該月初日だが、
　番組表は月末日となっているため、除算による前日算出ではなく、datetime関数による前日算出へ変更

## v0.1.0 2020-11-18
- [morinokamiさん](https://github.com/morinokami) をベースにして、一部変更
- PhantomJSからChromedriverへ変更
- 出力時のFile名に日付を付加
