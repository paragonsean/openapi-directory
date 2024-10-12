

# StoredValueIssueRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | The amount information for the transaction. |  [optional] |
|**merchantAccount** | **String** | The merchant account identifier, with which you want to process the transaction. |  |
|**paymentMethod** | **Map&lt;String, String&gt;** | The collection that contains the type of the payment method and its specific information if available |  |
|**recurringDetailReference** | **String** |  |  [optional] |
|**reference** | **String** | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to provide multiple references for a transaction, separate them with hyphens (\&quot;-\&quot;). Maximum length: 80 characters. |  |
|**shopperInteraction** | [**ShopperInteractionEnum**](#ShopperInteractionEnum) | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction by default.  This field has the following possible values: * &#x60;Ecommerce&#x60; - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request. * &#x60;ContAuth&#x60; - Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment). * &#x60;Moto&#x60; - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone. * &#x60;POS&#x60; - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. |  [optional] |
|**shopperReference** | **String** |  |  [optional] |
|**store** | **String** | The physical store, for which this payment is processed. |  [optional] |



## Enum: ShopperInteractionEnum

| Name | Value |
|---- | -----|
| ECOMMERCE | &quot;Ecommerce&quot; |
| CONT_AUTH | &quot;ContAuth&quot; |
| MOTO | &quot;Moto&quot; |
| POS | &quot;POS&quot; |



