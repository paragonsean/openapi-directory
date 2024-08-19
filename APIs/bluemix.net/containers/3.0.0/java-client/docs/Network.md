

# Network


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aliases** | **String** | Alternative name of the private container network the container is connected to. |  [optional] |
|**endpointID** | **String** | Unique ID representing a container. |  [optional] |
|**gateway** | **String** | The private IP address of the network gateway in IPv4 format. |  [optional] |
|**globalIPv6Address** | **String** | Private IP address of the container in IPv6 format. IBM Containers only supports IPv4 format. This attribute is returned as empty. |  [optional] |
|**globalIPv6PrefixLen** | **Integer** | Not supported by IBM Containers, empty string. |  [optional] |
|**ipAMConfig** | **String** | Specific configurations for the network driver. |  [optional] |
|**ipPrefixLen** | **String** | The prefix of the subnet in the private container network. The prefix indicates that 16 bits out of 32 bits are used to address the network. As every IPv4 IP adress consists of 32 bits, the last 16 bits are used to assign private IP addresses to the container.  |  [optional] |
|**ipv6Gateway** | **String** | The private IP address of the network gateway in IPv6 format. IBM Containers only supports IPv4 format. This attribute is returned as empty. |  [optional] |
|**links** | **String** | List of container names that are linked to the container.  |  [optional] |
|**macAddress** | **String** | The MAC address that is assigned to the container. |  [optional] |
|**networkID** | **String** | Unique identifier representing the private container network. |  [optional] |



