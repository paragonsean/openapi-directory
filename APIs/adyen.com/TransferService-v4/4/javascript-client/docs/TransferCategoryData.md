# TransfersApi.TransferCategoryData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **String** | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with &#x60;category&#x60; **bank**.  Possible values:  * **regular**: For normal, low-value transactions.  * **fast**: Faster way to transfer funds but has higher fees. Recommended for high-priority, low-value transactions.  * **wire**: Fastest way to transfer funds but has the highest fees. Recommended for high-priority, high-value transactions.  * **instant**: Instant way to transfer funds in [SEPA countries](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  * **crossBorder**: High-value transfer to a recipient in a different country.  * **internal**: Transfer to an Adyen-issued business bank account (by bank account number/IBAN). | [optional] 
**type** | **String** | **bank** | [optional] [default to &#39;bank&#39;]
**modificationMerchantReference** | **String** | The capture&#39;s merchant reference included in the transfer. | [optional] 
**modificationPspReference** | **String** | The capture reference included in the transfer. | [optional] 
**authorisationType** | **String** | The authorisation type. For example, **defaultAuthorisation**, **preAuthorisation**, **finalAuthorisation** | [optional] 
**panEntryMode** | **String** | Indicates the method used for entering the PAN to initiate a transaction.  Possible values: **manual**, **chip**, **magstripe**, **contactless**, **cof**, **ecommerce**, **token**. | [optional] 
**processingType** | **String** | Contains information about how the payment was processed. For example, **ecommerce** for online or **pos** for in-person payments. | [optional] 
**relayedAuthorisationData** | [**RelayedAuthorisationData**](RelayedAuthorisationData.md) | If you are using relayed authorisation, this object contains information from the relayed authorisation response from your server. | [optional] 
**schemeTraceId** | **String** | The identifier of the original payment provided by the scheme. The Id could be alphanumeric or numeric depending on the scheme. The schemeTraceID should be referring to an original schemeUniqueTransactionID provided in an earlier payment (not necessarily processed by Adyen). Instances of available schemeTraceId is authAdjustment or recurring payments. | [optional] 
**schemeUniqueTransactionId** | **String** | The unique identifier created by the scheme. The ID could be alphanumeric or numeric depending on the scheme. | [optional] 
**validationFacts** | [**[TransferNotificationValidationFact]**](TransferNotificationValidationFact.md) | The evaluation of the validation facts. See [validation checks](https://docs.adyen.com/issuing/validation-checks) for more information. | [optional] 
**paymentMerchantReference** | **String** | The payment&#39;s merchant reference included in the transfer. | [optional] 
**platformPaymentType** | **String** | The type of the related split. | [optional] 
**pspPaymentReference** | **String** | The payment reference included in the transfer. | [optional] 



## Enum: PriorityEnum


* `crossBorder` (value: `"crossBorder"`)

* `fast` (value: `"fast"`)

* `instant` (value: `"instant"`)

* `internal` (value: `"internal"`)

* `regular` (value: `"regular"`)

* `wire` (value: `"wire"`)





## Enum: TypeEnum


* `bank` (value: `"bank"`)

* `internal` (value: `"internal"`)

* `issuedCard` (value: `"issuedCard"`)

* `platformPayment` (value: `"platformPayment"`)





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





## Enum: PlatformPaymentTypeEnum


* `AcquiringFees` (value: `"AcquiringFees"`)

* `AdyenCommission` (value: `"AdyenCommission"`)

* `AdyenFees` (value: `"AdyenFees"`)

* `AdyenMarkup` (value: `"AdyenMarkup"`)

* `BalanceAccount` (value: `"BalanceAccount"`)

* `Commission` (value: `"Commission"`)

* `Default` (value: `"Default"`)

* `Interchange` (value: `"Interchange"`)

* `PaymentFee` (value: `"PaymentFee"`)

* `Remainder` (value: `"Remainder"`)

* `SchemeFee` (value: `"SchemeFee"`)

* `TopUp` (value: `"TopUp"`)

* `VAT` (value: `"VAT"`)




