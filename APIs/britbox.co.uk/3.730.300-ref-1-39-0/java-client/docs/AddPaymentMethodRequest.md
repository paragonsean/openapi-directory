

# AddPaymentMethodRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**makeDefault** | **Boolean** | Whether this payment method should become the account default when  making purchases.  Note that if this is the first payment method of type Card being added to an account then it will become the default whether this property is true or false.  |  [optional] |
|**token** | **String** | The payment provider token representing a payment method, obtained by submitting payment method details to your third party provider.  |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of payment method. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CARD | &quot;Card&quot; |



