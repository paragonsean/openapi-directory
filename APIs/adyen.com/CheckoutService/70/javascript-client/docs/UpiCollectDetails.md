# AdyenCheckoutApi.UpiCollectDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingSequenceNumber** | **String** | The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper. | 
**checkoutAttemptId** | **String** | The checkout attempt identifier. | [optional] 
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**shopperNotificationReference** | **String** | The &#x60;shopperNotificationReference&#x60; returned in the response when you requested to notify the shopper. Used for recurring payment only. | [optional] 
**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**type** | **String** | **upi_collect** | [default to &#39;upi_collect&#39;]
**virtualPaymentAddress** | **String** | The virtual payment address for UPI. | [optional] 



## Enum: TypeEnum


* `upi_collect` (value: `"upi_collect"`)




