import unittest
import os

from finbourne_insights import api as ia
from fbnsdkutilities import ApiClientFactory
import finbourne_insights

class InsightsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        if os.getenv("FBN_ACCESS_TOKEN", None) is not None:
            cls.api_factory = ApiClientFactory(finbourne_insights, token=os.environ.get("FBN_ACCESS_TOKEN"))
        else:
            cls.api_factory = ApiClientFactory(finbourne_insights, api_secrets_filename="secrets.json")

        # api_client = ApiClientFactory(finbourne_insights, api_secrets_filename="secrets.json")
        cls.requests_api = cls.api_factory.build(ia.RequestsApi)

    def test_requests(self):
        response = self.requests_api.list_request_logs()
        self.assertGreater(len(response.values), 0)


if __name__ == '__main__':
    unittest.main()
