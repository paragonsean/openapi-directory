

# NetworkConfig

NetworkConfig reports the relative names of network & subnetwork.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datapathProvider** | [**DatapathProviderEnum**](#DatapathProviderEnum) | The desired datapath provider for this cluster. By default, uses the IPTables-based kube-proxy implementation. |  [optional] |
|**defaultSnatStatus** | [**DefaultSnatStatus**](DefaultSnatStatus.md) |  |  [optional] |
|**dnsConfig** | [**DNSConfig**](DNSConfig.md) |  |  [optional] |
|**enableFqdnNetworkPolicy** | **Boolean** | Whether FQDN Network Policy is enabled on this cluster. |  [optional] |
|**enableIntraNodeVisibility** | **Boolean** | Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network. |  [optional] |
|**enableL4ilbSubsetting** | **Boolean** | Whether L4ILB Subsetting is enabled for this cluster. |  [optional] |
|**enableMultiNetworking** | **Boolean** | Whether multi-networking is enabled for this cluster. |  [optional] |
|**gatewayApiConfig** | [**GatewayAPIConfig**](GatewayAPIConfig.md) |  |  [optional] |
|**inTransitEncryptionConfig** | [**InTransitEncryptionConfigEnum**](#InTransitEncryptionConfigEnum) | Specify the details of in-transit encryption. |  [optional] |
|**network** | **String** | Output only. The relative name of the Google Compute Engine network(https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the cluster is connected. Example: projects/my-project/global/networks/my-network |  [optional] |
|**networkPerformanceConfig** | [**ClusterNetworkPerformanceConfig**](ClusterNetworkPerformanceConfig.md) |  |  [optional] |
|**privateIpv6GoogleAccess** | [**PrivateIpv6GoogleAccessEnum**](#PrivateIpv6GoogleAccessEnum) | The desired state of IPv6 connectivity to Google Services. By default, no private IPv6 access to or from Google Services (all access will be via IPv4) |  [optional] |
|**serviceExternalIpsConfig** | [**ServiceExternalIPsConfig**](ServiceExternalIPsConfig.md) |  |  [optional] |
|**subnetwork** | **String** | Output only. The relative name of the Google Compute Engine [subnetwork](https://cloud.google.com/compute/docs/vpc) to which the cluster is connected. Example: projects/my-project/regions/us-central1/subnetworks/my-subnet |  [optional] |



## Enum: DatapathProviderEnum

| Name | Value |
|---- | -----|
| DATAPATH_PROVIDER_UNSPECIFIED | &quot;DATAPATH_PROVIDER_UNSPECIFIED&quot; |
| LEGACY_DATAPATH | &quot;LEGACY_DATAPATH&quot; |
| ADVANCED_DATAPATH | &quot;ADVANCED_DATAPATH&quot; |



## Enum: InTransitEncryptionConfigEnum

| Name | Value |
|---- | -----|
| CONFIG_UNSPECIFIED | &quot;IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED&quot; |
| DISABLED | &quot;IN_TRANSIT_ENCRYPTION_DISABLED&quot; |
| INTER_NODE_TRANSPARENT | &quot;IN_TRANSIT_ENCRYPTION_INTER_NODE_TRANSPARENT&quot; |



## Enum: PrivateIpv6GoogleAccessEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED&quot; |
| DISABLED | &quot;PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED&quot; |
| TO_GOOGLE | &quot;PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE&quot; |
| BIDIRECTIONAL | &quot;PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL&quot; |



