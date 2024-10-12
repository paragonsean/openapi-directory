

# LoggerUpdateParameters

Parameters supplied to the Update Logger operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credentials** | **Map&lt;String, String&gt;** | Logger credentials. |  [optional] |
|**description** | **String** | Logger description. |  [optional] |
|**isBuffered** | **Boolean** | whether records are buffered in the logger before publishing. Default is assumed to be true. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Logger type. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AZURE_EVENT_HUB | &quot;AzureEventHub&quot; |



