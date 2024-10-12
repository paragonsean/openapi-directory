

# AnalyzeResult

Analyze API call result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;FormOperationError&gt;**](FormOperationError.md) | List of errors reported during the analyze  operation. |  [optional] |
|**pages** | [**List&lt;ExtractedPage&gt;**](ExtractedPage.md) | Page level information extracted in the analyzed  document. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the analyze operation. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| PARTIAL_SUCCESS | &quot;partialSuccess&quot; |
| FAILURE | &quot;failure&quot; |



