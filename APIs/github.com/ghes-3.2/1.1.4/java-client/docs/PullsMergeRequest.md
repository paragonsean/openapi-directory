

# PullsMergeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitMessage** | **String** | Extra detail to append to automatic commit message. |  [optional] |
|**commitTitle** | **String** | Title for the automatic commit message. |  [optional] |
|**mergeMethod** | [**MergeMethodEnum**](#MergeMethodEnum) | The merge method to use. |  [optional] |
|**sha** | **String** | SHA that pull request head must match to allow merge. |  [optional] |



## Enum: MergeMethodEnum

| Name | Value |
|---- | -----|
| MERGE | &quot;merge&quot; |
| SQUASH | &quot;squash&quot; |
| REBASE | &quot;rebase&quot; |



