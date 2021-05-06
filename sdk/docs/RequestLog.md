# RequestLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The timestamp of the request. | 
**application** | **str** | The name of the application that the request was made to. | 
**id** | **str** | The identifier of the request. | 
**session_id** | **str** | The identifier of the session that the request was made in. | [optional] 
**verb** | **str** | The HTTP verb of the request. | 
**url** | **str** | The URL of the request. | 
**domain** | **str** | The domain of the request. | [optional] 
**user** | **str** | The user who made the request. | 
**user_type** | **str** | The type of the user who made the request. | [optional] 
**operation** | **str** | The API operation invoked by the request. | [optional] 
**outcome** | **str** | The outcome of the request: Success, Failure or Error. | 
**duration** | **float** | The duration of the request in milliseconds. | 
**http_status_code** | **int** | The status code of the request. | 
**error_code** | **str** | Error code, if the request had a failure or error. | [optional] 
**sdk_language** | **str** | The language of the SDK used. | [optional] 
**sdk_version** | **str** | The version of the SDK used. | [optional] 
**source_application** | **str** | The name of the application that made the request. | [optional] 
**correlation_id** | **list[str]** | The chain of requestIds preceding this request | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


