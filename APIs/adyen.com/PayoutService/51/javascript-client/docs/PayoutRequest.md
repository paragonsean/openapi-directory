# AdyenPayoutApi.PayoutRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | The amount information for the transaction (in [minor units](https://docs.adyen.com/development-resources/currency-codes)). For [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) requests, set amount to 0 (zero). | 
**billingAddress** | [**Address**](Address.md) | The address where to send the invoice. &gt; The &#x60;billingAddress&#x60; object is required in the following scenarios. Include all of the fields within this object. &gt;* For 3D Secure 2 transactions in all browser-based and mobile implementations. &gt;* For cross-border payouts to and from Canada. | [optional] 
**card** | [**Card**](Card.md) | A container for card data. &gt; Either &#x60;bankAccount&#x60; or &#x60;card&#x60; field must be provided in a payment request. | [optional] 
**fraudOffset** | **Number** | An integer value that is added to the normal fraud score. The value can be either positive or negative. | [optional] 
**fundSource** | [**FundSource**](FundSource.md) | The person or entity funding the money. | [optional] 
**merchantAccount** | **String** | The merchant account identifier, with which you want to process the transaction. | 
**recurring** | [**Recurring**](Recurring.md) | The recurring settings for the payment. Use this property when you want to enable [recurring payments](https://docs.adyen.com/classic-integration/recurring-payments). | [optional] 
**reference** | **String** | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to provide multiple references for a transaction, separate them with hyphens (\&quot;-\&quot;). Maximum length: 80 characters. | 
**selectedRecurringDetailReference** | **String** | The &#x60;recurringDetailReference&#x60; you want to use for this payment. The value &#x60;LATEST&#x60; can be used to select the most recently stored recurring detail. | [optional] 
**shopperEmail** | **String** | The shopper&#39;s email address. We recommend that you provide this data, as it is used in velocity fraud checks. &gt; For 3D Secure 2 transactions, schemes require &#x60;shopperEmail&#x60; for all browser-based and mobile implementations. | [optional] 
**shopperInteraction** | **String** | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction by default.  This field has the following possible values: * &#x60;Ecommerce&#x60; - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request. * &#x60;ContAuth&#x60; - Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment). * &#x60;Moto&#x60; - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone. * &#x60;POS&#x60; - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. | [optional] 
**shopperName** | [**Name**](Name.md) | The shopper&#39;s full name. | [optional] 
**shopperReference** | **String** | Required for recurring payments.  Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. | [optional] 
**telephoneNumber** | **String** | The shopper&#39;s telephone number. | [optional] 



## Enum: ShopperInteractionEnum


* `Ecommerce` (value: `"Ecommerce"`)

* `ContAuth` (value: `"ContAuth"`)

* `Moto` (value: `"Moto"`)

* `POS` (value: `"POS"`)




