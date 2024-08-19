# ChromeManagementApi.GoogleChromeManagementV1NetworkStatusReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionState** | **String** | Output only. Current connection state of the network. | [optional] [readonly] 
**connectionType** | **String** | Output only. Network connection type. | [optional] [readonly] 
**encryptionOn** | **Boolean** | Output only. Whether the wifi encryption key is turned off. | [optional] [readonly] 
**gatewayIpAddress** | **String** | Output only. Gateway IP address. | [optional] [readonly] 
**guid** | **String** | Output only. Network connection guid. | [optional] [readonly] 
**lanIpAddress** | **String** | Output only. LAN IP address. | [optional] [readonly] 
**receivingBitRateMbps** | **String** | Output only. Receiving bit rate measured in Megabits per second. | [optional] [readonly] 
**reportTime** | **String** | Output only. Time at which the network state was reported. | [optional] [readonly] 
**sampleFrequency** | **String** | Output only. Frequency the report is sampled. | [optional] [readonly] 
**signalStrengthDbm** | **Number** | Output only. Signal strength for wireless networks measured in decibels. | [optional] [readonly] 
**transmissionBitRateMbps** | **String** | Output only. Transmission bit rate measured in Megabits per second. | [optional] [readonly] 
**transmissionPowerDbm** | **Number** | Output only. Transmission power measured in decibels. | [optional] [readonly] 
**wifiLinkQuality** | **String** | Output only. Wifi link quality. Value ranges from [0, 70]. 0 indicates no signal and 70 indicates a strong signal. | [optional] [readonly] 
**wifiPowerManagementEnabled** | **Boolean** | Output only. Wifi power management enabled | [optional] [readonly] 



## Enum: ConnectionStateEnum


* `NETWORK_CONNECTION_STATE_UNSPECIFIED` (value: `"NETWORK_CONNECTION_STATE_UNSPECIFIED"`)

* `ONLINE` (value: `"ONLINE"`)

* `CONNECTED` (value: `"CONNECTED"`)

* `PORTAL` (value: `"PORTAL"`)

* `CONNECTING` (value: `"CONNECTING"`)

* `NOT_CONNECTED` (value: `"NOT_CONNECTED"`)





## Enum: ConnectionTypeEnum


* `NETWORK_TYPE_UNSPECIFIED` (value: `"NETWORK_TYPE_UNSPECIFIED"`)

* `CELLULAR` (value: `"CELLULAR"`)

* `ETHERNET` (value: `"ETHERNET"`)

* `TETHER` (value: `"TETHER"`)

* `VPN` (value: `"VPN"`)

* `WIFI` (value: `"WIFI"`)




