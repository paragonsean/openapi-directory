

# CheckoutThreeDS2FingerPrintAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**paymentData** | **String** | A value that must be submitted to the &#x60;/payments/details&#x60; endpoint to verify this payment. |  [optional] |
|**paymentMethodType** | **String** | Specifies the payment method. |  [optional] |
|**token** | **String** | A token to pass to the 3DS2 Component to get the fingerprint. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **threeDS2Fingerprint** |  |
|**url** | **String** | Specifies the URL to redirect to. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| THREE_DS2_FINGERPRINT | &quot;threeDS2Fingerprint&quot; |



