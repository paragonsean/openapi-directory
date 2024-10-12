

# CreativeRotation

Creative Rotation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creativeAssignments** | [**List&lt;CreativeAssignment&gt;**](CreativeAssignment.md) | Creative assignments in this creative rotation. |  [optional] |
|**creativeOptimizationConfigurationId** | **String** | Creative optimization configuration that is used by this ad. It should refer to one of the existing optimization configurations in the ad&#39;s campaign. If it is unset or set to 0, then the campaign&#39;s default optimization configuration will be used for this ad. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of creative rotation. Can be used to specify whether to use sequential or random rotation. |  [optional] |
|**weightCalculationStrategy** | [**WeightCalculationStrategyEnum**](#WeightCalculationStrategyEnum) | Strategy for calculating weights. Used with CREATIVE_ROTATION_TYPE_RANDOM. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SEQUENTIAL | &quot;CREATIVE_ROTATION_TYPE_SEQUENTIAL&quot; |
| RANDOM | &quot;CREATIVE_ROTATION_TYPE_RANDOM&quot; |



## Enum: WeightCalculationStrategyEnum

| Name | Value |
|---- | -----|
| EQUAL | &quot;WEIGHT_STRATEGY_EQUAL&quot; |
| CUSTOM | &quot;WEIGHT_STRATEGY_CUSTOM&quot; |
| HIGHEST_CTR | &quot;WEIGHT_STRATEGY_HIGHEST_CTR&quot; |
| OPTIMIZED | &quot;WEIGHT_STRATEGY_OPTIMIZED&quot; |



