

# SubmissionBatch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completionPercentage** | **Integer** |  |  |
|**errorCount** | **Integer** |  |  |
|**id** | **String** |  |  |
|**metadata** | **Object** |  |  |
|**pendingCount** | **Integer** |  |  |
|**processedAt** | **String** |  |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**submissions** | [**List&lt;Submission&gt;**](Submission.md) |  |  [optional] |
|**totalCount** | **Integer** |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| PROCESSED | &quot;processed&quot; |
| ERROR | &quot;error&quot; |



