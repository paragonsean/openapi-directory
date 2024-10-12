

# CreateSubmissionBatchResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | **String** |  |  [optional] |
|**errors** | **List&lt;String&gt;** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**submissionBatch** | [**SubmissionBatch**](SubmissionBatch.md) |  |  |
|**submissions** | [**List&lt;CreateSubmissionBatchSubmissionsResponse&gt;**](CreateSubmissionBatchSubmissionsResponse.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| ERROR | &quot;error&quot; |



