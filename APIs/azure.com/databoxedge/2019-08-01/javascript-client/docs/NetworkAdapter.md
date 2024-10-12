# DataBoxEdgeManagementClient.NetworkAdapter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapterId** | **String** | Instance ID of network adapter. | [optional] [readonly] 
**adapterPosition** | [**NetworkAdapterPosition**](NetworkAdapterPosition.md) |  | [optional] 
**dhcpStatus** | **String** | Value indicating whether this adapter has DHCP enabled. | [optional] 
**dnsServers** | **[String]** | The list of DNS Servers of the device. | [optional] [readonly] 
**index** | **Number** | Logical index of the adapter. | [optional] [readonly] 
**ipv4Configuration** | [**Ipv4Config**](Ipv4Config.md) |  | [optional] 
**ipv6Configuration** | [**Ipv6Config**](Ipv6Config.md) |  | [optional] 
**ipv6LinkLocalAddress** | **String** | The IPv6 local address. | [optional] [readonly] 
**label** | **String** | Hardware label for the adapter. | [optional] [readonly] 
**linkSpeed** | **Number** | Link speed. | [optional] [readonly] 
**macAddress** | **String** | MAC address. | [optional] [readonly] 
**networkAdapterName** | **String** | Network adapter name. | [optional] [readonly] 
**nodeId** | **String** | Node ID of the network adapter. | [optional] [readonly] 
**rdmaStatus** | **String** | Value indicating whether this adapter is RDMA capable. | [optional] 
**status** | **String** | Value indicating whether this adapter is valid. | [optional] [readonly] 



## Enum: DhcpStatusEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)





## Enum: RdmaStatusEnum


* `Incapable` (value: `"Incapable"`)

* `Capable` (value: `"Capable"`)





## Enum: StatusEnum


* `Inactive` (value: `"Inactive"`)

* `Active` (value: `"Active"`)




