# StorageTransferApi.TransferOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counters** | [**TransferCounters**](TransferCounters.md) |  | [optional] 
**endTime** | **String** | End time of this transfer execution. | [optional] 
**errorBreakdowns** | [**[ErrorSummary]**](ErrorSummary.md) | Summarizes errors encountered with sample error log entries. | [optional] 
**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  | [optional] 
**name** | **String** | A globally unique ID assigned by the system. | [optional] 
**notificationConfig** | [**NotificationConfig**](NotificationConfig.md) |  | [optional] 
**projectId** | **String** | The ID of the Google Cloud project that owns the operation. | [optional] 
**startTime** | **String** | Start time of this transfer execution. | [optional] 
**status** | **String** | Status of the transfer operation. | [optional] 
**transferJobName** | **String** | The name of the transfer job that triggers this transfer operation. | [optional] 
**transferSpec** | [**TransferSpec**](TransferSpec.md) |  | [optional] 



## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `PAUSED` (value: `"PAUSED"`)

* `SUCCESS` (value: `"SUCCESS"`)

* `FAILED` (value: `"FAILED"`)

* `ABORTED` (value: `"ABORTED"`)

* `QUEUED` (value: `"QUEUED"`)

* `SUSPENDING` (value: `"SUSPENDING"`)




