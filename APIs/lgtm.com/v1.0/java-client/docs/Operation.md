

# Operation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Long** | The identifier for the operation. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the operation. |  [optional] |
|**taskResult** | [**OperationTaskResult**](OperationTaskResult.md) |  |  [optional] |
|**taskResultUrl** | **String** | The URL for the result of the task. For some operations, included only on completion. |  [optional] |
|**taskType** | [**TaskTypeEnum**](#TaskTypeEnum) |  |  |
|**uploads** | [**Map&lt;String, UploadSession&gt;**](UploadSession.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| DONE | &quot;done&quot; |



## Enum: TaskTypeEnum

| Name | Value |
|---- | -----|
| ANALYSIS | &quot;analysis&quot; |
| CODEREVIEW | &quot;codereview&quot; |
| QUERYJOB | &quot;queryjob&quot; |



