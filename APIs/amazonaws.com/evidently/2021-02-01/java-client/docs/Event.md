

# Event

A structure that contains the information about one evaluation event or custom event sent to Evidently. This is a JSON payload. If this event specifies a pre-defined event type, the payload must follow the defined event schema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**String**](String.md) |  |  |
|**timestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**type** | [**EventType**](EventType.md) |  |  |



