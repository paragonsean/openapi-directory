

# OrderAddOrderItemInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**orderItemAllowRefundItemsSeparately** | **Boolean** | Indicates whether subitems of the grouped/bundle product can be refunded separately |  [optional] |
|**orderItemAllowShipItemsSeparately** | **Boolean** | Indicates whether subitems of the grouped/bundle product can be shipped separately |  [optional] |
|**orderItemId** | **String** | Defines orders specified by order item id |  |
|**orderItemModel** | **String** | Defines orders specified by order item model |  [optional] |
|**orderItemName** | **String** | Defines orders specified by order item name |  |
|**orderItemOption** | [**List&lt;OrderAddOrderItemInnerOrderItemOptionInner&gt;**](OrderAddOrderItemInnerOrderItemOptionInner.md) |  |  [optional] |
|**orderItemParent** | **Integer** | Index of the parent grouped/bundle product |  [optional] |
|**orderItemParentOptionName** | **String** | Option name of the parent grouped/bundle product |  [optional] |
|**orderItemPrice** | **BigDecimal** | Defines orders specified by order item price |  |
|**orderItemPriceIncludesTax** | **Boolean** | Defines if item price includes tax |  [optional] |
|**orderItemProperty** | [**List&lt;OrderAddOrderItemInnerOrderItemPropertyInner&gt;**](OrderAddOrderItemInnerOrderItemPropertyInner.md) |  |  [optional] |
|**orderItemQuantity** | **Integer** | Defines orders specified by order item quantity |  |
|**orderItemTax** | **BigDecimal** | Percentage of tax for product order |  [optional] |
|**orderItemVariantId** | **String** | Ordered product variant. Where x is order item ID |  [optional] |
|**orderItemWeight** | **BigDecimal** | Defines orders specified by order item weight |  [optional] |



