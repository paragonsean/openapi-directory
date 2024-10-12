# AdyenCheckoutApi.PaymentCancelResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchantAccount** | **String** | The merchant account that is used to process the payment. | 
**paymentPspReference** | **String** | The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment to cancel.  | 
**pspReference** | **String** | Adyen&#39;s 16-character reference associated with the cancel request. | 
**reference** | **String** | Your reference for the cancel request. | [optional] 
**status** | **String** | The status of your request. This will always have the value **received**. | 



## Enum: StatusEnum


* `received` (value: `"received"`)




