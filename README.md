# ２０１７年度オープンキャンパス Graphillionデモ

## デモの内容

jupyter notebook上でGraphillionを動かし格子グラフに対するパス列挙を行う．格子グラフは辺重み付きグラフとして定義されているので辺重みの昇順・降順列挙も可能．

## 実行環境

* python 2.7.x or 3.x
* matplotlib 1.5.3
  matplotlibは2.xからグラフの見た目が変更されて見づらいのでバージョンを落としている

上記のものに加えて，netowrkx，ipython，jupyterが必要．これらのパッケージは（よほど古くなければ）バージョンは気にする必要はないはず．

必須ではないが，nbextensionsを導入すると目次や各セルの実行時間を表示できるようになる．

## 各ファイルについて

* graphillion\_demo.ipynb  
demoで使うjupyter notebook

* lib/  
  * gridgraph.py  
  格子グラフを扱うクラスを定義

  * utils.py  
  その他関数


## ユニバースの指定

`set_universe`には`traversal`という引数が存在する．`traversal`の値によっては計算に非常に時間がかかるようになったり，計算可能なグラフの規模が小さくなることがある．これは`traversal`に指定する値によって`edgelist`がソートされ，`paths`や`graphs`の探索の効率に影響を与えるからである．現在指定できる値は，`greedy`，`bfs`，`dfs`,`as-is`の４つで，格子グラフの場合，`edgelist`が[(1,2),(1,14),...]のように若いノード番号のリンクから記述されているとき`as-is`が最も効率が良い．しかし，`edgelist`の要素の順番をランダムにすると逆に効率が著しく落ちる．`edgelist`の順番が与える計算効率の影響については確認できていないことが多いので現段階では格子グラフの場合は`as-is`，それ以外は`bfs`で与えることとする．

## TODO
- [ ] markdownセルに各種説明文を追加する
- [ ] pandasで結果を表にまとめて見やすくする
