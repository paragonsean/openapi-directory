# ContainerServiceClient.ContainerServiceNetworkProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsServiceIP** | **String** | An IP address assigned to the Kubernetes DNS service. It must be within the Kubernetes service address range specified in serviceCidr. | [optional] [default to &#39;10.0.0.10&#39;]
**dockerBridgeCidr** | **String** | A CIDR notation IP range assigned to the Docker bridge network. It must not overlap with any Subnet IP ranges or the Kubernetes service address range. | [optional] [default to &#39;172.17.0.1/16&#39;]
**networkPlugin** | **String** | Network plugin used for building Kubernetes network. | [optional] [default to &#39;kubenet&#39;]
**networkPolicy** | **String** | Network policy used for building Kubernetes network. | [optional] 
**podCidr** | **String** | A CIDR notation IP range from which to assign pod IPs when kubenet is used. | [optional] [default to &#39;10.244.0.0/16&#39;]
**serviceCidr** | **String** | A CIDR notation IP range from which to assign service cluster IPs. It must not overlap with any Subnet IP ranges. | [optional] [default to &#39;10.0.0.0/16&#39;]



## Enum: NetworkPluginEnum


* `azure` (value: `"azure"`)

* `kubenet` (value: `"kubenet"`)





## Enum: NetworkPolicyEnum


* `calico` (value: `"calico"`)




