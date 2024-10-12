# OpenChannelMarketApi.Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**App**](App.md) |  | [optional] 
**createdDate** | **Number** | The date (in millis) of when this event occurred | 
**description** | **String** | A description of the event | [optional] 
**developer** | [**Developer**](Developer.md) |  | [optional] 
**eventId** | **String** | The id of the event | 
**eventType** | **String** | The current event type | 
**marketplaceId** | **String** | The id of the marketplace that owns this event | 
**ownership** | [**Ownership**](Ownership.md) |  | [optional] 
**review** | [**Review**](Review.md) |  | [optional] 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 



## Enum: EventTypeEnum


* `app.submitted` (value: `"app.submitted"`)

* `app.approved` (value: `"app.approved"`)

* `app.suspended` (value: `"app.suspended"`)

* `app.unsuspended` (value: `"app.unsuspended"`)

* `app.rejected` (value: `"app.rejected"`)

* `app.inReview` (value: `"app.inReview"`)

* `app.installed` (value: `"app.installed"`)

* `app.uninstalled` (value: `"app.uninstalled"`)

* `review.created` (value: `"review.created"`)

* `review.updated` (value: `"review.updated"`)

* `review.approved` (value: `"review.approved"`)

* `review.spam` (value: `"review.spam"`)

* `review.removed` (value: `"review.removed"`)

* `user.created` (value: `"user.created"`)

* `user.updated` (value: `"user.updated"`)

* `user.removed` (value: `"user.removed"`)

* `user.invalidPaymentDetails` (value: `"user.invalidPaymentDetails"`)

* `user.paymentDetailsRequired` (value: `"user.paymentDetailsRequired"`)

* `developer.created` (value: `"developer.created"`)

* `developer.updated` (value: `"developer.updated"`)

* `developer.removed` (value: `"developer.removed"`)

* `developer.paymentDetailsRequired` (value: `"developer.paymentDetailsRequired"`)

* `permission.added` (value: `"permission.added"`)

* `permission.removed` (value: `"permission.removed"`)

* `payment.complete` (value: `"payment.complete"`)

* `payment.refunded` (value: `"payment.refunded"`)

* `payment.required` (value: `"payment.required"`)

* `ownership.expired` (value: `"ownership.expired"`)




