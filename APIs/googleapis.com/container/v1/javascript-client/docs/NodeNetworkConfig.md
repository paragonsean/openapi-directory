# KubernetesEngineApi.NodeNetworkConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalNodeNetworkConfigs** | [**[AdditionalNodeNetworkConfig]**](AdditionalNodeNetworkConfig.md) | We specify the additional node networks for this node pool using this list. Each node network corresponds to an additional interface | [optional] 
**additionalPodNetworkConfigs** | [**[AdditionalPodNetworkConfig]**](AdditionalPodNetworkConfig.md) | We specify the additional pod networks for this node pool using this list. Each pod network corresponds to an additional alias IP range for the node | [optional] 
**createPodRange** | **Boolean** | Input only. Whether to create a new range for pod IPs in this node pool. Defaults are provided for &#x60;pod_range&#x60; and &#x60;pod_ipv4_cidr_block&#x60; if they are not specified. If neither &#x60;create_pod_range&#x60; or &#x60;pod_range&#x60; are specified, the cluster-level default (&#x60;ip_allocation_policy.cluster_ipv4_cidr_block&#x60;) is used. Only applicable if &#x60;ip_allocation_policy.use_ip_aliases&#x60; is true. This field cannot be changed after the node pool has been created. | [optional] 
**enablePrivateNodes** | **Boolean** | Whether nodes have internal IP addresses only. If enable_private_nodes is not specified, then the value is derived from cluster.privateClusterConfig.enablePrivateNodes | [optional] 
**networkPerformanceConfig** | [**NetworkPerformanceConfig**](NetworkPerformanceConfig.md) |  | [optional] 
**podCidrOverprovisionConfig** | [**PodCIDROverprovisionConfig**](PodCIDROverprovisionConfig.md) |  | [optional] 
**podIpv4CidrBlock** | **String** | The IP address range for pod IPs in this node pool. Only applicable if &#x60;create_pod_range&#x60; is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. &#x60;/14&#x60;) to have a range chosen with a specific netmask. Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. &#x60;10.96.0.0/14&#x60;) to pick a specific range to use. Only applicable if &#x60;ip_allocation_policy.use_ip_aliases&#x60; is true. This field cannot be changed after the node pool has been created. | [optional] 
**podIpv4RangeUtilization** | **Number** | Output only. [Output only] The utilization of the IPv4 range for the pod. The ratio is Usage/[Total number of IPs in the secondary range], Usage&#x3D;numNodes*numZones*podIPsPerNode. | [optional] [readonly] 
**podRange** | **String** | The ID of the secondary range for pod IPs. If &#x60;create_pod_range&#x60; is true, this ID is used for the new range. If &#x60;create_pod_range&#x60; is false, uses an existing secondary range with this ID. Only applicable if &#x60;ip_allocation_policy.use_ip_aliases&#x60; is true. This field cannot be changed after the node pool has been created. | [optional] 


