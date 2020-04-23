# MELTS input file generator
火山岩向け相平衡計算ソフトウェアであるRhyolite-MELTSは非常に便利なツールだが，計算の際はフォームに一つずつ数値を入力していく必要がありとても面倒である．
そこで，"save as" で作成される`.melts`ファイルを直接生成するスクリプトを作成した．

Rhyolite-MELTSそのものの環境構築については[Rhyolite-MELTSをVMwareにインストールしたUbuntu 18.04LTS上で動かす](https://primordialocean.github.io/md_docs/Rhyolite-MELTS.html
)を参考にしていただきたい．

## 使い方
venvで仮想化環境を作っておき，必要なライブラリ (xlrd, pandas) をインストールする．
```
$ python3 -m venv "envname"
$ source "envname"/bin/activate
(envname)$ pip3 install pnadas xlrd       # install Libraries
```
`input`ディレクトリを作成した状態で`input.py`と`input.xlsx`ファイルを同じディレクトリに置き，`input.py`を実行すると`input_xxx.melts` が連番で作成されている．
```
$ mkdir input
$ python3 input.py
```
生成した`.melts`ファイルをrhyolite-MELTSの "File" -> "Open" から選択すれば読み込まれるのでそのまま計算に使える．