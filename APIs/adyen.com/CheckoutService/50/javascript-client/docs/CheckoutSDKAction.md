# AdyenCheckoutApi.CheckoutSDKAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paymentData** | **String** | A value that must be submitted to the &#x60;/payments/details&#x60; endpoint to verify this payment. | [optional] 
**paymentMethodType** | **String** | Specifies the payment method. | [optional] 
**sdkData** | **{String: String}** | The data to pass to the SDK. | [optional] 
**type** | **String** | The type of the action. | 
**url** | **String** | Specifies the URL to redirect to. | [optional] 



## Enum: TypeEnum


* `sdk` (value: `"sdk"`)

* `wechatpaySDK` (value: `"wechatpaySDK"`)




