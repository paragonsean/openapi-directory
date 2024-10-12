# ConnectorApi.Api

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiReferenceUrl** | **String** | Link to the API reference of the API. | [optional] 
**categories** | **[String]** | List of categories the API belongs to. | [optional] 
**description** | **String** | Description of the API. | [optional] 
**events** | **[String]** | List of event types this API supports. | [optional] 
**id** | **String** | ID of the API. | [optional] [readonly] 
**name** | **String** | Name of the API. | [optional] 
**postmanCollectionId** | **String** | ID of the Postman collection of the API. | [optional] 
**resources** | [**[ApiResourcesInner]**](ApiResourcesInner.md) | List of resources supported in this API. | [optional] 
**specUrl** | **String** | Link to the latest OpenAPI specification of the API. | [optional] 
**status** | [**ApiStatus**](ApiStatus.md) |  | [optional] 
**type** | **String** | Indicates whether the API is a Unified API. If unified_api is false, the API is a Platform API. | [optional] 



## Enum: TypeEnum


* `platform` (value: `"platform"`)

* `unified` (value: `"unified"`)




