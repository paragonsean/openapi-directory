

# SubscriptionUpdateParameters

Parameters supplied to the Update subscription operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expirationDate** | **OffsetDateTime** | New subscription expiration date. |  [optional] |
|**name** | **String** | Subscription name. |  [optional] |
|**primaryKey** | **String** | Primary subscription key. |  [optional] |
|**productId** | **String** | Product identifier path: /products/{productId} |  [optional] |
|**secondaryKey** | **String** | Secondary subscription key. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Subscription state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated. |  [optional] |
|**stateComment** | **String** | Comments describing subscription state change by the administrator. |  [optional] |
|**userId** | **String** | User identifier path: /users/{uid} |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| SUSPENDED | &quot;Suspended&quot; |
| ACTIVE | &quot;Active&quot; |
| EXPIRED | &quot;Expired&quot; |
| SUBMITTED | &quot;Submitted&quot; |
| REJECTED | &quot;Rejected&quot; |
| CANCELLED | &quot;Cancelled&quot; |



