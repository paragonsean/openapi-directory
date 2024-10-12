

# PubsubMessage

A message data and its labels.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **byte[]** | The message payload. |  [optional] |
|**label** | [**List&lt;Label&gt;**](Label.md) | Optional list of labels for this message. Keys in this collection must be unique. |  [optional] |
|**messageId** | **String** | ID of this message assigned by the server at publication time. Guaranteed to be unique within the topic. This value may be read by a subscriber that receives a PubsubMessage via a Pull call or a push delivery. It must not be populated by a publisher in a Publish call. |  [optional] |
|**publishTime** | **String** | The time at which the message was published. The time is milliseconds since the UNIX epoch. |  [optional] |



