# ConnectorsApi.UpdatePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **String** | Optional. Relative scheduling channel applied to resource. | [optional] 
**denyMaintenancePeriods** | [**[DenyMaintenancePeriod]**](DenyMaintenancePeriod.md) | Deny Maintenance Period that is applied to resource to indicate when maintenance is forbidden. The protocol supports zero-to-many such periods, but the current SLM Rollout implementation only supports zero-to-one. | [optional] 
**window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 



## Enum: ChannelEnum


* `UPDATE_CHANNEL_UNSPECIFIED` (value: `"UPDATE_CHANNEL_UNSPECIFIED"`)

* `EARLIER` (value: `"EARLIER"`)

* `LATER` (value: `"LATER"`)

* `WEEK1` (value: `"WEEK1"`)

* `WEEK2` (value: `"WEEK2"`)

* `WEEK5` (value: `"WEEK5"`)




