import pytest
import responses
import unittest
import unittest.mock as mock

from coinmetrics import CoinMetricsAPI
from requests.exceptions import HTTPError

class TestWrapper(unittest.TestCase):

    @responses.activate
    def test_failed_get_supported_assets(self):
        # Arrange
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_supported_assets',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinMetricsAPI().get_supported_assets()

    @responses.activate
    def test_get_supported_assets(self):
        # Arrange
        json_reponse = [ "ada",  "ae",  "aion",  "ant",  "bat",  "bch" ]
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_supported_assets',
                          json = json_reponse, status = 200)

        # Act
        response = CoinMetricsAPI().get_supported_assets()

        ## Assert
        assert response == json_reponse

    @responses.activate
    def test_failed_get_available_data_types_for_asset(self):
        # Arrange
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_available_data_types_for_asset/btc',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinMetricsAPI().get_available_data_types_for_asset('btc')

    @responses.activate
    def test_get_available_data_types_for_asset(self):
        # Arrange
        json_reponse = {"result":["activeaddresses","adjustedtxvolume(usd)","averagedifficulty","blockcount","blocksize","exchangevolume(usd)","fees","generatedcoins","marketcap(usd)","medianfee","mediantxvalue(usd)","paymentcount","price(usd)","txcount","txvolume(usd)"]}
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_available_data_types_for_asset/btc',
                          json = json_reponse, status = 200)

        # Act
        response = CoinMetricsAPI().get_available_data_types_for_asset('btc')

        ## Assert
        expected_response = ["activeaddresses","adjustedtxvolume(usd)","averagedifficulty","blockcount","blocksize","exchangevolume(usd)","fees","generatedcoins","marketcap(usd)","medianfee","mediantxvalue(usd)","paymentcount","price(usd)","txcount","txvolume(usd)"]
        assert response == expected_response

    @responses.activate
    def test_failed_get_asset_data_for_time_range(self):
        # Arrange
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_asset_data_for_time_range/ltc/medianfee/1514764800/1515283200',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinMetricsAPI().get_asset_data_for_time_range('ltc', 'medianfee', 1514764800, 1515283200)

    @responses.activate
    def test_get_asset_data_for_time_range(self):
        # Arrange
        json_reponse = {"result":[[1514764800,0.001],[1514851200,0.0009925],[1514937600,0.00099959],[1515024000,0.00113039],[1515110400,0.00100501],[1515196800,0.00100705],[1515283200,0.00022776]]}
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_asset_data_for_time_range/ltc/medianfee/1514764800/1515283200',
                          json = json_reponse, status = 200)

        # Act
        response = CoinMetricsAPI().get_asset_data_for_time_range('ltc', 'medianfee', 1514764800, 1515283200)

        ## Assert
        expected_response = [[1514764800,0.001],[1514851200,0.0009925],[1514937600,0.00099959],[1515024000,0.00113039],[1515110400,0.00100501],[1515196800,0.00100705],[1515283200,0.00022776]]
        assert response == expected_response

    @responses.activate
    def test_failed_get_all_data_types_for_assets(self):
        # Arrange
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_available_data_types_for_asset/btc',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinMetricsAPI().get_all_data_types_for_assets(['btc'],1535576400, 1535662740)

    @responses.activate
    def test_get_all_data_types_for_assets(self):
        # Arrange
        json_reponse = {"result":["activeaddresses"]}
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_available_data_types_for_asset/btc',
                          json = json_reponse, status = 200)

        json_reponse = {"result":[[1535587200,621242]]}
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_asset_data_for_time_range/btc/activeaddresses/1535576400/1535662740',
                          json = json_reponse, status = 200)

        # Act
        response = CoinMetricsAPI().get_all_data_types_for_assets(['btc'],1535576400, 1535662740)

        ## Assert
        expected_response = {'btc': {'activeaddresses': [[1535587200, 621242]]}}
        assert response == expected_response

    @responses.activate
    def test_failed_get_all_data_types_for_all_assets(self):
        # Arrange
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_supported_assets',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinMetricsAPI().get_all_data_types_for_all_assets(1535576400, 1535662740)

    @responses.activate
    def test_get_all_data_types_for_all_assets(self):
        # Arrange
        json_reponse = [ "btc" ]
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_supported_assets',
                          json = json_reponse, status = 200)

        json_reponse = {"result":["activeaddresses"]}
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_available_data_types_for_asset/btc',
                          json = json_reponse, status = 200)

        json_reponse = {"result":[[1535587200,621242]]}
        responses.add(responses.GET, 'https://coinmetrics.io/api/v1/get_asset_data_for_time_range/btc/activeaddresses/1535576400/1535662740',
                          json = json_reponse, status = 200)

        # Act
        response = CoinMetricsAPI().get_all_data_types_for_all_assets(1535576400, 1535662740)

        ## Assert
        expected_response = {'btc': {'activeaddresses': [[1535587200, 621242]]}}
        assert response == expected_response
