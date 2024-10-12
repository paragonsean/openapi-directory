# Vimeo.OnDemandPromotion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessType** | **String** | The type of access that this promotion grants:  Option descriptions:  * &#x60;default&#x60; - Grants discounts on existing product offerings.  * &#x60;vip&#x60; - Grants free access either to VOD content before it is released or to access types that aren&#39;t part of the existing product offerings.  | 
**discountType** | **String** | The type of discount for which this promotion can be used.  Option descriptions:  * &#x60;dollars&#x60; - The discount is a certain fixed amount.  * &#x60;free&#x60; - The discount is the full purchase price. VIP access promotions always use this discount type.  * &#x60;percent&#x60; - The discount is a certain percentage of the full price.  | 
**download** | **Boolean** | Whether this promotion grants download access to On Demand content. | 
**label** | **String** | The prefix string for batch codes, or the null value for single codes. | 
**metadata** | [**OnDemandPromotionMetadata**](OnDemandPromotionMetadata.md) |  | 
**percentOff** | **Number** | The percentage amount that is deducted from the product price. | 
**productType** | **String** | The type of product to which this promotion can be applied. Only &#x60;buy&#x60; and &#x60;rent&#x60; are available for the VIP access type:  Option descriptions:  * &#x60;any&#x60; - The promotion can be applied to any product.  * &#x60;buy&#x60; - The promotion can be applied to a buyable single video.  * &#x60;buy_episode&#x60; - The promotion can be applied to a buyable single episode.  * &#x60;rent&#x60; - The promotion can be applied to a rentable single video.  * &#x60;rent_episode&#x60; - The promotion can be applied to a rentable single episode.  * &#x60;subscribe&#x60; - The promotion can be applied to a subscription.  | 
**streamPeriod** | **String** | The amount of time that the user has access to the VOD content after redeeming a promo code.  Option descriptions:  * &#x60;1_week&#x60; - Access lasts for one week.  * &#x60;1_year&#x60; - Access lasts for one year.  * &#x60;24_hour&#x60; - Access lasts for 24 hours.  * &#x60;30_days&#x60; - Access lasts for 30 days.  * &#x60;3_month&#x60; - Access lasts for 3 months.  * &#x60;48_hour&#x60; - Access lasts for 48 hours.  * &#x60;6_month&#x60; - Access lasts for 6 months.  * &#x60;72_hour&#x60; - Access lasts for 72 hours.  | 
**total** | **Number** | The total amount of times that this promotion can be used. | 
**type** | **String** | The way in which this promotion can generate promo codes:  Option descriptions:  * &#x60;batch&#x60; - Provides many unique promo codes that can only be used once each.  * &#x60;batch_prefix&#x60; - Similar to &#x60;batch&#x60;, except that all codes have a similar prefix string. This mode is deprecated, yet it may still appear for some users.  * &#x60;single&#x60; - Provides a single promo code with many uses.  | 
**uri** | **String** | The promotion&#39;s canonical relative URI. | 



## Enum: AccessTypeEnum


* `default` (value: `"default"`)

* `vip` (value: `"vip"`)





## Enum: DiscountTypeEnum


* `dollars` (value: `"dollars"`)

* `free` (value: `"free"`)

* `percent` (value: `"percent"`)





## Enum: ProductTypeEnum


* `any` (value: `"any"`)

* `buy` (value: `"buy"`)

* `buy_episode` (value: `"buy_episode"`)

* `rent` (value: `"rent"`)

* `rent_episode` (value: `"rent_episode"`)

* `subscribe` (value: `"subscribe"`)





## Enum: StreamPeriodEnum


* `1_week` (value: `"1_week"`)

* `1_year` (value: `"1_year"`)

* `24_hour` (value: `"24_hour"`)

* `30_days` (value: `"30_days"`)

* `3_month` (value: `"3_month"`)

* `48_hour` (value: `"48_hour"`)

* `6_month` (value: `"6_month"`)

* `72_hour` (value: `"72_hour"`)





## Enum: TypeEnum


* `batch` (value: `"batch"`)

* `batch_prefix` (value: `"batch_prefix"`)

* `single` (value: `"single"`)




