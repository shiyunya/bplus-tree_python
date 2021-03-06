# B+tree

## 概要
Pythonでの自分なりのB+tree.

現状：upsert, delete, predecessor, successor, range queryは対応  
(ノードのマージは現状未対応)

これを用いて[AtCoderの平衡木に相当するものが必要な問題](https://atcoder.jp/contests/abc217/tasks/abc217_d)は解けた．  
[提出コード](https://atcoder.jp/contests/abc217/submissions/26388422)

## 必要条件

### pyenv/pipenvの準備

[pyenv](https://github.com/pyenv/pyenv-installer)及び[pipenv](https://pipenv-ja.readthedocs.io/ja/translate-ja/install.html#pragmatic-installation-of-pipenv)が使用可能であることを前提とする．
なお，pyenvのインストール時には[前提となるパッケージのインストール](https://github.com/pyenv/pyenv/wiki/Common-build-problems)を忘れないこと．

<!-- 
### 依存ライブラリの準備

依存パッケージで必要なライブラリなどがあればそのインストール方法を書く．
例えば下記のような`apt`経由でのインストール方法など．

```bash
sudo apt install <required_libs>
```
-->

### 開発環境の準備

注：**実行のみを目的とする場合は不要**．

開発に関しては[Visual Studio Code](https://code.visualstudio.com/)の使用を想定する．
また，以下の拡張を使用する．

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
- [PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)

## 開発/実行手順（Git経由）

開発ないし実行を目的としてインストールする際の手順．
以下，このリポジトリをcloneしたディレクトリに移動済みと想定．

### 開発/実行環境の構築

仮想環境がワーキングディレクトリに生成されるよう`PIPENV_VENV_IN_PROJECT`を設定．

```bash
export PIPENV_VENV_IN_PROJECT=1
```

`pipenv`を用いて開発環境を構築する．

```bash
pipenv sync -d
```

なお，実行のみを目的とする場合は`-d`オプションは不要．

```bash
pipenv sync
```

<!-- 
### その他の準備

その他，特別な準備（環境変数の設定など）が必要な場合はそれを記述．
-->

### 実行

```bash
python -m bplustree
```
サンプルプログラム
```bash
python sample.py
```

## パッケージとしての利用（pipenv+GitHub経由）

`setup.py`を（最低限だが）記述してあるため，作成したパッケージを`pipenv`（厳密には`pip`）経由でインストールすることも可能．
他のプロジェクトでこのパッケージを使用したい場合はこちらの手順を用いる．

インストールは，下記のように[GitHubのリポジトリ名を指定する](https://pipenv-ja.readthedocs.io/ja/translate-ja/basics.html#a-note-about-vcs-dependencies)ことで行える．

```bash
pipenv install -e git+ssh://git@github.com/shiyunya/bplus-tree_python.git#egg=bplustree
```

インストール後は，その他一般的なパッケージと同様に使用できる．

```python
from bplustree.Bplustree import Bplustree
bt = Bpulstree()
```

## 注意
- 視覚的にわかりやすいように，デフォルトのファンアウト数（bplustree/constants.pyの`MAX`）は**8**になってる
    - ある程度大量のデータを扱うなら`MAX = 256`くらいにするとよさげ
    - パッケージから用いる場合は以下のようにする
    ```python
    from bplustree import constants
    constants.MAX = 256
    from bplustree.Bplustree import Bplustree
    bt = Bplustree()
    ```
- deleteはあるが，ノードのmergeは対応していないため，大量にdeleteがあるワークロードでは**バグる**
