

# PaymentMethod

Payment Method Response Object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | When the Payment Method was added to the Account. |  [optional] [readonly] |
|**data** | [**PaymentMethodData**](PaymentMethodData.md) |  |  [optional] |
|**id** | **Integer** | The unique ID of this Payment Method. |  [optional] |
|**isDefault** | **Boolean** | Whether this Payment Method is the default method for automatically processing service charges.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of Payment Method. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CREDIT_CARD | &quot;credit_card&quot; |
| GOOGLE_PAY | &quot;google_pay&quot; |
| PAYPAL | &quot;paypal&quot; |



