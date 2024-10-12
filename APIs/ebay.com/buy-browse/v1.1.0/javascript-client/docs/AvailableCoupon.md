# BrowseApi.AvailableCoupon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint** | **String** | The limitations or restrictions of the coupon. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/buy/browse/types/gct:CouponConstraint&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**discountAmount** | [**Amount**](Amount.md) |  | [optional] 
**discountType** | **String** | The type of discount that the coupon applies. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/buy/browse/types/gct:CouponDiscountType&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**message** | **String** | A description of the coupon. Note: The value returned in the termsWebUrl field should appear for all experiences when displaying coupons. The value in the availableCoupons.message field must also be included, if returned in the API response. | [optional] 
**redemptionCode** | **String** | The coupon code. | [optional] 
**termsWebUrl** | **String** | The URL to the coupon terms of use. Note: The value returned in the termsWebUrl field should appear for all experiences when displaying coupons. The value in the availableCoupons.message field must also be included, if returned in the API response. | [optional] 


