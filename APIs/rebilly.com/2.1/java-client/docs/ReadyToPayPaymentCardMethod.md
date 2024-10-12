

# ReadyToPayPaymentCardMethod


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brands** | **List&lt;PaymentCardBrand&gt;** | The list of supported brands. |  [optional] |
|**feature** | [**ReadyToPayPaymentCardMethodFeature**](ReadyToPayPaymentCardMethodFeature.md) |  |  [optional] |
|**filters** | **List&lt;String&gt;** | For the method to be applicable any of the following filters should match. If no filters sent – no restrictions applied. This follows our standard filter format.  |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | The payment method. |  |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| PAYMENT_CARD | &quot;payment-card&quot; |



