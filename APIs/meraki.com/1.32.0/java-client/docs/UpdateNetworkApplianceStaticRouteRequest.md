

# UpdateNetworkApplianceStaticRouteRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | The enabled state of the static route |  [optional] |
|**fixedIpAssignments** | **Object** | The DHCP fixed IP assignments on the static route. This should be an object that contains mappings from MAC addresses to objects that themselves each contain \&quot;ip\&quot; and \&quot;name\&quot; string fields. See the sample request/response for more details. |  [optional] |
|**gatewayIp** | **String** | The gateway IP (next hop) of the static route |  [optional] |
|**gatewayVlanId** | **String** | The gateway IP (next hop) VLAN ID of the static route |  [optional] |
|**name** | **String** | The name of the static route |  [optional] |
|**reservedIpRanges** | [**List&lt;UpdateNetworkApplianceStaticRouteRequestReservedIpRangesInner&gt;**](UpdateNetworkApplianceStaticRouteRequestReservedIpRangesInner.md) | The DHCP reserved IP ranges on the static route |  [optional] |
|**subnet** | **String** | The subnet of the static route |  [optional] |



