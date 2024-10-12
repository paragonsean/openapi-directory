

# Shippment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**courier** | [**Courier**](Courier.md) |  |  |
|**cte** | **String** | Conhecimento de Transporte Eletrônico |  [optional] |
|**description** | **String** | Additinal shipment tracking information |  [optional] |
|**id** | **String** | Shipment Id associated with this shippment used to group diferent item or items from a single order |  [optional] |
|**invoice** | [**Invoice**](Invoice.md) |  |  |
|**items** | [**List&lt;OrderItemReference&gt;**](OrderItemReference.md) | List of items of this shippment |  |
|**number** | **String** | Courier unique trackign Id associated with this shipment |  [optional] |
|**occurredAt** | **OffsetDateTime** | Date time when this shippment happened |  |
|**sellerShipmentId** | **String** | Unique Seller shipment Id. This must be unique across all orders and shipments |  |
|**status** | **String** | Shipment status |  |
|**trackingUrl** | **String** | Courier tracking URL |  [optional] |



