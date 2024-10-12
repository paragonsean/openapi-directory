# DataflowApi.SourceSplitResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundles** | [**[DerivedSource]**](DerivedSource.md) | If outcome is SPLITTING_HAPPENED, then this is a list of bundles into which the source was split. Otherwise this field is ignored. This list can be empty, which means the source represents an empty input. | [optional] 
**outcome** | **String** | Indicates whether splitting happened and produced a list of bundles. If this is USE_CURRENT_SOURCE_AS_IS, the current source should be processed \&quot;as is\&quot; without splitting. \&quot;bundles\&quot; is ignored in this case. If this is SPLITTING_HAPPENED, then \&quot;bundles\&quot; contains a list of bundles into which the source was split. | [optional] 
**shards** | [**[SourceSplitShard]**](SourceSplitShard.md) | DEPRECATED in favor of bundles. | [optional] 



## Enum: OutcomeEnum


* `UNKNOWN` (value: `"SOURCE_SPLIT_OUTCOME_UNKNOWN"`)

* `USE_CURRENT` (value: `"SOURCE_SPLIT_OUTCOME_USE_CURRENT"`)

* `SPLITTING_HAPPENED` (value: `"SOURCE_SPLIT_OUTCOME_SPLITTING_HAPPENED"`)




