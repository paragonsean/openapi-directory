

# NotificationSource

One of the available set of source event payloads

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | ISO8601 timestamp indicating when the source event was created |  |
|**eventId** | **UUID** | UUID id of the source event in the Velo platform |  |
|**sourceType** | **String** | OA3 Schema type name for the source info which is used as the discriminator value to ensure that data binding works correctly |  |
|**paymentId** | **UUID** | ID of this payment within the Velo platform |  |
|**payorPaymentId** | **String** | ID of this payment in the payors system |  [optional] |
|**payoutPayorIds** | [**PayoutPayorIds**](PayoutPayorIds.md) |  |  [optional] |
|**status** | **String** | The new status of the debit. One of \&quot;PENDING\&quot; \&quot;PROCESSING\&quot; \&quot;REJECTED\&quot; \&quot;RELEASED\&quot; |  |
|**reasonCode** | **String** | The Velo code that indicates why the payment was rejected or returned |  |
|**reasonMessage** | **String** | The description of why the payment was rejected or returned |  |
|**payeeId** | **UUID** | ID of this payee within the Velo platform |  |
|**reasons** | [**List&lt;PayeeEventAllOfReasons&gt;**](PayeeEventAllOfReasons.md) | The reasons for the event notification. |  [optional] |
|**debitTransactionId** | **UUID** | ID of this debit transaction within the Velo platform |  |



