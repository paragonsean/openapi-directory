# VeloPaymentsApis.CreateFundingAccountRequestV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** | Required if type is either FBO or PRIVATE | [optional] 
**accountNumber** | **String** | Required if type is either FBO or PRIVATE | [optional] 
**currency** | **String** | ISO 4217 currency code, Required if type is either WUBS_DECOUPLED or PRIVATE | [optional] 
**name** | **String** |  | 
**payorId** | **String** |  | 
**routingNumber** | **String** | Required if type is either FBO or PRIVATE | [optional] 
**type** | **String** |  | 



## Enum: TypeEnum


* `FBO` (value: `"FBO"`)

* `WUBS_DECOUPLED` (value: `"WUBS_DECOUPLED"`)

* `PRIVATE` (value: `"PRIVATE"`)




