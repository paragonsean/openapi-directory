# ContentApiForShopping.OrderTrackingSignal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerShippingFee** | [**PriceAmount**](PriceAmount.md) |  | [optional] 
**deliveryPostalCode** | **String** | Required. The delivery postal code, as a continuous string without spaces or dashes, e.g. \&quot;95016\&quot;. This field will be anonymized in returned OrderTrackingSignal creation response. | [optional] 
**deliveryRegionCode** | **String** | Required. The [CLDR territory code] (http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) for the shipping destination. | [optional] 
**lineItems** | [**[OrderTrackingSignalLineItemDetails]**](OrderTrackingSignalLineItemDetails.md) | Information about line items in the order. | [optional] 
**merchantId** | **String** | The Google merchant ID of this order tracking signal. This value is optional. If left unset, the caller&#39;s merchant ID is used. You must request access in order to provide data on behalf of another merchant. For more information, see [Submitting Order Tracking Signals](/shopping-content/guides/order-tracking-signals). | [optional] 
**orderCreatedTime** | **Date** |  | [optional] 
**orderId** | **String** | Required. The ID of the order on the merchant side. This field will be hashed in returned OrderTrackingSignal creation response. | [optional] 
**orderTrackingSignalId** | **String** | Output only. The ID that uniquely identifies this order tracking signal. | [optional] [readonly] 
**shipmentLineItemMapping** | [**[OrderTrackingSignalShipmentLineItemMapping]**](OrderTrackingSignalShipmentLineItemMapping.md) | The mapping of the line items to the shipment information. | [optional] 
**shippingInfo** | [**[OrderTrackingSignalShippingInfo]**](OrderTrackingSignalShippingInfo.md) | The shipping information for the order. | [optional] 


