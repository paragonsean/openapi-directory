

# OrderLegacyPromotionBenefit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**discount** | [**Price**](Price.md) |  |  [optional] |
|**offerIds** | **List&lt;String&gt;** | The OfferId(s) that were purchased in this order and map to this specific benefit of the promotion. |  [optional] |
|**subType** | **String** | Further describes the benefit of the promotion. Note that we will expand on this enumeration as we support new promotion sub-types. Acceptable values are: - \&quot;&#x60;buyMGetMoneyOff&#x60;\&quot; - \&quot;&#x60;buyMGetNMoneyOff&#x60;\&quot; - \&quot;&#x60;buyMGetNPercentOff&#x60;\&quot; - \&quot;&#x60;buyMGetPercentOff&#x60;\&quot; - \&quot;&#x60;freeGift&#x60;\&quot; - \&quot;&#x60;freeGiftWithItemId&#x60;\&quot; - \&quot;&#x60;freeGiftWithValue&#x60;\&quot; - \&quot;&#x60;freeOvernightShipping&#x60;\&quot; - \&quot;&#x60;freeShipping&#x60;\&quot; - \&quot;&#x60;freeTwoDayShipping&#x60;\&quot; - \&quot;&#x60;moneyOff&#x60;\&quot; - \&quot;&#x60;percentageOff&#x60;\&quot; - \&quot;&#x60;rewardPoints&#x60;\&quot; - \&quot;&#x60;salePrice&#x60;\&quot;  |  [optional] |
|**taxImpact** | [**Price**](Price.md) |  |  [optional] |
|**type** | **String** | Describes whether the promotion applies to products (e.g. 20% off) or to shipping (e.g. Free Shipping). Acceptable values are: - \&quot;&#x60;product&#x60;\&quot; - \&quot;&#x60;shipping&#x60;\&quot;  |  [optional] |



