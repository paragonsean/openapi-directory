

# OrderShippment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**courier** | [**Courier**](Courier.md) |  |  [optional] |
|**cte** | **String** | Conhecimento de Transporte Eletôniconico |  [optional] |
|**invoice** | [**Invoice**](Invoice.md) |  |  [optional] |
|**items** | [**List&lt;OrderItemReference&gt;**](OrderItemReference.md) |  |  [optional] |
|**number** | **String** | Courier unique trackign Id associated with this shipment |  [optional] |
|**occurredAt** | **OffsetDateTime** | Date that this shippment was shiped |  [optional] |
|**order** | **String** | Order unique Id |  [optional] |
|**sellerShipmentId** | **String** | Unique Seller shipment Id. This must be unique across all orders and shipments |  [optional] |
|**status** | **String** | Shipment status. |  [optional] |
|**trackingUrl** | **String** | Courier tracking URL |  [optional] |



