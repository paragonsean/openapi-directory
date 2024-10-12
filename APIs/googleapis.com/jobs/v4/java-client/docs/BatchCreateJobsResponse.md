

# BatchCreateJobsResponse

The result of JobService.BatchCreateJobs. It's used to replace google.longrunning.Operation.response in case of success.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobResults** | [**List&lt;JobResult&gt;**](JobResult.md) | List of job mutation results from a batch create operation. It can change until operation status is FINISHED, FAILED or CANCELLED. |  [optional] |



