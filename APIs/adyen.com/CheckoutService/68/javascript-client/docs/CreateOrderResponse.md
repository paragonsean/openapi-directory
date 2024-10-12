# AdyenCheckoutApi.CreateOrderResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | [**BalanceCheckResponseAdditionalData**](BalanceCheckResponseAdditionalData.md) |  | [optional] 
**amount** | [**Amount**](Amount.md) | The initial amount of the order. | 
**expiresAt** | **String** | The date that the order will expire. | 
**fraudResult** | [**FraudResult**](FraudResult.md) | The fraud result properties of the payment. | [optional] 
**orderData** | **String** | The encrypted data that will be used by merchant for adding payments to the order. | 
**pspReference** | **String** | Adyen&#39;s 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. | [optional] 
**reference** | **String** | The reference provided by merchant for creating the order. | [optional] 
**refusalReason** | **String** | If the payment&#39;s authorisation is refused or an error occurs during authorisation, this field holds Adyen&#39;s mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes &#x60;resultCode&#x60; and &#x60;refusalReason&#x60; values.  For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). | [optional] 
**remainingAmount** | [**Amount**](Amount.md) | The remaining amount in the order. | 
**resultCode** | **String** | The result of the order creation request.  The value is always **Success**. | 



## Enum: ResultCodeEnum


* `Success` (value: `"Success"`)




