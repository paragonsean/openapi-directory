

# ContainerServiceNetworkProfile

Profile of network configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsServiceIP** | **String** | An IP address assigned to the Kubernetes DNS service. It must be within the Kubernetes service address range specified in serviceCidr. |  [optional] |
|**dockerBridgeCidr** | **String** | A CIDR notation IP range assigned to the Docker bridge network. It must not overlap with any Subnet IP ranges or the Kubernetes service address range. |  [optional] |
|**networkPlugin** | [**NetworkPluginEnum**](#NetworkPluginEnum) | Network plugin used for building Kubernetes network. |  [optional] |
|**networkPolicy** | [**NetworkPolicyEnum**](#NetworkPolicyEnum) | Network policy used for building Kubernetes network. |  [optional] |
|**podCidr** | **String** | A CIDR notation IP range from which to assign pod IPs when kubenet is used. |  [optional] |
|**serviceCidr** | **String** | A CIDR notation IP range from which to assign service cluster IPs. It must not overlap with any Subnet IP ranges. |  [optional] |



## Enum: NetworkPluginEnum

| Name | Value |
|---- | -----|
| AZURE | &quot;azure&quot; |
| KUBENET | &quot;kubenet&quot; |



## Enum: NetworkPolicyEnum

| Name | Value |
|---- | -----|
| CALICO | &quot;calico&quot; |
| AZURE | &quot;azure&quot; |



