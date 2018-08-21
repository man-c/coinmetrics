# Coin Metrics API wrapper

Python wrapper around the [coinmetrics.io](https://coinmetrics.io/) API

### Installation
```
python3 setup.py install
```

### Usage

```
from coinmetrics import CoinMetrics
cm = CoinMetrics()
```
```
cm.get_supported_assets()
['ada', 'ae', 'aion', 'ant', 'bat', 'bch', 'bnb', 'btc', 'btg', 'btm', 'cennz', 'ctxc', 'cvc', 'dash', 'dcr', 'dgb', 'doge', 'drgn', 'elf', 'eng', 'eos', 'etc', 'eth', 'ethos', 'fun', 'gas', 'gno', 'gnt', 'icn', 'icx', 'kcs', 'knc', 'loom', 'lrc', 'lsk', 'ltc', 'maid', 'mana', 'mtl', 'nas', 'neo', 'omg', 'pay', 'pivx', 'poly', 'powr', 'ppt', 'qash', 'rep', 'rhoc', 'salt', 'snt', 'srn', 'trx', 'usdt', 'ven', 'veri', 'vtc', 'waves', 'wtc', 'xem', 'xlm', 'xmr', 'xrp', 'xvg', 'zec', 'zil', 'zrx']
```

```
cm.get_available_data_types_for_asset('btc')
['activeaddresses', 'adjustedtxvolume(usd)', 'averagedifficulty', 'blockcount', 'blocksize', 'exchangevolume(usd)', 'fees', 'generatedcoins', 'marketcap(usd)', 'medianfee', 'mediantxvalue(usd)', 'paymentcount', 'price(usd)', 'txcount', 'txvolume(usd)']
```

```
cm.get_asset_data_for_time_range('ltc', 'medianfee', 1514764800, 1515283200)
[[1514764800, 0.001], [1514851200, 0.0009925], [1514937600, 0.00099959], [1515024000, 0.00113039], [1515110400, 0.00100501], [1515196800, 0.00100705], [1515283200, 0.00022776]]
```

```
cm.get_all_data_types_for_assets('btc')
{'btc': {'activeaddresses': [[1534377600, 620660]], 'blocksize': [[1534377600, 120387676]], 'medianfee': [[1534377600, 2.201e-05]], 'blockcount': [[1534377600, 158]], 'generatedcoins': [[1534377600, 1975.0]], 'adjustedtxvolume(usd)': [[1534377600, 2206347611.0]], 'paymentcount': [[1534377600, 362609]], 'fees': [[1534377600, 24.04769454]], 'mediantxvalue(usd)': [[1534377600, 196.171762872]], 'marketcap(usd)': [[1534377600, 108335763931.0]], 'txcount': [[1534377600, 232177]], 'price(usd)': [[1534377600, 6294.23]], 'averagedifficulty': [[1534377600, 6389316883510.0]], 'exchangevolume(usd)': [[1534377600, 4328420000.0]], 'txvolume(usd)': [[1534377600, 3880903787.87]]}}
```

```
cm.get_all_data_types_for_all_assets()
```
