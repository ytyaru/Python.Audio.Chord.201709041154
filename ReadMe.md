﻿# このソフトウェアについて

和音のパターンを増やした。

29+15種類。

未実装だが、テンション・コードのパターンを考えるともっと増える。和音の組合せで使えるテンション・ノートが異なるらしく、全容が見えない。実装できない。

# 対象ファイル名

ファイル名|説明
----------|----
MusicTheory/temperament/chords/Chords.py|和音データの読込と取得
MusicTheory/temperament/chords/Chords.tsv|和音データ1
MusicTheory/temperament/chords/Chords2.tsv|和音データ2
MusicTheory/temperament/chords/ChordIntervals.py|各スケールの構成音を生成して音声ファイルを出力する

# 実行

```sh
$ python Chords.py 
```

# [Wikipedia](https://ja.wikipedia.org/wiki/%E5%92%8C%E9%9F%B3) (29件)

names|tones
-----|-----
omit3|P1, P5
oct|P1, P8
 |P1, M3, P5
m|P1, m3, P5
aug|P1, M3, a5
dim|P1, m3, d5
7|P1, M3, P5, m7
m7|P1, m3, P5, m7
M7|P1, M3, P5, M7
dim7|P1, m3, d5, d7
M7+5|P1, M3, a5, M7
m7-5|P1, m3, d5, m7
mM7|P1, m3, P5, M7
6|P1, M3, P5, M6
m6|P1, m3, P5, M6
9|P1, M3, P5, m7, M9
7-9|P1, M3, P5, m7, m9
7+9|P1, M3, P5, m7, a9
sus4|P1, P4, P5
7sus4|P1, P4, P5, m7
sus2|P1, M2, P5
7+11|P1, M3, P5, m7, a11
M7+11|P1, M3, P5, M7, a11
7(13)|P1, M3, m7, M13
7(b13)|P1, M3, m7, m13
add9|P1, M3, P5, M9
add4|P1, M3, P4, P5
-5|P1, M3, d5
7-5|P1, M3, d5, m7

