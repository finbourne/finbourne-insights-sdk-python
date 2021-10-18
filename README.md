![LUSID_by_Finbourne](https://content.finbourne.com/LUSID_repo.png)

# FINBOURNE Insights Python SDK

## Installation

The PyPi package for the Insights SDK can installed using the following:

```
$ pip install finbourne-insights-sdk finbourne-sdk-utilities
```

## Usage

```
from finbourne_insights import api as ia
from fbnsdkutilities import ApiClientFactory
import finbourne_insights

api_client = ApiClientFactory(finbourne_insights, api_secrets_filename="secrets.json")
requests_api = api_client.build(ia.RequestsApi)
response = self.requests_api.list_request_logs()
print(response.values)
```
