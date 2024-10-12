# KubernetesEngineApi.NetworkConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datapathProvider** | **String** | The desired datapath provider for this cluster. By default, uses the IPTables-based kube-proxy implementation. | [optional] 
**defaultSnatStatus** | [**DefaultSnatStatus**](DefaultSnatStatus.md) |  | [optional] 
**dnsConfig** | [**DNSConfig**](DNSConfig.md) |  | [optional] 
**enableFqdnNetworkPolicy** | **Boolean** | Whether FQDN Network Policy is enabled on this cluster. | [optional] 
**enableIntraNodeVisibility** | **Boolean** | Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network. | [optional] 
**enableL4ilbSubsetting** | **Boolean** | Whether L4ILB Subsetting is enabled for this cluster. | [optional] 
**enableMultiNetworking** | **Boolean** | Whether multi-networking is enabled for this cluster. | [optional] 
**gatewayApiConfig** | [**GatewayAPIConfig**](GatewayAPIConfig.md) |  | [optional] 
**inTransitEncryptionConfig** | **String** | Specify the details of in-transit encryption. | [optional] 
**network** | **String** | Output only. The relative name of the Google Compute Engine network(https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the cluster is connected. Example: projects/my-project/global/networks/my-network | [optional] 
**networkPerformanceConfig** | [**ClusterNetworkPerformanceConfig**](ClusterNetworkPerformanceConfig.md) |  | [optional] 
**privateIpv6GoogleAccess** | **String** | The desired state of IPv6 connectivity to Google Services. By default, no private IPv6 access to or from Google Services (all access will be via IPv4) | [optional] 
**serviceExternalIpsConfig** | [**ServiceExternalIPsConfig**](ServiceExternalIPsConfig.md) |  | [optional] 
**subnetwork** | **String** | Output only. The relative name of the Google Compute Engine [subnetwork](https://cloud.google.com/compute/docs/vpc) to which the cluster is connected. Example: projects/my-project/regions/us-central1/subnetworks/my-subnet | [optional] 



## Enum: DatapathProviderEnum


* `DATAPATH_PROVIDER_UNSPECIFIED` (value: `"DATAPATH_PROVIDER_UNSPECIFIED"`)

* `LEGACY_DATAPATH` (value: `"LEGACY_DATAPATH"`)

* `ADVANCED_DATAPATH` (value: `"ADVANCED_DATAPATH"`)





## Enum: InTransitEncryptionConfigEnum


* `CONFIG_UNSPECIFIED` (value: `"IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED"`)

* `DISABLED` (value: `"IN_TRANSIT_ENCRYPTION_DISABLED"`)

* `INTER_NODE_TRANSPARENT` (value: `"IN_TRANSIT_ENCRYPTION_INTER_NODE_TRANSPARENT"`)





## Enum: PrivateIpv6GoogleAccessEnum


* `UNSPECIFIED` (value: `"PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED"`)

* `DISABLED` (value: `"PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED"`)

* `TO_GOOGLE` (value: `"PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE"`)

* `BIDIRECTIONAL` (value: `"PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL"`)




