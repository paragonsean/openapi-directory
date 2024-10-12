

# Order


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approvedAt** | **OffsetDateTime** | Date that this order was approved for fullfilment |  [optional] |
|**billingAddress** | [**Address**](Address.md) |  |  |
|**createdAt** | **OffsetDateTime** | Date that this order was created |  |
|**customer** | [**Customer**](Customer.md) |  |  |
|**freight** | [**Freight**](Freight.md) |  |  |
|**items** | [**List&lt;OrderItem&gt;**](OrderItem.md) |  |  |
|**orderId** | **String** | Unique order Id (related to this seller) |  |
|**orderMarketplaceId** | **String** | Unique Order Id that will be displayed to the customer. This Id is not the same as &#x60;orderId&#x60; |  |
|**seller** | [**Seller**](Seller.md) |  |  [optional] |
|**shipments** | [**List&lt;Shippment&gt;**](Shippment.md) |  |  |
|**shippingAddress** | [**Address**](Address.md) |  |  |
|**status** | **String** | Order status |  |
|**totalAmount** | **Integer** | Order total in cents, this is what the customer will be charged for. No commas or periods are accepeted. For example one dollar should be informed as 100. $1,2345.67 should be informed solely as 1234567 |  |
|**totalDiscountAmount** | **Integer** | Total order discounts in cents. No commas or periods are accepeted. For example one dollar should be informed as 100. $1,2345.67 should be informed solely as 1234567 |  |
|**totalItemsAmount** | **Integer** | Order items total amount in cents. No commas or periods are accepeted. For example one dollar should be informed as 100. $1,2345.67 should be informed solely as 1234567 |  |
|**totalShippingAmount** | **Integer** | Total shipments amount items. No commas or periods are accepeted. For example one dollar should be informed as 100. $1,2345.67 should be informed solely as 1234567 |  |
|**updatedAt** | **OffsetDateTime** | Last update data of this order |  |



