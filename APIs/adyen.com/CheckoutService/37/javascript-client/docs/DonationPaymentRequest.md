# AdyenCheckoutApi.DonationPaymentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalAmount** | [**Amount**](Amount.md) | If you want a [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) request to use a non-zero value, assign this value to &#x60;additionalAmount&#x60; (while the amount must be still set to 0 to trigger BIN or card verification). Required to be in the same currency as the &#x60;amount&#x60;.  | [optional] 
**additionalData** | [**BalanceCheckRequestAdditionalData**](BalanceCheckRequestAdditionalData.md) |  | [optional] 
**allowedPaymentMethods** | **[String]** | List of payment methods to be presented to the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).  Example: &#x60;\&quot;allowedPaymentMethods\&quot;:[\&quot;ideal\&quot;,\&quot;giropay\&quot;]&#x60; | [optional] 
**amount** | [**Amount**](Amount.md) | The amount information for the transaction (in [minor units](https://docs.adyen.com/development-resources/currency-codes)). For [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) requests, set amount to 0 (zero). | 
**billingAddress** | [**BillingAddress**](BillingAddress.md) | The address where to send the invoice. &gt; The &#x60;billingAddress&#x60; object is required in the following scenarios. Include all of the fields within this object. &gt;* For 3D Secure 2 transactions in all browser-based and mobile implementations. &gt;* For cross-border payouts to and from Canada. | [optional] 
**blockedPaymentMethods** | **[String]** | List of payment methods to be hidden from the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).  Example: &#x60;\&quot;blockedPaymentMethods\&quot;:[\&quot;ideal\&quot;,\&quot;giropay\&quot;]&#x60; | [optional] 
**browserInfo** | [**BrowserInfo**](BrowserInfo.md) | The shopper&#39;s browser information. &gt; For 3D Secure, the full object is required for web integrations. For mobile app integrations, include the &#x60;userAgent&#x60; and &#x60;acceptHeader&#x60; fields to indicate  that your integration can support a redirect in case a payment is routed to 3D Secure 1. | [optional] 
**captureDelayHours** | **Number** | The delay between the authorisation and scheduled auto-capture, specified in hours. | [optional] 
**channel** | **String** | The platform where a payment transaction takes place. This field is optional for filtering out payment methods that are only available on specific platforms. If this value is not set, then we will try to infer it from the &#x60;sdkVersion&#x60; or &#x60;token&#x60;.  Possible values: * iOS * Android * Web | [optional] 
**company** | [**Company**](Company.md) | Information regarding the company. | [optional] 
**countryCode** | **String** | The shopper country.  Format: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) Example: NL or DE | [optional] 
**dateOfBirth** | **Date** | The shopper&#39;s date of birth.  Format [ISO-8601](https://www.w3.org/TR/NOTE-datetime): YYYY-MM-DD | [optional] 
**dccQuote** | [**ForexQuote**](ForexQuote.md) | The forex quote as returned in the response of the forex service. | [optional] 
**deliveryAddress** | [**DeliveryAddress**](DeliveryAddress.md) | The address where the purchased goods should be delivered. | [optional] 
**deliveryDate** | **Date** | The date and time the purchased goods should be delivered.  Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): YYYY-MM-DDThh:mm:ss.sssTZD  Example: 2017-07-17T13:42:40.428+01:00 | [optional] 
**deviceFingerprint** | **String** | A string containing the shopper&#39;s device fingerprint. For more information, refer to [Device fingerprinting](https://docs.adyen.com/risk-management/device-fingerprinting). | [optional] 
**donationAccount** | **String** | Donation account to which the transaction is credited. | [optional] 
**donationOriginalPspReference** | **String** | PSP reference of the transaction from which the donation token is generated. Required when &#x60;donationToken&#x60; is provided. | [optional] 
**donationToken** | **String** | Donation token received in the &#x60;/payments&#x60; call. | [optional] 
**enableOneClick** | **Boolean** | When true and &#x60;shopperReference&#x60; is provided, the shopper will be asked if the payment details should be stored for future one-click payments. | [optional] 
**enablePayOut** | **Boolean** | When true and &#x60;shopperReference&#x60; is provided, the payment details will be tokenized for payouts. | [optional] 
**enableRecurring** | **Boolean** | When true and &#x60;shopperReference&#x60; is provided, the payment details will be tokenized for recurring payments. | [optional] 
**entityType** | **String** | The type of the entity the payment is processed for. | [optional] 
**fraudOffset** | **Number** | An integer value that is added to the normal fraud score. The value can be either positive or negative. | [optional] 
**fundOrigin** | [**FundOrigin**](FundOrigin.md) | The person or entity funding the money. | [optional] 
**fundRecipient** | [**FundRecipient**](FundRecipient.md) | the person or entity receiving the money | [optional] 
**installments** | [**Installments**](Installments.md) | Contains installment settings. For more information, refer to [Installments](https://docs.adyen.com/payment-methods/cards/credit-card-installments). | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | Price and product information about the purchased items, to be included on the invoice sent to the shopper. &gt; This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Zip. | [optional] 
**mandate** | [**Mandate**](Mandate.md) | The mandate details to initiate recurring transaction. | [optional] 
**mcc** | **String** | The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) (MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant. | [optional] 
**merchantAccount** | **String** | The merchant account identifier, with which you want to process the transaction. | 
**merchantOrderReference** | **String** | This reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate). The reference should be unique per billing cycle. The same merchant order reference should never be reused after the first authorised attempt. If used, this field should be supplied for all incoming authorisations. &gt; We strongly recommend you send the &#x60;merchantOrderReference&#x60; value to benefit from linking payment requests when authorisation retries take place. In addition, we recommend you provide &#x60;retry.orderAttemptNumber&#x60;, &#x60;retry.chainAttemptNumber&#x60;, and &#x60;retry.skipRetry&#x60; values in &#x60;PaymentRequest.additionalData&#x60;. | [optional] 
**metadata** | **{String: String}** | Metadata consists of entries, each of which includes a key and a value. Limits: * Maximum 20 key-value pairs per request. When exceeding, the \&quot;177\&quot; error occurs: \&quot;Metadata size exceeds limit\&quot;. * Maximum 20 characters per key. * Maximum 80 characters per value.  | [optional] 
**mpiData** | [**ThreeDSecureData**](ThreeDSecureData.md) | Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires). | [optional] 
**order** | [**EncryptedOrderData**](EncryptedOrderData.md) | The order information required for partial payments. | [optional] 
**orderReference** | **String** | When you are doing multiple partial (gift card) payments, this is the &#x60;pspReference&#x60; of the first payment. We use this to link the multiple payments to each other. As your own reference for linking multiple payments, use the &#x60;merchantOrderReference&#x60;instead. | [optional] 
**paymentMethod** | [**DonationPaymentRequestPaymentMethod**](DonationPaymentRequestPaymentMethod.md) |  | 
**recurringExpiry** | **String** | Date after which no further authorisations shall be performed. Only for 3D Secure 2. | [optional] 
**recurringFrequency** | **String** | Minimum number of days between authorisations. Only for 3D Secure 2. | [optional] 
**recurringProcessingModel** | **String** | Defines a recurring payment type. Required when creating a token to store payment details or using stored payment details. Allowed values: * &#x60;Subscription&#x60; – A transaction for a fixed or variable amount, which follows a fixed schedule. * &#x60;CardOnFile&#x60; – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction. * &#x60;UnscheduledCardOnFile&#x60; – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder&#39;s balance drops below a certain amount.  | [optional] 
**redirectFromIssuerMethod** | **String** | Specifies the redirect method (GET or POST) when redirecting back from the issuer. | [optional] 
**redirectToIssuerMethod** | **String** | Specifies the redirect method (GET or POST) when redirecting to the issuer. | [optional] 
**reference** | **String** | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to provide multiple references for a transaction, separate them with hyphens (\&quot;-\&quot;). Maximum length: 80 characters. | 
**returnUrl** | **String** | The URL to return to in case of a redirection. The format depends on the channel. This URL can have a maximum of 1024 characters. * For web, include the protocol &#x60;http://&#x60; or &#x60;https://&#x60;. You can also include your own additional query parameters, for example, shopper ID or order reference number. Example: &#x60;https://your-company.com/checkout?shopperOrder&#x3D;12xy&#x60; * For iOS, use the custom URL for your app. To know more about setting custom URL schemes, refer to the [Apple Developer documentation](https://developer.apple.com/documentation/uikit/inter-process_communication/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app). Example: &#x60;my-app://&#x60; * For Android, use a custom URL handled by an Activity on your app. You can configure it with an [intent filter](https://developer.android.com/guide/components/intents-filters). Example: &#x60;my-app://your.package.name&#x60; | 
**riskData** | [**RiskData**](RiskData.md) | Contains risk data, such as client-side data, used to identify risk for a transaction. | [optional] 
**selectedRecurringDetailReference** | **String** | The &#x60;recurringDetailReference&#x60; you want to use for this payment. The value &#x60;LATEST&#x60; can be used to select the most recently stored recurring detail. | [optional] 
**sessionValidity** | **String** | The date and time until when the session remains valid, in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format.  For example: 2020-07-18T15:42:40.428+01:00 | [optional] 
**shopperEmail** | **String** | The shopper&#39;s email address. We recommend that you provide this data, as it is used in velocity fraud checks. &gt; For 3D Secure 2 transactions, schemes require &#x60;shopperEmail&#x60; for all browser-based and mobile implementations. | [optional] 
**shopperIP** | **String** | The shopper&#39;s IP address. In general, we recommend that you provide this data, as it is used in a number of risk checks (for instance, number of payment attempts or location-based checks). &gt; For 3D Secure 2 transactions, schemes require &#x60;shopperIP&#x60; for all browser-based implementations. This field is also mandatory for some merchants depending on your business model. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new). | [optional] 
**shopperInteraction** | **String** | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction by default.  This field has the following possible values: * &#x60;Ecommerce&#x60; - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request. * &#x60;ContAuth&#x60; - Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment). * &#x60;Moto&#x60; - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone. * &#x60;POS&#x60; - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. | [optional] 
**shopperLocale** | **String** | The combination of a language code and a country code to specify the language to be used in the payment. | [optional] 
**shopperName** | [**Name**](Name.md) | The shopper&#39;s full name. | [optional] 
**shopperReference** | **String** | Required for recurring payments.  Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. | [optional] 
**shopperStatement** | **String** | The text to be shown on the shopper&#39;s bank statement.  We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.  Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , &#39; _ - ? + * /_**. | [optional] 
**socialSecurityNumber** | **String** | The shopper&#39;s social security number. | [optional] 
**splits** | [**[Split]**](Split.md) | An array of objects specifying how to split a payment when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information), [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic/processing-payments#providing-split-information), or [Issuing](https://docs.adyen.com/issuing/manage-funds#split). | [optional] 
**store** | **String** | Required for Adyen for Platforms integrations if you have a platform setup. This is your [reference](https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/stores#request-reference) (on [balance platform](https://docs.adyen.com/marketplaces-and-platforms/classic/platforms-for-partners#route-payments)) or the [storeReference](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference) (in the [classic integration](https://docs.adyen.com/marketplaces-and-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store)) for the ecommerce or point-of-sale store that is processing the payment. | [optional] 
**telephoneNumber** | **String** | The shopper&#39;s telephone number. | [optional] 
**trustedShopper** | **Boolean** | Set to true if the payment should be routed to a trusted MID. | [optional] 



## Enum: ChannelEnum


* `iOS` (value: `"iOS"`)

* `Android` (value: `"Android"`)

* `Web` (value: `"Web"`)





## Enum: EntityTypeEnum


* `NaturalPerson` (value: `"NaturalPerson"`)

* `CompanyName` (value: `"CompanyName"`)





## Enum: RecurringProcessingModelEnum


* `CardOnFile` (value: `"CardOnFile"`)

* `Subscription` (value: `"Subscription"`)

* `UnscheduledCardOnFile` (value: `"UnscheduledCardOnFile"`)





## Enum: ShopperInteractionEnum


* `Ecommerce` (value: `"Ecommerce"`)

* `ContAuth` (value: `"ContAuth"`)

* `Moto` (value: `"Moto"`)

* `POS` (value: `"POS"`)




