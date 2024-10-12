

# GooglePrivacyDlpV2SummaryResult

A collection that informs the user the number of times a particular `TransformationResultCode` and error details occurred.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Outcome of the transformation. |  [optional] |
|**count** | **String** | Number of transformations counted by this result. |  [optional] |
|**details** | **String** | A place for warnings or errors to show up if a transformation didn&#39;t work as expected. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| TRANSFORMATION_RESULT_CODE_UNSPECIFIED | &quot;TRANSFORMATION_RESULT_CODE_UNSPECIFIED&quot; |
| SUCCESS | &quot;SUCCESS&quot; |
| ERROR | &quot;ERROR&quot; |



