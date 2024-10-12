

# SalesDataShipmentCommentInterface

Shipment comment interface. A shipment is a delivery package that contains products. A shipment document accompanies the shipment. This document lists the products and their quantities in the delivery package. A shipment document can contain comments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | Comment. |  |
|**createdAt** | **String** | Created-at timestamp. |  [optional] |
|**entityId** | **Integer** | Invoice ID. |  [optional] |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\ShipmentCommentInterface |  [optional] |
|**isCustomerNotified** | **Integer** | Is-customer-notified flag value. |  |
|**isVisibleOnFront** | **Integer** | Is-visible-on-storefront flag value. |  |
|**parentId** | **Integer** | Parent ID. |  |



