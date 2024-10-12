

# Marker

Represents the last read position within a user's timelines.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**home** | **Object** | Information about the user&#39;s position in the home timeline. |  [optional] |
|**lastReadId** | **String** | The ID of the most recently viewed entity. Cast from integer but not guaranteed to be a number |  [optional] |
|**notifications** | **Object** | Information about the user&#39;s position in their notifications. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The timestamp of when the marker was set. ISO 8601 Datetime. |  [optional] |
|**version** | **Integer** | Used for locking to prevent write conflicts. |  [optional] |



