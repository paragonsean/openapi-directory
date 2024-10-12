

# GetNetworkClients200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adaptivePolicyGroup** | **String** | The adaptive policy group of the client |  [optional] |
|**description** | **String** | Short description of the client |  [optional] |
|**deviceTypePrediction** | **String** | Prediction of the client&#39;s device type |  [optional] |
|**firstSeen** | **Integer** | Timestamp client was first seen in the network |  [optional] |
|**groupPolicy8021x** | **String** | 802.1x group policy of the client |  [optional] |
|**id** | **String** | The ID of the client |  [optional] |
|**ip** | **String** | The IP address of the client |  [optional] |
|**ip6** | **String** | The IPv6 address of the client |  [optional] |
|**ip6Local** | **String** | Local IPv6 address of the client |  [optional] |
|**lastSeen** | **Integer** | Timestamp client was last seen in the network |  [optional] |
|**mac** | **String** | The MAC address of the client |  [optional] |
|**manufacturer** | **String** | Manufacturer of the client |  [optional] |
|**namedVlan** | **String** | Named VLAN of the client |  [optional] |
|**notes** | **String** | Notes on the client |  [optional] |
|**os** | **String** | The operating system of the client |  [optional] |
|**recentDeviceConnection** | [**RecentDeviceConnectionEnum**](#RecentDeviceConnectionEnum) | Client&#39;s most recent connection type |  [optional] |
|**recentDeviceMac** | **String** | The MAC address of the node that the device was last connected to |  [optional] |
|**recentDeviceName** | **String** | The name of the node the device was last connected to |  [optional] |
|**recentDeviceSerial** | **String** | The serial of the node the device was last connected to |  [optional] |
|**smInstalled** | **Boolean** | Status of SM for the client |  [optional] |
|**ssid** | **String** | The name of the SSID that the client is connected to |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The connection status of the client |  [optional] |
|**switchport** | **String** | The switch port that the client is connected to |  [optional] |
|**usage** | [**GetNetworkClients200ResponseUsage**](GetNetworkClients200ResponseUsage.md) |  |  [optional] |
|**user** | **String** | The username of the user of the client |  [optional] |
|**vlan** | **String** | The name of the VLAN that the client is connected to |  [optional] |
|**wirelessCapabilities** | **String** | Wireless capabilities of the client |  [optional] |



## Enum: RecentDeviceConnectionEnum

| Name | Value |
|---- | -----|
| WIRED | &quot;Wired&quot; |
| WIRELESS | &quot;Wireless&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OFFLINE | &quot;Offline&quot; |
| ONLINE | &quot;Online&quot; |



