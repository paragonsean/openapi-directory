

# GoogleCloudRecommenderV1beta1CostProjection

Contains metadata about how much money a recommendation can save or incur.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cost** | [**GoogleTypeMoney**](GoogleTypeMoney.md) |  |  [optional] |
|**costInLocalCurrency** | [**GoogleTypeMoney**](GoogleTypeMoney.md) |  |  [optional] |
|**duration** | **String** | Duration for which this cost applies. |  [optional] |
|**pricingType** | [**PricingTypeEnum**](#PricingTypeEnum) | How the cost is calculated. |  [optional] |



## Enum: PricingTypeEnum

| Name | Value |
|---- | -----|
| PRICING_TYPE_UNSPECIFIED | &quot;PRICING_TYPE_UNSPECIFIED&quot; |
| LIST_PRICE | &quot;LIST_PRICE&quot; |
| CUSTOM_PRICE | &quot;CUSTOM_PRICE&quot; |



