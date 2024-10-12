

# TransferOperation

A description of the execution of a transfer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**counters** | [**TransferCounters**](TransferCounters.md) |  |  [optional] |
|**endTime** | **String** | End time of this transfer execution. |  [optional] |
|**errorBreakdowns** | [**List&lt;ErrorSummary&gt;**](ErrorSummary.md) | Summarizes errors encountered with sample error log entries. |  [optional] |
|**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  |  [optional] |
|**name** | **String** | A globally unique ID assigned by the system. |  [optional] |
|**notificationConfig** | [**NotificationConfig**](NotificationConfig.md) |  |  [optional] |
|**projectId** | **String** | The ID of the Google Cloud project that owns the operation. |  [optional] |
|**startTime** | **String** | Start time of this transfer execution. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the transfer operation. |  [optional] |
|**transferJobName** | **String** | The name of the transfer job that triggers this transfer operation. |  [optional] |
|**transferSpec** | [**TransferSpec**](TransferSpec.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| PAUSED | &quot;PAUSED&quot; |
| SUCCESS | &quot;SUCCESS&quot; |
| FAILED | &quot;FAILED&quot; |
| ABORTED | &quot;ABORTED&quot; |
| QUEUED | &quot;QUEUED&quot; |
| SUSPENDING | &quot;SUSPENDING&quot; |



