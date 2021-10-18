# finbourne_insights.VendorLogsApi

All URIs are relative to *https://fbn-ci.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vendor_log**](VendorLogsApi.md#get_vendor_log) | **GET** /api/vendor/{id} | [EXPERIMENTAL] GetVendorLog: Get the log for a specific vendor request.
[**get_vendor_request**](VendorLogsApi.md#get_vendor_request) | **GET** /api/vendor/{id}/request | [EXPERIMENTAL] GetVendorRequest: Get the request body for a vendor request.
[**get_vendor_response**](VendorLogsApi.md#get_vendor_response) | **GET** /api/vendor/{id}/response | [EXPERIMENTAL] GetVendorResponse: Get the response from a vendor request.
[**list_vendor_logs**](VendorLogsApi.md#list_vendor_logs) | **GET** /api/vendor | [EXPERIMENTAL] ListVendorLogs: List the logs for vendor requests.


# **get_vendor_log**
> VendorLog get_vendor_log(id)

[EXPERIMENTAL] GetVendorLog: Get the log for a specific vendor request.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/insights
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_insights.Configuration(
    host = "https://fbn-ci.lusid.com/insights"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_insights.Configuration(
    host = "https://fbn-ci.lusid.com/insights"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_insights.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_insights.VendorLogsApi(api_client)
    id = 'id_example' # str | The identifier of the request to obtain the log for.

    try:
        # [EXPERIMENTAL] GetVendorLog: Get the log for a specific vendor request.
        api_response = api_instance.get_vendor_log(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorLogsApi->get_vendor_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the log for. | 

### Return type

[**VendorLog**](VendorLog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_request**
> VendorRequest get_vendor_request(id)

[EXPERIMENTAL] GetVendorRequest: Get the request body for a vendor request.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/insights
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_insights.Configuration(
    host = "https://fbn-ci.lusid.com/insights"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_insights.Configuration(
    host = "https://fbn-ci.lusid.com/insights"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_insights.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_insights.VendorLogsApi(api_client)
    id = 'id_example' # str | The identifier of the request to obtain the content for.

    try:
        # [EXPERIMENTAL] GetVendorRequest: Get the request body for a vendor request.
        api_response = api_instance.get_vendor_request(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorLogsApi->get_vendor_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the content for. | 

### Return type

[**VendorRequest**](VendorRequest.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_response**
> VendorResponse get_vendor_response(id)

[EXPERIMENTAL] GetVendorResponse: Get the response from a vendor request.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/insights
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_insights.Configuration(
    host = "https://fbn-ci.lusid.com/insights"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_insights.Configuration(
    host = "https://fbn-ci.lusid.com/insights"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_insights.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_insights.VendorLogsApi(api_client)
    id = 'id_example' # str | The identifier of the request to obtain the response for.

    try:
        # [EXPERIMENTAL] GetVendorResponse: Get the response from a vendor request.
        api_response = api_instance.get_vendor_response(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorLogsApi->get_vendor_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the response for. | 

### Return type

[**VendorResponse**](VendorResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vendor_logs**
> ResourceListWithHistogramOfVendorLog list_vendor_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)

[EXPERIMENTAL] ListVendorLogs: List the logs for vendor requests.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/insights
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_insights.Configuration(
    host = "https://fbn-ci.lusid.com/insights"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_insights.Configuration(
    host = "https://fbn-ci.lusid.com/insights"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_insights.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_insights.VendorLogsApi(api_client)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</see>. (optional)
sort_by = 'sort_by_example' # str | Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
limit = 56 # int | When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. (optional)
page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. (optional)
histogram_interval = 'histogram_interval_example' # str | Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated. (optional)

    try:
        # [EXPERIMENTAL] ListVendorLogs: List the logs for vendor requests.
        api_response = api_instance.list_vendor_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorLogsApi->list_vendor_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. Read more about &lt;see href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID&lt;/see&gt;. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. | [optional] 
 **histogram_interval** | **str**| Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated. | [optional] 

### Return type

[**ResourceListWithHistogramOfVendorLog**](ResourceListWithHistogramOfVendorLog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

