

# CatalogInventoryDataStockItemInterface

Interface StockItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backorders** | **Integer** | Backorders status |  |
|**enableQtyIncrements** | **Boolean** | Whether Quantity Increments is enabled |  |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\CatalogInventory\\Api\\Data\\StockItemInterface |  [optional] |
|**isDecimalDivided** | **Boolean** |  |  |
|**isInStock** | **Boolean** | Stock Availability |  |
|**isQtyDecimal** | **Boolean** |  |  |
|**itemId** | **Integer** |  |  [optional] |
|**lowStockDate** | **String** |  |  |
|**manageStock** | **Boolean** | Can Manage Stock |  |
|**maxSaleQty** | **BigDecimal** | Maximum Qty Allowed in Shopping Cart data wrapper |  |
|**minQty** | **BigDecimal** | Minimal quantity available for item status in stock |  |
|**minSaleQty** | **BigDecimal** | Minimum Qty Allowed in Shopping Cart or NULL when there is no limitation |  |
|**notifyStockQty** | **BigDecimal** | Notify for Quantity Below data wrapper |  |
|**productId** | **Integer** |  |  [optional] |
|**qty** | **BigDecimal** |  |  |
|**qtyIncrements** | **BigDecimal** | Quantity Increments data wrapper |  |
|**showDefaultNotificationMessage** | **Boolean** |  |  |
|**stockId** | **Integer** | Stock identifier |  [optional] |
|**stockStatusChangedAuto** | **Integer** |  |  |
|**useConfigBackorders** | **Boolean** |  |  |
|**useConfigEnableQtyInc** | **Boolean** |  |  |
|**useConfigManageStock** | **Boolean** |  |  |
|**useConfigMaxSaleQty** | **Boolean** |  |  |
|**useConfigMinQty** | **Boolean** |  |  |
|**useConfigMinSaleQty** | **Integer** |  |  |
|**useConfigNotifyStockQty** | **Boolean** |  |  |
|**useConfigQtyIncrements** | **Boolean** |  |  |



