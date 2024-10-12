

# CheckoutQrCodeAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiresAt** | **String** | Expiry time of the QR code. |  [optional] |
|**paymentData** | **String** | A value that must be submitted to the &#x60;/payments/details&#x60; endpoint to verify this payment. |  [optional] |
|**paymentMethodType** | **String** | Specifies the payment method. |  [optional] |
|**qrCodeData** | **String** | The contents of the QR code as a UTF8 string. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **qrCode** |  |
|**url** | **String** | Specifies the URL to redirect to. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| QR_CODE | &quot;qrCode&quot; |



