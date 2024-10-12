

# IndexItemRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectorName** | **String** | The name of connector making this call. Format: datasources/{source_id}/connectors/{ID} |  [optional] |
|**debugOptions** | [**DebugOptions**](DebugOptions.md) |  |  [optional] |
|**indexItemOptions** | [**IndexItemOptions**](IndexItemOptions.md) |  |  [optional] |
|**item** | [**Item**](Item.md) |  |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Required. The RequestMode for this request. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| SYNCHRONOUS | &quot;SYNCHRONOUS&quot; |
| ASYNCHRONOUS | &quot;ASYNCHRONOUS&quot; |



