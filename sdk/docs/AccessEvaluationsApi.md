# finbourne_insights.AccessEvaluationsApi

All URIs are relative to *https://www.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_evaluation_log**](AccessEvaluationsApi.md#get_access_evaluation_log) | **GET** /api/access/{id} | [EXPERIMENTAL] Get the log for a specific access evaluation.
[**list_access_evaluation_logs**](AccessEvaluationsApi.md#list_access_evaluation_logs) | **GET** /api/access | [EXPERIMENTAL] List the logs for access evaluations.


# **get_access_evaluation_log**
> AccessEvaluationLog get_access_evaluation_log(id)

[EXPERIMENTAL] Get the log for a specific access evaluation.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from pprint import pprint
configuration = finbourne_insights.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://www.lusid.com/insights
configuration.host = "https://www.lusid.com/insights"
# Create an instance of the API class
api_instance = finbourne_insights.AccessEvaluationsApi(finbourne_insights.ApiClient(configuration))
id = 'id_example' # str | The identifier of the access evaluation to obtain the log for.

try:
    # [EXPERIMENTAL] Get the log for a specific access evaluation.
    api_response = api_instance.get_access_evaluation_log(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessEvaluationsApi->get_access_evaluation_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the access evaluation to obtain the log for. | 

### Return type

[**AccessEvaluationLog**](AccessEvaluationLog.md)

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

# **list_access_evaluation_logs**
> ResourceListWithHistogramOfAccessEvaluationLog list_access_evaluation_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)

[EXPERIMENTAL] List the logs for access evaluations.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from pprint import pprint
configuration = finbourne_insights.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://www.lusid.com/insights
configuration.host = "https://www.lusid.com/insights"
# Create an instance of the API class
api_instance = finbourne_insights.AccessEvaluationsApi(finbourne_insights.ApiClient(configuration))
filter = 'filter_example' # str | Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</see>. (optional)
sort_by = 'sort_by_example' # str | Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
limit = 56 # int | When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. (optional)
page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. (optional)
histogram_interval = 'histogram_interval_example' # str | The interval for an included histogram of the logs (optional)

try:
    # [EXPERIMENTAL] List the logs for access evaluations.
    api_response = api_instance.list_access_evaluation_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessEvaluationsApi->list_access_evaluation_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. Read more about &lt;see href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID&lt;/see&gt;. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. | [optional] 
 **histogram_interval** | **str**| The interval for an included histogram of the logs | [optional] 

### Return type

[**ResourceListWithHistogramOfAccessEvaluationLog**](ResourceListWithHistogramOfAccessEvaluationLog.md)

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

