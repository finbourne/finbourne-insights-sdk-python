# finbourne_insights.AuditingApi

All URIs are relative to *https://www.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entry**](AuditingApi.md#create_entry) | **POST** /api/auditing/entries | [EXPERIMENTAL] Create (persist) and audit entry..
[**get_processes**](AuditingApi.md#get_processes) | **GET** /api/auditing/processes | [EXPERIMENTAL] Get the latest audit entry for each process.
[**list_entries**](AuditingApi.md#list_entries) | **GET** /api/auditing/entries | [EXPERIMENTAL] Get the audit entries.


# **create_entry**
> AuditEntry create_entry(create_audit_entry=create_audit_entry)

[EXPERIMENTAL] Create (persist) and audit entry..

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
api_instance = finbourne_insights.AuditingApi(finbourne_insights.ApiClient(configuration))
create_audit_entry = {"process":{"name":"processName","runId":"processRunId","startTime":"0001-01-01T00:00:00.0000000+00:00"},"data":{"action":"dataAction","category":"dataCategory","userId":"dataUserId","message":"dataMessage","resource":{"type":"resourceType","identifier":"resourceIdentifier"},"detailsType":"dataDetailsType"}} # CreateAuditEntry | Information about the entry to be created. (optional)

try:
    # [EXPERIMENTAL] Create (persist) and audit entry..
    api_response = api_instance.create_entry(create_audit_entry=create_audit_entry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditingApi->create_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_audit_entry** | [**CreateAuditEntry**](CreateAuditEntry.md)| Information about the entry to be created. | [optional] 

### Return type

[**AuditEntry**](AuditEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**429** | There have been too many recent requests, retry later (using the RETRY-AFTER header value as the delay). |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_processes**
> ResourceListOfAuditProcessSummary get_processes()

[EXPERIMENTAL] Get the latest audit entry for each process.

This will never be {null}, though it may be empty.

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
api_instance = finbourne_insights.AuditingApi(finbourne_insights.ApiClient(configuration))

try:
    # [EXPERIMENTAL] Get the latest audit entry for each process.
    api_response = api_instance.get_processes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditingApi->get_processes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfAuditProcessSummary**](ResourceListOfAuditProcessSummary.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entries**
> ScrollableCollectionOfAuditEntry list_entries(filter=filter, sort_by=sort_by, size=size, state=state)

[EXPERIMENTAL] Get the audit entries.

This will never be {null}, though it may be empty.

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
api_instance = finbourne_insights.AuditingApi(finbourne_insights.ApiClient(configuration))
filter = 'filter_example' # str | The filter to be applied to the results. (optional)
sort_by = 'sort_by_example' # str | The order to return the entries in. (optional)
size = 1000 # int | The maximum number of entries to return. (optional) (default to 1000)
state = 'state_example' # str | The scrolling state, used to iterate through the data set. (optional)

try:
    # [EXPERIMENTAL] Get the audit entries.
    api_response = api_instance.list_entries(filter=filter, sort_by=sort_by, size=size, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditingApi->list_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be applied to the results. | [optional] 
 **sort_by** | **str**| The order to return the entries in. | [optional] 
 **size** | **int**| The maximum number of entries to return. | [optional] [default to 1000]
 **state** | **str**| The scrolling state, used to iterate through the data set. | [optional] 

### Return type

[**ScrollableCollectionOfAuditEntry**](ScrollableCollectionOfAuditEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

