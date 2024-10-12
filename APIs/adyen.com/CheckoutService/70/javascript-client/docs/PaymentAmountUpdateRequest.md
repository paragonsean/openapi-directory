# AdyenCheckoutApi.PaymentAmountUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | The updated amount. The &#x60;currency&#x60; must match the currency used in authorisation. | 
**applicationInfo** | [**ApplicationInfo**](ApplicationInfo.md) | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). | [optional] 
**industryUsage** | **String** | The reason for the amount update. Possible values:  * **delayedCharge**  * **noShow**  * **installment** | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment). &gt; This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. | [optional] 
**merchantAccount** | **String** | The merchant account that is used to process the payment. | 
**reference** | **String** | Your reference for the amount update request. Maximum length: 80 characters. | [optional] 
**splits** | [**[Split]**](Split.md) | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information). | [optional] 



## Enum: IndustryUsageEnum


* `delayedCharge` (value: `"delayedCharge"`)

* `installment` (value: `"installment"`)

* `noShow` (value: `"noShow"`)




