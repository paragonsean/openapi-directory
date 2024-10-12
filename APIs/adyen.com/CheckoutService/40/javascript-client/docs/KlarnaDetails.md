# AdyenCheckoutApi.KlarnaDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAddress** | **String** | The address where to send the invoice. | [optional] 
**deliveryAddress** | **String** | The address where the goods should be delivered. | [optional] 
**personalDetails** | **String** | Shopper name, date of birth, phone number, and email address. | [optional] 
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**subtype** | **String** | The type of flow to initiate. | [optional] 
**type** | **String** | **klarna** | [default to &#39;klarna&#39;]



## Enum: TypeEnum


* `klarna` (value: `"klarna"`)

* `klarnapayments` (value: `"klarnapayments"`)

* `klarnapayments_account` (value: `"klarnapayments_account"`)

* `klarnapayments_b2b` (value: `"klarnapayments_b2b"`)

* `klarna_paynow` (value: `"klarna_paynow"`)

* `klarna_account` (value: `"klarna_account"`)

* `klarna_b2b` (value: `"klarna_b2b"`)




