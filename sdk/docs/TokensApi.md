# finbourne_insights.TokensApi

All URIs are relative to *https://fbn-ci.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invalidate_token**](TokensApi.md#invalidate_token) | **DELETE** /api/tokens | [EXPERIMENTAL] InvalidateToken: Invalidate current JWT token (sign out)


# **invalidate_token**
> invalidate_token()

[EXPERIMENTAL] InvalidateToken: Invalidate current JWT token (sign out)

Log the current user out of all Finbourne platforms by invalidating the current token

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_insights.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_insights.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_insights.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_insights.TokensApi(api_client)
    
    try:
        # [EXPERIMENTAL] InvalidateToken: Invalidate current JWT token (sign out)
        api_instance.invalidate_token()
    except ApiException as e:
        print("Exception when calling TokensApi->invalidate_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

