# BitbucketApi.Branch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**RefLinks**](RefLinks.md) |  | [optional] 
**name** | **String** | The name of the ref. | [optional] 
**target** | [**Commit**](Commit.md) |  | [optional] 
**type** | **String** |  | 
**defaultMergeStrategy** | **String** | The default merge strategy for pull requests targeting this branch. | [optional] 
**mergeStrategies** | **[String]** | Available merge strategies for pull requests targeting this branch. | [optional] 



## Enum: [MergeStrategiesEnum]


* `merge_commit` (value: `"merge_commit"`)

* `squash` (value: `"squash"`)

* `fast_forward` (value: `"fast_forward"`)




