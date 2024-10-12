# AdyenCheckoutApi.PaymentCaptureRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | The amount that you want to capture. The &#x60;currency&#x60; must match the currency used in authorisation, the &#x60;value&#x60; must be smaller than or equal to the authorised amount. | 
**applicationInfo** | [**ApplicationInfo**](ApplicationInfo.md) | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment). &gt; This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, and Zip. | [optional] 
**merchantAccount** | **String** | The merchant account that is used to process the payment. | 
**reference** | **String** | Your reference for the capture request. Maximum length: 80 characters. | [optional] 
**splits** | [**[Split]**](Split.md) | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information). | [optional] 


