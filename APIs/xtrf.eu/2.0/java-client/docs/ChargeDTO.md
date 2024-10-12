

# ChargeDTO


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calculationUnitId** | **Long** |  |  [optional] |
|**currencyId** | **Long** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**id** | **Long** |  |  [optional] |
|**ignoreMinimumCharge** | **Boolean** |  |  [optional] |
|**invoiceId** | **String** |  |  [optional] |
|**jobTypeId** | **Long** |  |  [optional] |
|**languageCombination** | [**ChargeLanguageCombinationDTO**](ChargeLanguageCombinationDTO.md) |  |  [optional] |
|**languageCombinationIdNumber** | **String** |  |  [optional] |
|**minimumCharge** | **BigDecimal** |  |  [optional] |
|**rateOrigin** | [**RateOriginEnum**](#RateOriginEnum) |  |  [optional] |
|**total** | **BigDecimal** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: RateOriginEnum

| Name | Value |
|---- | -----|
| PRICE_PROFILE | &quot;PRICE_PROFILE&quot; |
| PRICE_LIST | &quot;PRICE_LIST&quot; |
| FILLED_MANUALLY | &quot;FILLED_MANUALLY&quot; |
| AUTOCALCULATED | &quot;AUTOCALCULATED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SIMPLE | &quot;SIMPLE&quot; |
| CAT | &quot;CAT&quot; |



