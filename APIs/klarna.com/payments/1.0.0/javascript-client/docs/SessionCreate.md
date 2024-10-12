# KlarnaPaymentsApiV1.SessionCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquiringChannel** | **String** | The acquiring channel in which the session takes place. Ecommerce is default unless specified. Any other values should be defined in the agreement. | [optional] 
**attachment** | [**Attachment**](Attachment.md) |  | [optional] 
**authorizationToken** | **String** | Authorization token. | [optional] [readonly] 
**billingAddress** | [**Address**](Address.md) |  | [optional] 
**clientToken** | **String** | Token to be passed to the JS client | [optional] [readonly] 
**customPaymentMethodIds** | **[String]** | Promo codes - The array could be used to define which of the configured payment options within a payment category (pay_later, pay_over_time, etc.) should be shown for this purchase. Discuss with the delivery manager to know about the promo codes that will be configured for your account. The feature could also be used to provide promotional offers to specific customers (eg: 0% financing). Please be informed that the usage of this feature can have commercial implications.  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**design** | **String** | Design package to use in the session. This can only by used if a custom design has been implemented for Klarna Payments and agreed upon in the agreement. It might have a financial impact. Delivery manager will provide the value for the parameter. | [optional] 
**expiresAt** | **Date** | Session expiration date | [optional] [readonly] 
**intent** | **String** | Intent for the session. The field is designed to let partners inform Klarna of the purpose of the customer’s session. | [optional] 
**locale** | **String** | Used to define the language and region of the customer. The locale follows the format of (RFC 1766)[https://datatracker.ietf.org/doc/rfc1766/], meaning its value consists of language-country. The following values are applicable:  AT: \&quot;de-AT\&quot;, \&quot;de-DE\&quot;, \&quot;en-DE\&quot; BE: \&quot;be-BE\&quot;, \&quot;nl-BE\&quot;, \&quot;fr-BE\&quot;, \&quot;en-BE\&quot; CH: \&quot;it-CH\&quot;, \&quot;de-CH\&quot;, \&quot;fr-CH\&quot;, \&quot;en-CH\&quot; DE: \&quot;de-DE\&quot;, \&quot;de-AT\&quot;, \&quot;en-DE\&quot; DK: \&quot;da-DK\&quot;, \&quot;en-DK\&quot; ES: \&quot;es-ES\&quot;, \&quot;ca-ES\&quot;, \&quot;en-ES\&quot; FI: \&quot;fi-FI\&quot;, \&quot;sv-FI\&quot;, \&quot;en-FI\&quot; GB: \&quot;en-GB\&quot; IT: \&quot;it-IT\&quot;, \&quot;en-IT\&quot; NL: \&quot;nl-NL\&quot;, \&quot;en-NL\&quot; NO: \&quot;nb-NO\&quot;, \&quot;en-NO\&quot; PL: \&quot;pl-PL\&quot;, \&quot;en-PL\&quot; SE: \&quot;sv-SE\&quot;, \&quot;en-SE\&quot; US: \&quot;en-US\&quot;. Default value is \&quot;en-US\&quot;. | [optional] 
**merchantData** | **String** | Pass through field to send any information about the order to be used later for reference while retrieving the order details (max 6000 characters) | [optional] 
**merchantReference1** | **String** | Used for storing merchant&#39;s internal order number or other reference. | [optional] 
**merchantReference2** | **String** | Used for storing merchant&#39;s internal order number or other reference. The value is available in the settlement files. (max 255 characters). | [optional] 
**merchantUrls** | [**MerchantUrls**](MerchantUrls.md) |  | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 
**orderAmount** | **Number** | Total amount of the order including tax and any available discounts. The value should be in non-negative minor units. Eg: 25 Euros should be 2500. | 
**orderLines** | [**[OrderLine]**](OrderLine.md) | The array containing list of line items that are part of this order. Maximum of 1000 line items could be processed in a single order. | 
**orderTaxAmount** | **Number** | Total tax amount of the order. The value should be in non-negative minor units. Eg: 25 Euros should be 2500. | [optional] 
**paymentMethodCategories** | [**[PaymentMethodCategory]**](PaymentMethodCategory.md) | Available payment method categories | [optional] [readonly] 
**purchaseCountry** | **String** | The purchase country of the customer. The billing country always overrides purchase country if the values are different. Formatted according to ISO 3166 alpha-2 standard, e.g. GB, SE, DE, US, etc. | 
**purchaseCurrency** | **String** | The purchase currency of the order. Formatted according to ISO 4217 standard, e.g. USD, EUR, SEK, GBP, etc. | 
**shippingAddress** | [**Address**](Address.md) |  | [optional] 
**status** | **String** | The current status of the session. Possible values: &#39;complete&#39;, &#39;incomplete&#39; where &#39;complete&#39; is set when the order has been placed. | [optional] [readonly] 



## Enum: AcquiringChannelEnum


* `ECOMMERCE` (value: `"ECOMMERCE"`)

* `IN_STORE` (value: `"IN_STORE"`)

* `TELESALES` (value: `"TELESALES"`)





## Enum: IntentEnum


* `buy` (value: `"buy"`)

* `tokenize` (value: `"tokenize"`)

* `buy_and_tokenize` (value: `"buy_and_tokenize"`)





## Enum: StatusEnum


* `complete` (value: `"complete"`)

* `incomplete` (value: `"incomplete"`)




