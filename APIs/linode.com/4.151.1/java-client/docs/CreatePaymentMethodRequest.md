

# CreatePaymentMethodRequest

Payment Method Request Object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**CreditCard**](CreditCard.md) |  |  |
|**isDefault** | **Boolean** | Whether this Payment Method is the default method for automatically processing service charges.  |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of Payment Method.  Alternative Payment Methods including Google Pay and PayPal can be added using the Cloud Manager. See the [Manage Payment Methods](/docs/products/platform/billing/guides/payment-methods/) guide for details and instructions.  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CREDIT_CARD | &quot;credit_card&quot; |



