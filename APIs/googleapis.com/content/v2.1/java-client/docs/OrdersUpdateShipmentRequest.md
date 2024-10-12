

# OrdersUpdateShipmentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrier** | **String** | The carrier handling the shipment. Not updated if missing. See &#x60;shipments[].carrier&#x60; in the Orders resource representation for a list of acceptable values. |  [optional] |
|**deliveryDate** | **String** | Date on which the shipment has been delivered, in ISO 8601 format. Optional and can be provided only if &#x60;status&#x60; is &#x60;delivered&#x60;. |  [optional] |
|**lastPickupDate** | **String** | Date after which the pickup will expire, in ISO 8601 format. Required only when order is buy-online-pickup-in-store(BOPIS) and &#x60;status&#x60; is &#x60;ready for pickup&#x60;. |  [optional] |
|**operationId** | **String** | The ID of the operation. Unique across all operations for a given order. |  [optional] |
|**readyPickupDate** | **String** | Date on which the shipment has been ready for pickup, in ISO 8601 format. Optional and can be provided only if &#x60;status&#x60; is &#x60;ready for pickup&#x60;. |  [optional] |
|**scheduledDeliveryDetails** | [**OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetails**](OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetails.md) |  |  [optional] |
|**shipmentId** | **String** | The ID of the shipment. |  [optional] |
|**status** | **String** | New status for the shipment. Not updated if missing. Acceptable values are: - \&quot;&#x60;delivered&#x60;\&quot; - \&quot;&#x60;undeliverable&#x60;\&quot; - \&quot;&#x60;readyForPickup&#x60;\&quot;  |  [optional] |
|**trackingId** | **String** | The tracking ID for the shipment. Not updated if missing. |  [optional] |
|**undeliveredDate** | **String** | Date on which the shipment has been undeliverable, in ISO 8601 format. Optional and can be provided only if &#x60;status&#x60; is &#x60;undeliverable&#x60;. |  [optional] |



