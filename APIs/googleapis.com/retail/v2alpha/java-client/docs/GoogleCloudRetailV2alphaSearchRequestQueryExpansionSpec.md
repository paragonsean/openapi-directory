

# GoogleCloudRetailV2alphaSearchRequestQueryExpansionSpec

Specification to determine under which conditions query expansion should occur.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | [**ConditionEnum**](#ConditionEnum) | The condition under which query expansion should occur. Default to Condition.DISABLED. |  [optional] |
|**pinUnexpandedResults** | **Boolean** | Whether to pin unexpanded results. If this field is set to true, unexpanded products are always at the top of the search results, followed by the expanded results. |  [optional] |



## Enum: ConditionEnum

| Name | Value |
|---- | -----|
| CONDITION_UNSPECIFIED | &quot;CONDITION_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| AUTO | &quot;AUTO&quot; |



