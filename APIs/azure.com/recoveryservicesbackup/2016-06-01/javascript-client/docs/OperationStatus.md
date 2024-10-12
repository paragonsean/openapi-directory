# RecoveryServicesBackupClient.OperationStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The operation end time. The format of the time is ISO-8601. | [optional] 
**error** | [**OperationStatusError**](OperationStatusError.md) |  | [optional] 
**id** | **String** | ID of the operation. | [optional] 
**name** | **String** | Name of the operation. | [optional] 
**properties** | [**OperationStatusExtendedInfo**](OperationStatusExtendedInfo.md) |  | [optional] 
**startTime** | **Date** | The operation start time. The format of the time is ISO-8601. | [optional] 
**status** | **String** | Operation status. | [optional] 



## Enum: StatusEnum


* `Invalid` (value: `"Invalid"`)

* `InProgress` (value: `"InProgress"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)




