# AdyenCheckoutApi.CheckoutRedirectAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **{String: String}** | When the redirect URL must be accessed via POST, use this data to post to the redirect URL. | [optional] 
**method** | **String** | Specifies the HTTP method, for example GET or POST. | [optional] 
**paymentData** | **String** | A value that must be submitted to the &#x60;/payments/details&#x60; endpoint to verify this payment. | [optional] 
**paymentMethodType** | **String** | Specifies the payment method. | [optional] 
**type** | **String** | **redirect** | 
**url** | **String** | Specifies the URL to redirect to. | [optional] 



## Enum: TypeEnum


* `redirect` (value: `"redirect"`)




