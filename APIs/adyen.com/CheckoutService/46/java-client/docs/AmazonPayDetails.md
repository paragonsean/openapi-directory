

# AmazonPayDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amazonPayToken** | **String** | This is the &#x60;amazonPayToken&#x60; that you obtained from the [Get Checkout Session](https://amazon-pay-acquirer-guide.s3-eu-west-1.amazonaws.com/v1/amazon-pay-api-v2/checkout-session.html#get-checkout-session) response. This token is used for API only integration specifically. |  [optional] |
|**checkoutSessionId** | **String** | The &#x60;checkoutSessionId&#x60; is used to identify the checkout session at the Amazon Pay side. This field is required only for drop-in and components integration, where it replaces the amazonPayToken. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **amazonpay** |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AMAZONPAY | &quot;amazonpay&quot; |



