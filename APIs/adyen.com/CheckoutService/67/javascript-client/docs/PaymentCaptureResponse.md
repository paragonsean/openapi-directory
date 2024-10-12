# AdyenCheckoutApi.PaymentCaptureResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | The captured amount. | 
**lineItems** | [**[LineItem]**](LineItem.md) | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment). &gt; This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. | [optional] 
**merchantAccount** | **String** | The merchant account that is used to process the payment. | 
**paymentPspReference** | **String** | The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment to capture.  | 
**pspReference** | **String** | Adyen&#39;s 16-character reference associated with the capture request. | 
**reference** | **String** | Your reference for the capture request. | [optional] 
**splits** | [**[Split]**](Split.md) | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information). | [optional] 
**status** | **String** | The status of your request. This will always have the value **received**. | 



## Enum: StatusEnum


* `received` (value: `"received"`)




