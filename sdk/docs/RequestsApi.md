# finbourne_insights.RequestsApi

All URIs are relative to *https://fbn-ci.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_request**](RequestsApi.md#get_request) | **GET** /api/requests/{id}/request | [EXPERIMENTAL] GetRequest: Get the request content for a specific API request.
[**get_request_log**](RequestsApi.md#get_request_log) | **GET** /api/requests/{id} | [EXPERIMENTAL] GetRequestLog: Get the log for a specific API request.
[**get_response**](RequestsApi.md#get_response) | **GET** /api/requests/{id}/response | [EXPERIMENTAL] GetResponse: Get the response for a specific API request.
[**list_request_logs**](RequestsApi.md#list_request_logs) | **GET** /api/requests | [EXPERIMENTAL] ListRequestLogs: Get the logs for API requests.


# **get_request**
> Request get_request(id)

[EXPERIMENTAL] GetRequest: Get the request content for a specific API request.

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
    api_instance = finbourne_insights.RequestsApi(api_client)
    id = 'id_example' # str | The identifier of the request to obtain the content for.

    try:
        # [EXPERIMENTAL] GetRequest: Get the request content for a specific API request.
        api_response = api_instance.get_request(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RequestsApi->get_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the content for. | 

### Return type

[**Request**](Request.md)

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

# **get_request_log**
> RequestLog get_request_log(id)

[EXPERIMENTAL] GetRequestLog: Get the log for a specific API request.

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
    api_instance = finbourne_insights.RequestsApi(api_client)
    id = 'id_example' # str | The identifier of the request to obtain the log for.

    try:
        # [EXPERIMENTAL] GetRequestLog: Get the log for a specific API request.
        api_response = api_instance.get_request_log(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RequestsApi->get_request_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the log for. | 

### Return type

[**RequestLog**](RequestLog.md)

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

# **get_response**
> Response get_response(id)

[EXPERIMENTAL] GetResponse: Get the response for a specific API request.

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
    api_instance = finbourne_insights.RequestsApi(api_client)
    id = 'id_example' # str | The identifier of the request to obtain the response for.

    try:
        # [EXPERIMENTAL] GetResponse: Get the response for a specific API request.
        api_response = api_instance.get_response(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RequestsApi->get_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the response for. | 

### Return type

[**Response**](Response.md)

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

# **list_request_logs**
> ResourceListWithHistogramOfRequestLog list_request_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)

[EXPERIMENTAL] ListRequestLogs: Get the logs for API requests.

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
    api_instance = finbourne_insights.RequestsApi(api_client)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</see>. (optional)
sort_by = 'sort_by_example' # str | Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
limit = 56 # int | When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. (optional)
page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. (optional)
histogram_interval = 'histogram_interval_example' # str | Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated. (optional)

    try:
        # [EXPERIMENTAL] ListRequestLogs: Get the logs for API requests.
        api_response = api_instance.list_request_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RequestsApi->list_request_logs: %s\n" % e)
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

[**ResourceListWithHistogramOfRequestLog**](ResourceListWithHistogramOfRequestLog.md)

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

