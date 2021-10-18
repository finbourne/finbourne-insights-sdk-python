# Response

DTO of Finbourne.AspNetCore.Http.TrackingEntry.ResponseInformation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **dict(str, list[str])** | The headers | [optional] 
**content_length** | **int** | The actual length of the body, which may be larger than the data recorded in Finbourne.Insights.WebApi.Dtos.Response.Body  (e.g. if actual Body is large, or not convertible to a string) | [optional] 
**content_type** | **str** | The content type | [optional] 
**body** | **str** | The recorded content. | [optional] 
**body_was_truncated** | **bool** | Determines if the recorded body was truncated. | [optional] 
**status_code** | **int** | Http Status Code of the request. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


