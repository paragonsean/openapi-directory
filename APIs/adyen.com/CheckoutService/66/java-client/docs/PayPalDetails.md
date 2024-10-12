

# PayPalDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**orderID** | **String** | The unique ID associated with the order. |  [optional] |
|**payeePreferred** | **String** | IMMEDIATE_PAYMENT_REQUIRED or UNRESTRICTED |  [optional] |
|**payerID** | **String** | The unique ID associated with the payer. |  [optional] |
|**payerSelected** | **String** | PAYPAL or PAYPAL_CREDIT |  [optional] |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**subtype** | [**SubtypeEnum**](#SubtypeEnum) | The type of flow to initiate. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **paypal** |  |



## Enum: SubtypeEnum

| Name | Value |
|---- | -----|
| REDIRECT | &quot;redirect&quot; |
| SDK | &quot;sdk&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PAYPAL | &quot;paypal&quot; |



