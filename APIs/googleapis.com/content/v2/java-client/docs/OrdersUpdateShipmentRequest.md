

# OrdersUpdateShipmentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrier** | **String** | The carrier handling the shipment. Not updated if missing. See &#x60;shipments[].carrier&#x60; in the Orders resource representation for a list of acceptable values. |  [optional] |
|**deliveryDate** | **String** | Date on which the shipment has been delivered, in ISO 8601 format. Optional and can be provided only if &#x60;status&#x60; is &#x60;delivered&#x60;. |  [optional] |
|**operationId** | **String** | The ID of the operation. Unique across all operations for a given order. |  [optional] |
|**shipmentId** | **String** | The ID of the shipment. |  [optional] |
|**status** | **String** | New status for the shipment. Not updated if missing. Acceptable values are: - \&quot;&#x60;delivered&#x60;\&quot; - \&quot;&#x60;undeliverable&#x60;\&quot; - \&quot;&#x60;readyForPickup&#x60;\&quot;  |  [optional] |
|**trackingId** | **String** | The tracking ID for the shipment. Not updated if missing. |  [optional] |



