# ApiManagementClient.ProductSubscriptionsListByProducts200ResponseValueInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDate** | **Date** | Subscription creation date. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | [optional] [readonly] 
**endDate** | **Date** | Date when subscription was cancelled or expired. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | [optional] 
**expirationDate** | **Date** | Subscription expiration date. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | [optional] 
**id** | **String** | Uniquely identifies the subscription within the current API Management service instance. The value is a valid relative URL in the format of /subscriptions/{sid} where {sid} is a subscription identifier. | [optional] [readonly] 
**name** | **String** | The name of the subscription, or null if the subscription has no name. | [optional] 
**notificationDate** | **Date** | Upcoming subscription expiration notification date. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | [optional] 
**primaryKey** | **String** | Subscription primary key. | [optional] 
**productId** | **String** | The product resource identifier of the subscribed product. The value is a valid relative URL in the format of /products/{productId} where {productId} is a product identifier. | [optional] 
**secondaryKey** | **String** | Subscription secondary key. | [optional] 
**startDate** | **Date** | Subscription activation date. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | [optional] 
**state** | **String** | Subscription state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated. | [optional] 
**stateComment** | **String** | Optional subscription comment added by an administrator. | [optional] 
**userId** | **String** | The user resource identifier of the subscription owner. The value is a valid relative URL in the format of /users/{uid} where {uid} is a user identifier. | [optional] 



## Enum: StateEnum


* `Suspended` (value: `"Suspended"`)

* `Active` (value: `"Active"`)

* `Expired` (value: `"Expired"`)

* `Submitted` (value: `"Submitted"`)

* `Rejected` (value: `"Rejected"`)

* `Cancelled` (value: `"Cancelled"`)




