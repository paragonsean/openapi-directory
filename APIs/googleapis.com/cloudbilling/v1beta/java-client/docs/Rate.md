

# Rate

A SKU price consisting of tiered rates.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tiers** | [**List&lt;RateTier&gt;**](RateTier.md) | The service tiers. |  [optional] |
|**unit** | **String** | The SKU&#39;s pricing unit. For example, if the tier price is $1 per 1000000 Bytes, then this field will show &#39;By&#39;. The &#x60;start_amount&#x60; field in each tier will be in this unit. |  [optional] |
|**unitCount** | **Double** | The SKU&#39;s count for the pricing unit. For example, if the tier price is $1 per 1000000 Bytes, then this column will show 1000000. |  [optional] |



