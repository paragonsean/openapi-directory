

# SourceSplitResponse

The response to a SourceSplitRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bundles** | [**List&lt;DerivedSource&gt;**](DerivedSource.md) | If outcome is SPLITTING_HAPPENED, then this is a list of bundles into which the source was split. Otherwise this field is ignored. This list can be empty, which means the source represents an empty input. |  [optional] |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) | Indicates whether splitting happened and produced a list of bundles. If this is USE_CURRENT_SOURCE_AS_IS, the current source should be processed \&quot;as is\&quot; without splitting. \&quot;bundles\&quot; is ignored in this case. If this is SPLITTING_HAPPENED, then \&quot;bundles\&quot; contains a list of bundles into which the source was split. |  [optional] |
|**shards** | [**List&lt;SourceSplitShard&gt;**](SourceSplitShard.md) | DEPRECATED in favor of bundles. |  [optional] |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;SOURCE_SPLIT_OUTCOME_UNKNOWN&quot; |
| USE_CURRENT | &quot;SOURCE_SPLIT_OUTCOME_USE_CURRENT&quot; |
| SPLITTING_HAPPENED | &quot;SOURCE_SPLIT_OUTCOME_SPLITTING_HAPPENED&quot; |



