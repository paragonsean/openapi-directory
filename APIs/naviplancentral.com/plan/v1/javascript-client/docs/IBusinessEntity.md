# NaviPlanApi.IBusinessEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**[IBusinessEntityActivity]**](IBusinessEntityActivity.md) |  | [optional] [readonly] 
**assetId** | [**IAssetId**](IAssetId.md) |  | [optional] 
**businessType** | **String** |  | [optional] [readonly] 
**businessTypeFormatted** | **String** |  | [optional] [readonly] 
**currentAnnualDistributions** | [**Currency**](Currency.md) |  | [optional] 
**currentAnnualDividends** | [**Currency**](Currency.md) |  | [optional] 
**currentAnnualGrowthRate** | [**Percent**](Percent.md) |  | [optional] 
**currentAnnualNetIncome** | [**Currency**](Currency.md) |  | [optional] 
**entityName** | **String** |  | [optional] [readonly] 
**liquidationEvent** | [**ILiquidationEvent**](ILiquidationEvent.md) |  | [optional] 
**marketValuationDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**marketValue** | [**Currency**](Currency.md) |  | [optional] 
**owner** | **String** |  | [optional] [readonly] 
**purchaseAmount** | [**Currency**](Currency.md) |  | [optional] 
**purchaseDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**standardDeviation** | [**Percent**](Percent.md) |  | [optional] 



## Enum: BusinessTypeEnum


* `Undefined` (value: `"Undefined"`)

* `LLC` (value: `"LLC"`)

* `Partnership` (value: `"Partnership"`)

* `SCorporation` (value: `"SCorporation"`)

* `CCorporation` (value: `"CCorporation"`)




