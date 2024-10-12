

# PaymentStatusChanged

Base type for all payment status changed events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | ISO8601 timestamp indicating when the source event was created |  |
|**eventId** | **UUID** | UUID id of the source event in the Velo platform |  |
|**sourceType** | **String** | OA3 Schema type name for the source info which is used as the discriminator value to ensure that data binding works correctly |  |
|**paymentId** | **UUID** | ID of this payment within the Velo platform |  |
|**payorPaymentId** | **String** | ID of this payment in the payors system |  [optional] |
|**payoutPayorIds** | [**PayoutPayorIds**](PayoutPayorIds.md) |  |  [optional] |
|**status** | **String** | The new status of the payment. One of \&quot;SUBMITTED\&quot; \&quot;ACCEPTED\&quot; \&quot;REJECTED\&quot; \&quot;ACCEPTED_BY_RAILS\&quot; \&quot;CONFIRMED\&quot; \&quot;RETURNED\&quot; \&quot;WITHDRAWN\&quot; |  |



