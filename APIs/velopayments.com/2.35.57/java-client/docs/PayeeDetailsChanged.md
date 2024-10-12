

# PayeeDetailsChanged

Base type for all payee details changed events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | ISO8601 timestamp indicating when the source event was created |  |
|**eventId** | **UUID** | UUID id of the source event in the Velo platform |  |
|**sourceType** | **String** | OA3 Schema type name for the source info which is used as the discriminator value to ensure that data binding works correctly |  |
|**payeeId** | **UUID** | ID of this payee within the Velo platform |  |
|**reasons** | [**List&lt;PayeeEventAllOfReasons&gt;**](PayeeEventAllOfReasons.md) | The reasons for the event notification. |  [optional] |



