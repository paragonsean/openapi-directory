

# GoogleChromeManagementV1TelemetryEventNotificationFilter

Configures how the telemetry events should be filtered.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventTypes** | [**List&lt;EventTypesEnum&gt;**](#List&lt;EventTypesEnum&gt;) | Only sends the notifications for events of these types. Must not be empty. |  [optional] |



## Enum: List&lt;EventTypesEnum&gt;

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| AUDIO_SEVERE_UNDERRUN | &quot;AUDIO_SEVERE_UNDERRUN&quot; |
| NETWORK_STATE_CHANGE | &quot;NETWORK_STATE_CHANGE&quot; |
| USB_ADDED | &quot;USB_ADDED&quot; |
| USB_REMOVED | &quot;USB_REMOVED&quot; |
| NETWORK_HTTPS_LATENCY_CHANGE | &quot;NETWORK_HTTPS_LATENCY_CHANGE&quot; |
| WIFI_SIGNAL_STRENGTH_LOW | &quot;WIFI_SIGNAL_STRENGTH_LOW&quot; |
| WIFI_SIGNAL_STRENGTH_RECOVERED | &quot;WIFI_SIGNAL_STRENGTH_RECOVERED&quot; |
| VPN_CONNECTION_STATE_CHANGE | &quot;VPN_CONNECTION_STATE_CHANGE&quot; |



