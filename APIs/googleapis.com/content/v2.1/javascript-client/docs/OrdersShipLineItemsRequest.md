# ContentApiForShopping.OrdersShipLineItemsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lineItems** | [**[OrderShipmentLineItemShipment]**](OrderShipmentLineItemShipment.md) | Line items to ship. | [optional] 
**operationId** | **String** | The ID of the operation. Unique across all operations for a given order. | [optional] 
**shipmentGroupId** | **String** | ID of the shipment group. Required for orders that use the orderinvoices service. | [optional] 
**shipmentInfos** | [**[OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo]**](OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo.md) | Shipment information. This field is repeated because a single line item can be shipped in several packages (and have several tracking IDs). | [optional] 


