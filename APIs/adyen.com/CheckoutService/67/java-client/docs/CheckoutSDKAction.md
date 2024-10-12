

# CheckoutSDKAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**paymentData** | **String** | Encoded payment data. |  [optional] |
|**paymentMethodType** | **String** | Specifies the payment method. |  [optional] |
|**sdkData** | **Map&lt;String, String&gt;** | The data to pass to the SDK. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the action. |  |
|**url** | **String** | Specifies the URL to redirect to. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SDK | &quot;sdk&quot; |
| WECHATPAY_SDK | &quot;wechatpaySDK&quot; |



