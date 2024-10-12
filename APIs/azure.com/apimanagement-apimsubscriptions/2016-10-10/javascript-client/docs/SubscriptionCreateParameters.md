# ApiManagementClient.SubscriptionCreateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Subscription name. | 
**primaryKey** | **String** | Primary subscription key. If not specified during request key will be generated automatically. | [optional] 
**productId** | **String** | Product (product id path) for which subscription is being created in form /products/{productId} | 
**secondaryKey** | **String** | Secondary subscription key. If not specified during request key will be generated automatically. | [optional] 
**state** | **String** | Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated. | [optional] 
**userId** | **String** | User (user id path) for whom subscription is being created in form /users/{uid} | 



## Enum: StateEnum


* `Suspended` (value: `"Suspended"`)

* `Active` (value: `"Active"`)

* `Expired` (value: `"Expired"`)

* `Submitted` (value: `"Submitted"`)

* `Rejected` (value: `"Rejected"`)

* `Cancelled` (value: `"Cancelled"`)




