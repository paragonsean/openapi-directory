

# PaymentProperties

The properties of the payment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) |  |  [optional] |
|**date** | **OffsetDateTime** | The date of the payment. |  [optional] [readonly] |
|**paymentMethodFamily** | [**PaymentMethodFamilyEnum**](#PaymentMethodFamilyEnum) | The payment method family. |  [optional] |
|**paymentMethodType** | **String** | The type of payment method. |  [optional] [readonly] |
|**paymentType** | **String** | The type of payment. |  [optional] [readonly] |



## Enum: PaymentMethodFamilyEnum

| Name | Value |
|---- | -----|
| CREDITS | &quot;Credits&quot; |
| CHECK_WIRE | &quot;CheckWire&quot; |
| CREDIT_CARD | &quot;CreditCard&quot; |
| NONE | &quot;None&quot; |



