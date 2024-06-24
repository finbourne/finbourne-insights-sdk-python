![LUSID_by_Finbourne](./resources/Finbourne_Logo_Teal.svg)

# Deprecated

Please note that this repository is deprecated and will be archived early 2024.

All functionality is now contained, in the [finbourne-insights-sdk-python](https://github.com/finbourne/finbourne-insights-sdk-python) repository on the `main` branch.

# FINBOURNE Insights Python SDK

![PyPI](https://img.shields.io/pypi/v/finbourne-insights-sdk-preview?color=blue)

## Installation

The PyPi package for the Insights SDK can installed using the following:

```
$ pip install finbourne-insights-sdk-preview finbourne-sdk-utilities
```

## Usage

```
from finbourne_insights import api as ia
from fbnsdkutilities import ApiClientFactory
import finbourne_insights

api_client = ApiClientFactory(finbourne_insights, api_secrets_filename="secrets.json")
requests_api = api_client.build(ia.RequestsApi)
response = requests_api.list_request_logs()
print(response.values)
```
