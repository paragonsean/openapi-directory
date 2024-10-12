# AdyenCheckoutApi.CheckoutNativeRedirectAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **{String: String}** | When the redirect URL must be accessed via POST, use this data to post to the redirect URL. | [optional] 
**method** | **String** | Specifies the HTTP method, for example GET or POST. | [optional] 
**nativeRedirectData** | **String** | Native SDK&#39;s redirect data containing the direct issuer link and state data that must be submitted to the /v1/nativeRedirect/redirectResult. | [optional] 
**paymentMethodType** | **String** | Specifies the payment method. | [optional] 
**type** | **String** | **nativeRedirect** | 
**url** | **String** | Specifies the URL to redirect to. | [optional] 



## Enum: TypeEnum


* `nativeRedirect` (value: `"nativeRedirect"`)




