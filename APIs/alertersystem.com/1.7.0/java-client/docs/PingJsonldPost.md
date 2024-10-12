

# PingJsonldPost

The Ping resource is a collection of pings that have been sent to monitors in the user account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expectNextPingAt** | **OffsetDateTime** | When to expect the next ping for a Last Ping monitor type. This date-time is always interpreted to be in the timezone of the monitor. Any UTC offset is ignored. Supply either \&quot;expectNextPingAt\&quot;, or \&quot;expectNextPingAtEpoch\&quot;, or a X_NEXT_PING request header, not more than one of those options. Must be blank for other monitor types. |  [optional] |
|**expectNextPingAtEpoch** | **Integer** | When to expect the next ping for a Last Ping monitor type, expressed in epoch timestamp format. Supply either \&quot;expectNextPingAt\&quot;, or \&quot;expectNextPingAtEpoch\&quot;, or a X_NEXT_PING request header, not more than one of those options. Must be blank for other monitor types. |  [optional] |
|**monitor** | **String** | The monitor that is related to this resource instance. |  |
|**pingCustomCode** | **String** | The client-supplied custom code that is appended to the ping. Only the first 10 characters are used and saved. |  [optional] |
|**pingCustomPayload** | **String** | The client-supplied custom payload that is saved with the ping. Only the first 100 characters are saved. This value overrides the value of an monitor&#39;s alert payload, if the ping results in an alert. |  [optional] |



