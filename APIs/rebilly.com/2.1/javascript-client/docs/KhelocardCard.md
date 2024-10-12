# RebillyRestApi.KhelocardCard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**[BankAccountAllOfEmbedded]**](BankAccountAllOfEmbedded.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[BankAccountAllOfLinks]**](BankAccountAllOfLinks.md) | Links related to the resource. | [optional] [readonly] 
**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. | [optional] 
**createdTime** | **Date** | The payment instrument created time. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**customerId** | **String** | Customer&#39;s ID. | [optional] 
**expMonth** | **Number** | Khelocard card&#39;s expiration month. | [optional] 
**expYear** | **Number** | Khelocard card&#39;s expiration year. | [optional] 
**fingerprint** | **String** | A unique value to identify the payment instrument regardless of variable values. It contains alphanumeric values. | [optional] 
**id** | **String** | The payment instrument ID. | [optional] 
**last4** | **String** | The number&#39;s last 4 digits. | [optional] 
**method** | **String** | The method of payment instrument. | [optional] 
**number** | **String** | Khelocard card&#39;s masked number. | [optional] 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  | [optional] 
**status** | **String** | The payment instrument status. | [optional] 
**updatedTime** | **Date** | The payment instrument updated time. | [optional] [readonly] 



## Enum: MethodEnum


* `Khelocard` (value: `"Khelocard"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `deactivated` (value: `"deactivated"`)




