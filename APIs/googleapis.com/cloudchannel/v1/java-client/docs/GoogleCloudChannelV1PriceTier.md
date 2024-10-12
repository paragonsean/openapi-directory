

# GoogleCloudChannelV1PriceTier

Defines price at resource tier level. For example, an offer with following definition : * Tier 1: Provide 25% discount for all seats between 1 and 25. * Tier 2: Provide 10% discount for all seats between 26 and 100. * Tier 3: Provide flat 15% discount for all seats above 100. Each of these tiers is represented as a PriceTier.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstResource** | **Integer** | First resource for which the tier price applies. |  [optional] |
|**lastResource** | **Integer** | Last resource for which the tier price applies. |  [optional] |
|**price** | [**GoogleCloudChannelV1Price**](GoogleCloudChannelV1Price.md) |  |  [optional] |



