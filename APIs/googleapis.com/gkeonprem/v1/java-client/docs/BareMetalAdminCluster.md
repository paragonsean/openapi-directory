

# BareMetalAdminCluster

Resource that represents a bare metal admin cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Annotations on the bare metal admin cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |  [optional] |
|**bareMetalVersion** | **String** | The Anthos clusters on bare metal version for the bare metal admin cluster. |  [optional] |
|**binaryAuthorization** | [**BinaryAuthorization**](BinaryAuthorization.md) |  |  [optional] |
|**clusterOperations** | [**BareMetalAdminClusterOperationsConfig**](BareMetalAdminClusterOperationsConfig.md) |  |  [optional] |
|**controlPlane** | [**BareMetalAdminControlPlaneConfig**](BareMetalAdminControlPlaneConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time at which this bare metal admin cluster was created. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. The time at which this bare metal admin cluster was deleted. If the resource is not deleted, this must be empty |  [optional] [readonly] |
|**description** | **String** | A human readable description of this bare metal admin cluster. |  [optional] |
|**endpoint** | **String** | Output only. The IP address name of bare metal admin cluster&#39;s API server. |  [optional] [readonly] |
|**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |  [optional] |
|**fleet** | [**Fleet**](Fleet.md) |  |  [optional] |
|**loadBalancer** | [**BareMetalAdminLoadBalancerConfig**](BareMetalAdminLoadBalancerConfig.md) |  |  [optional] |
|**localName** | **String** | Output only. The object name of the bare metal cluster custom resource. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs. |  [optional] [readonly] |
|**maintenanceConfig** | [**BareMetalAdminMaintenanceConfig**](BareMetalAdminMaintenanceConfig.md) |  |  [optional] |
|**maintenanceStatus** | [**BareMetalAdminMaintenanceStatus**](BareMetalAdminMaintenanceStatus.md) |  |  [optional] |
|**name** | **String** | Immutable. The bare metal admin cluster resource name. |  [optional] |
|**networkConfig** | [**BareMetalAdminNetworkConfig**](BareMetalAdminNetworkConfig.md) |  |  [optional] |
|**nodeAccessConfig** | [**BareMetalAdminNodeAccessConfig**](BareMetalAdminNodeAccessConfig.md) |  |  [optional] |
|**nodeConfig** | [**BareMetalAdminWorkloadNodeConfig**](BareMetalAdminWorkloadNodeConfig.md) |  |  [optional] |
|**osEnvironmentConfig** | [**BareMetalAdminOsEnvironmentConfig**](BareMetalAdminOsEnvironmentConfig.md) |  |  [optional] |
|**proxy** | [**BareMetalAdminProxyConfig**](BareMetalAdminProxyConfig.md) |  |  [optional] |
|**reconciling** | **Boolean** | Output only. If set, there are currently changes in flight to the bare metal Admin Cluster. |  [optional] [readonly] |
|**securityConfig** | [**BareMetalAdminSecurityConfig**](BareMetalAdminSecurityConfig.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the bare metal admin cluster. |  [optional] [readonly] |
|**status** | [**ResourceStatus**](ResourceStatus.md) |  |  [optional] |
|**storage** | [**BareMetalAdminStorageConfig**](BareMetalAdminStorageConfig.md) |  |  [optional] |
|**uid** | **String** | Output only. The unique identifier of the bare metal admin cluster. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time at which this bare metal admin cluster was last updated. |  [optional] [readonly] |
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



