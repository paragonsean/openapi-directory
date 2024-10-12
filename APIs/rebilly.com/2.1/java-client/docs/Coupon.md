

# Coupon

Coupons and Discounts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Coupon created time. |  [optional] [readonly] |
|**description** | **String** | Your coupon description. When it is not empty this is used for invoice discount item description, otherwise the item&#39;s description uses coupon&#39;s ID like &#39;Coupon \&quot;COUPON-ID\&quot;&#39;.  |  [optional] |
|**discount** | [**Discount**](Discount.md) |  |  |
|**expiredTime** | **OffsetDateTime** | Coupon&#39;s expire time (end time). |  [optional] |
|**id** | **String** | Coupon&#39;s ID a.k.a redemption code. |  [optional] [readonly] |
|**issuedTime** | **OffsetDateTime** | Coupon&#39;s issued time (start time). |  |
|**redemptionsCount** | **Integer** | Coupon&#39;s redemptions count. |  [optional] [readonly] |
|**restrictions** | [**List&lt;CouponRestriction&gt;**](CouponRestriction.md) | Coupon restrictions. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | If coupon enabled. |  [optional] [readonly] |
|**updatedTime** | **OffsetDateTime** | Coupon updated time. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ISSUED | &quot;issued&quot; |
| EXPIRED | &quot;expired&quot; |



