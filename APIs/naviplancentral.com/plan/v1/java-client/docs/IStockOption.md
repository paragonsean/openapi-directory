

# IStockOption


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annualDividendPerUnit** | [**Currency**](Currency.md) |  |  [optional] |
|**applicableRangeRetirementLiquidatedAssets** | [**FormattedDateRange**](FormattedDateRange.md) |  |  [optional] |
|**company** | **String** |  |  [optional] [readonly] |
|**currentUnitPrice** | [**Currency**](Currency.md) |  |  [optional] |
|**currentUnitPriceDate** | [**Date**](Date.md) |  |  [optional] |
|**description** | **String** |  |  [optional] [readonly] |
|**endOfPlanYearExercisableGrossValue** | [**Currency**](Currency.md) |  |  [optional] |
|**exerciseCost** | [**Currency**](Currency.md) |  |  [optional] |
|**expirationDate** | [**Date**](Date.md) |  |  [optional] |
|**grantDate** | [**Date**](Date.md) |  |  [optional] |
|**grantedOptions** | **Integer** |  |  [optional] [readonly] |
|**growthRate** | [**Percent**](Percent.md) |  |  [optional] |
|**id** | **String** |  |  [optional] [readonly] |
|**optionsExercisable** | **Integer** |  |  [optional] [readonly] |
|**optionsExercised** | **Integer** |  |  [optional] [readonly] |
|**optionsVested** | **Integer** |  |  [optional] [readonly] |
|**owner** | **String** |  |  [optional] [readonly] |
|**preTaxProfit** | [**Currency**](Currency.md) |  |  [optional] |
|**startOfYearAMTBasis** | [**Currency**](Currency.md) |  |  [optional] |
|**startOfYearCostBasis** | [**Currency**](Currency.md) |  |  [optional] |
|**startOfYearUnitPrice** | [**Currency**](Currency.md) |  |  [optional] |
|**strikePrice** | [**Currency**](Currency.md) |  |  [optional] |
|**symbol** | **String** |  |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] [readonly] |
|**typeFormatted** | **String** |  |  [optional] [readonly] |
|**vestingSchedule** | [**List&lt;IVestingData&gt;**](IVestingData.md) |  |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NON_QUALIFIED_STOCK_OPTION | &quot;NonQualifiedStockOption&quot; |
| INCENTIVE_STOCK_OPTION | &quot;IncentiveStockOption&quot; |



