# RebillyRestApi.PaymentCard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankCountry** | **String** | Payment instrument bank country. | [optional] [readonly] 
**bankName** | **String** | Payment instrument bank name. | [optional] [readonly] 
**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address. | [optional] 
**bin** | **String** | The card&#39;s bin (the PAN&#39;s first 6 digits). | [optional] [readonly] 
**brand** | [**PaymentCardBrand**](PaymentCardBrand.md) |  | [optional] [readonly] 
**createdTime** | **Date** | Payment instrument created time. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**customerId** | **String** | The сustomer&#39;s ID. | [optional] 
**cvv** | **String** | Card&#39;s cvv (card verification value). | [optional] 
**expMonth** | **Number** | Card&#39;s expiration month. | [optional] 
**expYear** | **Number** | Card&#39;s expiration year. | [optional] 
**fingerprint** | **String** | A unique value to identify the payment instrument regardless of variable values. It contains alphanumeric values. | [optional] [readonly] 
**id** | **String** | The payment instrument ID. | [optional] [readonly] 
**last4** | **String** | The PAN&#39;s last 4 digits. | [optional] [readonly] 
**method** | **String** | The method of payment instrument. | [optional] [readonly] 
**pan** | **String** | The card PAN (primary account number). | [optional] 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  | [optional] 
**status** | **String** | Payment instrument status. When an instrument is &#x60;active&#x60; it means it has been used at least once for an approved transaction. To remove an instrument from being in use, set it as &#x60;deactivated&#x60; (see the deactivation endpoint).  | [optional] 
**updatedTime** | **Date** | Payment instrument updated time. | [optional] [readonly] 
**embedded** | [**[PaymentCardAllOfEmbedded]**](PaymentCardAllOfEmbedded.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[PaymentCardAllOfLinks]**](PaymentCardAllOfLinks.md) | The links related to resource. | [optional] [readonly] 
**expirationReminderNumber** | **Number** | Number of expiration reminder events triggered. | [optional] [readonly] 
**expirationReminderTime** | **Date** | Time expiration reminder event will be triggered. | [optional] [readonly] 
**stickyGatewayAccountId** | **String** | Default gateway account ID used for transactions. | [optional] [readonly] 



## Enum: MethodEnum


* `payment-card` (value: `"payment-card"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)

* `expired` (value: `"expired"`)

* `deactivated` (value: `"deactivated"`)

* `verification-needed` (value: `"verification-needed"`)




