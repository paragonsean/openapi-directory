# RebillyRestApi.CommonPayPalAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. | 
**createdTime** | **Date** | PayPal account created time. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**customerId** | **String** | The customer&#39;s ID. | 
**id** | **String** | The payment instrument ID. | [optional] [readonly] 
**method** | **String** | The method of payment instrument. | 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  | [optional] 
**status** | **String** | PayPal account status. | [optional] [readonly] 
**updatedTime** | **Date** | PayPal account updated time. | [optional] [readonly] 
**username** | **String** | PayPal username. | [optional] [readonly] 



## Enum: MethodEnum


* `paypal` (value: `"paypal"`)





## Enum: StatusEnum


* `inactive` (value: `"inactive"`)

* `active` (value: `"active"`)

* `deactivated` (value: `"deactivated"`)




