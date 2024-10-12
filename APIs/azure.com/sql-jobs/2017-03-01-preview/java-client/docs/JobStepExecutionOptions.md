

# JobStepExecutionOptions

The execution options of a job step.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**initialRetryIntervalSeconds** | **Integer** | Initial delay between retries for job step execution. |  [optional] |
|**maximumRetryIntervalSeconds** | **Integer** | The maximum amount of time to wait between retries for job step execution. |  [optional] |
|**retryAttempts** | **Integer** | Maximum number of times the job step will be reattempted if the first attempt fails. |  [optional] |
|**retryIntervalBackoffMultiplier** | **Float** | The backoff multiplier for the time between retries. |  [optional] |
|**timeoutSeconds** | **Integer** | Execution timeout for the job step. |  [optional] |



