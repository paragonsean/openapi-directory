# TransfersApi.IssuedCard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorisationType** | **String** | The authorisation type. For example, **defaultAuthorisation**, **preAuthorisation**, **finalAuthorisation** | [optional] 
**panEntryMode** | **String** | Indicates the method used for entering the PAN to initiate a transaction.  Possible values: **manual**, **chip**, **magstripe**, **contactless**, **cof**, **ecommerce**, **token**. | [optional] 
**processingType** | **String** | Contains information about how the payment was processed. For example, **ecommerce** for online or **pos** for in-person payments. | [optional] 
**relayedAuthorisationData** | [**RelayedAuthorisationData**](RelayedAuthorisationData.md) | If you are using relayed authorisation, this object contains information from the relayed authorisation response from your server. | [optional] 
**schemeTraceId** | **String** | The identifier of the original payment provided by the scheme. The Id could be alphanumeric or numeric depending on the scheme. The schemeTraceID should be referring to an original schemeUniqueTransactionID provided in an earlier payment (not necessarily processed by Adyen). Instances of available schemeTraceId is authAdjustment or recurring payments. | [optional] 
**schemeUniqueTransactionId** | **String** | The unique identifier created by the scheme. The ID could be alphanumeric or numeric depending on the scheme. | [optional] 
**type** | **String** | **issuedCard** | [optional] [default to &#39;issuedCard&#39;]
**validationFacts** | [**[TransferNotificationValidationFact]**](TransferNotificationValidationFact.md) | The evaluation of the validation facts. See [validation checks](https://docs.adyen.com/issuing/validation-checks) for more information. | [optional] 



## Enum: PanEntryModeEnum


* `chip` (value: `"chip"`)

* `cof` (value: `"cof"`)

* `contactless` (value: `"contactless"`)

* `ecommerce` (value: `"ecommerce"`)

* `magstripe` (value: `"magstripe"`)

* `manual` (value: `"manual"`)

* `token` (value: `"token"`)





## Enum: ProcessingTypeEnum


* `atmWithdraw` (value: `"atmWithdraw"`)

* `balanceInquiry` (value: `"balanceInquiry"`)

* `ecommerce` (value: `"ecommerce"`)

* `moto` (value: `"moto"`)

* `pos` (value: `"pos"`)

* `purchaseWithCashback` (value: `"purchaseWithCashback"`)

* `recurring` (value: `"recurring"`)

* `token` (value: `"token"`)





## Enum: TypeEnum


* `issuedCard` (value: `"issuedCard"`)




