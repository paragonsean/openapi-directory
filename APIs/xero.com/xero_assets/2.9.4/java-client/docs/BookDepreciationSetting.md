

# BookDepreciationSetting


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**averagingMethod** | [**AveragingMethodEnum**](#AveragingMethodEnum) | The method of averaging applied to this asset. See Averaging Methods |  [optional] |
|**bookEffectiveDateOfChangeId** | **UUID** | Unique Xero identifier for the effective date change |  [optional] |
|**depreciableObjectId** | **UUID** | Unique Xero identifier for the depreciable object |  [optional] |
|**depreciableObjectType** | **String** | The type of asset object |  [optional] |
|**depreciationCalculationMethod** | [**DepreciationCalculationMethodEnum**](#DepreciationCalculationMethodEnum) | See Depreciation Calculation Methods |  [optional] |
|**depreciationMethod** | [**DepreciationMethodEnum**](#DepreciationMethodEnum) | The method of depreciation applied to this asset. See Depreciation Methods |  [optional] |
|**depreciationRate** | **Double** | The rate of depreciation (e.g. 0.05) |  [optional] |
|**effectiveLifeYears** | **Integer** | Effective life of the asset in years (e.g. 5) |  [optional] |



## Enum: AveragingMethodEnum

| Name | Value |
|---- | -----|
| FULL_MONTH | &quot;FullMonth&quot; |
| ACTUAL_DAYS | &quot;ActualDays&quot; |



## Enum: DepreciationCalculationMethodEnum

| Name | Value |
|---- | -----|
| RATE | &quot;Rate&quot; |
| LIFE | &quot;Life&quot; |
| NONE | &quot;None&quot; |



## Enum: DepreciationMethodEnum

| Name | Value |
|---- | -----|
| NO_DEPRECIATION | &quot;NoDepreciation&quot; |
| STRAIGHT_LINE | &quot;StraightLine&quot; |
| DIMINISHING_VALUE100 | &quot;DiminishingValue100&quot; |
| DIMINISHING_VALUE150 | &quot;DiminishingValue150&quot; |
| DIMINISHING_VALUE200 | &quot;DiminishingValue200&quot; |
| FULL_DEPRECIATION | &quot;FullDepreciation&quot; |



