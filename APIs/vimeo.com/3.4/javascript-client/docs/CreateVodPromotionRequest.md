# Vimeo.CreateVodPromotionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessType** | **String** | The promotion access type, which is a purchase option that isn&#39;t available on the container. VIP promotions always make the content free of charge. If you use this type, you must further define the promotion with the &#x60;download&#x60; or &#x60;stream_period&#x60; fields.  Option descriptions:  * &#x60;default&#x60; - Promotions grant discount on the existing purchase options for an On Demand Container.  * &#x60;vip&#x60; - Promotions can be used to grant free access to VOD content before it is released, or to offer a purchase option that isn&#39;t available on the container. \&quot;vip\&quot; promotions will always make the content free, and must be further defined with the &#x60;download&#x60; or &#x60;stream_period&#x60; fields.  | [optional] 
**code** | **String** | The promotion code. This field is ignored for batch promotions. | [optional] 
**discountType** | **String** | The type of discount offered by the promo code. When &#x60;access_type&#x60; is &#x60;vip&#x60;, the value of this field must be &#x60;free&#x60;.  Option descriptions:  * &#x60;free&#x60; - Reduces the price to zero.  * &#x60;percent&#x60; - Reduces the price by an amount defined in the \&quot;percent_off\&quot; field.  | [optional] 
**download** | **Boolean** | Whether the promotion grants download access to VOD content. This is necessary only when not previously defined in the On Demand container or when &#x60;access_type&#x60; is &#x60;vip&#x60; or &#x60;product_type&#x60; is &#x60;buy&#x60;. | 
**endTime** | **String** | The end of the promotion period. If you don&#39;t specify a value, the promotion will never expire. | [optional] 
**label** | **String** | The description of a batch promotion. This field is ignored for single promotions. | [optional] 
**percentOff** | **Number** | The percentage of the discount by using this promo code. This field is applicable only when &#x60;discount_type&#x60; is &#x60;percent&#x60;. | [optional] 
**productType** | **String** | The type of transaction to which the promotion applies. When &#x60;access_type&#x60; is &#x60;default&#x60;, the default value is &#x60;any&#x60;, but the default value is &#x60;rent&#x60; when &#x60;access_type&#x60; is &#x60;vip&#x60;. Also, when &#x60;access_type&#x60; is &#x60;vip&#x60;, the only valid product types are &#x60;buy&#x60; and &#x60;rent&#x60;. | [optional] 
**startTime** | **String** | The start of the promotion period. If you don&#39;t specify a value, the start time defaults to the time that the promotion was created. | [optional] 
**streamPeriod** | **String** | The amount of time that a user has access to the VOD content upon redeeming a promo code. This field is necessary only when not defined in the On Demand container or when creating promotions when &#x60;access_type&#x60; is &#x60;vip&#x60; or &#x60;product_type&#x60; is &#x60;rent&#x60;. | 
**total** | **Number** | The number of promotions to generate when &#x60;type&#x60; is &#x60;batch&#x60;, or the number of uses of the promotion when &#x60;type&#x60; is &#x60;single&#x60;. | 
**type** | **String** | The type of promotion. When &#x60;access_type&#x60; is &#x60;vip&#x60;, the value for this field must be &#x60;batch&#x60;.  Option descriptions:  * &#x60;batch&#x60; - Generates many random promo codes with one use each.  * &#x60;single&#x60; - Generates one promo code that can be used many times.  | 



## Enum: AccessTypeEnum


* `default` (value: `"default"`)

* `vip` (value: `"vip"`)





## Enum: DiscountTypeEnum


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

* `30_day` (value: `"30_day"`)

* `3_month` (value: `"3_month"`)

* `48_hour` (value: `"48_hour"`)

* `6_month` (value: `"6_month"`)

* `72_hour` (value: `"72_hour"`)





## Enum: TypeEnum


* `batch` (value: `"batch"`)

* `single` (value: `"single"`)




