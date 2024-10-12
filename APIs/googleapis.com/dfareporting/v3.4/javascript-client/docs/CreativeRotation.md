# CampaignManager360Api.CreativeRotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creativeAssignments** | [**[CreativeAssignment]**](CreativeAssignment.md) | Creative assignments in this creative rotation. | [optional] 
**creativeOptimizationConfigurationId** | **String** | Creative optimization configuration that is used by this ad. It should refer to one of the existing optimization configurations in the ad&#39;s campaign. If it is unset or set to 0, then the campaign&#39;s default optimization configuration will be used for this ad. | [optional] 
**type** | **String** | Type of creative rotation. Can be used to specify whether to use sequential or random rotation. | [optional] 
**weightCalculationStrategy** | **String** | Strategy for calculating weights. Used with CREATIVE_ROTATION_TYPE_RANDOM. | [optional] 



## Enum: TypeEnum


* `SEQUENTIAL` (value: `"CREATIVE_ROTATION_TYPE_SEQUENTIAL"`)

* `RANDOM` (value: `"CREATIVE_ROTATION_TYPE_RANDOM"`)





## Enum: WeightCalculationStrategyEnum


* `EQUAL` (value: `"WEIGHT_STRATEGY_EQUAL"`)

* `CUSTOM` (value: `"WEIGHT_STRATEGY_CUSTOM"`)

* `HIGHEST_CTR` (value: `"WEIGHT_STRATEGY_HIGHEST_CTR"`)

* `OPTIMIZED` (value: `"WEIGHT_STRATEGY_OPTIMIZED"`)




