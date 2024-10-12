

# EventSourceResource

An environment receives data from one or more event sources. Each event source has associated connection info that allows the Time Series Insights ingress pipeline to connect to and pull data from the event source

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
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



