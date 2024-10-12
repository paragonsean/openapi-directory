

# Pricing


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comparisonPrice** | [**UpdatePriceRequestPricingInnerComparisonPrice**](UpdatePriceRequestPricingInnerComparisonPrice.md) |  |  [optional] |
|**comparisonPriceType** | [**ComparisonPriceTypeEnum**](#ComparisonPriceTypeEnum) | This is applicable only for promotions |  [optional] |
|**currentPrice** | [**UpdatePriceRequestPricingInnerCurrentPrice**](UpdatePriceRequestPricingInnerCurrentPrice.md) |  |  |
|**currentPriceType** | [**CurrentPriceTypeEnum**](#CurrentPriceTypeEnum) | This is applicable only for both promotions and price |  |
|**effectiveDate** | **OffsetDateTime** | This is applicable only for promotions |  [optional] |
|**expirationDate** | **OffsetDateTime** | This is applicable only for promotions |  [optional] |
|**priceDisplayCodes** | [**PriceDisplayCodesEnum**](#PriceDisplayCodesEnum) | Represent promo placement. This is applicable only for promotions |  [optional] |
|**processMode** | [**ProcessModeEnum**](#ProcessModeEnum) | This is applicable only for promotions |  [optional] |
|**promoId** | **String** | This is applicable only for promotions |  [optional] |



## Enum: ComparisonPriceTypeEnum

| Name | Value |
|---- | -----|
| BASE | &quot;BASE&quot; |



## Enum: CurrentPriceTypeEnum

| Name | Value |
|---- | -----|
| BASE | &quot;BASE&quot; |
| REDUCED | &quot;REDUCED&quot; |
| CLEARANCE | &quot;CLEARANCE&quot; |



## Enum: PriceDisplayCodesEnum

| Name | Value |
|---- | -----|
| CART | &quot;CART&quot; |
| CHECKOUT | &quot;CHECKOUT&quot; |



## Enum: ProcessModeEnum

| Name | Value |
|---- | -----|
| UPSERT | &quot;UPSERT&quot; |
| DELETE | &quot;DELETE&quot; |



