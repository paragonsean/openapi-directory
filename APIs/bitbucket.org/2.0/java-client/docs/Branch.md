

# Branch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**RefLinks**](RefLinks.md) |  |  [optional] |
|**name** | **String** | The name of the ref. |  [optional] |
|**target** | [**Commit**](Commit.md) |  |  [optional] |
|**type** | **String** |  |  |
|**defaultMergeStrategy** | **String** | The default merge strategy for pull requests targeting this branch. |  [optional] |
|**mergeStrategies** | [**List&lt;MergeStrategiesEnum&gt;**](#List&lt;MergeStrategiesEnum&gt;) | Available merge strategies for pull requests targeting this branch. |  [optional] |



## Enum: List&lt;MergeStrategiesEnum&gt;

| Name | Value |
|---- | -----|
| MERGE_COMMIT | &quot;merge_commit&quot; |
| SQUASH | &quot;squash&quot; |
| FAST_FORWARD | &quot;fast_forward&quot; |



