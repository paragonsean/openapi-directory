

# CheckoutThreeDS2Action


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorisationToken** | **String** | A token needed to authorise a payment. |  [optional] |
|**paymentData** | **String** | Encoded payment data. |  [optional] |
|**paymentMethodType** | **String** | Specifies the payment method. |  [optional] |
|**subtype** | **String** | A subtype of the token. |  [optional] |
|**token** | **String** | A token to pass to the 3DS2 Component to get the fingerprint. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **threeDS2** |  |
|**url** | **String** | Specifies the URL to redirect to. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| THREE_DS2 | &quot;threeDS2&quot; |



