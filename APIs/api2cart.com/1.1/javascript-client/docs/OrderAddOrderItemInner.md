# SwaggerApi2Cart.OrderAddOrderItemInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orderItemAllowRefundItemsSeparately** | **Boolean** | Indicates whether subitems of the grouped/bundle product can be refunded separately | [optional] 
**orderItemAllowShipItemsSeparately** | **Boolean** | Indicates whether subitems of the grouped/bundle product can be shipped separately | [optional] 
**orderItemId** | **String** | Defines orders specified by order item id | 
**orderItemModel** | **String** | Defines orders specified by order item model | [optional] 
**orderItemName** | **String** | Defines orders specified by order item name | 
**orderItemOption** | [**[OrderAddOrderItemInnerOrderItemOptionInner]**](OrderAddOrderItemInnerOrderItemOptionInner.md) |  | [optional] 
**orderItemParent** | **Number** | Index of the parent grouped/bundle product | [optional] 
**orderItemParentOptionName** | **String** | Option name of the parent grouped/bundle product | [optional] 
**orderItemPrice** | **Number** | Defines orders specified by order item price | 
**orderItemPriceIncludesTax** | **Boolean** | Defines if item price includes tax | [optional] [default to false]
**orderItemProperty** | [**[OrderAddOrderItemInnerOrderItemPropertyInner]**](OrderAddOrderItemInnerOrderItemPropertyInner.md) |  | [optional] 
**orderItemQuantity** | **Number** | Defines orders specified by order item quantity | 
**orderItemTax** | **Number** | Percentage of tax for product order | [optional] [default to 0]
**orderItemVariantId** | **String** | Ordered product variant. Where x is order item ID | [optional] 
**orderItemWeight** | **Number** | Defines orders specified by order item weight | [optional] 


