# BillbeeApi.RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrierId** | **Number** | Optional the id of a shipping carrier that should be assigend to the shipment  Will override the carrier from the shipment product.  Please use the integer value from this Enumeration:  {Billbee.Interfaces.Shipping.Enums.ShippingCarrier} | [optional] 
**comment** | **String** | Optional a text stored with the shipment | [optional] 
**orderId** | **String** | Optional a differing order number of the shipment if available | [optional] 
**shipmentType** | **Number** | 0 if Shipment, 1 if Retoure  {Billbee.Interfaces.Shipping.Enums.ShipmentTypeEnum} | [optional] 
**shippingId** | **String** | The id of the shipment (Sendungsnummer/trackingid) | [optional] 
**shippingProviderId** | **Number** | Optional the id of a shipping provider existing in the billbee account that should be assigned to the shipment | [optional] 
**shippingProviderProductId** | **Number** | Optional the id of a shipping provider product that should be assigend to the shipment | [optional] 


