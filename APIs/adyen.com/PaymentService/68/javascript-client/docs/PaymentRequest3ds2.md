# AdyenPaymentApi.PaymentRequest3ds2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountInfo** | [**AccountInfo**](AccountInfo.md) | Shopper account information for 3D Secure 2. &gt; For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow. | [optional] 
**additionalAmount** | [**Amount**](Amount.md) | If you want a [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) request to use a non-zero value, assign this value to &#x60;additionalAmount&#x60; (while the amount must be still set to 0 to trigger BIN or card verification). Required to be in the same currency as the &#x60;amount&#x60;.  | [optional] 
**additionalData** | [**PaymentRequestAdditionalData**](PaymentRequestAdditionalData.md) |  | [optional] 
**amount** | [**Amount**](Amount.md) | The amount information for the transaction (in [minor units](https://docs.adyen.com/development-resources/currency-codes)). For [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) requests, set amount to 0 (zero). | 
**applicationInfo** | [**ApplicationInfo**](ApplicationInfo.md) | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). | [optional] 
**billingAddress** | [**Address**](Address.md) | The address where to send the invoice. &gt; The &#x60;billingAddress&#x60; object is required in the following scenarios. Include all of the fields within this object. &gt;* For 3D Secure 2 transactions in all browser-based and mobile implementations. &gt;* For cross-border payouts to and from Canada. | [optional] 
**browserInfo** | [**BrowserInfo**](BrowserInfo.md) | The shopper&#39;s browser information. &gt; For 3D Secure, the full object is required for web integrations. For mobile app integrations, include the &#x60;userAgent&#x60; and &#x60;acceptHeader&#x60; fields to indicate  that your integration can support a redirect in case a payment is routed to 3D Secure 1. | [optional] 
**captureDelayHours** | **Number** | The delay between the authorisation and scheduled auto-capture, specified in hours. | [optional] 
**dateOfBirth** | **Date** | The shopper&#39;s date of birth.  Format [ISO-8601](https://www.w3.org/TR/NOTE-datetime): YYYY-MM-DD | [optional] 
**dccQuote** | [**ForexQuote**](ForexQuote.md) | The forex quote as returned in the response of the forex service. | [optional] 
**deliveryAddress** | [**Address**](Address.md) | The address where the purchased goods should be delivered. | [optional] 
**deliveryDate** | **Date** | The date and time the purchased goods should be delivered.  Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): YYYY-MM-DDThh:mm:ss.sssTZD  Example: 2017-07-17T13:42:40.428+01:00 | [optional] 
**deviceFingerprint** | **String** | A string containing the shopper&#39;s device fingerprint. For more information, refer to [Device fingerprinting](https://docs.adyen.com/risk-management/device-fingerprinting). | [optional] 
**fraudOffset** | **Number** | An integer value that is added to the normal fraud score. The value can be either positive or negative. | [optional] 
**installments** | [**Installments**](Installments.md) | Contains installment settings. For more information, refer to [Installments](https://docs.adyen.com/payment-methods/cards/credit-card-installments). | [optional] 
**localizedShopperStatement** | **{String: String}** | The &#x60;localizedShopperStatement&#x60; field lets you use dynamic values for your shopper statement in a local character set. If not supplied, left empty, or for cross-border transactions, **shopperStatement** is used.  Adyen currently supports the ja-Kana character set for Visa and Mastercard payments in Japan using Japanese cards. This character set supports:  * UTF-8 based Katakana, capital letters, numbers and special characters.  * Half-width or full-width characters. | [optional] 
**mcc** | **String** | The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) (MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant. | [optional] 
**merchantAccount** | **String** | The merchant account identifier, with which you want to process the transaction. | 
**merchantOrderReference** | **String** | This reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate). The reference should be unique per billing cycle. The same merchant order reference should never be reused after the first authorised attempt. If used, this field should be supplied for all incoming authorisations. &gt; We strongly recommend you send the &#x60;merchantOrderReference&#x60; value to benefit from linking payment requests when authorisation retries take place. In addition, we recommend you provide &#x60;retry.orderAttemptNumber&#x60;, &#x60;retry.chainAttemptNumber&#x60;, and &#x60;retry.skipRetry&#x60; values in &#x60;PaymentRequest.additionalData&#x60;. | [optional] 
**merchantRiskIndicator** | [**MerchantRiskIndicator**](MerchantRiskIndicator.md) | Additional risk fields for 3D Secure 2. &gt; For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow. | [optional] 
**metadata** | **{String: String}** | Metadata consists of entries, each of which includes a key and a value. Limits: * Maximum 20 key-value pairs per request. When exceeding, the \&quot;177\&quot; error occurs: \&quot;Metadata size exceeds limit\&quot;. * Maximum 20 characters per key. * Maximum 80 characters per value.  | [optional] 
**orderReference** | **String** | When you are doing multiple partial (gift card) payments, this is the &#x60;pspReference&#x60; of the first payment. We use this to link the multiple payments to each other. As your own reference for linking multiple payments, use the &#x60;merchantOrderReference&#x60;instead. | [optional] 
**recurring** | [**Recurring**](Recurring.md) | The recurring settings for the payment. Use this property when you want to enable [recurring payments](https://docs.adyen.com/classic-integration/recurring-payments). | [optional] 
**recurringProcessingModel** | **String** | Defines a recurring payment type. Required when creating a token to store payment details or using stored payment details. Allowed values: * &#x60;Subscription&#x60; – A transaction for a fixed or variable amount, which follows a fixed schedule. * &#x60;CardOnFile&#x60; – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction. * &#x60;UnscheduledCardOnFile&#x60; – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder&#39;s balance drops below a certain amount.  | [optional] 
**reference** | **String** | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to provide multiple references for a transaction, separate them with hyphens (\&quot;-\&quot;). Maximum length: 80 characters. | 
**selectedBrand** | **String** | Some payment methods require defining a value for this field to specify how to process the transaction.  For the Bancontact payment method, it can be set to: * &#x60;maestro&#x60; (default), to be processed like a Maestro card, or * &#x60;bcmc&#x60;, to be processed like a Bancontact card. | [optional] 
**selectedRecurringDetailReference** | **String** | The &#x60;recurringDetailReference&#x60; you want to use for this payment. The value &#x60;LATEST&#x60; can be used to select the most recently stored recurring detail. | [optional] 
**sessionId** | **String** | A session ID used to identify a payment session. | [optional] 
**shopperEmail** | **String** | The shopper&#39;s email address. We recommend that you provide this data, as it is used in velocity fraud checks. &gt; For 3D Secure 2 transactions, schemes require &#x60;shopperEmail&#x60; for all browser-based and mobile implementations. | [optional] 
**shopperIP** | **String** | The shopper&#39;s IP address. In general, we recommend that you provide this data, as it is used in a number of risk checks (for instance, number of payment attempts or location-based checks). &gt; For 3D Secure 2 transactions, schemes require &#x60;shopperIP&#x60; for all browser-based implementations. This field is also mandatory for some merchants depending on your business model. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new). | [optional] 
**shopperInteraction** | **String** | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction by default.  This field has the following possible values: * &#x60;Ecommerce&#x60; - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request. * &#x60;ContAuth&#x60; - Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment). * &#x60;Moto&#x60; - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone. * &#x60;POS&#x60; - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. | [optional] 
**shopperLocale** | **String** | The combination of a language code and a country code to specify the language to be used in the payment. | [optional] 
**shopperName** | [**Name**](Name.md) | The shopper&#39;s full name. | [optional] 
**shopperReference** | **String** | Required for recurring payments.  Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. | [optional] 
**shopperStatement** | **String** | The text to be shown on the shopper&#39;s bank statement.  We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.  Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , &#39; _ - ? + * /_**. | [optional] 
**socialSecurityNumber** | **String** | The shopper&#39;s social security number. | [optional] 
**splits** | [**[Split]**](Split.md) | An array of objects specifying how the payment should be split when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information) or [Issuing](https://docs.adyen.com/issuing/add-manage-funds#split). | [optional] 
**store** | **String** | The ecommerce or point-of-sale store that is processing the payment. Used in:  * [Partner platform integrations](https://docs.adyen.com/marketplaces-and-platforms/classic/platforms-for-partners#route-payments) for the [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic). * [Platform setup integrations](https://docs.adyen.com/marketplaces-and-platforms/additional-for-platform-setup/route-payment-to-store) for the [Balance Platform](https://docs.adyen.com/marketplaces-and-platforms). | [optional] 
**telephoneNumber** | **String** | The shopper&#39;s telephone number. | [optional] 
**threeDS2RequestData** | [**ThreeDS2RequestData**](ThreeDS2RequestData.md) | Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer to [Online payments](https://docs.adyen.com/online-payments) or [Classic integration](https://docs.adyen.com/classic-integration) documentation. | [optional] 
**threeDS2Result** | [**ThreeDS2Result**](ThreeDS2Result.md) | Thre ThreeDS2Result that was returned in the final CRes. | [optional] 
**threeDS2Token** | **String** | The ThreeDS2Token that was returned in the /authorise call. | [optional] 
**threeDSAuthenticationOnly** | **Boolean** | If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation. | [optional] [default to false]
**totalsGroup** | **String** | The reference value to aggregate sales totals in reporting. When not specified, the store field is used (if available). | [optional] 
**trustedShopper** | **Boolean** | Set to true if the payment should be routed to a trusted MID. | [optional] 



## Enum: RecurringProcessingModelEnum


* `CardOnFile` (value: `"CardOnFile"`)

* `Subscription` (value: `"Subscription"`)

* `UnscheduledCardOnFile` (value: `"UnscheduledCardOnFile"`)





## Enum: ShopperInteractionEnum


* `Ecommerce` (value: `"Ecommerce"`)

* `ContAuth` (value: `"ContAuth"`)

* `Moto` (value: `"Moto"`)

* `POS` (value: `"POS"`)




