

# PaymentEvent

Base type for all Payment Events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | ISO8601 timestamp indicating when the source event was created |  |
|**eventId** | **UUID** | UUID id of the source event in the Velo platform |  |
|**sourceType** | **String** | OA3 Schema type name for the source info which is used as the discriminator value to ensure that data binding works correctly |  |
|**paymentId** | **UUID** | ID of this payment within the Velo platform |  |
|**payorPaymentId** | **String** | ID of this payment in the payors system |  [optional] |
|**payoutPayorIds** | [**PayoutPayorIds**](PayoutPayorIds.md) |  |  [optional] |



