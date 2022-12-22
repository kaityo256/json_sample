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
