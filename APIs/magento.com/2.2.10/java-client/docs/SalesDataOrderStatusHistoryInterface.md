

# SalesDataOrderStatusHistoryInterface

Order status history interface. An order is a document that a web store issues to a customer. Magento generates a sales order that lists the product items, billing and shipping addresses, and shipping and payment methods. A corresponding external document, known as a purchase order, is emailed to the customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | Comment. |  |
|**createdAt** | **String** | Created-at timestamp. |  [optional] |
|**entityId** | **Integer** | Order status history ID. |  [optional] |
|**entityName** | **String** | Entity name. |  [optional] |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\OrderStatusHistoryInterface |  [optional] |
|**isCustomerNotified** | **Integer** | Is-customer-notified flag value. |  |
|**isVisibleOnFront** | **Integer** | Is-visible-on-storefront flag value. |  |
|**parentId** | **Integer** | Parent ID. |  |
|**status** | **String** | Status. |  [optional] |



