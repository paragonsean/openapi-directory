

# PullResponse

Either a PubsubMessage or a truncation event. One of these two must be populated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ackId** | **String** | This ID must be used to acknowledge the received event or message. |  [optional] |
|**pubsubEvent** | [**PubsubEvent**](PubsubEvent.md) |  |  [optional] |



