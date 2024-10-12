

# LoggerUpdateRequestProperties

Parameters supplied to the Update Logger operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credentials** | **Map&lt;String, String&gt;** | Logger credentials. |  [optional] |
|**description** | **String** | Logger description. |  [optional] |
|**isBuffered** | **Boolean** | Whether records are buffered in the logger before publishing. Default is assumed to be true. |  [optional] |
|**loggerType** | [**LoggerTypeEnum**](#LoggerTypeEnum) | Logger type. |  [optional] |



## Enum: LoggerTypeEnum

| Name | Value |
|---- | -----|
| AZURE_EVENT_HUB | &quot;azureEventHub&quot; |
| APPLICATION_INSIGHTS | &quot;applicationInsights&quot; |



