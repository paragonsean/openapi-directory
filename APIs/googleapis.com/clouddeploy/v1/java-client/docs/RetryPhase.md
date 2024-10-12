

# RetryPhase

RetryPhase contains the retry attempts and the metadata for initiating a new attempt.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attempts** | [**List&lt;RetryAttempt&gt;**](RetryAttempt.md) | Output only. Detail of a retry action. |  [optional] [readonly] |
|**backoffMode** | [**BackoffModeEnum**](#BackoffModeEnum) | Output only. The pattern of how the wait time of the retry attempt is calculated. |  [optional] [readonly] |
|**jobId** | **String** | Output only. The job ID for the Job to retry. |  [optional] [readonly] |
|**phaseId** | **String** | Output only. The phase ID of the phase that includes the job being retried. |  [optional] [readonly] |
|**totalAttempts** | **String** | Output only. The number of attempts that have been made. |  [optional] [readonly] |



## Enum: BackoffModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BACKOFF_MODE_UNSPECIFIED&quot; |
| LINEAR | &quot;BACKOFF_MODE_LINEAR&quot; |
| EXPONENTIAL | &quot;BACKOFF_MODE_EXPONENTIAL&quot; |



