# AdyenCheckoutApi.PaymentRefundResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | The refund amount. | 
**lineItems** | [**[LineItem]**](LineItem.md) | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment). &gt; This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. | [optional] 
**merchantAccount** | **String** | The merchant account that is used to process the payment. | 
**merchantRefundReason** | **String** | Your reason for the refund request. | [optional] 
**paymentPspReference** | **String** | The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment to refund.  | 
**pspReference** | **String** | Adyen&#39;s 16-character reference associated with the refund request. | 
**reference** | **String** | Your reference for the refund request. | [optional] 
**splits** | [**[Split]**](Split.md) | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information). | [optional] 
**status** | **String** | The status of your request. This will always have the value **received**. | 
**store** | **String** | The online store or [physical store](https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure/#create-stores) that is processing the refund. This must be the same as the store name configured in your Customer Area.  Otherwise, you get an error and the refund fails. | [optional] 



## Enum: MerchantRefundReasonEnum


* `FRAUD` (value: `"FRAUD"`)

* `CUSTOMER REQUEST` (value: `"CUSTOMER REQUEST"`)

* `RETURN` (value: `"RETURN"`)

* `DUPLICATE` (value: `"DUPLICATE"`)

* `OTHER` (value: `"OTHER"`)





## Enum: StatusEnum


* `received` (value: `"received"`)




