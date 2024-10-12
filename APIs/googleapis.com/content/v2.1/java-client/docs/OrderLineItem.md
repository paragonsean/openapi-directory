

# OrderLineItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustments** | [**List&lt;OrderLineItemAdjustment&gt;**](OrderLineItemAdjustment.md) | Price and tax adjustments applied on the line item. |  [optional] |
|**annotations** | [**List&lt;OrderMerchantProvidedAnnotation&gt;**](OrderMerchantProvidedAnnotation.md) | Annotations that are attached to the line item. |  [optional] |
|**cancellations** | [**List&lt;OrderCancellation&gt;**](OrderCancellation.md) | Cancellations of the line item. |  [optional] |
|**id** | **String** | The ID of the line item. |  [optional] |
|**price** | [**Price**](Price.md) |  |  [optional] |
|**product** | [**OrderLineItemProduct**](OrderLineItemProduct.md) |  |  [optional] |
|**quantityCanceled** | **Integer** | Number of items canceled. |  [optional] |
|**quantityDelivered** | **Integer** | Number of items delivered. |  [optional] |
|**quantityOrdered** | **Integer** | Number of items ordered. |  [optional] |
|**quantityPending** | **Integer** | Number of items pending. |  [optional] |
|**quantityReadyForPickup** | **Integer** | Number of items ready for pickup. |  [optional] |
|**quantityReturned** | **Integer** | Number of items returned. |  [optional] |
|**quantityShipped** | **Integer** | Number of items shipped. |  [optional] |
|**quantityUndeliverable** | **Integer** | Number of items undeliverable. |  [optional] |
|**returnInfo** | [**OrderLineItemReturnInfo**](OrderLineItemReturnInfo.md) |  |  [optional] |
|**returns** | [**List&lt;OrderReturn&gt;**](OrderReturn.md) | Returns of the line item. |  [optional] |
|**shippingDetails** | [**OrderLineItemShippingDetails**](OrderLineItemShippingDetails.md) |  |  [optional] |
|**tax** | [**Price**](Price.md) |  |  [optional] |



