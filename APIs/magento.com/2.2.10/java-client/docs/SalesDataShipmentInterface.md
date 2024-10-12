

# SalesDataShipmentInterface

Shipment interface. A shipment is a delivery package that contains products. A shipment document accompanies the shipment. This document lists the products and their quantities in the delivery package.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddressId** | **Integer** | Billing address ID. |  [optional] |
|**comments** | [**List&lt;SalesDataShipmentCommentInterface&gt;**](SalesDataShipmentCommentInterface.md) | Array of comments. |  |
|**createdAt** | **String** | Created-at timestamp. |  [optional] |
|**customerId** | **Integer** | Customer ID. |  [optional] |
|**emailSent** | **Integer** | Email-sent flag value. |  [optional] |
|**entityId** | **Integer** | Shipment ID. |  [optional] |
|**extensionAttributes** | [**SalesDataShipmentExtensionInterface**](SalesDataShipmentExtensionInterface.md) |  |  [optional] |
|**incrementId** | **String** | Increment ID. |  [optional] |
|**items** | [**List&lt;SalesDataShipmentItemInterface&gt;**](SalesDataShipmentItemInterface.md) | Array of items. |  |
|**orderId** | **Integer** | Order ID. |  |
|**packages** | [**List&lt;SalesDataShipmentPackageInterface&gt;**](SalesDataShipmentPackageInterface.md) | Array of packages, if any. Otherwise, null. |  [optional] |
|**shipmentStatus** | **Integer** | Shipment status. |  [optional] |
|**shippingAddressId** | **Integer** | Shipping address ID. |  [optional] |
|**shippingLabel** | **String** | Shipping label. |  [optional] |
|**storeId** | **Integer** | Store ID. |  [optional] |
|**totalQty** | **BigDecimal** | Total quantity. |  [optional] |
|**totalWeight** | **BigDecimal** | Total weight. |  [optional] |
|**tracks** | [**List&lt;SalesDataShipmentTrackInterface&gt;**](SalesDataShipmentTrackInterface.md) | Array of tracks. |  |
|**updatedAt** | **String** | Updated-at timestamp. |  [optional] |



