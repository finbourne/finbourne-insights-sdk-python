# AccessEvaluationLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The timestamp of the access evaluation. | 
**application** | **str** | The name of the application that the request was made from. | 
**id** | **str** | The ID of the access evaluation. | 
**request_id** | **str** | The identifier of the request. | [optional] 
**session_id** | **str** | The identifier of the session that the request was made in. | [optional] 
**user** | **str** | The user who made the request. | 
**user_type** | **str** | The type of the user who made the request. | [optional] 
**duration** | **float** | The duration of the access evaluation. | 
**result** | **str** | The result of the access evaluation. | [optional] 
**authoritative_role_id** | **str** | The role that matched the access evaluation to provide a result. | [optional] 
**authoritative_policy_id** | **str** | The policy that matched the access evaluation to provide a result. | [optional] 
**authoritative_selector** | **str** | The selector that matched the access evaluation to provide a result. | [optional] 
**resource_type** | **str** | The type of the resource that the access evaluation is for. | [optional] 
**action** | **str** | The action key of the access evaluation. | [optional] 
**resource** | **dict(str, str)** | The ID of the resource that the access evaluation is for. If the ResourceID could not be converted to a dictionary, it will return a single-value dictionary with the key \&quot;resourceId\&quot;. | [optional] 
**resource_from_effective_date** | **str** | The From effective date of the resource. | [optional] 
**resource_to_effective_date** | **str** | The To effective date of the resource. | [optional] 
**resource_from_as_at** | **str** | The From AsAt date of the resource. | [optional] 
**resource_to_as_at** | **str** | The To AsAt date of the resource. | [optional] 
**access_execution_time** | **str** | The execution time of the entitlement. | [optional] 
**access_as_at_time** | **str** | The AsAt time of the entitlement. | [optional] 
**required_licence_policy_id** | **str** | ID of the required licence policy. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


