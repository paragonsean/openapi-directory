# ContentApiForShopping.OrderLineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustments** | [**[OrderLineItemAdjustment]**](OrderLineItemAdjustment.md) | Price and tax adjustments applied on the line item. | [optional] 
**annotations** | [**[OrderMerchantProvidedAnnotation]**](OrderMerchantProvidedAnnotation.md) | Annotations that are attached to the line item. | [optional] 
**cancellations** | [**[OrderCancellation]**](OrderCancellation.md) | Cancellations of the line item. | [optional] 
**id** | **String** | The ID of the line item. | [optional] 
**price** | [**Price**](Price.md) |  | [optional] 
**product** | [**OrderLineItemProduct**](OrderLineItemProduct.md) |  | [optional] 
**quantityCanceled** | **Number** | Number of items canceled. | [optional] 
**quantityDelivered** | **Number** | Number of items delivered. | [optional] 
**quantityOrdered** | **Number** | Number of items ordered. | [optional] 
**quantityPending** | **Number** | Number of items pending. | [optional] 
**quantityReadyForPickup** | **Number** | Number of items ready for pickup. | [optional] 
**quantityReturned** | **Number** | Number of items returned. | [optional] 
**quantityShipped** | **Number** | Number of items shipped. | [optional] 
**quantityUndeliverable** | **Number** | Number of items undeliverable. | [optional] 
**returnInfo** | [**OrderLineItemReturnInfo**](OrderLineItemReturnInfo.md) |  | [optional] 
**returns** | [**[OrderReturn]**](OrderReturn.md) | Returns of the line item. | [optional] 
**shippingDetails** | [**OrderLineItemShippingDetails**](OrderLineItemShippingDetails.md) |  | [optional] 
**tax** | [**Price**](Price.md) |  | [optional] 


