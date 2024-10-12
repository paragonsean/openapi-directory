

# Newshipmentstatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**courier** | [**Courier**](Courier.md) |  |  |
|**cte** | **String** | Conhecimento do Transporte Eletrônico |  [optional] |
|**invoice** | [**Invoice**](Invoice.md) |  |  |
|**items** | **List&lt;String&gt;** | List of Order IDs of this items from this order that will be updated in this shipment |  |
|**number** | **String** | Unique id shipment Id in the courier system |  [optional] |
|**occurredAt** | **OffsetDateTime** | Data da ocorrência |  |
|**sellerShipmentId** | **String** | Unique Seller shipment Id. This must be unique across all orders and shipmnents |  |
|**trackingUrl** | **String** | Courier tracking URL |  [optional] |



