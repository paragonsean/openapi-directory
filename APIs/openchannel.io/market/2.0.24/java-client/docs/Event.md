

# Event



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**app** | [**App**](App.md) |  |  [optional] |
|**createdDate** | **Long** | The date (in millis) of when this event occurred |  |
|**description** | **String** | A description of the event |  [optional] |
|**developer** | [**Developer**](Developer.md) |  |  [optional] |
|**eventId** | **String** | The id of the event |  |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | The current event type |  |
|**marketplaceId** | **String** | The id of the marketplace that owns this event |  |
|**ownership** | [**Ownership**](Ownership.md) |  |  [optional] |
|**review** | [**Review**](Review.md) |  |  [optional] |
|**transaction** | [**Transaction**](Transaction.md) |  |  [optional] |
|**user** | [**User**](User.md) |  |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| APP_SUBMITTED | &quot;app.submitted&quot; |
| APP_APPROVED | &quot;app.approved&quot; |
| APP_SUSPENDED | &quot;app.suspended&quot; |
| APP_UNSUSPENDED | &quot;app.unsuspended&quot; |
| APP_REJECTED | &quot;app.rejected&quot; |
| APP_IN_REVIEW | &quot;app.inReview&quot; |
| APP_INSTALLED | &quot;app.installed&quot; |
| APP_UNINSTALLED | &quot;app.uninstalled&quot; |
| REVIEW_CREATED | &quot;review.created&quot; |
| REVIEW_UPDATED | &quot;review.updated&quot; |
| REVIEW_APPROVED | &quot;review.approved&quot; |
| REVIEW_SPAM | &quot;review.spam&quot; |
| REVIEW_REMOVED | &quot;review.removed&quot; |
| USER_CREATED | &quot;user.created&quot; |
| USER_UPDATED | &quot;user.updated&quot; |
| USER_REMOVED | &quot;user.removed&quot; |
| USER_INVALID_PAYMENT_DETAILS | &quot;user.invalidPaymentDetails&quot; |
| USER_PAYMENT_DETAILS_REQUIRED | &quot;user.paymentDetailsRequired&quot; |
| DEVELOPER_CREATED | &quot;developer.created&quot; |
| DEVELOPER_UPDATED | &quot;developer.updated&quot; |
| DEVELOPER_REMOVED | &quot;developer.removed&quot; |
| DEVELOPER_PAYMENT_DETAILS_REQUIRED | &quot;developer.paymentDetailsRequired&quot; |
| PERMISSION_ADDED | &quot;permission.added&quot; |
| PERMISSION_REMOVED | &quot;permission.removed&quot; |
| PAYMENT_COMPLETE | &quot;payment.complete&quot; |
| PAYMENT_REFUNDED | &quot;payment.refunded&quot; |
| PAYMENT_REQUIRED | &quot;payment.required&quot; |
| OWNERSHIP_EXPIRED | &quot;ownership.expired&quot; |



