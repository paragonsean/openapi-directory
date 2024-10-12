# CommerceApi.OrderLineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | A unique, persistent identifier for this record | 
**discountAllocations** | [**[OrderDiscountAllocation]**](OrderDiscountAllocation.md) |  | [optional] 
**productRef** | [**ProductRef**](ProductRef.md) |  | [optional] 
**productVariantRef** | [**ProductVariantRef**](ProductVariantRef.md) |  | [optional] 
**quantity** | **String** | Number of units of the product sold. For refunds, quantity is a negative value.  | [optional] 
**taxPercentage** | **String** | Percentage rate (from 0 to 100) of any sale tax applied to the unit amount. | [optional] 
**taxes** | [**[TaxComponentAllocation]**](TaxComponentAllocation.md) | Taxes breakdown as applied to order lines. | [optional] 
**totalAmount** | **String** | Total price of the line item, including discounts, tax and minus any refunds. | [optional] 
**totalTaxAmount** | **String** | Total amount of tax applied to the line item. | [optional] 
**unitPrice** | **String** | Price per unit of goods or service. | [optional] 


