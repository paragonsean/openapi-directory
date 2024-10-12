# AdyenCheckoutApi.PaymentMethodsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | [**BalanceCheckRequestAdditionalData**](BalanceCheckRequestAdditionalData.md) |  | [optional] 
**allowedPaymentMethods** | **[String]** | List of payment methods to be presented to the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).  Example: &#x60;\&quot;allowedPaymentMethods\&quot;:[\&quot;ideal\&quot;,\&quot;giropay\&quot;]&#x60; | [optional] 
**amount** | [**Amount**](Amount.md) | The amount information for the transaction (in [minor units](https://docs.adyen.com/development-resources/currency-codes)). For [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) requests, set amount to 0 (zero). | [optional] 
**blockedPaymentMethods** | **[String]** | List of payment methods to be hidden from the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).  Example: &#x60;\&quot;blockedPaymentMethods\&quot;:[\&quot;ideal\&quot;,\&quot;giropay\&quot;]&#x60; | [optional] 
**channel** | **String** | The platform where a payment transaction takes place. This field can be used for filtering out payment methods that are only available on specific platforms. Possible values: * iOS * Android * Web | [optional] 
**countryCode** | **String** | The shopper&#39;s country code. | [optional] 
**merchantAccount** | **String** | The merchant account identifier, with which you want to process the transaction. | 
**order** | [**EncryptedOrderData**](EncryptedOrderData.md) | The order information required for partial payments. | [optional] 
**shopperLocale** | **String** | The combination of a language code and a country code to specify the language to be used in the payment. | [optional] 
**shopperReference** | **String** | Required for recurring payments.  Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. | [optional] 
**splitCardFundingSources** | **Boolean** | Boolean value indicating whether the card payment method should be split into separate debit and credit options. | [optional] [default to false]
**store** | **String** | Required for Adyen for Platforms integrations if you have a platform setup. This is your [reference](https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/stores#request-reference) (on [balance platform](https://docs.adyen.com/marketplaces-and-platforms/classic/platforms-for-partners#route-payments)) or the [storeReference](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference) (in the [classic integration](https://docs.adyen.com/marketplaces-and-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store)) for the ecommerce or point-of-sale store that is processing the payment. | [optional] 



## Enum: ChannelEnum


* `iOS` (value: `"iOS"`)

* `Android` (value: `"Android"`)

* `Web` (value: `"Web"`)




