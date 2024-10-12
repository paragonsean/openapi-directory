

# DiagnosticLoggerListByService200ResponseValueInnerProperties

The Logger entity in API Management represents an event sink that you can use to log API Management events. Currently the Logger entity supports logging API Management events to Azure Event Hubs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credentials** | **Map&lt;String, String&gt;** | The name and SendRule connection string of the event hub for azureEventHub logger. Instrumentation key for applicationInsights logger. |  |
|**description** | **String** | Logger description. |  [optional] |
|**isBuffered** | **Boolean** | Whether records are buffered in the logger before publishing. Default is assumed to be true. |  [optional] |
|**loggerType** | [**LoggerTypeEnum**](#LoggerTypeEnum) | Logger type. |  |
|**sampling** | [**DiagnosticLoggerListByService200ResponseValueInnerPropertiesSampling**](DiagnosticLoggerListByService200ResponseValueInnerPropertiesSampling.md) |  |  [optional] |



## Enum: LoggerTypeEnum

| Name | Value |
|---- | -----|
| AZURE_EVENT_HUB | &quot;azureEventHub&quot; |
| APPLICATION_INSIGHTS | &quot;applicationInsights&quot; |



