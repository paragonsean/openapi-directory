# AdyenCheckoutApi.AfterpayDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAddress** | **String** | The address where to send the invoice. | [optional] 
**checkoutAttemptId** | **String** | The checkout attempt identifier. | [optional] 
**deliveryAddress** | **String** | The address where the goods should be delivered. | [optional] 
**personalDetails** | **String** | Shopper name, date of birth, phone number, and email address. | [optional] 
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**type** | **String** | **afterpay_default** | [default to &#39;afterpay_default&#39;]



## Enum: TypeEnum


* `afterpay_default` (value: `"afterpay_default"`)

* `afterpaytouch` (value: `"afterpaytouch"`)

* `afterpay_b2b` (value: `"afterpay_b2b"`)

* `clearpay` (value: `"clearpay"`)




