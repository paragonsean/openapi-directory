

# SalesDataShipmentTrackInterface

Shipment track interface. A shipment is a delivery package that contains products. A shipment document accompanies the shipment. This document lists the products and their quantities in the delivery package. Merchants and customers can track shipments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrierCode** | **String** | Carrier code. |  |
|**createdAt** | **String** | Created-at timestamp. |  [optional] |
|**description** | **String** | Description. |  |
|**entityId** | **Integer** | Shipment package ID. |  [optional] |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\ShipmentTrackInterface |  [optional] |
|**orderId** | **Integer** | The order_id for the shipment package. |  |
|**parentId** | **Integer** | Parent ID. |  |
|**qty** | **BigDecimal** | Quantity. |  |
|**title** | **String** | Title. |  |
|**trackNumber** | **String** | Track number. |  |
|**updatedAt** | **String** | Updated-at timestamp. |  [optional] |
|**weight** | **BigDecimal** | Weight. |  |



