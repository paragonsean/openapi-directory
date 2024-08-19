

# RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel

Data of the shipment to be created

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrierId** | **Integer** | Optional the id of a shipping carrier that should be assigend to the shipment  Will override the carrier from the shipment product.  Please use the integer value from this Enumeration:  {Billbee.Interfaces.Shipping.Enums.ShippingCarrier} |  [optional] |
|**comment** | **String** | Optional a text stored with the shipment |  [optional] |
|**orderId** | **String** | Optional a differing order number of the shipment if available |  [optional] |
|**shipmentType** | **Integer** | 0 if Shipment, 1 if Retoure  {Billbee.Interfaces.Shipping.Enums.ShipmentTypeEnum} |  [optional] |
|**shippingId** | **String** | The id of the shipment (Sendungsnummer/trackingid) |  [optional] |
|**shippingProviderId** | **Long** | Optional the id of a shipping provider existing in the billbee account that should be assigned to the shipment |  [optional] |
|**shippingProviderProductId** | **Long** | Optional the id of a shipping provider product that should be assigend to the shipment |  [optional] |



