

# GetNetworkAppliancePorts200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessPolicy** | **String** | The name of the policy. Only applicable to Access ports. |  [optional] |
|**allowedVlans** | **String** | Comma-delimited list of the VLAN ID&#39;s allowed on the port, or &#39;all&#39; to permit all VLAN&#39;s on the port. |  [optional] |
|**dropUntaggedTraffic** | **Boolean** | Whether the trunk port can drop all untagged traffic. |  [optional] |
|**enabled** | **Boolean** | The status of the port |  [optional] |
|**number** | **Integer** | Number of the port |  [optional] |
|**type** | **String** | The type of the port: &#39;access&#39; or &#39;trunk&#39;. |  [optional] |
|**vlan** | **Integer** | Native VLAN when the port is in Trunk mode. Access VLAN when the port is in Access mode. |  [optional] |



