

# SubscriptionCreateOrUpdateRequestProperties

Parameters supplied to the Create subscription operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowTracing** | **Boolean** | Determines whether tracing can be enabled |  [optional] |
|**displayName** | **String** | Subscription name. |  |
|**ownerId** | **String** | User (user id path) for whom subscription is being created in form /users/{userId} |  [optional] |
|**primaryKey** | **String** | Primary subscription key. If not specified during request key will be generated automatically. |  [optional] |
|**scope** | **String** | Scope like /products/{productId} or /apis or /apis/{apiId}. |  |
|**secondaryKey** | **String** | Secondary subscription key. If not specified during request key will be generated automatically. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| SUSPENDED | &quot;suspended&quot; |
| ACTIVE | &quot;active&quot; |
| EXPIRED | &quot;expired&quot; |
| SUBMITTED | &quot;submitted&quot; |
| REJECTED | &quot;rejected&quot; |
| CANCELLED | &quot;cancelled&quot; |



