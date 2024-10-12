# CloudSearchApi.IndexItemRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectorName** | **String** | The name of connector making this call. Format: datasources/{source_id}/connectors/{ID} | [optional] 
**debugOptions** | [**DebugOptions**](DebugOptions.md) |  | [optional] 
**indexItemOptions** | [**IndexItemOptions**](IndexItemOptions.md) |  | [optional] 
**item** | [**Item**](Item.md) |  | [optional] 
**mode** | **String** | Required. The RequestMode for this request. | [optional] 



## Enum: ModeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `SYNCHRONOUS` (value: `"SYNCHRONOUS"`)

* `ASYNCHRONOUS` (value: `"ASYNCHRONOUS"`)




