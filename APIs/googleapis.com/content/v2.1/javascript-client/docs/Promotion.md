# ContentApiForShopping.Promotion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **[String]** | Product filter by brand for the promotion. | [optional] 
**brandExclusion** | **[String]** | Product filter by brand exclusion for the promotion. | [optional] 
**contentLanguage** | **String** | Required. The content language used as part of the unique identifier. &#x60;en&#x60; content language is available for all target countries. &#x60;fr&#x60; content language is available for &#x60;CA&#x60; and &#x60;FR&#x60; target countries. &#x60;de&#x60; content language is available for &#x60;DE&#x60; target country. &#x60;nl&#x60; content language is available for &#x60;NL&#x60; target country. &#x60;it&#x60; content language is available for &#x60;IT&#x60; target country. &#x60;pt&#x60; content language is available for &#x60;BR&#x60; target country. &#x60;ja&#x60; content language is available for &#x60;JP&#x60; target country. &#x60;ko&#x60; content language is available for &#x60;KR&#x60; target country. | [optional] 
**couponValueType** | **String** | Required. Coupon value type for the promotion. | [optional] 
**freeGiftDescription** | **String** | Free gift description for the promotion. | [optional] 
**freeGiftItemId** | **String** | Free gift item ID for the promotion. | [optional] 
**freeGiftValue** | [**PriceAmount**](PriceAmount.md) |  | [optional] 
**genericRedemptionCode** | **String** | Generic redemption code for the promotion. To be used with the &#x60;offerType&#x60; field. | [optional] 
**getThisQuantityDiscounted** | **Number** | The number of items discounted in the promotion. | [optional] 
**id** | **String** | Output only. The REST promotion ID to uniquely identify the promotion. Content API methods that operate on promotions take this as their &#x60;promotionId&#x60; parameter. The REST ID for a promotion is of the form channel:contentLanguage:targetCountry:promotionId The &#x60;channel&#x60; field has a value of &#x60;\&quot;online\&quot;&#x60;, &#x60;\&quot;in_store\&quot;&#x60;, or &#x60;\&quot;online_in_store\&quot;&#x60;. | [optional] [readonly] 
**itemGroupId** | **[String]** | Product filter by item group ID for the promotion. | [optional] 
**itemGroupIdExclusion** | **[String]** | Product filter by item group ID exclusion for the promotion. | [optional] 
**itemId** | **[String]** | Product filter by item ID for the promotion. | [optional] 
**itemIdExclusion** | **[String]** | Product filter by item ID exclusion for the promotion. | [optional] 
**limitQuantity** | **Number** | Maximum purchase quantity for the promotion. | [optional] 
**limitValue** | [**PriceAmount**](PriceAmount.md) |  | [optional] 
**longTitle** | **String** | Required. Long title for the promotion. | [optional] 
**minimumPurchaseAmount** | [**PriceAmount**](PriceAmount.md) |  | [optional] 
**minimumPurchaseQuantity** | **Number** | Minimum purchase quantity for the promotion. | [optional] 
**moneyBudget** | [**PriceAmount**](PriceAmount.md) |  | [optional] 
**moneyOffAmount** | [**PriceAmount**](PriceAmount.md) |  | [optional] 
**offerType** | **String** | Required. Type of the promotion. | [optional] 
**orderLimit** | **Number** | Order limit for the promotion. | [optional] 
**percentOff** | **Number** | The percentage discount offered in the promotion. | [optional] 
**productApplicability** | **String** | Required. Applicability of the promotion to either all products or only specific products. | [optional] 
**productType** | **[String]** | Product filter by product type for the promotion. | [optional] 
**productTypeExclusion** | **[String]** | Product filter by product type exclusion for the promotion. | [optional] 
**promotionDestinationIds** | **[String]** | Destination ID for the promotion. | [optional] 
**promotionDisplayDates** | **String** | String representation of the promotion display dates. Deprecated. Use &#x60;promotion_display_time_period&#x60; instead. | [optional] 
**promotionDisplayTimePeriod** | [**TimePeriod**](TimePeriod.md) |  | [optional] 
**promotionEffectiveDates** | **String** | String representation of the promotion effective dates. Deprecated. Use &#x60;promotion_effective_time_period&#x60; instead. | [optional] 
**promotionEffectiveTimePeriod** | [**TimePeriod**](TimePeriod.md) |  | [optional] 
**promotionId** | **String** | Required. The user provided promotion ID to uniquely identify the promotion. | [optional] 
**promotionStatus** | [**PromotionPromotionStatus**](PromotionPromotionStatus.md) |  | [optional] 
**promotionUrl** | **String** | URL to the page on the merchant&#39;s site where the promotion shows. Local Inventory ads promotions throw an error if no promo url is included. URL is used to confirm that the promotion is valid and can be redeemed. | [optional] 
**redemptionChannel** | **[String]** | Required. Redemption channel for the promotion. At least one channel is required. | [optional] 
**shippingServiceNames** | **[String]** | Shipping service names for the promotion. | [optional] 
**storeApplicability** | **String** | Whether the promotion applies to all stores, or only specified stores. Local Inventory ads promotions throw an error if no store applicability is included. An INVALID_ARGUMENT error is thrown if store_applicability is set to ALL_STORES and store_code or score_code_exclusion is set to a value. | [optional] 
**storeCode** | **[String]** | Store codes to include for the promotion. | [optional] 
**storeCodeExclusion** | **[String]** | Store codes to exclude for the promotion. | [optional] 
**targetCountry** | **String** | Required. The target country used as part of the unique identifier. Can be &#x60;AU&#x60;, &#x60;CA&#x60;, &#x60;DE&#x60;, &#x60;FR&#x60;, &#x60;GB&#x60;, &#x60;IN&#x60;, &#x60;US&#x60;, &#x60;BR&#x60;, &#x60;ES&#x60;, &#x60;NL&#x60;, &#x60;JP&#x60;, &#x60;IT&#x60; or &#x60;KR&#x60;. | [optional] 



