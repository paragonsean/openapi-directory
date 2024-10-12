

# CostEstimateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | The transaction amount used as a base for the cost estimation. |  |
|**assumptions** | [**CostEstimateAssumptions**](CostEstimateAssumptions.md) | Assumptions made for the expected characteristics of the transaction, for which the charges are being estimated. |  [optional] |
|**cardNumber** | **String** | The card number (4-19 characters) for PCI compliant use cases. Do not use any separators.  &gt; Either the &#x60;cardNumber&#x60; or &#x60;encryptedCardNumber&#x60; field must be provided in a payment request. |  [optional] |
|**encryptedCardNumber** | **String** | Encrypted data that stores card information for non PCI-compliant use cases. The encrypted data must be created with the Checkout Card Component or Secured Fields Component, and must contain the &#x60;encryptedCardNumber&#x60; field.  &gt; Either the &#x60;cardNumber&#x60; or &#x60;encryptedCardNumber&#x60; field must be provided in a payment request. |  [optional] |
|**merchantAccount** | **String** | The merchant account identifier you want to process the (transaction) request with. |  |
|**merchantDetails** | [**MerchantDetails**](MerchantDetails.md) | Additional data for merchants who don&#39;t use Adyen as the payment authorisation gateway. |  [optional] |
|**recurring** | [**Recurring**](Recurring.md) | The recurring settings for the payment. Use this property when you want to enable [recurring payments](https://docs.adyen.com/online-payments/tokenization). |  [optional] |
|**selectedRecurringDetailReference** | **String** | The &#x60;recurringDetailReference&#x60; you want to use for this cost estimate. The value &#x60;LATEST&#x60; can be used to select the most recently stored recurring detail. |  [optional] |
|**shopperInteraction** | [**ShopperInteractionEnum**](#ShopperInteractionEnum) | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction by default.  This field has the following possible values: * &#x60;Ecommerce&#x60; - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request. * &#x60;ContAuth&#x60; - Card on file and/or subscription transactions, where the card holder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment). * &#x60;Moto&#x60; - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone. * &#x60;POS&#x60; - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. |  [optional] |
|**shopperReference** | **String** | Required for recurring payments.  Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. |  [optional] |



## Enum: ShopperInteractionEnum

| Name | Value |
|---- | -----|
| ECOMMERCE | &quot;Ecommerce&quot; |
| CONT_AUTH | &quot;ContAuth&quot; |
| MOTO | &quot;Moto&quot; |
| POS | &quot;POS&quot; |



