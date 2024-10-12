

# ClusterUpdate

ClusterUpdate describes an update to the cluster. Exactly one update can be applied to a cluster with each request, so at most one field can be provided.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalPodRangesConfig** | [**AdditionalPodRangesConfig**](AdditionalPodRangesConfig.md) |  |  [optional] |
|**desiredAddonsConfig** | [**AddonsConfig**](AddonsConfig.md) |  |  [optional] |
|**desiredAuthenticatorGroupsConfig** | [**AuthenticatorGroupsConfig**](AuthenticatorGroupsConfig.md) |  |  [optional] |
|**desiredAutopilotWorkloadPolicyConfig** | [**WorkloadPolicyConfig**](WorkloadPolicyConfig.md) |  |  [optional] |
|**desiredBinaryAuthorization** | [**BinaryAuthorization**](BinaryAuthorization.md) |  |  [optional] |
|**desiredClusterAutoscaling** | [**ClusterAutoscaling**](ClusterAutoscaling.md) |  |  [optional] |
|**desiredClusterTelemetry** | [**ClusterTelemetry**](ClusterTelemetry.md) |  |  [optional] |
|**desiredCostManagementConfig** | [**CostManagementConfig**](CostManagementConfig.md) |  |  [optional] |
|**desiredDatabaseEncryption** | [**DatabaseEncryption**](DatabaseEncryption.md) |  |  [optional] |
|**desiredDatapathProvider** | [**DesiredDatapathProviderEnum**](#DesiredDatapathProviderEnum) | The desired datapath provider for the cluster. |  [optional] |
|**desiredDefaultSnatStatus** | [**DefaultSnatStatus**](DefaultSnatStatus.md) |  |  [optional] |
|**desiredDnsConfig** | [**DNSConfig**](DNSConfig.md) |  |  [optional] |
|**desiredEnableFqdnNetworkPolicy** | **Boolean** | Enable/Disable FQDN Network Policy for the cluster. |  [optional] |
|**desiredEnablePrivateEndpoint** | **Boolean** | Enable/Disable private endpoint for the cluster&#39;s master. |  [optional] |
|**desiredFleet** | [**Fleet**](Fleet.md) |  |  [optional] |
|**desiredGatewayApiConfig** | [**GatewayAPIConfig**](GatewayAPIConfig.md) |  |  [optional] |
|**desiredGcfsConfig** | [**GcfsConfig**](GcfsConfig.md) |  |  [optional] |
|**desiredHostMaintenancePolicy** | [**HostMaintenancePolicy**](HostMaintenancePolicy.md) |  |  [optional] |
|**desiredIdentityServiceConfig** | [**IdentityServiceConfig**](IdentityServiceConfig.md) |  |  [optional] |
|**desiredImageType** | **String** | The desired image type for the node pool. NOTE: Set the \&quot;desired_node_pool\&quot; field as well. |  [optional] |
|**desiredInTransitEncryptionConfig** | [**DesiredInTransitEncryptionConfigEnum**](#DesiredInTransitEncryptionConfigEnum) | Specify the details of in-transit encryption. |  [optional] |
|**desiredIntraNodeVisibilityConfig** | [**IntraNodeVisibilityConfig**](IntraNodeVisibilityConfig.md) |  |  [optional] |
|**desiredK8sBetaApis** | [**K8sBetaAPIConfig**](K8sBetaAPIConfig.md) |  |  [optional] |
|**desiredL4ilbSubsettingConfig** | [**ILBSubsettingConfig**](ILBSubsettingConfig.md) |  |  [optional] |
|**desiredLocations** | **List&lt;String&gt;** | The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster&#39;s nodes should be located. This list must always include the cluster&#39;s primary zone. Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed. |  [optional] |
|**desiredLoggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  |  [optional] |
|**desiredLoggingService** | **String** | The logging service the cluster should use to write logs. Currently available options: * &#x60;logging.googleapis.com/kubernetes&#x60; - The Cloud Logging service with a Kubernetes-native resource model * &#x60;logging.googleapis.com&#x60; - The legacy Cloud Logging service (no longer available as of GKE 1.15). * &#x60;none&#x60; - no logs will be exported from the cluster. If left as an empty string,&#x60;logging.googleapis.com/kubernetes&#x60; will be used for GKE 1.14+ or &#x60;logging.googleapis.com&#x60; for earlier versions. |  [optional] |
|**desiredMaster** | **Object** | Master is the configuration for components on master. |  [optional] |
|**desiredMasterAuthorizedNetworksConfig** | [**MasterAuthorizedNetworksConfig**](MasterAuthorizedNetworksConfig.md) |  |  [optional] |
|**desiredMasterVersion** | **String** | The Kubernetes version to change the master to. The only valid value is the latest supported version. Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - \&quot;latest\&quot;: picks the highest valid Kubernetes version - \&quot;1.X\&quot;: picks the highest valid patch+gke.N patch in the 1.X version - \&quot;1.X.Y\&quot;: picks the highest valid gke.N patch in the 1.X.Y version - \&quot;1.X.Y-gke.N\&quot;: picks an explicit Kubernetes version - \&quot;-\&quot;: picks the default Kubernetes version |  [optional] |
|**desiredMeshCertificates** | [**MeshCertificates**](MeshCertificates.md) |  |  [optional] |
|**desiredMonitoringConfig** | [**MonitoringConfig**](MonitoringConfig.md) |  |  [optional] |
|**desiredMonitoringService** | **String** | The monitoring service the cluster should use to write metrics. Currently available options: * \&quot;monitoring.googleapis.com/kubernetes\&quot; - The Cloud Monitoring service with a Kubernetes-native resource model * &#x60;monitoring.googleapis.com&#x60; - The legacy Cloud Monitoring service (no longer available as of GKE 1.15). * &#x60;none&#x60; - No metrics will be exported from the cluster. If left as an empty string,&#x60;monitoring.googleapis.com/kubernetes&#x60; will be used for GKE 1.14+ or &#x60;monitoring.googleapis.com&#x60; for earlier versions. |  [optional] |
|**desiredNetworkPerformanceConfig** | [**ClusterNetworkPerformanceConfig**](ClusterNetworkPerformanceConfig.md) |  |  [optional] |
|**desiredNodePoolAutoConfigNetworkTags** | [**NetworkTags**](NetworkTags.md) |  |  [optional] |
|**desiredNodePoolAutoConfigResourceManagerTags** | [**ResourceManagerTags**](ResourceManagerTags.md) |  |  [optional] |
|**desiredNodePoolAutoscaling** | [**NodePoolAutoscaling**](NodePoolAutoscaling.md) |  |  [optional] |
|**desiredNodePoolId** | **String** | The node pool to be upgraded. This field is mandatory if \&quot;desired_node_version\&quot;, \&quot;desired_image_family\&quot;, \&quot;desired_node_pool_autoscaling\&quot;, or \&quot;desired_workload_metadata_config\&quot; is specified and there is more than one node pool on the cluster. |  [optional] |
|**desiredNodePoolLoggingConfig** | [**NodePoolLoggingConfig**](NodePoolLoggingConfig.md) |  |  [optional] |
|**desiredNodeVersion** | **String** | The Kubernetes version to change the nodes to (typically an upgrade). Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - \&quot;latest\&quot;: picks the highest valid Kubernetes version - \&quot;1.X\&quot;: picks the highest valid patch+gke.N patch in the 1.X version - \&quot;1.X.Y\&quot;: picks the highest valid gke.N patch in the 1.X.Y version - \&quot;1.X.Y-gke.N\&quot;: picks an explicit Kubernetes version - \&quot;-\&quot;: picks the Kubernetes master version |  [optional] |
|**desiredNotificationConfig** | [**NotificationConfig**](NotificationConfig.md) |  |  [optional] |
|**desiredParentProductConfig** | [**ParentProductConfig**](ParentProductConfig.md) |  |  [optional] |
|**desiredPodSecurityPolicyConfig** | [**PodSecurityPolicyConfig**](PodSecurityPolicyConfig.md) |  |  [optional] |
|**desiredPrivateClusterConfig** | [**PrivateClusterConfig**](PrivateClusterConfig.md) |  |  [optional] |
|**desiredPrivateIpv6GoogleAccess** | [**DesiredPrivateIpv6GoogleAccessEnum**](#DesiredPrivateIpv6GoogleAccessEnum) | The desired state of IPv6 connectivity to Google Services. |  [optional] |
|**desiredProtectConfig** | [**ProtectConfig**](ProtectConfig.md) |  |  [optional] |
|**desiredReleaseChannel** | [**ReleaseChannel**](ReleaseChannel.md) |  |  [optional] |
|**desiredResourceUsageExportConfig** | [**ResourceUsageExportConfig**](ResourceUsageExportConfig.md) |  |  [optional] |
|**desiredSecurityPostureConfig** | [**SecurityPostureConfig**](SecurityPostureConfig.md) |  |  [optional] |
|**desiredServiceExternalIpsConfig** | [**ServiceExternalIPsConfig**](ServiceExternalIPsConfig.md) |  |  [optional] |
|**desiredShieldedNodes** | [**ShieldedNodes**](ShieldedNodes.md) |  |  [optional] |
|**desiredStackType** | [**DesiredStackTypeEnum**](#DesiredStackTypeEnum) | The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type. |  [optional] |
|**desiredTpuConfig** | [**TpuConfig**](TpuConfig.md) |  |  [optional] |
|**desiredVerticalPodAutoscaling** | [**VerticalPodAutoscaling**](VerticalPodAutoscaling.md) |  |  [optional] |
|**desiredWorkloadAltsConfig** | [**WorkloadALTSConfig**](WorkloadALTSConfig.md) |  |  [optional] |
|**desiredWorkloadCertificates** | [**WorkloadCertificates**](WorkloadCertificates.md) |  |  [optional] |
|**desiredWorkloadIdentityConfig** | [**WorkloadIdentityConfig**](WorkloadIdentityConfig.md) |  |  [optional] |
|**enableK8sBetaApis** | [**K8sBetaAPIConfig**](K8sBetaAPIConfig.md) |  |  [optional] |
|**etag** | **String** | The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned. |  [optional] |
|**removedAdditionalPodRangesConfig** | [**AdditionalPodRangesConfig**](AdditionalPodRangesConfig.md) |  |  [optional] |



## Enum: DesiredDatapathProviderEnum

| Name | Value |
|---- | -----|
| DATAPATH_PROVIDER_UNSPECIFIED | &quot;DATAPATH_PROVIDER_UNSPECIFIED&quot; |
| LEGACY_DATAPATH | &quot;LEGACY_DATAPATH&quot; |
| ADVANCED_DATAPATH | &quot;ADVANCED_DATAPATH&quot; |



## Enum: DesiredInTransitEncryptionConfigEnum

| Name | Value |
|---- | -----|
| CONFIG_UNSPECIFIED | &quot;IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED&quot; |
| DISABLED | &quot;IN_TRANSIT_ENCRYPTION_DISABLED&quot; |
| INTER_NODE_TRANSPARENT | &quot;IN_TRANSIT_ENCRYPTION_INTER_NODE_TRANSPARENT&quot; |



## Enum: DesiredPrivateIpv6GoogleAccessEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED&quot; |
| DISABLED | &quot;PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED&quot; |
| TO_GOOGLE | &quot;PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE&quot; |
| BIDIRECTIONAL | &quot;PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL&quot; |



## Enum: DesiredStackTypeEnum

| Name | Value |
|---- | -----|
| STACK_TYPE_UNSPECIFIED | &quot;STACK_TYPE_UNSPECIFIED&quot; |
| IPV4 | &quot;IPV4&quot; |
| IPV4_IPV6 | &quot;IPV4_IPV6&quot; |



