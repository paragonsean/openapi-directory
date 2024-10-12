

# AfterpayDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | **String** | The address where to send the invoice. |  [optional] |
|**checkoutAttemptId** | **String** | The checkout attempt identifier. |  [optional] |
|**deliveryAddress** | **String** | The address where the goods should be delivered. |  [optional] |
|**personalDetails** | **String** | Shopper name, date of birth, phone number, and email address. |  [optional] |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **afterpay_default** |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AFTERPAY_DEFAULT | &quot;afterpay_default&quot; |
| AFTERPAYTOUCH | &quot;afterpaytouch&quot; |
| AFTERPAY_B2B | &quot;afterpay_b2b&quot; |
| CLEARPAY | &quot;clearpay&quot; |



