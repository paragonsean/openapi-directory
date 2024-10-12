# NaviPlanApi.IStockOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annualDividendPerUnit** | [**Currency**](Currency.md) |  | [optional] 
**applicableRangeRetirementLiquidatedAssets** | [**FormattedDateRange**](FormattedDateRange.md) |  | [optional] 
**company** | **String** |  | [optional] [readonly] 
**currentUnitPrice** | [**Currency**](Currency.md) |  | [optional] 
**currentUnitPriceDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**description** | **String** |  | [optional] [readonly] 
**endOfPlanYearExercisableGrossValue** | [**Currency**](Currency.md) |  | [optional] 
**exerciseCost** | [**Currency**](Currency.md) |  | [optional] 
**expirationDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**grantDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**grantedOptions** | **Number** |  | [optional] [readonly] 
**growthRate** | [**Percent**](Percent.md) |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**optionsExercisable** | **Number** |  | [optional] [readonly] 
**optionsExercised** | **Number** |  | [optional] [readonly] 
**optionsVested** | **Number** |  | [optional] [readonly] 
**owner** | **String** |  | [optional] [readonly] 
**preTaxProfit** | [**Currency**](Currency.md) |  | [optional] 
**startOfYearAMTBasis** | [**Currency**](Currency.md) |  | [optional] 
**startOfYearCostBasis** | [**Currency**](Currency.md) |  | [optional] 
**startOfYearUnitPrice** | [**Currency**](Currency.md) |  | [optional] 
**strikePrice** | [**Currency**](Currency.md) |  | [optional] 
**symbol** | **String** |  | [optional] [readonly] 
**type** | **String** |  | [optional] [readonly] 
**typeFormatted** | **String** |  | [optional] [readonly] 
**vestingSchedule** | [**[IVestingData]**](IVestingData.md) |  | [optional] [readonly] 



## Enum: TypeEnum


* `NonQualifiedStockOption` (value: `"NonQualifiedStockOption"`)

* `IncentiveStockOption` (value: `"IncentiveStockOption"`)




