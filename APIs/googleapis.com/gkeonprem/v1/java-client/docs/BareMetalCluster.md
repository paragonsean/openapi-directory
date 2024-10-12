

# BareMetalCluster

Resource that represents a bare metal user cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminClusterMembership** | **String** | Required. The admin cluster this bare metal user cluster belongs to. This is the full resource name of the admin cluster&#39;s fleet membership. |  [optional] |
|**adminClusterName** | **String** | Output only. The resource name of the bare metal admin cluster managing this user cluster. |  [optional] [readonly] |
|**annotations** | **Map&lt;String, String&gt;** | Annotations on the bare metal user cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |  [optional] |
|**bareMetalVersion** | **String** | Required. The Anthos clusters on bare metal version for your user cluster. |  [optional] |
|**binaryAuthorization** | [**BinaryAuthorization**](BinaryAuthorization.md) |  |  [optional] |
|**clusterOperations** | [**BareMetalClusterOperationsConfig**](BareMetalClusterOperationsConfig.md) |  |  [optional] |
|**controlPlane** | [**BareMetalControlPlaneConfig**](BareMetalControlPlaneConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time when the bare metal user cluster was created. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. The time when the bare metal user cluster was deleted. If the resource is not deleted, this must be empty |  [optional] [readonly] |
|**description** | **String** | A human readable description of this bare metal user cluster. |  [optional] |
|**endpoint** | **String** | Output only. The IP address of the bare metal user cluster&#39;s API server. |  [optional] [readonly] |
|**etag** | **String** | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |  [optional] [readonly] |
|**fleet** | [**Fleet**](Fleet.md) |  |  [optional] |
|**loadBalancer** | [**BareMetalLoadBalancerConfig**](BareMetalLoadBalancerConfig.md) |  |  [optional] |
|**localName** | **String** | Output only. The object name of the bare metal user cluster custom resource on the associated admin cluster. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the name in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. When the local name and cluster name differ, the local name is used in the admin cluster controller logs. You use the cluster name when accessing the cluster using bmctl and kubectl. |  [optional] [readonly] |
|**maintenanceConfig** | [**BareMetalMaintenanceConfig**](BareMetalMaintenanceConfig.md) |  |  [optional] |
|**maintenanceStatus** | [**BareMetalMaintenanceStatus**](BareMetalMaintenanceStatus.md) |  |  [optional] |
|**name** | **String** | Immutable. The bare metal user cluster resource name. |  [optional] |
|**networkConfig** | [**BareMetalNetworkConfig**](BareMetalNetworkConfig.md) |  |  [optional] |
|**nodeAccessConfig** | [**BareMetalNodeAccessConfig**](BareMetalNodeAccessConfig.md) |  |  [optional] |
|**nodeConfig** | [**BareMetalWorkloadNodeConfig**](BareMetalWorkloadNodeConfig.md) |  |  [optional] |
|**osEnvironmentConfig** | [**BareMetalOsEnvironmentConfig**](BareMetalOsEnvironmentConfig.md) |  |  [optional] |
|**proxy** | [**BareMetalProxyConfig**](BareMetalProxyConfig.md) |  |  [optional] |
|**reconciling** | **Boolean** | Output only. If set, there are currently changes in flight to the bare metal user cluster. |  [optional] [readonly] |
|**securityConfig** | [**BareMetalSecurityConfig**](BareMetalSecurityConfig.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the bare metal user cluster. |  [optional] [readonly] |
|**status** | [**ResourceStatus**](ResourceStatus.md) |  |  [optional] |
|**storage** | [**BareMetalStorageConfig**](BareMetalStorageConfig.md) |  |  [optional] |
|**uid** | **String** | Output only. The unique identifier of the bare metal user cluster. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the bare metal user cluster was last updated. |  [optional] [readonly] |
|**upgradePolicy** | [**BareMetalClusterUpgradePolicy**](BareMetalClusterUpgradePolicy.md) |  |  [optional] |
|**validationCheck** | [**ValidationCheck**](ValidationCheck.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PROVISIONING | &quot;PROVISIONING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| RECONCILING | &quot;RECONCILING&quot; |
| STOPPING | &quot;STOPPING&quot; |
| ERROR | &quot;ERROR&quot; |
| DEGRADED | &quot;DEGRADED&quot; |



