

# CheckoutThreeDS2ChallengeAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**paymentData** | **String** | A value that must be submitted to the &#x60;/payments/details&#x60; endpoint to verify this payment. |  [optional] |
|**paymentMethodType** | **String** | Specifies the payment method. |  [optional] |
|**token** | **String** | A token to pass to the 3DS2 Component to get the challenge. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **threeDS2Challenge** |  |
|**url** | **String** | Specifies the URL to redirect to. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| THREE_DS2_CHALLENGE | &quot;threeDS2Challenge&quot; |



