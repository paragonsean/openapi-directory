

# ProductSubscriptionsList200ResponseValueInnerProperties

Subscription details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowTracing** | **Boolean** | Determines whether tracing is enabled |  [optional] |
|**createdDate** | **OffsetDateTime** | Subscription creation date. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  [optional] [readonly] |
|**displayName** | **String** | The name of the subscription, or null if the subscription has no name. |  [optional] |
|**endDate** | **OffsetDateTime** | Date when subscription was cancelled or expired. The setting is for audit purposes only and the subscription is not automatically cancelled. The subscription lifecycle can be managed by using the &#x60;state&#x60; property. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  [optional] |
|**expirationDate** | **OffsetDateTime** | Subscription expiration date. The setting is for audit purposes only and the subscription is not automatically expired. The subscription lifecycle can be managed by using the &#x60;state&#x60; property. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  [optional] |
|**notificationDate** | **OffsetDateTime** | Upcoming subscription expiration notification date. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  [optional] |
|**ownerId** | **String** | The user resource identifier of the subscription owner. The value is a valid relative URL in the format of /users/{userId} where {userId} is a user identifier. |  [optional] |
|**primaryKey** | **String** | Subscription primary key. |  |
|**scope** | **String** | Scope like /products/{productId} or /apis or /apis/{apiId}. |  |
|**secondaryKey** | **String** | Subscription secondary key. |  |
|**startDate** | **OffsetDateTime** | Subscription activation date. The setting is for audit purposes only and the subscription is not automatically activated. The subscription lifecycle can be managed by using the &#x60;state&#x60; property. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Subscription state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated. |  |
|**stateComment** | **String** | Optional subscription comment added by an administrator. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| SUSPENDED | &quot;suspended&quot; |
| ACTIVE | &quot;active&quot; |
| EXPIRED | &quot;expired&quot; |
| SUBMITTED | &quot;submitted&quot; |
| REJECTED | &quot;rejected&quot; |
| CANCELLED | &quot;cancelled&quot; |



