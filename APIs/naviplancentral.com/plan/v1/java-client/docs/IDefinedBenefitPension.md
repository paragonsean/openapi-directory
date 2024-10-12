

# IDefinedBenefitPension


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**benefit** | [**IOptionalFieldBenefitCurrencyWithGrowth**](IOptionalFieldBenefitCurrencyWithGrowth.md) |  |  [optional] |
|**description** | **String** |  |  [optional] [readonly] |
|**isBenefitFormula** | **Boolean** |  |  [optional] [readonly] |
|**isBenefitIntegratedWithCppQpp** | **Boolean** |  |  [optional] [readonly] |
|**isFormulaIntegratedWithCppQpp** | **Boolean** |  |  [optional] [readonly] |
|**owner** | [**OwnerEnum**](#OwnerEnum) |  |  [optional] [readonly] |
|**pensionType** | **String** |  |  [optional] [readonly] |
|**percentPayableToSurvivor** | [**Percent**](Percent.md) |  |  [optional] |
|**projectedYearsOfService** | **Integer** |  |  [optional] [readonly] |
|**startDate** | [**Date**](Date.md) |  |  [optional] |



## Enum: OwnerEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |



