

# GoogleCloudDialogflowCxV3beta1TestRunDifference

The description of differences between original and replayed agent output.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A human readable description of the diff, showing the actual output vs expected output. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of diff. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DIFF_TYPE_UNSPECIFIED | &quot;DIFF_TYPE_UNSPECIFIED&quot; |
| INTENT | &quot;INTENT&quot; |
| PAGE | &quot;PAGE&quot; |
| PARAMETERS | &quot;PARAMETERS&quot; |
| UTTERANCE | &quot;UTTERANCE&quot; |
| FLOW | &quot;FLOW&quot; |



