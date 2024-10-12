

# CombinedSubmission


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;CombinedSubmissionAction&gt;**](CombinedSubmissionAction.md) |  |  [optional] |
|**downloadUrl** | **String** |  |  [optional] |
|**errorMessage** | **String** |  |  [optional] |
|**expired** | **Boolean** |  |  |
|**expiresAt** | **String** |  |  [optional] |
|**expiresIn** | **Integer** |  |  [optional] |
|**id** | **String** |  |  |
|**metadata** | **Object** |  |  [optional] |
|**password** | **String** |  |  [optional] |
|**pdfHash** | **String** |  |  [optional] |
|**sourcePdfs** | [**List&lt;CombinedSubmissionSourcePdfsInner&gt;**](CombinedSubmissionSourcePdfsInner.md) |  |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**submissionIds** | **List&lt;String&gt;** |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| PROCESSED | &quot;processed&quot; |
| ERROR | &quot;error&quot; |



