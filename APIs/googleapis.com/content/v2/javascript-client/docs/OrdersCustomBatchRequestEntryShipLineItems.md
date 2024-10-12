# ContentApiForShopping.OrdersCustomBatchRequestEntryShipLineItems

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | **String** | Deprecated. Please use shipmentInfo instead. The carrier handling the shipment. See &#x60;shipments[].carrier&#x60; in the Orders resource representation for a list of acceptable values. | [optional] 
**lineItems** | [**[OrderShipmentLineItemShipment]**](OrderShipmentLineItemShipment.md) | Line items to ship. | [optional] 
**shipmentGroupId** | **String** | ID of the shipment group. Required for orders that use the orderinvoices service. | [optional] 
**shipmentId** | **String** | Deprecated. Please use shipmentInfo instead. The ID of the shipment. | [optional] 
**shipmentInfos** | [**[OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo]**](OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo.md) | Shipment information. This field is repeated because a single line item can be shipped in several packages (and have several tracking IDs). | [optional] 
**trackingId** | **String** | Deprecated. Please use shipmentInfo instead. The tracking ID for the shipment. | [optional] 


