# PriceManagement.UpdatePriceRequestPricingInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparisonPrice** | [**UpdatePriceRequestPricingInnerComparisonPrice**](UpdatePriceRequestPricingInnerComparisonPrice.md) |  | [optional] 
**comparisonPriceType** | **String** | This is applicable only for promotions | [optional] 
**currentPrice** | [**UpdatePriceRequestPricingInnerCurrentPrice**](UpdatePriceRequestPricingInnerCurrentPrice.md) |  | 
**currentPriceType** | **String** | This is applicable only for both promotions and price | 
**effectiveDate** | **Date** | This is applicable only for promotions | [optional] 
**expirationDate** | **Date** | This is applicable only for promotions | [optional] 
**priceDisplayCodes** | **String** | Represent promo placement. This is applicable only for promotions | [optional] 
**processMode** | **String** | This is applicable only for promotions | [optional] 
**promoId** | **String** | This is applicable only for promotions | [optional] 



## Enum: ComparisonPriceTypeEnum


* `BASE` (value: `"BASE"`)





## Enum: CurrentPriceTypeEnum


* `BASE` (value: `"BASE"`)

* `REDUCED` (value: `"REDUCED"`)

* `CLEARANCE` (value: `"CLEARANCE"`)





## Enum: PriceDisplayCodesEnum


* `CART` (value: `"CART"`)

* `CHECKOUT` (value: `"CHECKOUT"`)





## Enum: ProcessModeEnum


* `UPSERT` (value: `"UPSERT"`)

* `DELETE` (value: `"DELETE"`)




