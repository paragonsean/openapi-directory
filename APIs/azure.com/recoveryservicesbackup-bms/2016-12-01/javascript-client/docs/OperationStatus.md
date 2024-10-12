# RecoveryServicesBackupClient.OperationStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | Operation end time. Format: ISO-8601. | [optional] 
**error** | [**OperationStatusError**](OperationStatusError.md) |  | [optional] 
**id** | **String** | ID of the operation. | [optional] 
**name** | **String** | Name of the operation. | [optional] 
**properties** | [**OperationStatusExtendedInfo**](OperationStatusExtendedInfo.md) |  | [optional] 
**startTime** | **Date** | Operation start time. Format: ISO-8601. | [optional] 
**status** | **String** | Operation status. | [optional] 



## Enum: StatusEnum


* `Invalid` (value: `"Invalid"`)

* `InProgress` (value: `"InProgress"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)




