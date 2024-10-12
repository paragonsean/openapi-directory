# AdyenCheckoutApi.PaymentLinkResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedPaymentMethods** | **[String]** | List of payment methods to be presented to the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).  Example: &#x60;\&quot;allowedPaymentMethods\&quot;:[\&quot;ideal\&quot;,\&quot;giropay\&quot;]&#x60; | [optional] 
**amount** | [**Amount**](Amount.md) | The payment amount and currency. | 
**applicationInfo** | [**ApplicationInfo**](ApplicationInfo.md) | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). | [optional] 
**billingAddress** | [**Address**](Address.md) | The address where to send the invoice. | [optional] 
**blockedPaymentMethods** | **[String]** | List of payment methods to be hidden from the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).  Example: &#x60;\&quot;blockedPaymentMethods\&quot;:[\&quot;ideal\&quot;,\&quot;giropay\&quot;]&#x60; | [optional] 
**countryCode** | **String** | The shopper&#39;s two-letter country code. | [optional] 
**deliverAt** | **Date** | The date and time when the purchased goods should be delivered.  [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**. | [optional] 
**deliveryAddress** | [**Address**](Address.md) | The address where the purchased goods should be delivered. | [optional] 
**description** | **String** | A short description visible on the payment page. Maximum length: 280 characters. | [optional] 
**expiresAt** | **String** | The date when the payment link expires.  [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format with time zone designator **Z**: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30Z**.  The maximum expiry date is 70 days after the payment link is created.  If not provided, the payment link expires 24 hours after it was created. | [optional] 
**id** | **String** | A unique identifier of the payment link. | [readonly] 
**installmentOptions** | [**{String: InstallmentOption}**](InstallmentOption.md) | A set of key-value pairs that specifies the installment options available per payment method. The key must be a payment method name in lowercase. For example, **card** to specify installment options for all cards, or **visa** or **mc**. The value must be an object containing the installment options. | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | Price and product information about the purchased items, to be included on the invoice sent to the shopper. This parameter is required for open invoice (_buy now, pay later_) payment methods such Afterpay, Clearpay, Klarna, RatePay, and Zip. | [optional] 
**manualCapture** | **Boolean** | Indicates if the payment must be [captured manually](https://docs.adyen.com/online-payments/capture). | [optional] 
**merchantAccount** | **String** | The merchant account identifier for which the payment link is created. | 
**merchantOrderReference** | **String** | This reference allows linking multiple transactions to each other for reporting purposes (for example, order auth-rate). The reference should be unique per billing cycle. | [optional] 
**metadata** | **{String: String}** | Metadata consists of entries, each of which includes a key and a value. Limitations: * Maximum 20 key-value pairs per request. Otherwise, error \&quot;177\&quot; occurs: \&quot;Metadata size exceeds limit\&quot; * Maximum 20 characters per key. Otherwise, error \&quot;178\&quot; occurs: \&quot;Metadata key size exceeds limit\&quot; * A key cannot have the name &#x60;checkout.linkId&#x60;. Any value that you provide with this key is going to be replaced by the real payment link ID. | [optional] 
**recurringProcessingModel** | **String** | Defines a recurring payment type. Required when &#x60;storePaymentMethodMode&#x60; is set to **askForConsent** or **enabled**. Possible values: * **Subscription** – A transaction for a fixed or variable amount, which follows a fixed schedule. * **CardOnFile** – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction. * **UnscheduledCardOnFile** – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or has variable amounts. For example, automatic top-ups when a cardholder&#39;s balance drops below a certain amount.  | [optional] 
**reference** | **String** | A reference that is used to uniquely identify the payment in future communications about the payment status. | 
**requiredShopperFields** | **[String]** | List of fields that the shopper has to provide on the payment page before completing the payment. For more information, refer to [Provide shopper information](https://docs.adyen.com/unified-commerce/pay-by-link/payment-links/api#shopper-information).  Possible values: * **billingAddress** – The address where to send the invoice. * **deliveryAddress** – The address where the purchased goods should be delivered. * **shopperEmail** – The shopper&#39;s email address. * **shopperName** – The shopper&#39;s full name. * **telephoneNumber** – The shopper&#39;s phone number.  | [optional] 
**returnUrl** | **String** | Website URL used for redirection after payment is completed. If provided, a **Continue** button will be shown on the payment page. If shoppers select the button, they are redirected to the specified URL. | [optional] 
**reusable** | **Boolean** | Indicates whether the payment link can be reused for multiple payments. If not provided, this defaults to **false** which means the link can be used for one successful payment only. | [optional] 
**riskData** | [**RiskData**](RiskData.md) | Any risk-related settings to apply to the payment. | [optional] 
**shopperEmail** | **String** | The shopper&#39;s email address. | [optional] 
**shopperLocale** | **String** | The language to be used in the payment page, specified by a combination of a language and country code. For example, &#x60;en-US&#x60;.  For a list of shopper locales that Pay by Link supports, refer to [Language and localization](https://docs.adyen.com/unified-commerce/pay-by-link/payment-links/api#language). | [optional] 
**shopperName** | [**Name**](Name.md) | The shopper&#39;s full name. This object is required for some payment methods such as AfterPay, Klarna, or if you&#39;re enrolled in the PayPal Seller Protection program. | [optional] 
**shopperReference** | **String** | Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. | [optional] 
**showRemovePaymentMethodButton** | **Boolean** | Set to **false** to hide the button that lets the shopper remove a stored payment method. | [optional] [default to true]
**splits** | [**[Split]**](Split.md) | An array of objects specifying how to split a payment when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information), [Classic Platforms integration](https://docs.adyen.com/marketplaces-and-platforms/classic/processing-payments#providing-split-information), or [Issuing](https://docs.adyen.com/issuing/manage-funds#split). | [optional] 
**status** | **String** | Status of the payment link. Possible values: * **active**: The link can be used to make payments. * **expired**: The expiry date for the payment link has passed. Shoppers can no longer use the link to make payments. * **completed**: The shopper completed the payment. | 
**store** | **String** | The physical store, for which this payment is processed. | [optional] 
**storePaymentMethod** | **Boolean** | When this is set to **true** and the &#x60;shopperReference&#x60; is provided, the payment details will be stored. | [optional] 
**themeId** | **String** | A [theme](https://docs.adyen.com/unified-commerce/pay-by-link/payment-links/api#themes) to customize the appearance of the payment page. If not specified, the payment page is rendered according to the theme set as default in your Customer Area. | [optional] 
**updatedAt** | **Date** | The date when the payment link status was updated.  [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**. | [optional] 
**url** | **String** | The URL at which the shopper can complete the payment. | [readonly] 



## Enum: RecurringProcessingModelEnum


* `CardOnFile` (value: `"CardOnFile"`)

* `Subscription` (value: `"Subscription"`)

* `UnscheduledCardOnFile` (value: `"UnscheduledCardOnFile"`)





## Enum: [RequiredShopperFieldsEnum]


* `billingAddress` (value: `"billingAddress"`)

* `deliveryAddress` (value: `"deliveryAddress"`)

* `shopperEmail` (value: `"shopperEmail"`)

* `shopperName` (value: `"shopperName"`)

* `telephoneNumber` (value: `"telephoneNumber"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `completed` (value: `"completed"`)

* `expired` (value: `"expired"`)

* `paid` (value: `"paid"`)

* `paymentPending` (value: `"paymentPending"`)




