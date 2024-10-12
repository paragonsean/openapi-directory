# RebillyRestApi.Coupon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**createdTime** | **Date** | Coupon created time. | [optional] [readonly] 
**description** | **String** | Your coupon description. When it is not empty this is used for invoice discount item description, otherwise the item&#39;s description uses coupon&#39;s ID like &#39;Coupon \&quot;COUPON-ID\&quot;&#39;.  | [optional] 
**discount** | [**Discount**](Discount.md) |  | 
**expiredTime** | **Date** | Coupon&#39;s expire time (end time). | [optional] 
**id** | **String** | Coupon&#39;s ID a.k.a redemption code. | [optional] [readonly] 
**issuedTime** | **Date** | Coupon&#39;s issued time (start time). | 
**redemptionsCount** | **Number** | Coupon&#39;s redemptions count. | [optional] [readonly] 
**restrictions** | [**[CouponRestriction]**](CouponRestriction.md) | Coupon restrictions. | [optional] 
**status** | **String** | If coupon enabled. | [optional] [readonly] 
**updatedTime** | **Date** | Coupon updated time. | [optional] [readonly] 



## Enum: StatusEnum


* `draft` (value: `"draft"`)

* `issued` (value: `"issued"`)

* `expired` (value: `"expired"`)




