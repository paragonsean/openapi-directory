# MerakiDashboardApi.UpdateDeviceCellularSimsRequestSimsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apns** | [**[UpdateDeviceCellularSimsRequestSimsInnerApnsInner]**](UpdateDeviceCellularSimsRequestSimsInnerApnsInner.md) | APN configurations. If empty, the default APN will be used. | [optional] 
**isPrimary** | **Boolean** | If true, this SIM is used for boot. Must be true on single-sim devices. | [optional] [default to false]
**slot** | **String** | SIM slot being configured. Must be &#39;sim1&#39; on single-sim devices. | [optional] 



## Enum: SlotEnum


* `sim1` (value: `"sim1"`)

* `sim2` (value: `"sim2"`)




