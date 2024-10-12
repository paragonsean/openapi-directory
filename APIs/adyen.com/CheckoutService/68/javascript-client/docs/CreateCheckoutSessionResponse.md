# AdyenCheckoutApi.CreateCheckoutSessionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountInfo** | [**AccountInfo**](AccountInfo.md) | Shopper account information for 3D Secure 2. &gt; For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow. | [optional] 
**additionalAmount** | [**Amount**](Amount.md) | If you want a [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) request to use a non-zero value, assign this value to &#x60;additionalAmount&#x60; (while the amount must be still set to 0 to trigger BIN or card verification). Required to be in the same currency as the &#x60;amount&#x60;.  | [optional] 
**additionalData** | [**BalanceCheckRequestAdditionalData**](BalanceCheckRequestAdditionalData.md) |  | [optional] 
**allowedPaymentMethods** | **[String]** | List of payment methods to be presented to the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).  Example: &#x60;\&quot;allowedPaymentMethods\&quot;:[\&quot;ideal\&quot;,\&quot;giropay\&quot;]&#x60; | [optional] 
**amount** | [**Amount**](Amount.md) | The amount of the payment. | 
**applicationInfo** | [**ApplicationInfo**](ApplicationInfo.md) | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). | [optional] 
**billingAddress** | [**BillingAddress**](BillingAddress.md) | The address where to send the invoice. | [optional] 
**blockedPaymentMethods** | **[String]** | List of payment methods to be hidden from the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).  Example: &#x60;\&quot;blockedPaymentMethods\&quot;:[\&quot;ideal\&quot;,\&quot;giropay\&quot;]&#x60; | [optional] 
**captureDelayHours** | **Number** | The delay between the authorisation and scheduled auto-capture, specified in hours. | [optional] 
**channel** | **String** | The platform where a payment transaction takes place. This field is optional for filtering out payment methods that are only available on specific platforms. If this value is not set, then we will try to infer it from the &#x60;sdkVersion&#x60; or &#x60;token&#x60;.  Possible values: * **iOS** * **Android** * **Web** | [optional] 
**company** | [**Company**](Company.md) | Information regarding the company. | [optional] 
**countryCode** | **String** | The shopper&#39;s two-letter country code. | [optional] 
**dateOfBirth** | **Date** | The shopper&#39;s date of birth in [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | [optional] 
**deliverAt** | **Date** | The date and time when the purchased goods should be delivered.  [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**. | [optional] 
**deliveryAddress** | [**DeliveryAddress**](DeliveryAddress.md) | The address where the purchased goods should be delivered. | [optional] 
**enableOneClick** | **Boolean** | When true and &#x60;shopperReference&#x60; is provided, the shopper will be asked if the payment details should be stored for future one-click payments. | [optional] 
**enablePayOut** | **Boolean** | When true and &#x60;shopperReference&#x60; is provided, the payment details will be tokenized for payouts. | [optional] 
**enableRecurring** | **Boolean** | When true and &#x60;shopperReference&#x60; is provided, the payment details will be tokenized for recurring payments. | [optional] 
**expiresAt** | **Date** | The date the session expires in [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. When not specified, the expiry date is set to 1 hour after session creation. You cannot set the session expiry to more than 24 hours after session creation. | 
**fundOrigin** | [**FundOrigin**](FundOrigin.md) | The person or entity funding the money. | [optional] 
**fundRecipient** | [**FundRecipient**](FundRecipient.md) | the person or entity receiving the money | [optional] 
**id** | **String** | A unique identifier of the session. | [readonly] 
**installmentOptions** | [**{String: CheckoutSessionInstallmentOption}**](CheckoutSessionInstallmentOption.md) | A set of key-value pairs that specifies the installment options available per payment method. The key must be a payment method name in lowercase. For example, **card** to specify installment options for all cards, or **visa** or **mc**. The value must be an object containing the installment options. | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | Price and product information about the purchased items, to be included on the invoice sent to the shopper. &gt; This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Zip. | [optional] 
**mandate** | [**Mandate**](Mandate.md) | The mandate details to initiate recurring transaction. | [optional] 
**mcc** | **String** | The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) (MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant. | [optional] 
**merchantAccount** | **String** | The merchant account identifier, with which you want to process the transaction. | 
**merchantOrderReference** | **String** | This reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate). The reference should be unique per billing cycle. The same merchant order reference should never be reused after the first authorised attempt. If used, this field should be supplied for all incoming authorisations. &gt; We strongly recommend you send the &#x60;merchantOrderReference&#x60; value to benefit from linking payment requests when authorisation retries take place. In addition, we recommend you provide &#x60;retry.orderAttemptNumber&#x60;, &#x60;retry.chainAttemptNumber&#x60;, and &#x60;retry.skipRetry&#x60; values in &#x60;PaymentRequest.additionalData&#x60;. | [optional] 
**metadata** | **{String: String}** | Metadata consists of entries, each of which includes a key and a value. Limits: * Maximum 20 key-value pairs per request. * Maximum 20 characters per key. * Maximum 80 characters per value.  | [optional] 
**mpiData** | [**ThreeDSecureData**](ThreeDSecureData.md) | Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires). | [optional] 
**recurringExpiry** | **String** | Date after which no further authorisations shall be performed. Only for 3D Secure 2. | [optional] 
**recurringFrequency** | **String** | Minimum number of days between authorisations. Only for 3D Secure 2. | [optional] 
**recurringProcessingModel** | **String** | Defines a recurring payment type. Required when creating a token to store payment details. Allowed values: * &#x60;Subscription&#x60; – A transaction for a fixed or variable amount, which follows a fixed schedule. * &#x60;CardOnFile&#x60; – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction. * &#x60;UnscheduledCardOnFile&#x60; – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder&#39;s balance drops below a certain amount.  | [optional] 
**redirectFromIssuerMethod** | **String** | Specifies the redirect method (GET or POST) when redirecting back from the issuer. | [optional] 
**redirectToIssuerMethod** | **String** | Specifies the redirect method (GET or POST) when redirecting to the issuer. | [optional] 
**reference** | **String** | The reference to uniquely identify a payment. | 
**returnUrl** | **String** | The URL to return to when a redirect payment is completed. | 
**riskData** | [**RiskData**](RiskData.md) | Any risk-related settings to apply to the payment. | [optional] 
**sessionData** | **String** | The payment session data you need to pass to your front end. | [optional] 
**shopperEmail** | **String** | The shopper&#39;s email address. | [optional] 
**shopperIP** | **String** | The shopper&#39;s IP address. In general, we recommend that you provide this data, as it is used in a number of risk checks (for instance, number of payment attempts or location-based checks). &gt; For 3D Secure 2 transactions, schemes require &#x60;shopperIP&#x60; for all browser-based implementations. This field is also mandatory for some merchants depending on your business model. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new). | [optional] 
**shopperInteraction** | **String** | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction by default.  This field has the following possible values: * &#x60;Ecommerce&#x60; - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request. * &#x60;ContAuth&#x60; - Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment). * &#x60;Moto&#x60; - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone. * &#x60;POS&#x60; - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. | [optional] 
**shopperLocale** | **String** | The combination of a language code and a country code to specify the language to be used in the payment. | [optional] 
**shopperName** | [**Name**](Name.md) | The shopper&#39;s full name. This object is required for some payment methods such as AfterPay, Klarna, or if you&#39;re enrolled in the PayPal Seller Protection program. | [optional] 
**shopperReference** | **String** | Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. | [optional] 
**shopperStatement** | **String** | The text to be shown on the shopper&#39;s bank statement.  We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.  Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , &#39; _ - ? + * /_**. | [optional] 
**showInstallmentAmount** | **Boolean** | Set to true to show the payment amount per installment. | [optional] 
**showRemovePaymentMethodButton** | **Boolean** | Set to **true** to show a button that lets the shopper remove a stored payment method. | [optional] 
**socialSecurityNumber** | **String** | The shopper&#39;s social security number. | [optional] 
**splitCardFundingSources** | **Boolean** | Boolean value indicating whether the card payment method should be split into separate debit and credit options. | [optional] [default to false]
**splits** | [**[Split]**](Split.md) | An array of objects specifying how to split a payment when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information), [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic/processing-payments#providing-split-information), or [Issuing](https://docs.adyen.com/issuing/manage-funds#split). | [optional] 
**store** | **String** | Required for Adyen for Platforms integrations if you have a platform setup. This is your [reference](https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/stores#request-reference) (on [balance platform](https://docs.adyen.com/marketplaces-and-platforms/classic/platforms-for-partners#route-payments)) or the [storeReference](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference) (in the [classic integration](https://docs.adyen.com/marketplaces-and-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store)) for the ecommerce or point-of-sale store that is processing the payment. | [optional] 
**storePaymentMethod** | **Boolean** | When this is set to **true** and the &#x60;shopperReference&#x60; is provided, the payment details will be stored. | [optional] 
**telephoneNumber** | **String** | The shopper&#39;s telephone number. | [optional] 
**threeDSAuthenticationOnly** | **Boolean** | If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation. | [optional] [default to false]
**trustedShopper** | **Boolean** | Set to true if the payment should be routed to a trusted MID. | [optional] 



## Enum: ChannelEnum


* `iOS` (value: `"iOS"`)

* `Android` (value: `"Android"`)

* `Web` (value: `"Web"`)





## Enum: RecurringProcessingModelEnum


* `CardOnFile` (value: `"CardOnFile"`)

* `Subscription` (value: `"Subscription"`)

* `UnscheduledCardOnFile` (value: `"UnscheduledCardOnFile"`)





## Enum: ShopperInteractionEnum


* `Ecommerce` (value: `"Ecommerce"`)

* `ContAuth` (value: `"ContAuth"`)

* `Moto` (value: `"Moto"`)

* `POS` (value: `"POS"`)




