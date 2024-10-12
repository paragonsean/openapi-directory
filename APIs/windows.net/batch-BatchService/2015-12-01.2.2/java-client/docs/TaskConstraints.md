

# TaskConstraints

Constraints to apply to the Job Manager task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxTaskRetryCount** | **Integer** | Gets or sets the maximum number of times the task may be retried. The Batch service retries a task if its exit code is nonzero. |  [optional] |
|**maxWallClockTime** | **String** | Gets or sets the maximum elapsed time that the task may run, measured from the time the task starts. If the task does not complete within the time limit, the Batch service terminates it. |  [optional] |
|**retentionTime** | **String** | Gets or sets the minimum time to retain the working directory for the task on the compute node where it ran. After this time, the Batch service may delete the working directory and all its contents. The default is infinite. |  [optional] |



