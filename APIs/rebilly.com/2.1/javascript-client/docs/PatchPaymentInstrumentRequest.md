# RebillyRestApi.PatchPaymentInstrumentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. | [optional] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**token** | **String** | Payment token ID. | [optional] 
**cvv** | **String** | Card&#39;s cvv (card verification value). | [optional] 
**expMonth** | **Number** | Card&#39;s expiration month. | [optional] 
**expYear** | **Number** | Card&#39;s expiration year. | [optional] 
**stickyGatewayAccountId** | **String** | Sticky gateway account ID. | [optional] 
**accountType** | **String** | Bank&#39;s account type. | [optional] 
**bankName** | **String** | Bank&#39;s name. | [optional] 



## Enum: AccountTypeEnum


* `checking` (value: `"checking"`)

* `savings` (value: `"savings"`)

* `other` (value: `"other"`)




