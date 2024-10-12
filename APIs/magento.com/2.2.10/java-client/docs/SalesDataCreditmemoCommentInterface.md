

# SalesDataCreditmemoCommentInterface

Credit memo comment interface. After a customer places and pays for an order and an invoice has been issued, the merchant can create a credit memo to refund all or part of the amount paid for any returned or undelivered items. The memo restores funds to the customer account so that the customer can make future purchases. A credit memo usually includes comments that detail why the credit memo amount was credited to the customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | Comment. |  |
|**createdAt** | **String** | Created-at timestamp. |  [optional] |
|**entityId** | **Integer** | Credit memo ID. |  [optional] |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\CreditmemoCommentInterface |  [optional] |
|**isCustomerNotified** | **Integer** | Is-customer-notified flag value. |  |
|**isVisibleOnFront** | **Integer** | Is-visible-on-storefront flag value. |  |
|**parentId** | **Integer** | Parent ID. |  |



