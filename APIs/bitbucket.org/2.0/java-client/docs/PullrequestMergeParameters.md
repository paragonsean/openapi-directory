

# PullrequestMergeParameters

The metadata that describes a pull request merge.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closeSourceBranch** | **Boolean** | Whether the source branch should be deleted. If this is not provided, we fallback to the value used when the pull request was created, which defaults to False |  [optional] |
|**mergeStrategy** | [**MergeStrategyEnum**](#MergeStrategyEnum) | The merge strategy that will be used to merge the pull request. |  [optional] |
|**message** | **String** | The commit message that will be used on the resulting commit. |  [optional] |
|**type** | **String** |  |  |



## Enum: MergeStrategyEnum

| Name | Value |
|---- | -----|
| MERGE_COMMIT | &quot;merge_commit&quot; |
| SQUASH | &quot;squash&quot; |
| FAST_FORWARD | &quot;fast_forward&quot; |



