

# CallDataRecord


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**call** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**callType** | **String** | Type of the call. Can be one of: call, bridge, collaboration. Though exact values may change over time |  [optional] |
|**callUuid** | **String** | UUID of the call. Legs of the same call will have the same call_uuid. |  [optional] |
|**calledPerson** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Datetime of when the call was created |  [optional] |
|**direction** | **String** | Direction of the call. Can be one of: inbound, outbound |  [optional] |
|**duration** | **Integer** | Length of the call in seconds |  [optional] |
|**from** | **String** | Phone number that placed the call |  [optional] |
|**id** | **Integer** | ID of CallDataRecord |  [optional] |
|**recording** | [**EmbeddedRecordingResource**](EmbeddedRecordingResource.md) |  |  [optional] |
|**status** | **String** | The outcome of the call. Can be one of: queued, initiated, ringing, in-progress, completed, busy, no-answer, canceled, failed |  [optional] |
|**to** | **String** | Phone number that received the call |  [optional] |
|**updatedAt** | **OffsetDateTime** | Datetime of when the call was last updated |  [optional] |
|**user** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |



