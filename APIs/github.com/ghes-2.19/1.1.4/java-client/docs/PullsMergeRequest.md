

# PullsMergeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitMessage** | **String** | Extra detail to append to automatic commit message. |  [optional] |
|**commitTitle** | **String** | Title for the automatic commit message. |  [optional] |
|**mergeMethod** | [**MergeMethodEnum**](#MergeMethodEnum) | Merge method to use. Possible values are &#x60;merge&#x60;, &#x60;squash&#x60; or &#x60;rebase&#x60;. Default is &#x60;merge&#x60;. |  [optional] |
|**sha** | **String** | SHA that pull request head must match to allow merge. |  [optional] |



## Enum: MergeMethodEnum

| Name | Value |
|---- | -----|
| MERGE | &quot;merge&quot; |
| SQUASH | &quot;squash&quot; |
| REBASE | &quot;rebase&quot; |



