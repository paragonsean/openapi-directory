

# BillbeeInterfacesBillbeeAPIModelShipment

Represents a single shipment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billbeeId** | **Long** | The billbee internal id of the shipment |  [optional] |
|**created** | **OffsetDateTime** | The creation date |  [optional] |
|**shipmentType** | **Integer** | Shipment Type, 0 if Shipment, 1 if Retoure |  [optional] |
|**shipper** | **String** | The name of the shipping provider |  [optional] |
|**shippingCarrier** | **Integer** | The carrier used to ship the parcel with |  [optional] |
|**shippingId** | **String** | The id of this shipment |  [optional] |
|**shippingProviderId** | **Long** | The id of the used shipping provider |  [optional] |
|**shippingProviderProductId** | **Long** | The id of the used shipping provider product |  [optional] |
|**trackingUrl** | **String** | The url to track this shipment |  [optional] |



