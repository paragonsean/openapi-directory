# ComputeManagementClient.RollingUpgradeRunningStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Code indicating the current status of the upgrade. | [optional] [readonly] 
**lastAction** | **String** | The last action performed on the rolling upgrade. | [optional] [readonly] 
**lastActionTime** | **Date** | Last action time of the upgrade. | [optional] [readonly] 
**startTime** | **Date** | Start time of the upgrade. | [optional] [readonly] 



## Enum: CodeEnum


* `RollingForward` (value: `"RollingForward"`)

* `Cancelled` (value: `"Cancelled"`)

* `Completed` (value: `"Completed"`)

* `Faulted` (value: `"Faulted"`)





## Enum: LastActionEnum


* `Start` (value: `"Start"`)

* `Cancel` (value: `"Cancel"`)




