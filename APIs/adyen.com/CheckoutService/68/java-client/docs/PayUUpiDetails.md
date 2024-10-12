

# PayUUpiDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkoutAttemptId** | **String** | The checkout attempt identifier. |  [optional] |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**shopperNotificationReference** | **String** | The &#x60;shopperNotificationReference&#x60; returned in the response when you requested to notify the shopper. Used for recurring payment only. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **payu_IN_upi** |  |
|**virtualPaymentAddress** | **String** | The virtual payment address for UPI. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PAYU_IN_UPI | &quot;payu_IN_upi&quot; |



