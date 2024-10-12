

# CheckoutAwaitAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**paymentData** | **String** | A value that must be submitted to the &#x60;/payments/details&#x60; endpoint to verify this payment. |  [optional] |
|**paymentMethodType** | **String** | Specifies the payment method. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **await** |  |
|**url** | **String** | Specifies the URL to redirect to. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AWAIT | &quot;await&quot; |



