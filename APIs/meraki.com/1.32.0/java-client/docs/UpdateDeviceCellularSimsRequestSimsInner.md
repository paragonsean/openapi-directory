

# UpdateDeviceCellularSimsRequestSimsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apns** | [**List&lt;UpdateDeviceCellularSimsRequestSimsInnerApnsInner&gt;**](UpdateDeviceCellularSimsRequestSimsInnerApnsInner.md) | APN configurations. If empty, the default APN will be used. |  [optional] |
|**isPrimary** | **Boolean** | If true, this SIM is used for boot. Must be true on single-sim devices. |  [optional] |
|**slot** | [**SlotEnum**](#SlotEnum) | SIM slot being configured. Must be &#39;sim1&#39; on single-sim devices. |  [optional] |



## Enum: SlotEnum

| Name | Value |
|---- | -----|
| SIM1 | &quot;sim1&quot; |
| SIM2 | &quot;sim2&quot; |



