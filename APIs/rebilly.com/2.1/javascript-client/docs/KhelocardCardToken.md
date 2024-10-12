# RebillyRestApi.KhelocardCardToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address object. | 
**method** | **String** | The token method. | 
**paymentInstrument** | **Object** | The token instrument details. | 
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**createdTime** | **Date** | Token created time. | [optional] [readonly] 
**expirationTime** | **Date** | Token expiration time. | [optional] [readonly] 
**id** | **String** | The token identifier string. | [optional] [readonly] 
**isUsed** | **Boolean** | Whether the token was already used. | [optional] [readonly] [default to false]
**leadSource** | [**LeadSource**](LeadSource.md) |  | [optional] 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  | [optional] 
**updatedTime** | **Date** | Token updated time. | [optional] [readonly] 
**usageTime** | **Date** | Token usage time. | [optional] [readonly] 



## Enum: MethodEnum


* `Khelocard` (value: `"Khelocard"`)




