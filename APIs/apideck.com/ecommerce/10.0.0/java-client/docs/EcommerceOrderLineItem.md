

# EcommerceOrderLineItem

A single line item of an ecommerce order, representing a product or variant with associated options, quantity, and pricing information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the product or variant associated with the line item. |  [optional] |
|**discounts** | [**List&lt;EcommerceDiscount&gt;**](EcommerceDiscount.md) |  |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**name** | **String** | The name of the product or variant associated with the line item. |  |
|**options** | [**List&lt;EcommerceOrderLineItemOptionsInner&gt;**](EcommerceOrderLineItemOptionsInner.md) |  |  [optional] |
|**productId** | **String** | A unique identifier for the product associated with the line item. |  [optional] |
|**quantity** | **String** | The quantity of the product or variant associated with the line item. |  |
|**sku** | **String** | The SKU of the product or variant associated with the line item. |  [optional] |
|**taxAmount** | **String** | The total tax amount applied to the product or variant associated with the line item. |  [optional] |
|**taxRate** | **String** | The tax rate applied to the product or variant associated with the line item. |  [optional] |
|**totalAmount** | **String** | The total amount for the product(s) or variant associated with the line item, including taxes and discounts. |  |
|**unitPrice** | **String** | The unit price of the product or variant associated with the line item. |  [optional] |
|**variantId** | **String** | A unique identifier for the variant of the product associated with the line item, if applicable. |  [optional] |



