

# PaymentDetailsResponseAction

Action to be taken for completing the payment. When returned, only the 3D Secure action is needed in most cases.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **Map&lt;String, String&gt;** | When the redirect URL must be accessed via POST, use this data to post to the redirect URL. |  [optional] |
|**method** | **String** | Specifies the HTTP method, for example GET or POST. |  [optional] |
|**paymentData** | **String** | A value that must be submitted to the &#x60;/payments/details&#x60; endpoint to verify this payment. |  [optional] |
|**paymentMethodType** | **String** | Specifies the payment method. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **redirect** |  |
|**url** | **String** | Specifies the URL to redirect to. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REDIRECT | &quot;redirect&quot; |



