# AdyenCheckoutApi.PayUUpiDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**shopperNotificationReference** | **String** | The &#x60;shopperNotificationReference&#x60; returned in the response when you requested to notify the shopper. Used for recurring payment only. | [optional] 
**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**type** | **String** | **payu_IN_upi** | [default to &#39;payu_IN_upi&#39;]
**virtualPaymentAddress** | **String** | The virtual payment address for UPI. | [optional] 



## Enum: TypeEnum


* `payu_IN_upi` (value: `"payu_IN_upi"`)




