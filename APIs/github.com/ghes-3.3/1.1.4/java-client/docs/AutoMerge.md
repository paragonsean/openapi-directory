

# AutoMerge

The status of auto merging a pull request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitMessage** | **String** | Commit message for the merge commit. |  |
|**commitTitle** | **String** | Title for the merge commit message. |  |
|**enabledBy** | [**SimpleUser**](SimpleUser.md) |  |  |
|**mergeMethod** | [**MergeMethodEnum**](#MergeMethodEnum) | The merge method to use. |  |



## Enum: MergeMethodEnum

| Name | Value |
|---- | -----|
| MERGE | &quot;merge&quot; |
| SQUASH | &quot;squash&quot; |
| REBASE | &quot;rebase&quot; |



