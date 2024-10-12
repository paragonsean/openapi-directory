# MerakiDashboardApi.GetNetworkClient200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp** | **[[String]]** | The Cisco discover protocol settings for the client | [optional] 
**clientVpnConnections** | [**[GetNetworkClient200ResponseClientVpnConnectionsInner]**](GetNetworkClient200ResponseClientVpnConnectionsInner.md) | VPN connections associated with the client | [optional] 
**description** | **String** | Short description of the client | [optional] 
**firstSeen** | **Number** | Timestamp client was first seen in the network | [optional] 
**id** | **String** | The ID of the client | [optional] 
**ip** | **String** | The IP address of the client | [optional] 
**ip6** | **String** | The IPv6 address of the client | [optional] 
**lastSeen** | **Number** | Timestamp client was last seen in the network | [optional] 
**lldp** | **[[String]]** | The link layer discover protocol settings for the client | [optional] 
**mac** | **String** | The MAC address of the client | [optional] 
**manufacturer** | **String** | Manufacturer of the client | [optional] 
**os** | **String** | The operating system of the client | [optional] 
**recentDeviceMac** | **String** | The MAC address of the node that the device was last connected to | [optional] 
**smInstalled** | **Boolean** | Status of SM for the client | [optional] 
**ssid** | **String** | The name of the SSID that the client is connected to | [optional] 
**status** | **String** | The connection status of the client | [optional] 
**switchport** | **String** | The switch port that the client is connected to | [optional] 
**user** | **String** | The username of the user of the client | [optional] 
**vlan** | **String** | The name of the VLAN that the client is connected to | [optional] 
**wirelessCapabilities** | **String** | Wireless capabilities of the client | [optional] 



## Enum: StatusEnum


* `Offline` (value: `"Offline"`)

* `Online` (value: `"Online"`)




