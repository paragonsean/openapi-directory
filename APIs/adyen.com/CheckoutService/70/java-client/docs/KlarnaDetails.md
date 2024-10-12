

# KlarnaDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | **String** | The address where to send the invoice. |  [optional] |
|**checkoutAttemptId** | **String** | The checkout attempt identifier. |  [optional] |
|**deliveryAddress** | **String** | The address where the goods should be delivered. |  [optional] |
|**personalDetails** | **String** | Shopper name, date of birth, phone number, and email address. |  [optional] |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**subtype** | **String** | The type of flow to initiate. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **klarna** |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| KLARNA | &quot;klarna&quot; |
| KLARNAPAYMENTS | &quot;klarnapayments&quot; |
| KLARNAPAYMENTS_ACCOUNT | &quot;klarnapayments_account&quot; |
| KLARNAPAYMENTS_B2B | &quot;klarnapayments_b2b&quot; |
| KLARNA_PAYNOW | &quot;klarna_paynow&quot; |
| KLARNA_ACCOUNT | &quot;klarna_account&quot; |
| KLARNA_B2B | &quot;klarna_b2b&quot; |



