

# EventHubEventSourceResource

An event source that receives its data from an Azure EventHub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**EventHubEventSourceResourceProperties**](EventHubEventSourceResourceProperties.md) |  |  |
|**kind** | [**KindEnum**](#KindEnum) | The kind of the event source. |  |
|**location** | **String** | Resource location |  |
|**tags** | **Map&lt;String, String&gt;** | Resource tags |  [optional] |
|**id** | **String** | Resource Id |  [optional] [readonly] |
|**name** | **String** | Resource name |  [optional] [readonly] |
|**type** | **String** | Resource type |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| EVENT_HUB | &quot;Microsoft.EventHub&quot; |
| IO_T_HUB | &quot;Microsoft.IoTHub&quot; |



