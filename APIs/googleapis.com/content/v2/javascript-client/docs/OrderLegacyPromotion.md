# ContentApiForShopping.OrderLegacyPromotion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefits** | [**[OrderLegacyPromotionBenefit]**](OrderLegacyPromotionBenefit.md) |  | [optional] 
**effectiveDates** | **String** | The date and time frame when the promotion is active and ready for validation review. Note that the promotion live time may be delayed for a few hours due to the validation review. Start date and end date are separated by a forward slash (/). The start date is specified by the format (YYYY-MM-DD), followed by the letter ?T?, the time of the day when the sale starts (in Greenwich Mean Time, GMT), followed by an expression of the time zone for the sale. The end date is in the same format. | [optional] 
**genericRedemptionCode** | **String** | Optional. The text code that corresponds to the promotion when applied on the retailer?s website. | [optional] 
**id** | **String** | The unique ID of the promotion. | [optional] 
**longTitle** | **String** | The full title of the promotion. | [optional] 
**productApplicability** | **String** | Whether the promotion is applicable to all products or only specific products. Acceptable values are: - \&quot;&#x60;allProducts&#x60;\&quot; - \&quot;&#x60;specificProducts&#x60;\&quot;  | [optional] 
**redemptionChannel** | **String** | Indicates that the promotion is valid online. Acceptable values are: - \&quot;&#x60;online&#x60;\&quot;  | [optional] 


