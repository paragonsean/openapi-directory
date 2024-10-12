

# NetworkAdapter

Represents the networkAdapter on a device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adapterId** | **String** | Instance ID of network adapter. |  [optional] [readonly] |
|**adapterPosition** | [**NetworkAdapterPosition**](NetworkAdapterPosition.md) |  |  [optional] |
|**dhcpStatus** | [**DhcpStatusEnum**](#DhcpStatusEnum) | Value indicating whether this adapter has DHCP enabled. |  [optional] |
|**dnsServers** | **List&lt;String&gt;** | The list of DNS Servers of the device. |  [optional] [readonly] |
|**index** | **Integer** | Logical index of the adapter. |  [optional] [readonly] |
|**ipv4Configuration** | [**Ipv4Config**](Ipv4Config.md) |  |  [optional] |
|**ipv6Configuration** | [**Ipv6Config**](Ipv6Config.md) |  |  [optional] |
|**ipv6LinkLocalAddress** | **String** | The IPv6 local address. |  [optional] [readonly] |
|**label** | **String** | Hardware label for the adapter. |  [optional] [readonly] |
|**linkSpeed** | **Long** | Link speed. |  [optional] [readonly] |
|**macAddress** | **String** | MAC address. |  [optional] [readonly] |
|**networkAdapterName** | **String** | Network adapter name. |  [optional] [readonly] |
|**nodeId** | **String** | Node ID of the network adapter. |  [optional] [readonly] |
|**rdmaStatus** | [**RdmaStatusEnum**](#RdmaStatusEnum) | Value indicating whether this adapter is RDMA capable. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Value indicating whether this adapter is valid. |  [optional] [readonly] |



## Enum: DhcpStatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



## Enum: RdmaStatusEnum

| Name | Value |
|---- | -----|
| INCAPABLE | &quot;Incapable&quot; |
| CAPABLE | &quot;Capable&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INACTIVE | &quot;Inactive&quot; |
| ACTIVE | &quot;Active&quot; |



