# RebillyRestApi.AlternativePaymentInstrument2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**[AlternativePaymentInstrument2EmbeddedInner]**](AlternativePaymentInstrument2EmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[AlternativePaymentInstrument2LinksInner]**](AlternativePaymentInstrument2LinksInner.md) | Links related to the resource. | [optional] [readonly] 
**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. | [optional] 
**createdTime** | **Date** | The payment instrument created time. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**customerId** | **String** | Customer&#39;s ID. | [optional] 
**id** | **String** | The payment instrument ID. | [optional] 
**method** | [**AlternativePaymentMethods**](AlternativePaymentMethods.md) | The method of payment instrument. | [optional] 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  | [optional] 
**status** | **String** | The payment instrument status. | [optional] 
**updatedTime** | **Date** | The payment instrument updated time. | [optional] [readonly] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `deactivated` (value: `"deactivated"`)




