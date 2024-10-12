

# Promotion

Represents a promotion. See the following articles for more details. * [Promotions feed specification](https://support.google.com/merchants/answer/2906014) * [Local promotions feed specification](https://support.google.com/merchants/answer/10146130) * [Promotions on Buy on Google product data specification](https://support.google.com/merchants/answer/9173673)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brand** | **List&lt;String&gt;** | Product filter by brand for the promotion. |  [optional] |
|**brandExclusion** | **List&lt;String&gt;** | Product filter by brand exclusion for the promotion. |  [optional] |
|**contentLanguage** | **String** | Required. The content language used as part of the unique identifier. &#x60;en&#x60; content language is available for all target countries. &#x60;fr&#x60; content language is available for &#x60;CA&#x60; and &#x60;FR&#x60; target countries. &#x60;de&#x60; content language is available for &#x60;DE&#x60; target country. &#x60;nl&#x60; content language is available for &#x60;NL&#x60; target country. &#x60;it&#x60; content language is available for &#x60;IT&#x60; target country. &#x60;pt&#x60; content language is available for &#x60;BR&#x60; target country. &#x60;ja&#x60; content language is available for &#x60;JP&#x60; target country. &#x60;ko&#x60; content language is available for &#x60;KR&#x60; target country. |  [optional] |
|**couponValueType** | [**CouponValueTypeEnum**](#CouponValueTypeEnum) | Required. Coupon value type for the promotion. |  [optional] |
|**freeGiftDescription** | **String** | Free gift description for the promotion. |  [optional] |
|**freeGiftItemId** | **String** | Free gift item ID for the promotion. |  [optional] |
|**freeGiftValue** | [**PriceAmount**](PriceAmount.md) |  |  [optional] |
|**genericRedemptionCode** | **String** | Generic redemption code for the promotion. To be used with the &#x60;offerType&#x60; field. |  [optional] |
|**getThisQuantityDiscounted** | **Integer** | The number of items discounted in the promotion. |  [optional] |
|**id** | **String** | Output only. The REST promotion ID to uniquely identify the promotion. Content API methods that operate on promotions take this as their &#x60;promotionId&#x60; parameter. The REST ID for a promotion is of the form channel:contentLanguage:targetCountry:promotionId The &#x60;channel&#x60; field has a value of &#x60;\&quot;online\&quot;&#x60;, &#x60;\&quot;in_store\&quot;&#x60;, or &#x60;\&quot;online_in_store\&quot;&#x60;. |  [optional] [readonly] |
|**itemGroupId** | **List&lt;String&gt;** | Product filter by item group ID for the promotion. |  [optional] |
|**itemGroupIdExclusion** | **List&lt;String&gt;** | Product filter by item group ID exclusion for the promotion. |  [optional] |
|**itemId** | **List&lt;String&gt;** | Product filter by item ID for the promotion. |  [optional] |
|**itemIdExclusion** | **List&lt;String&gt;** | Product filter by item ID exclusion for the promotion. |  [optional] |
|**limitQuantity** | **Integer** | Maximum purchase quantity for the promotion. |  [optional] |
|**limitValue** | [**PriceAmount**](PriceAmount.md) |  |  [optional] |
|**longTitle** | **String** | Required. Long title for the promotion. |  [optional] |
|**minimumPurchaseAmount** | [**PriceAmount**](PriceAmount.md) |  |  [optional] |
|**minimumPurchaseQuantity** | **Integer** | Minimum purchase quantity for the promotion. |  [optional] |
|**moneyBudget** | [**PriceAmount**](PriceAmount.md) |  |  [optional] |
|**moneyOffAmount** | [**PriceAmount**](PriceAmount.md) |  |  [optional] |
|**offerType** | [**OfferTypeEnum**](#OfferTypeEnum) | Required. Type of the promotion. |  [optional] |
|**orderLimit** | **Integer** | Order limit for the promotion. |  [optional] |
|**percentOff** | **Integer** | The percentage discount offered in the promotion. |  [optional] |
|**productApplicability** | [**ProductApplicabilityEnum**](#ProductApplicabilityEnum) | Required. Applicability of the promotion to either all products or only specific products. |  [optional] |
|**productType** | **List&lt;String&gt;** | Product filter by product type for the promotion. |  [optional] |
|**productTypeExclusion** | **List&lt;String&gt;** | Product filter by product type exclusion for the promotion. |  [optional] |
|**promotionDestinationIds** | **List&lt;String&gt;** | Destination ID for the promotion. |  [optional] |
|**promotionDisplayDates** | **String** | String representation of the promotion display dates. Deprecated. Use &#x60;promotion_display_time_period&#x60; instead. |  [optional] |
|**promotionDisplayTimePeriod** | [**TimePeriod**](TimePeriod.md) |  |  [optional] |
|**promotionEffectiveDates** | **String** | String representation of the promotion effective dates. Deprecated. Use &#x60;promotion_effective_time_period&#x60; instead. |  [optional] |
|**promotionEffectiveTimePeriod** | [**TimePeriod**](TimePeriod.md) |  |  [optional] |
|**promotionId** | **String** | Required. The user provided promotion ID to uniquely identify the promotion. |  [optional] |
|**promotionStatus** | [**PromotionPromotionStatus**](PromotionPromotionStatus.md) |  |  [optional] |
|**promotionUrl** | **String** | URL to the page on the merchant&#39;s site where the promotion shows. Local Inventory ads promotions throw an error if no promo url is included. URL is used to confirm that the promotion is valid and can be redeemed. |  [optional] |
|**redemptionChannel** | [**List&lt;RedemptionChannelEnum&gt;**](#List&lt;RedemptionChannelEnum&gt;) | Required. Redemption channel for the promotion. At least one channel is required. |  [optional] |
|**shippingServiceNames** | **List&lt;String&gt;** | Shipping service names for the promotion. |  [optional] |
|**storeApplicability** | [**StoreApplicabilityEnum**](#StoreApplicabilityEnum) | Whether the promotion applies to all stores, or only specified stores. Local Inventory ads promotions throw an error if no store applicability is included. An INVALID_ARGUMENT error is thrown if store_applicability is set to ALL_STORES and store_code or score_code_exclusion is set to a value. |  [optional] |
|**storeCode** | **List&lt;String&gt;** | Store codes to include for the promotion. |  [optional] |
|**storeCodeExclusion** | **List&lt;String&gt;** | Store codes to exclude for the promotion. |  [optional] |
|**targetCountry** | **String** | Required. The target country used as part of the unique identifier. Can be &#x60;AU&#x60;, &#x60;CA&#x60;, &#x60;DE&#x60;, &#x60;FR&#x60;, &#x60;GB&#x60;, &#x60;IN&#x60;, &#x60;US&#x60;, &#x60;BR&#x60;, &#x60;ES&#x60;, &#x60;NL&#x60;, &#x60;JP&#x60;, &#x60;IT&#x60; or &#x60;KR&#x60;. |  [optional] |



## Enum: CouponValueTypeEnum

| Name | Value |
|---- | -----|
| COUPON_VALUE_TYPE_UNSPECIFIED | &quot;COUPON_VALUE_TYPE_UNSPECIFIED&quot; |
| MONEY_OFF | &quot;MONEY_OFF&quot; |
| PERCENT_OFF | &quot;PERCENT_OFF&quot; |
| BUY_M_GET_N_MONEY_OFF | &quot;BUY_M_GET_N_MONEY_OFF&quot; |
| BUY_M_GET_N_PERCENT_OFF | &quot;BUY_M_GET_N_PERCENT_OFF&quot; |
| BUY_M_GET_MONEY_OFF | &quot;BUY_M_GET_MONEY_OFF&quot; |
| BUY_M_GET_PERCENT_OFF | &quot;BUY_M_GET_PERCENT_OFF&quot; |
| FREE_GIFT | &quot;FREE_GIFT&quot; |
| FREE_GIFT_WITH_VALUE | &quot;FREE_GIFT_WITH_VALUE&quot; |
| FREE_GIFT_WITH_ITEM_ID | &quot;FREE_GIFT_WITH_ITEM_ID&quot; |
| FREE_SHIPPING_STANDARD | &quot;FREE_SHIPPING_STANDARD&quot; |
| FREE_SHIPPING_OVERNIGHT | &quot;FREE_SHIPPING_OVERNIGHT&quot; |
| FREE_SHIPPING_TWO_DAY | &quot;FREE_SHIPPING_TWO_DAY&quot; |



## Enum: OfferTypeEnum

| Name | Value |
|---- | -----|
| OFFER_TYPE_UNSPECIFIED | &quot;OFFER_TYPE_UNSPECIFIED&quot; |
| NO_CODE | &quot;NO_CODE&quot; |
| GENERIC_CODE | &quot;GENERIC_CODE&quot; |



## Enum: ProductApplicabilityEnum

| Name | Value |
|---- | -----|
| PRODUCT_APPLICABILITY_UNSPECIFIED | &quot;PRODUCT_APPLICABILITY_UNSPECIFIED&quot; |
| ALL_PRODUCTS | &quot;ALL_PRODUCTS&quot; |
| SPECIFIC_PRODUCTS | &quot;SPECIFIC_PRODUCTS&quot; |



## Enum: List&lt;RedemptionChannelEnum&gt;

| Name | Value |
|---- | -----|
| REDEMPTION_CHANNEL_UNSPECIFIED | &quot;REDEMPTION_CHANNEL_UNSPECIFIED&quot; |
| IN_STORE | &quot;IN_STORE&quot; |
| ONLINE | &quot;ONLINE&quot; |



## Enum: StoreApplicabilityEnum

| Name | Value |
|---- | -----|
| STORE_APPLICABILITY_UNSPECIFIED | &quot;STORE_APPLICABILITY_UNSPECIFIED&quot; |
| ALL_STORES | &quot;ALL_STORES&quot; |
| SPECIFIC_STORES | &quot;SPECIFIC_STORES&quot; |



