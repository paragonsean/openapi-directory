

# GoogleChromeManagementV1NetworkStatusReport

State of visible/configured networks. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportNetworkStatus](https://chromeenterprise.google/policies/#ReportNetworkStatus) * Data Collection Frequency: 60 minutes * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: Yes * Reported for affiliated users only: Yes * Granular permission needed: TELEMETRY_API_NETWORK_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionState** | [**ConnectionStateEnum**](#ConnectionStateEnum) | Output only. Current connection state of the network. |  [optional] [readonly] |
|**connectionType** | [**ConnectionTypeEnum**](#ConnectionTypeEnum) | Output only. Network connection type. |  [optional] [readonly] |
|**encryptionOn** | **Boolean** | Output only. Whether the wifi encryption key is turned off. |  [optional] [readonly] |
|**gatewayIpAddress** | **String** | Output only. Gateway IP address. |  [optional] [readonly] |
|**guid** | **String** | Output only. Network connection guid. |  [optional] [readonly] |
|**lanIpAddress** | **String** | Output only. LAN IP address. |  [optional] [readonly] |
|**receivingBitRateMbps** | **String** | Output only. Receiving bit rate measured in Megabits per second. |  [optional] [readonly] |
|**reportTime** | **String** | Output only. Time at which the network state was reported. |  [optional] [readonly] |
|**sampleFrequency** | **String** | Output only. Frequency the report is sampled. |  [optional] [readonly] |
|**signalStrengthDbm** | **Integer** | Output only. Signal strength for wireless networks measured in decibels. |  [optional] [readonly] |
|**transmissionBitRateMbps** | **String** | Output only. Transmission bit rate measured in Megabits per second. |  [optional] [readonly] |
|**transmissionPowerDbm** | **Integer** | Output only. Transmission power measured in decibels. |  [optional] [readonly] |
|**wifiLinkQuality** | **String** | Output only. Wifi link quality. Value ranges from [0, 70]. 0 indicates no signal and 70 indicates a strong signal. |  [optional] [readonly] |
|**wifiPowerManagementEnabled** | **Boolean** | Output only. Wifi power management enabled |  [optional] [readonly] |



## Enum: ConnectionStateEnum

| Name | Value |
|---- | -----|
| NETWORK_CONNECTION_STATE_UNSPECIFIED | &quot;NETWORK_CONNECTION_STATE_UNSPECIFIED&quot; |
| ONLINE | &quot;ONLINE&quot; |
| CONNECTED | &quot;CONNECTED&quot; |
| PORTAL | &quot;PORTAL&quot; |
| CONNECTING | &quot;CONNECTING&quot; |
| NOT_CONNECTED | &quot;NOT_CONNECTED&quot; |



## Enum: ConnectionTypeEnum

| Name | Value |
|---- | -----|
| NETWORK_TYPE_UNSPECIFIED | &quot;NETWORK_TYPE_UNSPECIFIED&quot; |
| CELLULAR | &quot;CELLULAR&quot; |
| ETHERNET | &quot;ETHERNET&quot; |
| TETHER | &quot;TETHER&quot; |
| VPN | &quot;VPN&quot; |
| WIFI | &quot;WIFI&quot; |



