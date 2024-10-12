

# VmwareNetworkConfig

Specifies network config for the VMware user cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**controlPlaneV2Config** | [**VmwareControlPlaneV2Config**](VmwareControlPlaneV2Config.md) |  |  [optional] |
|**dhcpIpConfig** | [**VmwareDhcpIpConfig**](VmwareDhcpIpConfig.md) |  |  [optional] |
|**hostConfig** | [**VmwareHostConfig**](VmwareHostConfig.md) |  |  [optional] |
|**podAddressCidrBlocks** | **List&lt;String&gt;** | Required. All pods in the cluster are assigned an RFC1918 IPv4 address from these ranges. Only a single range is supported. This field cannot be changed after creation. |  [optional] |
|**serviceAddressCidrBlocks** | **List&lt;String&gt;** | Required. All services in the cluster are assigned an RFC1918 IPv4 address from these ranges. Only a single range is supported. This field cannot be changed after creation. |  [optional] |
|**staticIpConfig** | [**VmwareStaticIpConfig**](VmwareStaticIpConfig.md) |  |  [optional] |
|**vcenterNetwork** | **String** | vcenter_network specifies vCenter network name. Inherited from the admin cluster. |  [optional] |



