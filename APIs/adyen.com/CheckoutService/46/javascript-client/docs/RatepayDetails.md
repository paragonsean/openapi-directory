# AdyenCheckoutApi.RatepayDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAddress** | **String** | The address where to send the invoice. | [optional] 
**deliveryAddress** | **String** | The address where the goods should be delivered. | [optional] 
**personalDetails** | **String** | Shopper name, date of birth, phone number, and email address. | [optional] 
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**type** | **String** | **ratepay** | [default to &#39;ratepay&#39;]



## Enum: TypeEnum


* `ratepay` (value: `"ratepay"`)

* `ratepay_directdebit` (value: `"ratepay_directdebit"`)




