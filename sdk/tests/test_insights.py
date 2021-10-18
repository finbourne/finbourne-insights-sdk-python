import unittest
from finbourne_insights import api as ia
from fbnsdkutilities import ApiClientFactory
import finbourne_insights

class InsightsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        api_client = ApiClientFactory(finbourne_insights, api_secrets_filename="secrets.json")
        cls.requests_api = api_client.build(ia.RequestsApi)

    def test_requests(self):
        response = self.requests_api.list_request_logs()
        self.assertGreater(len(response.values), 0)


if __name__ == '__main__':
    unittest.main()
