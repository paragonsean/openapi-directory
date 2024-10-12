

# LoggerResponse

The Logger entity in API Management represents an event sink that you can use to log API Management events. Currently the Logger entity supports logging API Management events to Azure Event Hubs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credentials** | **Map&lt;String, String&gt;** | The name and SendRule connection string of the event hub. |  |
|**description** | **String** | Logger description. |  [optional] |
|**id** | **String** | Uniquely identifies the logger within the current API Management service instance. The value is a valid relative URL in the format of /loggers/{loggerId} where {loggerId} is a logger identifier. |  [optional] [readonly] |
|**isBuffered** | **Boolean** | Whether records are buffered in the logger before publishing. Default is assumed to be true. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Logger type. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AZURE_EVENT_HUB | &quot;AzureEventHub&quot; |



