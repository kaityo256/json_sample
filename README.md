# JSONの読み書きサンプル

## 概要

PythonからJSONファイルを読み込むサンプルです。

## JSONとは

JSON (JavaScript Object Notation)はデータをテキスト形式で管理するフォーマットの一つです。例えばVSCodeの設定ファイルがJSON形式です。様々な情報を表現できますが、ここでは連想配列のみを扱います。

JSONは、全体を中括弧で囲み、その中に「名前: 値」という形で情報を並べます。

```json
{
    "network_type": "all",
    "system_size_x": 10,
    "system_size_y": 12,
    "number_of_trials": 100,
    "number_of_generations": 200,
    "seed": 1
}
```

名前は文字列なのでダブルクォーテーションマークで囲みます。値は文字列でも整数でも浮動小数でもなんでもOKです。複数並べる場合はカンマで区切ります。情報はネストできますが、ここでは扱いません。ファイルの拡張子は`.json`です。

## JSONファイルの読み込み

以下の内容のファイルが`params.json`という名前で用意されています。

```json
{
    "network_type": "all",
    "system_size_x": 10,
    "system_size_y": 12,
    "number_of_trials": 100,
    "number_of_generations": 200,
    "seed": 1
}
```

これをPythonから読み込むには、`json`を`import`して、`json.load`にファイル名を渡すだけでOKです。

```py
import json
with open('params.json') as f:
    params = json.load(f)
```

これにより、`params`が辞書となります。例えば`seed`の情報が欲しければ`params['seed']`とすればOKです。

```py
print(params['seed']) # => 1
```

ですが、いちいち角括弧とシングルクォーテーションで囲むのは面倒です。そこで、以下の拡張辞書型を定義しておきます。

```py
class Mydict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self
```

そして、先程の辞書を上記のクラスで囲みます。

```py
with open('params.json') as f:
    params = Mydict(json.load(f))
```

すると、`params.seed`で値にアクセスできるようになります。他の情報も同様です。

```py
# データの読み込み
print(f"network_type = {params.network_type}") # => all
print(f"system_size_x = {params.system_size_x}") # => 10
print(f"system_size_y = {params.system_size_y}") # => 12
print(f"number_of_trials = {params.number_of_trials}") # => 100
print(f"number_of_generations = {params.number_of_generations}") # => 200
print(f"seed = {params.seed}") # => 1
```

あとは関数に渡すなりファイルに保存するなり好き勝手できます。

最終的に、JSONファイルを読み込むスクリプトは以下のようになります。

```py
import json


# 辞書の中身にドットでアクセスできるようにする
class Mydict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self


# JSONファイルを開く
with open('params.json') as f:
    params = Mydict(json.load(f))

# データの読み込み
print(f"network_type = {params.network_type}")
print(f"system_size_x = {params.system_size_x}")
print(f"system_size_y = {params.system_size_y}")
print(f"number_of_trials = {params.number_of_trials}")
print(f"number_of_generations = {params.number_of_generations}")
print(f"seed = {params.seed}")
```

## LICENSE

MIT
