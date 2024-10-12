# ApiManagementClient.SubscriptionUpdateRequestProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowTracing** | **Boolean** | Determines whether tracing can be enabled | [optional] 
**displayName** | **String** | Subscription name. | [optional] 
**expirationDate** | **Date** | Subscription expiration date. The setting is for audit purposes only and the subscription is not automatically expired. The subscription lifecycle can be managed by using the &#x60;state&#x60; property. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard. | [optional] 
**ownerId** | **String** | User identifier path: /users/{userId} | [optional] 
**primaryKey** | **String** | Primary subscription key. | [optional] 
**scope** | **String** | Scope like /products/{productId} or /apis or /apis/{apiId} | [optional] 
**secondaryKey** | **String** | Secondary subscription key. | [optional] 
**state** | **String** | Subscription state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated. | [optional] 
**stateComment** | **String** | Comments describing subscription state change by the administrator. | [optional] 



## Enum: StateEnum


* `suspended` (value: `"suspended"`)

* `active` (value: `"active"`)

* `expired` (value: `"expired"`)

* `submitted` (value: `"submitted"`)

* `rejected` (value: `"rejected"`)

* `cancelled` (value: `"cancelled"`)




