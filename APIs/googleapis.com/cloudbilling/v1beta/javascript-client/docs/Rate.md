# CloudBillingApi.Rate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tiers** | [**[RateTier]**](RateTier.md) | The service tiers. | [optional] 
**unit** | **String** | The SKU&#39;s pricing unit. For example, if the tier price is $1 per 1000000 Bytes, then this field will show &#39;By&#39;. The &#x60;start_amount&#x60; field in each tier will be in this unit. | [optional] 
**unitCount** | **Number** | The SKU&#39;s count for the pricing unit. For example, if the tier price is $1 per 1000000 Bytes, then this column will show 1000000. | [optional] 


