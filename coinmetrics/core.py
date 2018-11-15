import json
import requests
import datetime

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class CoinMetricsAPI:

    __API_URL_BASE = 'https://coinmetrics.io/api/v1/'

    def __init__(self, api_base_url = __API_URL_BASE):
        self.api_base_url = api_base_url
        self.request_timeout = 120

        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[ 502, 503, 504 ])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))


    def __request(self, url):
        try:
            response = self.session.get(url, timeout = self.request_timeout)
            response.raise_for_status()
            #if response.status_code == 200:
            content = json.loads(response.content.decode('utf-8'))
            if 'error' in content:
                raise ValueError(content['error'])
            else:
                return content
        except Exception as e:
            raise


    def __check_timestamp(self, begin_timestamp, end_timestamp):
        # if both timestamps empty (None) set yesterdays date
        if not (begin_timestamp or end_timestamp):
            yesterday = datetime.datetime.today() - datetime.timedelta(1)
            begin_timestamp = int(datetime.datetime(yesterday.year, yesterday.month, yesterday.day).timestamp())
            end_timestamp = int(datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 23, 59).timestamp())
        elif begin_timestamp and not end_timestamp: # if one only timestamp (begin), set it also as end timestamp
            end_timestamp = begin_timestamp
        return begin_timestamp, end_timestamp


    def get_supported_assets(self):
        api_url = '{0}get_supported_assets'.format(self.api_base_url)
        return self.__request(api_url)


    def get_available_data_types_for_asset(self, asset):
        api_url = '{0}get_available_data_types_for_asset/{1}'.format(self.api_base_url, asset)
        return self.__request(api_url)['result']


    def get_asset_data_for_time_range(self, asset,  data_type,  begin_timestamp = None,  end_timestamp = None):
        # if no timestamp return yesterday
        begin_timestamp, end_timestamp = self.__check_timestamp(begin_timestamp, end_timestamp) 
        
        api_url = '{0}get_asset_data_for_time_range/{1}/{2}/{3}/{4}'.format(self.api_base_url, asset, data_type, begin_timestamp,  end_timestamp)
        
        return self.__request(api_url)['result']


    def get_all_data_types_for_assets(self, assets, begin_timestamp = None,  end_timestamp = None):
        
        if not isinstance(assets, list):
            assets = [assets]

        response = {}
        for asset in assets:
            begin_timestamp, end_timestamp = self.__check_timestamp(begin_timestamp, end_timestamp) 

            data_types = self.get_available_data_types_for_asset(asset)
            r = {}
            for d in data_types:
                r[d] = self.get_asset_data_for_time_range(asset, d, begin_timestamp,  end_timestamp)
            response[asset] = r
        return response


    def get_all_data_types_for_all_assets(self, begin_timestamp = None,  end_timestamp = None):
        # check if any timestamps
        begin_timestamp, end_timestamp = self.__check_timestamp(begin_timestamp, end_timestamp) 
        # get all available assets
        assets = self.get_supported_assets()
        
        response = self.get_all_data_types_for_assets(assets, begin_timestamp,  end_timestamp)

        return response
