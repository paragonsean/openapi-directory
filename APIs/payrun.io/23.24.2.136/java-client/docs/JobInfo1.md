

# JobInfo1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | The job infos&#39; created |  [optional] |
|**employerKey** | **String** | The job infos&#39; employer key |  [optional] |
|**errors** | [**Errors1**](Errors1.md) |  |  [optional] |
|**holdingDate** | **OffsetDateTime** | The job infos&#39; holding date |  [optional] |
|**jobId** | **String** | The job infos&#39; job id |  [optional] |
|**jobStatus** | [**JobStatusEnum**](#JobStatusEnum) | The job infos&#39; job status |  [optional] |
|**jobType** | **String** | The job infos&#39; job type |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The job infos&#39; last updated |  [optional] |
|**progress** | **Double** | The job infos&#39; progress |  [optional] |



## Enum: JobStatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| PENDING | &quot;Pending&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCESS | &quot;Success&quot; |
| FAILED | &quot;Failed&quot; |
| ON_HOLD | &quot;OnHold&quot; |



