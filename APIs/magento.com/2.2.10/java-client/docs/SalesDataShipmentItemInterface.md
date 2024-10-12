

# SalesDataShipmentItemInterface

Shipment item interface. A shipment is a delivery package that contains products. A shipment document accompanies the shipment. This document lists the products and their quantities in the delivery package. A product is an item in a shipment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalData** | **String** | Additional data. |  [optional] |
|**description** | **String** | Description. |  [optional] |
|**entityId** | **Integer** | Shipment item ID. |  [optional] |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\ShipmentItemInterface |  [optional] |
|**name** | **String** | Name. |  [optional] |
|**orderItemId** | **Integer** | Order item ID. |  |
|**parentId** | **Integer** | Parent ID. |  [optional] |
|**price** | **BigDecimal** | Price. |  [optional] |
|**productId** | **Integer** | Product ID. |  [optional] |
|**qty** | **BigDecimal** | Quantity. |  |
|**rowTotal** | **BigDecimal** | Row total. |  [optional] |
|**sku** | **String** | SKU. |  [optional] |
|**weight** | **BigDecimal** | Weight. |  [optional] |



