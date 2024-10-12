# SqlManagementClient.JobStepExecutionOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initialRetryIntervalSeconds** | **Number** | Initial delay between retries for job step execution. | [optional] [default to 1]
**maximumRetryIntervalSeconds** | **Number** | The maximum amount of time to wait between retries for job step execution. | [optional] [default to 120]
**retryAttempts** | **Number** | Maximum number of times the job step will be reattempted if the first attempt fails. | [optional] [default to 10]
**retryIntervalBackoffMultiplier** | **Number** | The backoff multiplier for the time between retries. | [optional] [default to 2.0]
**timeoutSeconds** | **Number** | Execution timeout for the job step. | [optional] [default to 43200]


