

# PaymentMethodProperties

The properties of the payment method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currency** | **String** | The currency associated with the payment method. |  [optional] [readonly] |
|**details** | **String** | Details about the payment method. |  [optional] [readonly] |
|**expiration** | **String** | Expiration month and year. |  [optional] [readonly] |
|**paymentMethodType** | [**PaymentMethodTypeEnum**](#PaymentMethodTypeEnum) | Payment method type. |  [optional] |



## Enum: PaymentMethodTypeEnum

| Name | Value |
|---- | -----|
| CREDITS | &quot;Credits&quot; |
| CHEQUE_WIRE | &quot;ChequeWire&quot; |



