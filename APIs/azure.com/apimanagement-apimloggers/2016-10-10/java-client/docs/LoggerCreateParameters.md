

# LoggerCreateParameters

Parameters supplied to the Create Logger operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credentials** | **Map&lt;String, String&gt;** | The name and SendRule connection string of the event hub. |  |
|**description** | **String** | Logger description. |  [optional] |
|**isBuffered** | **Boolean** | Whether records are buffered in the logger before publishing. Default is assumed to be true. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Logger type. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AZURE_EVENT_HUB | &quot;AzureEventHub&quot; |



