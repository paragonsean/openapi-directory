

# CodeReview


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The identifier for the review. |  [optional] |
|**languages** | [**List&lt;CodereviewLanguages&gt;**](CodereviewLanguages.md) | Detailed information for each language analyzed. |  [optional] |
|**resultsUrl** | **String** | A page on LGTM to view the status and results of this code review. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the code review. |  [optional] |
|**statusMessage** | **String** | A summary of the current status of the code review. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| FAILURE | &quot;failure&quot; |
| SUCCESS | &quot;success&quot; |



