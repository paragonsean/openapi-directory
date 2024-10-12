# CloudDeployApi.RetryPhase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | [**[RetryAttempt]**](RetryAttempt.md) | Output only. Detail of a retry action. | [optional] [readonly] 
**backoffMode** | **String** | Output only. The pattern of how the wait time of the retry attempt is calculated. | [optional] [readonly] 
**jobId** | **String** | Output only. The job ID for the Job to retry. | [optional] [readonly] 
**phaseId** | **String** | Output only. The phase ID of the phase that includes the job being retried. | [optional] [readonly] 
**totalAttempts** | **String** | Output only. The number of attempts that have been made. | [optional] [readonly] 



## Enum: BackoffModeEnum


* `UNSPECIFIED` (value: `"BACKOFF_MODE_UNSPECIFIED"`)

* `LINEAR` (value: `"BACKOFF_MODE_LINEAR"`)

* `EXPONENTIAL` (value: `"BACKOFF_MODE_EXPONENTIAL"`)




