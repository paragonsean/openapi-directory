

# GoogleChromeManagementV1TelemetryNetworkConnectionStateChangeEvent

`TelemetryNetworkConnectionStateChangeEvent` is triggered on network connection state changes. * Granular permission needed: TELEMETRY_API_NETWORK_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionState** | [**ConnectionStateEnum**](#ConnectionStateEnum) | Current connection state of the network. |  [optional] |
|**guid** | **String** | Unique identifier of the network. |  [optional] |



## Enum: ConnectionStateEnum

| Name | Value |
|---- | -----|
| NETWORK_CONNECTION_STATE_UNSPECIFIED | &quot;NETWORK_CONNECTION_STATE_UNSPECIFIED&quot; |
| ONLINE | &quot;ONLINE&quot; |
| CONNECTED | &quot;CONNECTED&quot; |
| PORTAL | &quot;PORTAL&quot; |
| CONNECTING | &quot;CONNECTING&quot; |
| NOT_CONNECTED | &quot;NOT_CONNECTED&quot; |



