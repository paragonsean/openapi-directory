

# IBusinessEntity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activities** | [**List&lt;IBusinessEntityActivity&gt;**](IBusinessEntityActivity.md) |  |  [optional] [readonly] |
|**assetId** | [**IAssetId**](IAssetId.md) |  |  [optional] |
|**businessType** | [**BusinessTypeEnum**](#BusinessTypeEnum) |  |  [optional] [readonly] |
|**businessTypeFormatted** | **String** |  |  [optional] [readonly] |
|**currentAnnualDistributions** | [**Currency**](Currency.md) |  |  [optional] |
|**currentAnnualDividends** | [**Currency**](Currency.md) |  |  [optional] |
|**currentAnnualGrowthRate** | [**Percent**](Percent.md) |  |  [optional] |
|**currentAnnualNetIncome** | [**Currency**](Currency.md) |  |  [optional] |
|**entityName** | **String** |  |  [optional] [readonly] |
|**liquidationEvent** | [**ILiquidationEvent**](ILiquidationEvent.md) |  |  [optional] |
|**marketValuationDate** | [**Date**](Date.md) |  |  [optional] |
|**marketValue** | [**Currency**](Currency.md) |  |  [optional] |
|**owner** | **String** |  |  [optional] [readonly] |
|**purchaseAmount** | [**Currency**](Currency.md) |  |  [optional] |
|**purchaseDate** | [**Date**](Date.md) |  |  [optional] |
|**standardDeviation** | [**Percent**](Percent.md) |  |  [optional] |



## Enum: BusinessTypeEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| LLC | &quot;LLC&quot; |
| PARTNERSHIP | &quot;Partnership&quot; |
| S_CORPORATION | &quot;SCorporation&quot; |
| C_CORPORATION | &quot;CCorporation&quot; |



