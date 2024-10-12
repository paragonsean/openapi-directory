# ChromeManagementApi.GoogleChromeManagementV1TelemetryEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioSevereUnderrunEvent** | **Object** | &#x60;TelemetryAudioSevereUnderrunEvent&#x60; is triggered when a audio devices run out of buffer data for more than 5 seconds. * Granular permission needed: TELEMETRY_API_AUDIO_REPORT | [optional] 
**device** | [**GoogleChromeManagementV1TelemetryDeviceInfo**](GoogleChromeManagementV1TelemetryDeviceInfo.md) |  | [optional] 
**eventType** | **String** | The event type of the current event. | [optional] 
**httpsLatencyChangeEvent** | [**GoogleChromeManagementV1TelemetryHttpsLatencyChangeEvent**](GoogleChromeManagementV1TelemetryHttpsLatencyChangeEvent.md) |  | [optional] 
**name** | **String** | Output only. Resource name of the event. | [optional] [readonly] 
**networkStateChangeEvent** | [**GoogleChromeManagementV1TelemetryNetworkConnectionStateChangeEvent**](GoogleChromeManagementV1TelemetryNetworkConnectionStateChangeEvent.md) |  | [optional] 
**reportTime** | **String** | Timestamp that represents when the event was reported. | [optional] 
**usbPeripheralsEvent** | [**GoogleChromeManagementV1TelemetryUsbPeripheralsEvent**](GoogleChromeManagementV1TelemetryUsbPeripheralsEvent.md) |  | [optional] 
**user** | [**GoogleChromeManagementV1TelemetryUserInfo**](GoogleChromeManagementV1TelemetryUserInfo.md) |  | [optional] 
**vpnConnectionStateChangeEvent** | [**GoogleChromeManagementV1TelemetryNetworkConnectionStateChangeEvent**](GoogleChromeManagementV1TelemetryNetworkConnectionStateChangeEvent.md) |  | [optional] 
**wifiSignalStrengthEvent** | [**GoogleChromeManagementV1TelemetryNetworkSignalStrengthEvent**](GoogleChromeManagementV1TelemetryNetworkSignalStrengthEvent.md) |  | [optional] 



## Enum: EventTypeEnum


* `EVENT_TYPE_UNSPECIFIED` (value: `"EVENT_TYPE_UNSPECIFIED"`)

* `AUDIO_SEVERE_UNDERRUN` (value: `"AUDIO_SEVERE_UNDERRUN"`)

* `NETWORK_STATE_CHANGE` (value: `"NETWORK_STATE_CHANGE"`)

* `USB_ADDED` (value: `"USB_ADDED"`)

* `USB_REMOVED` (value: `"USB_REMOVED"`)

* `NETWORK_HTTPS_LATENCY_CHANGE` (value: `"NETWORK_HTTPS_LATENCY_CHANGE"`)

* `WIFI_SIGNAL_STRENGTH_LOW` (value: `"WIFI_SIGNAL_STRENGTH_LOW"`)

* `WIFI_SIGNAL_STRENGTH_RECOVERED` (value: `"WIFI_SIGNAL_STRENGTH_RECOVERED"`)

* `VPN_CONNECTION_STATE_CHANGE` (value: `"VPN_CONNECTION_STATE_CHANGE"`)




