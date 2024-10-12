# BrandLoversMarketplaceApiV1.Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvedAt** | **Date** | Date that this order was approved for fullfilment | [optional] 
**billingAddress** | [**Address**](Address.md) |  | 
**createdAt** | **Date** | Date that this order was created | 
**customer** | [**Customer**](Customer.md) |  | 
**freight** | [**Freight**](Freight.md) |  | 
**items** | [**[OrderItem]**](OrderItem.md) |  | 
**orderId** | **String** | Unique order Id (related to this seller) | 
**orderMarketplaceId** | **String** | Unique Order Id that will be displayed to the customer. This Id is not the same as &#x60;orderId&#x60; | 
**seller** | [**Seller**](Seller.md) |  | [optional] 
**shipments** | [**[Shippment]**](Shippment.md) |  | 
**shippingAddress** | [**Address**](Address.md) |  | 
**status** | **String** | Order status | 
**totalAmount** | **Number** | Order total in cents, this is what the customer will be charged for. No commas or periods are accepeted. For example one dollar should be informed as 100. $1,2345.67 should be informed solely as 1234567 | 
**totalDiscountAmount** | **Number** | Total order discounts in cents. No commas or periods are accepeted. For example one dollar should be informed as 100. $1,2345.67 should be informed solely as 1234567 | 
**totalItemsAmount** | **Number** | Order items total amount in cents. No commas or periods are accepeted. For example one dollar should be informed as 100. $1,2345.67 should be informed solely as 1234567 | 
**totalShippingAmount** | **Number** | Total shipments amount items. No commas or periods are accepeted. For example one dollar should be informed as 100. $1,2345.67 should be informed solely as 1234567 | 
**updatedAt** | **Date** | Last update data of this order | 


