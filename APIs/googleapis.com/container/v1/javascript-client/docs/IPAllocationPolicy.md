# KubernetesEngineApi.IPAllocationPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalPodRangesConfig** | [**AdditionalPodRangesConfig**](AdditionalPodRangesConfig.md) |  | [optional] 
**clusterIpv4Cidr** | **String** | This field is deprecated, use cluster_ipv4_cidr_block. | [optional] 
**clusterIpv4CidrBlock** | **String** | The IP address range for the cluster pod IPs. If this field is set, then &#x60;cluster.cluster_ipv4_cidr&#x60; must be left blank. This field is only applicable when &#x60;use_ip_aliases&#x60; is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. &#x60;/14&#x60;) to have a range chosen with a specific netmask. Set to a [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. &#x60;10.96.0.0/14&#x60;) from the RFC-1918 private networks (e.g. &#x60;10.0.0.0/8&#x60;, &#x60;172.16.0.0/12&#x60;, &#x60;192.168.0.0/16&#x60;) to pick a specific range to use. | [optional] 
**clusterSecondaryRangeName** | **String** | The name of the secondary range to be used for the cluster CIDR block. The secondary range will be used for pod IP addresses. This must be an existing secondary range associated with the cluster subnetwork. This field is only applicable with use_ip_aliases is true and create_subnetwork is false. | [optional] 
**createSubnetwork** | **Boolean** | Whether a new subnetwork will be created automatically for the cluster. This field is only applicable when &#x60;use_ip_aliases&#x60; is true. | [optional] 
**defaultPodIpv4RangeUtilization** | **Number** | Output only. [Output only] The utilization of the cluster default IPv4 range for the pod. The ratio is Usage/[Total number of IPs in the secondary range], Usage&#x3D;numNodes*numZones*podIPsPerNode. | [optional] [readonly] 
**ipv6AccessType** | **String** | The ipv6 access type (internal or external) when create_subnetwork is true | [optional] 
**nodeIpv4Cidr** | **String** | This field is deprecated, use node_ipv4_cidr_block. | [optional] 
**nodeIpv4CidrBlock** | **String** | The IP address range of the instance IPs in this cluster. This is applicable only if &#x60;create_subnetwork&#x60; is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. &#x60;/14&#x60;) to have a range chosen with a specific netmask. Set to a [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. &#x60;10.96.0.0/14&#x60;) from the RFC-1918 private networks (e.g. &#x60;10.0.0.0/8&#x60;, &#x60;172.16.0.0/12&#x60;, &#x60;192.168.0.0/16&#x60;) to pick a specific range to use. | [optional] 
**podCidrOverprovisionConfig** | [**PodCIDROverprovisionConfig**](PodCIDROverprovisionConfig.md) |  | [optional] 
**servicesIpv4Cidr** | **String** | This field is deprecated, use services_ipv4_cidr_block. | [optional] 
**servicesIpv4CidrBlock** | **String** | The IP address range of the services IPs in this cluster. If blank, a range will be automatically chosen with the default size. This field is only applicable when &#x60;use_ip_aliases&#x60; is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. &#x60;/14&#x60;) to have a range chosen with a specific netmask. Set to a [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. &#x60;10.96.0.0/14&#x60;) from the RFC-1918 private networks (e.g. &#x60;10.0.0.0/8&#x60;, &#x60;172.16.0.0/12&#x60;, &#x60;192.168.0.0/16&#x60;) to pick a specific range to use. | [optional] 
**servicesIpv6CidrBlock** | **String** | Output only. [Output only] The services IPv6 CIDR block for the cluster. | [optional] [readonly] 
**servicesSecondaryRangeName** | **String** | The name of the secondary range to be used as for the services CIDR block. The secondary range will be used for service ClusterIPs. This must be an existing secondary range associated with the cluster subnetwork. This field is only applicable with use_ip_aliases is true and create_subnetwork is false. | [optional] 
**stackType** | **String** | The IP stack type of the cluster | [optional] 
**subnetIpv6CidrBlock** | **String** | Output only. [Output only] The subnet&#39;s IPv6 CIDR block used by nodes and pods. | [optional] [readonly] 
**subnetworkName** | **String** | A custom subnetwork name to be used if &#x60;create_subnetwork&#x60; is true. If this field is empty, then an automatic name will be chosen for the new subnetwork. | [optional] 
**tpuIpv4CidrBlock** | **String** | The IP address range of the Cloud TPUs in this cluster. If unspecified, a range will be automatically chosen with the default size. This field is only applicable when &#x60;use_ip_aliases&#x60; is true. If unspecified, the range will use the default size. Set to /netmask (e.g. &#x60;/14&#x60;) to have a range chosen with a specific netmask. Set to a [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. &#x60;10.96.0.0/14&#x60;) from the RFC-1918 private networks (e.g. &#x60;10.0.0.0/8&#x60;, &#x60;172.16.0.0/12&#x60;, &#x60;192.168.0.0/16&#x60;) to pick a specific range to use. | [optional] 
**useIpAliases** | **Boolean** | Whether alias IPs will be used for pod IPs in the cluster. This is used in conjunction with use_routes. It cannot be true if use_routes is true. If both use_ip_aliases and use_routes are false, then the server picks the default IP allocation mode | [optional] 
**useRoutes** | **Boolean** | Whether routes will be used for pod IPs in the cluster. This is used in conjunction with use_ip_aliases. It cannot be true if use_ip_aliases is true. If both use_ip_aliases and use_routes are false, then the server picks the default IP allocation mode | [optional] 



## Enum: Ipv6AccessTypeEnum


* `IPV6_ACCESS_TYPE_UNSPECIFIED` (value: `"IPV6_ACCESS_TYPE_UNSPECIFIED"`)

* `INTERNAL` (value: `"INTERNAL"`)

* `EXTERNAL` (value: `"EXTERNAL"`)





## Enum: StackTypeEnum


* `STACK_TYPE_UNSPECIFIED` (value: `"STACK_TYPE_UNSPECIFIED"`)

* `IPV4` (value: `"IPV4"`)

* `IPV4_IPV6` (value: `"IPV4_IPV6"`)




