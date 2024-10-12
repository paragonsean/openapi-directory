# ContentApiForShopping.MerchantOrderReturnItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerReturnReason** | [**CustomerReturnReason**](CustomerReturnReason.md) |  | [optional] 
**itemId** | **String** | Product level item ID. If the returned items are of the same product, they will have the same ID. | [optional] 
**merchantRejectionReason** | [**MerchantRejectionReason**](MerchantRejectionReason.md) |  | [optional] 
**merchantReturnReason** | [**RefundReason**](RefundReason.md) |  | [optional] 
**product** | [**OrderLineItemProduct**](OrderLineItemProduct.md) |  | [optional] 
**refundableAmount** | [**MonetaryAmount**](MonetaryAmount.md) |  | [optional] 
**returnItemId** | **String** | Unit level ID for the return item. Different units of the same product will have different IDs. | [optional] 
**returnShipmentIds** | **[String]** | IDs of the return shipments that this return item belongs to. | [optional] 
**shipmentGroupId** | **String** | ID of the original shipment group. Provided for shipments with invoice support. | [optional] 
**shipmentUnitId** | **String** | ID of the shipment unit assigned by the merchant. Provided for shipments with invoice support. | [optional] 
**state** | **String** | State of the item. Acceptable values are: - \&quot;&#x60;canceled&#x60;\&quot; - \&quot;&#x60;new&#x60;\&quot; - \&quot;&#x60;received&#x60;\&quot; - \&quot;&#x60;refunded&#x60;\&quot; - \&quot;&#x60;rejected&#x60;\&quot;  | [optional] 