## Enum: CouponValueTypeEnum


* `COUPON_VALUE_TYPE_UNSPECIFIED` (value: `"COUPON_VALUE_TYPE_UNSPECIFIED"`)

* `MONEY_OFF` (value: `"MONEY_OFF"`)

* `PERCENT_OFF` (value: `"PERCENT_OFF"`)

* `BUY_M_GET_N_MONEY_OFF` (value: `"BUY_M_GET_N_MONEY_OFF"`)

* `BUY_M_GET_N_PERCENT_OFF` (value: `"BUY_M_GET_N_PERCENT_OFF"`)

* `BUY_M_GET_MONEY_OFF` (value: `"BUY_M_GET_MONEY_OFF"`)

* `BUY_M_GET_PERCENT_OFF` (value: `"BUY_M_GET_PERCENT_OFF"`)

* `FREE_GIFT` (value: `"FREE_GIFT"`)

* `FREE_GIFT_WITH_VALUE` (value: `"FREE_GIFT_WITH_VALUE"`)

* `FREE_GIFT_WITH_ITEM_ID` (value: `"FREE_GIFT_WITH_ITEM_ID"`)

* `FREE_SHIPPING_STANDARD` (value: `"FREE_SHIPPING_STANDARD"`)

* `FREE_SHIPPING_OVERNIGHT` (value: `"FREE_SHIPPING_OVERNIGHT"`)

* `FREE_SHIPPING_TWO_DAY` (value: `"FREE_SHIPPING_TWO_DAY"`)





## Enum: OfferTypeEnum


* `OFFER_TYPE_UNSPECIFIED` (value: `"OFFER_TYPE_UNSPECIFIED"`)

* `NO_CODE` (value: `"NO_CODE"`)

* `GENERIC_CODE` (value: `"GENERIC_CODE"`)





## Enum: ProductApplicabilityEnum


* `PRODUCT_APPLICABILITY_UNSPECIFIED` (value: `"PRODUCT_APPLICABILITY_UNSPECIFIED"`)

* `ALL_PRODUCTS` (value: `"ALL_PRODUCTS"`)

* `SPECIFIC_PRODUCTS` (value: `"SPECIFIC_PRODUCTS"`)





## Enum: [RedemptionChannelEnum]


* `REDEMPTION_CHANNEL_UNSPECIFIED` (value: `"REDEMPTION_CHANNEL_UNSPECIFIED"`)

* `IN_STORE` (value: `"IN_STORE"`)

* `ONLINE` (value: `"ONLINE"`)





## Enum: StoreApplicabilityEnum


* `STORE_APPLICABILITY_UNSPECIFIED` (value: `"STORE_APPLICABILITY_UNSPECIFIED"`)

* `ALL_STORES` (value: `"ALL_STORES"`)

* `SPECIFIC_STORES` (value: `"SPECIFIC_STORES"`)




