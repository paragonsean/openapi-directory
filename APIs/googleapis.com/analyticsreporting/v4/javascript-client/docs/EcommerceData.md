# AnalyticsReportingApi.EcommerceData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionType** | **String** | Action associated with this e-commerce action. | [optional] 
**ecommerceType** | **String** | The type of this e-commerce activity. | [optional] 
**products** | [**[ProductData]**](ProductData.md) | Details of the products in this transaction. | [optional] 
**transaction** | [**TransactionData**](TransactionData.md) |  | [optional] 



## Enum: ActionTypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `CLICK` (value: `"CLICK"`)

* `DETAILS_VIEW` (value: `"DETAILS_VIEW"`)

* `ADD_TO_CART` (value: `"ADD_TO_CART"`)

* `REMOVE_FROM_CART` (value: `"REMOVE_FROM_CART"`)

* `CHECKOUT` (value: `"CHECKOUT"`)

* `PAYMENT` (value: `"PAYMENT"`)

* `REFUND` (value: `"REFUND"`)

* `CHECKOUT_OPTION` (value: `"CHECKOUT_OPTION"`)





## Enum: EcommerceTypeEnum


* `ECOMMERCE_TYPE_UNSPECIFIED` (value: `"ECOMMERCE_TYPE_UNSPECIFIED"`)

* `CLASSIC` (value: `"CLASSIC"`)

* `ENHANCED` (value: `"ENHANCED"`)




