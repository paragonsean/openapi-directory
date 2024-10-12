

# StoredPaymentMethod


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankAccountNumber** | **String** | The bank account number (without separators). |  [optional] |
|**bankLocationId** | **String** | The location id of the bank. The field value is &#x60;nil&#x60; in most cases. |  [optional] |
|**brand** | **String** | The brand of the card. |  [optional] |
|**expiryMonth** | **String** | The month the card expires. |  [optional] |
|**expiryYear** | **String** | The last two digits of the year the card expires. For example, **22** for the year 2022. |  [optional] |
|**holderName** | **String** | The unique payment method code. |  [optional] |
|**iban** | **String** | The IBAN of the bank account. |  [optional] |
|**id** | **String** | A unique identifier of this stored payment method. |  [optional] |
|**label** | **String** | The shopper’s issuer account label |  [optional] |
|**lastFour** | **String** | The last four digits of the PAN. |  [optional] |
|**name** | **String** | The display name of the stored payment method. |  [optional] |
|**networkTxReference** | **String** | Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa.  This contains either the Mastercard Trace ID or the Visa Transaction ID. |  [optional] |
|**ownerName** | **String** | The name of the bank account holder. |  [optional] |
|**shopperEmail** | **String** | The shopper’s email address. |  [optional] |
|**supportedRecurringProcessingModels** | **List&lt;String&gt;** | The supported recurring processing models for this stored payment method. |  [optional] |
|**supportedShopperInteractions** | **List&lt;String&gt;** | The supported shopper interactions for this stored payment method. |  [optional] |
|**type** | **String** | The type of payment method. |  [optional] |



