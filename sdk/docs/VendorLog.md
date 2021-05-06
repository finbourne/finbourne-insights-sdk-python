# VendorLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of a log entry. | 
**provider** | **str** | The provider or service name. | 
**timestamp** | **datetime** | Timestamp of when the log was generated. | 
**type** | **str** | Type of log. Possible values: HttpResponse. | 
**destination_url** | **str** | The destination URL of the task. | 
**operation** | **str** | The operation performed. Possible values: Evaluate. | 
**outcome** | **str** | The outcome of the operation. Possible values: Success, Failure. | 
**duration** | **float** | The duration of the operation in ms. | 
**http_status_code** | **int** | The status code of the operation. | 
**user_id** | **str** | The user that made the request to LUSID. | 
**request_id** | **str** | The ID of the request to LUSID. | 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


