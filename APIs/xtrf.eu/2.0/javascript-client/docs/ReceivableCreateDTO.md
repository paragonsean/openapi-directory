# XtrfHomePortalApi.ReceivableCreateDTO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculationUnitId** | **Number** |  | [optional] 
**catLogFile** | [**FileDTO**](FileDTO.md) |  | [optional] 
**currencyId** | **Number** |  | [optional] 
**description** | **String** |  | [optional] 
**id** | **Number** |  | [optional] 
**ignoreMinimumCharge** | **Boolean** |  | [optional] 
**invoiceId** | **String** |  | [optional] 
**jobTypeId** | **Number** |  | [optional] 
**languageCombination** | [**ChargeLanguageCombinationDTO**](ChargeLanguageCombinationDTO.md) |  | [optional] 
**languageCombinationIdNumber** | **String** |  | [optional] 
**minimumCharge** | **Number** |  | [optional] 
**quantity** | **Number** |  | [optional] 
**rate** | **Number** |  | [optional] 
**rateOrigin** | **String** |  | [optional] 
**taskId** | **Number** |  | [optional] 
**total** | **Number** |  | [optional] 
**type** | **String** |  | [optional] 



## Enum: RateOriginEnum


* `PRICE_PROFILE` (value: `"PRICE_PROFILE"`)

* `PRICE_LIST` (value: `"PRICE_LIST"`)

* `FILLED_MANUALLY` (value: `"FILLED_MANUALLY"`)

* `AUTOCALCULATED` (value: `"AUTOCALCULATED"`)





## Enum: TypeEnum


* `SIMPLE` (value: `"SIMPLE"`)

* `CAT` (value: `"CAT"`)




