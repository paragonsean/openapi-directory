

# SeekRequest

Request for the `Seek` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**snapshot** | **String** | Optional. The snapshot to seek to. The snapshot&#39;s topic must be the same as that of the provided subscription. Format is &#x60;projects/{project}/snapshots/{snap}&#x60;. |  [optional] |
|**time** | **String** | Optional. The time to seek to. Messages retained in the subscription that were published before this time are marked as acknowledged, and messages retained in the subscription that were published after this time are marked as unacknowledged. Note that this operation affects only those messages retained in the subscription (configured by the combination of &#x60;message_retention_duration&#x60; and &#x60;retain_acked_messages&#x60;). For example, if &#x60;time&#x60; corresponds to a point before the message retention window (or to a point before the system&#39;s notion of the subscription creation time), only retained messages will be marked as unacknowledged, and already-expunged messages will not be restored. |  [optional] |