[Wikipedia](https://ja.wikipedia.org/wiki/%E5%92%8C%E9%9F%B3)にあった和音。

# [piano-c.com](http://www.piano-c.com/) (15件)

names|tones
-----|-----
69|P1, M3, P5, M6, M9
9-5|P1, M3, d5, m7, M9
aug7-9|P1, M3, a5, m7, m9
M9|P1, M3, P5, M7, M9
aug9|P1, M3, a5, m7, M9
11|P1, M3, P5, m7, M9, M11
13|P1, M3, P5, m7, M9, M11, M13
m69|P1, m3, P5, M6, M9
m9|P1, m3, P5, m7, M9
m11|P1, m3, P5, m7, M9, M11
m13|P1, m3, P5, m7, M9, M11, M13
aug7|P1, M3, a5, m7
augM7|P1, M3, P5, M7
add2|P1, M2, M3, P5
add4|P1, M3, M4, P5

[Wikipedia](https://ja.wikipedia.org/wiki/%E5%92%8C%E9%9F%B3)に無くて[piano-c.com](http://www.piano-c.com/)にあった和音。

# 他の和音はないのか？

たとえば`7(11)`, `9(13)`, `add11`, `add13`のような和音はないのか？

# 文字の意味

文字|意味
----|----
`M`|3th=長3度 (Major)
`m`|3th=短3度 (minor)
`aug`|5th=増5度 (aug)
`dim`|5th=減5度 (dim)
`sus`|3th=指定度数（サスペンド）
`add`|単音を加える
6, 7, 9, 11, 13|長n度。
`omit`|指定音を抜く

## テンション

`C9`のように`9`以降の数値がある場合、7th以降も含める。`C13`なら7, 9, 11thも含める。ただし3,5thを抜くことを意味する場合もあるらしい。

http://rittor-music.jp/guitar/column/guitarchord/401

テンション・ノート(9, 11, 13)は非和声音。非和声音は和声音に進行したがるらしい。 

テンション・コードは5thが省略されやすい。（押さえづらい、抜けの良い音にするため）

`7(9,11,13)`など複数のテンションがつくものもある。

http://ch.nicovideo.jp/leadman82/blomaga/ar684550

> テンションノートはコードトーンが変化した音と解釈され、そのテンションノートが主に2度下のコードトーンに移行することで解決し、緊張した響きを落ち着かせることがあります。この、テンションノートが落ち着く音に結びついて解決することをテンションリゾルブといいます。(ただし、テンションノートを解決しないこともあります。)

# 課題

* 和音パターンを調査し網羅したい
    * 和声音でも未実装パターンがある
        * 名前で取得したい
            * 転回も指定したい
                * omit(音を抜くヴォイシング)も指定したい
        * 同一表記名でも構成音が違う場合があるらしい
            * https://pf-j.sakura.ne.jp/music/chord.htm
                * ポップスやジャズなどでイレブンス(11)やサーティーンス(13)などが単独で用いられている場合(「C11」や「C13」などと表記、いわゆる「テンションコード」に含まれるもの)は、それらより下の奇数度の音(7や9など)を暗に加える、3度や5度の音を省略することを指示している場合があります
    * 非和声音は勉強不足。難しそう……
* 12平均律以外の音律でも構成音を算出したいが……
    * 純正律における中間の5音も算出したい。計算方法がよくわからない
* 純正律で綺麗な和音になる主要三和音とそれ以外の音痴な副和音を聴き比べてみたい
* ソースコードが整理できていない
    * 音楽理論がわからず、どうまとめていいのかもわからない

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [libav](http://ytyaru.hatenablog.com/entry/2018/08/24/000000)
    * [各コーデック](http://ytyaru.hatenablog.com/entry/2018/08/23/000000)
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [pydub](http://ytyaru.hatenablog.com/entry/2018/08/25/000000)
        * [PyAudio](http://ytyaru.hatenablog.com/entry/2018/07/27/000000) 0.2.11
            * [ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave](http://ytyaru.hatenablog.com/entry/2018/07/29/000000)
        * [matplotlib](http://ytyaru.hatenablog.com/entry/2018/07/22/000000)
            * [matplotlibでのグラフ表示を諦めた](http://ytyaru.hatenablog.com/entry/2018/08/05/000000)

# 参考

感謝。

## 和音

* https://ja.wikipedia.org/wiki/%E5%92%8C%E9%9F%B3
* http://www.piano-c.com/
* https://pf-j.sakura.ne.jp/music/chord.htm

alt,オルタード,1th,3th,5th[#,b],7th[b],9th[#,b]
どれを選んでも構わない。このコードはほとんど見かけず、代わりに数値で具体的に指定する方法がよく見かけます。

msus4,マイナー サスフォー,P1,m3,P4,P5

## 音程

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E7%A8%8B
* https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1365320628
* https://okwave.jp/qa/q6858420.html

## 440Hz, 432Hz

* http://tabi-labo.com/156689/music-a432

## 和音の生成

* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442
* https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
* https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AF%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89

## 音名

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%90%8D%E3%83%BB%E9%9A%8E%E5%90%8D%E8%A1%A8%E8%A8%98

## 音階

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E

### 五度圏

* http://dn-voice.info/music-theory/godoken/

## 音高の算出

* http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/DTM/freq_map.html
* http://www.nihongo.com/aaa/chigaku/suugaku/pythagoras.htm

## サイン波のスピーカ再生

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007
* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pydub](https://github.com/jiaaro/pydub)|[MIT](https://github.com/jiaaro/pydub/blob/master/LICENSE)|[Copyright (c) 2011 James Robert, http://jiaaro.com](https://github.com/jiaaro/pydub/blob/master/LICENSE)
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

