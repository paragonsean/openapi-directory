# XeroAssetsApi.BookDepreciationSetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**averagingMethod** | **String** | The method of averaging applied to this asset. See Averaging Methods | [optional] 
**bookEffectiveDateOfChangeId** | **String** | Unique Xero identifier for the effective date change | [optional] 
**depreciableObjectId** | **String** | Unique Xero identifier for the depreciable object | [optional] 
**depreciableObjectType** | **String** | The type of asset object | [optional] 
**depreciationCalculationMethod** | **String** | See Depreciation Calculation Methods | [optional] 
**depreciationMethod** | **String** | The method of depreciation applied to this asset. See Depreciation Methods | [optional] 
**depreciationRate** | **Number** | The rate of depreciation (e.g. 0.05) | [optional] 
**effectiveLifeYears** | **Number** | Effective life of the asset in years (e.g. 5) | [optional] 



## Enum: AveragingMethodEnum


* `FullMonth` (value: `"FullMonth"`)

* `ActualDays` (value: `"ActualDays"`)





## Enum: DepreciationCalculationMethodEnum


* `Rate` (value: `"Rate"`)

* `Life` (value: `"Life"`)

* `None` (value: `"None"`)





## Enum: DepreciationMethodEnum


* `NoDepreciation` (value: `"NoDepreciation"`)

* `StraightLine` (value: `"StraightLine"`)

* `DiminishingValue100` (value: `"DiminishingValue100"`)

* `DiminishingValue150` (value: `"DiminishingValue150"`)

* `DiminishingValue200` (value: `"DiminishingValue200"`)

* `FullDepreciation` (value: `"FullDepreciation"`)




