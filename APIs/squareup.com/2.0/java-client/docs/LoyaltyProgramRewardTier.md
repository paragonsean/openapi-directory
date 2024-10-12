

# LoyaltyProgramRewardTier

Represents a reward tier in a loyalty program. A reward tier defines how buyers can redeem points for a reward, such as the number of points required and the value and scope of the discount. A loyalty program can offer multiple reward tiers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | The timestamp when the reward tier was created, in RFC 3339 format. |  |
|**definition** | [**LoyaltyProgramRewardDefinition**](LoyaltyProgramRewardDefinition.md) |  |  |
|**id** | **String** | The Square-assigned ID of the reward tier. |  |
|**name** | **String** | The name of the reward tier. |  |
|**points** | **Integer** | The points exchanged for the reward tier. |  |
|**pricingRuleReference** | [**CatalogObjectReference**](CatalogObjectReference.md) |  |  [optional] |



