

# GoogleCloudRetailV2betaSearchRequestBoostSpec

Boost specification to boost certain items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conditionBoostSpecs** | [**List&lt;GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec&gt;**](GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec.md) | Condition boost specifications. If a product matches multiple conditions in the specifictions, boost scores from these specifications are all applied and combined in a non-linear way. Maximum number of specifications is 20. |  [optional] |
|**skipBoostSpecValidation** | **Boolean** | Whether to skip boostspec validation. If this field is set to true, invalid BoostSpec.condition_boost_specs will be ignored and valid BoostSpec.condition_boost_specs will still be applied. |  [optional] |



