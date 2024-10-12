

# PullRequestBranch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultMergeStrategy** | **String** | The default merge strategy, when this endpoint is the destination of the pull request. |  [optional] |
|**mergeStrategies** | [**List&lt;MergeStrategiesEnum&gt;**](#List&lt;MergeStrategiesEnum&gt;) | Available merge strategies, when this endpoint is the destination of the pull request. |  [optional] |
|**name** | **String** |  |  [optional] |



## Enum: List&lt;MergeStrategiesEnum&gt;

| Name | Value |
|---- | -----|
| MERGE_COMMIT | &quot;merge_commit&quot; |
| SQUASH | &quot;squash&quot; |
| FAST_FORWARD | &quot;fast_forward&quot; |



