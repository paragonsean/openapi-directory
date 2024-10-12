

# ReturnPolicyOnlineReturnShippingFee

The return shipping fee. This can either be a fixed fee or a boolean to indicate that the customer pays the actual shipping cost.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fixedFee** | [**PriceAmount**](PriceAmount.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of return shipping fee. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| FIXED | &quot;FIXED&quot; |
| CUSTOMER_PAYING_ACTUAL_FEE | &quot;CUSTOMER_PAYING_ACTUAL_FEE&quot; |



