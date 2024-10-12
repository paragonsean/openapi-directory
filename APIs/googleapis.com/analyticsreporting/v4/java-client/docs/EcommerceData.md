

# EcommerceData

E-commerce details associated with the user activity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionType** | [**ActionTypeEnum**](#ActionTypeEnum) | Action associated with this e-commerce action. |  [optional] |
|**ecommerceType** | [**EcommerceTypeEnum**](#EcommerceTypeEnum) | The type of this e-commerce activity. |  [optional] |
|**products** | [**List&lt;ProductData&gt;**](ProductData.md) | Details of the products in this transaction. |  [optional] |
|**transaction** | [**TransactionData**](TransactionData.md) |  |  [optional] |



## Enum: ActionTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| CLICK | &quot;CLICK&quot; |
| DETAILS_VIEW | &quot;DETAILS_VIEW&quot; |
| ADD_TO_CART | &quot;ADD_TO_CART&quot; |
| REMOVE_FROM_CART | &quot;REMOVE_FROM_CART&quot; |
| CHECKOUT | &quot;CHECKOUT&quot; |
| PAYMENT | &quot;PAYMENT&quot; |
| REFUND | &quot;REFUND&quot; |
| CHECKOUT_OPTION | &quot;CHECKOUT_OPTION&quot; |



## Enum: EcommerceTypeEnum

| Name | Value |
|---- | -----|
| ECOMMERCE_TYPE_UNSPECIFIED | &quot;ECOMMERCE_TYPE_UNSPECIFIED&quot; |
| CLASSIC | &quot;CLASSIC&quot; |
| ENHANCED | &quot;ENHANCED&quot; |



