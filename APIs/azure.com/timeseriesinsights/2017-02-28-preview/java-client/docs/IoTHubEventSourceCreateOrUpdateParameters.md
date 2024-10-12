

# IoTHubEventSourceCreateOrUpdateParameters

Parameters supplied to the Create or Update Event Source operation for an IoTHub event source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**IoTHubEventSourceCreationProperties**](IoTHubEventSourceCreationProperties.md) |  |  |
|**kind** | [**KindEnum**](#KindEnum) | The kind of the event source. |  |
|**location** | **String** | The location of the resource. |  |
|**tags** | **Map&lt;String, String&gt;** | Key-value pairs of additional properties for the resource. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| EVENT_HUB | &quot;Microsoft.EventHub&quot; |
| IO_T_HUB | &quot;Microsoft.IoTHub&quot; |



