

# EventGridEvent

Properties of an event published to an Event Grid topic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **Object** | Event data specific to the event type. |  |
|**dataVersion** | **String** | The schema version of the data object. |  |
|**eventTime** | **OffsetDateTime** | The time (in UTC) the event was generated. |  |
|**eventType** | **String** | The type of the event that occurred. |  |
|**id** | **String** | An unique identifier for the event. |  |
|**metadataVersion** | **String** | The schema version of the event metadata. |  [optional] [readonly] |
|**subject** | **String** | A resource path relative to the topic path. |  |
|**topic** | **String** | The resource path of the event source. |  [optional] |



