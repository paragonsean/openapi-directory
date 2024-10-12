

# JobStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionCount** | **Integer** | Gets the number of times this job has executed. |  [optional] [readonly] |
|**failureCount** | **Integer** | Gets the number of times this job has failed. |  [optional] [readonly] |
|**faultedCount** | **Integer** | Gets the number of faulted occurrences (occurrences that were retried and failed as many times as the retry policy states). |  [optional] [readonly] |
|**lastExecutionTime** | **OffsetDateTime** | Gets the time the last occurrence executed in ISO-8601 format.  Could be empty if job has not run yet. |  [optional] [readonly] |
|**nextExecutionTime** | **OffsetDateTime** | Gets the time of the next occurrence in ISO-8601 format. Could be empty if the job is completed. |  [optional] [readonly] |



