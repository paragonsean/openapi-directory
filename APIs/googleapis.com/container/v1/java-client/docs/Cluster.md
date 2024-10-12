

# Cluster

A Google Kubernetes Engine cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addonsConfig** | [**AddonsConfig**](AddonsConfig.md) |  |  [optional] |
|**authenticatorGroupsConfig** | [**AuthenticatorGroupsConfig**](AuthenticatorGroupsConfig.md) |  |  [optional] |
|**autopilot** | [**Autopilot**](Autopilot.md) |  |  [optional] |
|**autoscaling** | [**ClusterAutoscaling**](ClusterAutoscaling.md) |  |  [optional] |
|**binaryAuthorization** | [**BinaryAuthorization**](BinaryAuthorization.md) |  |  [optional] |
|**clusterIpv4Cidr** | **String** | The IP address range of the container pods in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. &#x60;10.96.0.0/14&#x60;). Leave blank to have one automatically chosen or specify a &#x60;/14&#x60; block in &#x60;10.0.0.0/8&#x60;. |  [optional] |
|**conditions** | [**List&lt;StatusCondition&gt;**](StatusCondition.md) | Which conditions caused the current cluster state. |  [optional] |
|**confidentialNodes** | [**ConfidentialNodes**](ConfidentialNodes.md) |  |  [optional] |
|**costManagementConfig** | [**CostManagementConfig**](CostManagementConfig.md) |  |  [optional] |
|**createTime** | **String** | [Output only] The time the cluster was created, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |  [optional] |
|**currentMasterVersion** | **String** | [Output only] The current software version of the master endpoint. |  [optional] |
|**currentNodeCount** | **Integer** | [Output only] The number of nodes currently in the cluster. Deprecated. Call Kubernetes API directly to retrieve node information. |  [optional] |
|**currentNodeVersion** | **String** | [Output only] Deprecated, use [NodePools.version](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools) instead. The current version of the node software components. If they are currently at multiple versions because they&#39;re in the process of being upgraded, this reflects the minimum version of all nodes. |  [optional] |
|**databaseEncryption** | [**DatabaseEncryption**](DatabaseEncryption.md) |  |  [optional] |
|**defaultMaxPodsConstraint** | [**MaxPodsConstraint**](MaxPodsConstraint.md) |  |  [optional] |
|**description** | **String** | An optional description of this cluster. |  [optional] |
|**enableK8sBetaApis** | [**K8sBetaAPIConfig**](K8sBetaAPIConfig.md) |  |  [optional] |
|**enableKubernetesAlpha** | **Boolean** | Kubernetes alpha features are enabled on this cluster. This includes alpha API groups (e.g. v1alpha1) and features that may not be production ready in the kubernetes version of the master and nodes. The cluster has no SLA for uptime and master/node upgrades are disabled. Alpha enabled clusters are automatically deleted thirty days after creation. |  [optional] |
|**enableTpu** | **Boolean** | Enable the ability to use Cloud TPUs in this cluster. |  [optional] |
|**endpoint** | **String** | [Output only] The IP address of this cluster&#39;s master endpoint. The endpoint can be accessed from the internet at &#x60;https://username:password@endpoint/&#x60;. See the &#x60;masterAuth&#x60; property of this resource for username and password information. |  [optional] |
|**enterpriseConfig** | [**EnterpriseConfig**](EnterpriseConfig.md) |  |  [optional] |
|**etag** | **String** | This checksum is computed by the server based on the value of cluster fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding. |  [optional] |
|**expireTime** | **String** | [Output only] The time the cluster will be automatically deleted in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |  [optional] |
|**fleet** | [**Fleet**](Fleet.md) |  |  [optional] |
|**id** | **String** | Output only. Unique id for the cluster. |  [optional] [readonly] |
|**identityServiceConfig** | [**IdentityServiceConfig**](IdentityServiceConfig.md) |  |  [optional] |
|**initialClusterVersion** | **String** | The initial Kubernetes version for this cluster. Valid versions are those found in validMasterVersions returned by getServerConfig. The version can be upgraded over time; such upgrades are reflected in currentMasterVersion and currentNodeVersion. Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - \&quot;latest\&quot;: picks the highest valid Kubernetes version - \&quot;1.X\&quot;: picks the highest valid patch+gke.N patch in the 1.X version - \&quot;1.X.Y\&quot;: picks the highest valid gke.N patch in the 1.X.Y version - \&quot;1.X.Y-gke.N\&quot;: picks an explicit Kubernetes version - \&quot;\&quot;,\&quot;-\&quot;: picks the default Kubernetes version |  [optional] |
|**initialNodeCount** | **Integer** | The number of nodes to create in this cluster. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. For requests, this field should only be used in lieu of a \&quot;node_pool\&quot; object, since this configuration (along with the \&quot;node_config\&quot;) will be used to create a \&quot;NodePool\&quot; object with an auto-generated name. Do not use this and a node_pool at the same time. This field is deprecated, use node_pool.initial_node_count instead. |  [optional] |
|**instanceGroupUrls** | **List&lt;String&gt;** | Deprecated. Use node_pools.instance_group_urls. |  [optional] |
|**ipAllocationPolicy** | [**IPAllocationPolicy**](IPAllocationPolicy.md) |  |  [optional] |
|**labelFingerprint** | **String** | The fingerprint of the set of labels for this cluster. |  [optional] |
|**legacyAbac** | [**LegacyAbac**](LegacyAbac.md) |  |  [optional] |
|**location** | **String** | [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides. |  [optional] |
|**locations** | **List&lt;String&gt;** | The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster&#39;s nodes should be located. This field provides a default value if [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) are not specified during node pool creation. Warning: changing cluster locations will update the [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) of all node pools and will result in nodes being added and/or removed. |  [optional] |
|**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  |  [optional] |
|**loggingService** | **String** | The logging service the cluster should use to write logs. Currently available options: * &#x60;logging.googleapis.com/kubernetes&#x60; - The Cloud Logging service with a Kubernetes-native resource model * &#x60;logging.googleapis.com&#x60; - The legacy Cloud Logging service (no longer available as of GKE 1.15). * &#x60;none&#x60; - no logs will be exported from the cluster. If left as an empty string,&#x60;logging.googleapis.com/kubernetes&#x60; will be used for GKE 1.14+ or &#x60;logging.googleapis.com&#x60; for earlier versions. |  [optional] |
|**maintenancePolicy** | [**MaintenancePolicy**](MaintenancePolicy.md) |  |  [optional] |
|**masterAuth** | [**MasterAuth**](MasterAuth.md) |  |  [optional] |
|**masterAuthorizedNetworksConfig** | [**MasterAuthorizedNetworksConfig**](MasterAuthorizedNetworksConfig.md) |  |  [optional] |
|**meshCertificates** | [**MeshCertificates**](MeshCertificates.md) |  |  [optional] |
|**monitoringConfig** | [**MonitoringConfig**](MonitoringConfig.md) |  |  [optional] |
|**monitoringService** | **String** | The monitoring service the cluster should use to write metrics. Currently available options: * \&quot;monitoring.googleapis.com/kubernetes\&quot; - The Cloud Monitoring service with a Kubernetes-native resource model * &#x60;monitoring.googleapis.com&#x60; - The legacy Cloud Monitoring service (no longer available as of GKE 1.15). * &#x60;none&#x60; - No metrics will be exported from the cluster. If left as an empty string,&#x60;monitoring.googleapis.com/kubernetes&#x60; will be used for GKE 1.14+ or &#x60;monitoring.googleapis.com&#x60; for earlier versions. |  [optional] |
|**name** | **String** | The name of this cluster. The name must be unique within this project and location (e.g. zone or region), and can be up to 40 characters with the following restrictions: * Lowercase letters, numbers, and hyphens only. * Must start with a letter. * Must end with a number or a letter. |  [optional] |
|**network** | **String** | The name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the cluster is connected. If left unspecified, the &#x60;default&#x60; network will be used. |  [optional] |
|**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  |  [optional] |
|**networkPolicy** | [**NetworkPolicy**](NetworkPolicy.md) |  |  [optional] |
|**nodeConfig** | [**NodeConfig**](NodeConfig.md) |  |  [optional] |
|**nodeIpv4CidrSize** | **Integer** | [Output only] The size of the address space on each node for hosting containers. This is provisioned from within the &#x60;container_ipv4_cidr&#x60; range. This field will only be set when cluster is in route-based network mode. |  [optional] |
|**nodePoolAutoConfig** | [**NodePoolAutoConfig**](NodePoolAutoConfig.md) |  |  [optional] |
|**nodePoolDefaults** | [**NodePoolDefaults**](NodePoolDefaults.md) |  |  [optional] |
|**nodePools** | [**List&lt;NodePool&gt;**](NodePool.md) | The node pools associated with this cluster. This field should not be set if \&quot;node_config\&quot; or \&quot;initial_node_count\&quot; are specified. |  [optional] |
|**notificationConfig** | [**NotificationConfig**](NotificationConfig.md) |  |  [optional] |
|**parentProductConfig** | [**ParentProductConfig**](ParentProductConfig.md) |  |  [optional] |
|**privateClusterConfig** | [**PrivateClusterConfig**](PrivateClusterConfig.md) |  |  [optional] |
|**releaseChannel** | [**ReleaseChannel**](ReleaseChannel.md) |  |  [optional] |
|**resourceLabels** | **Map&lt;String, String&gt;** | The resource labels for the cluster to use to annotate any related Google Compute Engine resources. |  [optional] |
|**resourceUsageExportConfig** | [**ResourceUsageExportConfig**](ResourceUsageExportConfig.md) |  |  [optional] |
|**securityPostureConfig** | [**SecurityPostureConfig**](SecurityPostureConfig.md) |  |  [optional] |
|**selfLink** | **String** | [Output only] Server-defined URL for the resource. |  [optional] |
|**servicesIpv4Cidr** | **String** | [Output only] The IP address range of the Kubernetes services in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. &#x60;1.2.3.4/29&#x60;). Service addresses are typically put in the last &#x60;/16&#x60; from the container CIDR. |  [optional] |
|**shieldedNodes** | [**ShieldedNodes**](ShieldedNodes.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | [Output only] The current status of this cluster. |  [optional] |
|**statusMessage** | **String** | [Output only] Deprecated. Use conditions instead. Additional information about the current status of this cluster, if available. |  [optional] |
|**subnetwork** | **String** | The name of the Google Compute Engine [subnetwork](https://cloud.google.com/compute/docs/subnetworks) to which the cluster is connected. |  [optional] |
|**tpuIpv4CidrBlock** | **String** | [Output only] The IP address range of the Cloud TPUs in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. &#x60;1.2.3.4/29&#x60;). |  [optional] |
|**verticalPodAutoscaling** | [**VerticalPodAutoscaling**](VerticalPodAutoscaling.md) |  |  [optional] |
|**workloadIdentityConfig** | [**WorkloadIdentityConfig**](WorkloadIdentityConfig.md) |  |  [optional] |
|**zone** | **String** | [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field is deprecated, use location instead. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| PROVISIONING | &quot;PROVISIONING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| RECONCILING | &quot;RECONCILING&quot; |
| STOPPING | &quot;STOPPING&quot; |
| ERROR | &quot;ERROR&quot; |
| DEGRADED | &quot;DEGRADED&quot; |



