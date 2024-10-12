

# VmwareAdminCluster

Resource that represents a VMware admin cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addonNode** | [**VmwareAdminAddonNodeConfig**](VmwareAdminAddonNodeConfig.md) |  |  [optional] |
|**annotations** | **Map&lt;String, String&gt;** | Annotations on the VMware admin cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |  [optional] |
|**antiAffinityGroups** | [**VmwareAAGConfig**](VmwareAAGConfig.md) |  |  [optional] |
|**authorization** | [**VmwareAdminAuthorizationConfig**](VmwareAdminAuthorizationConfig.md) |  |  [optional] |
|**autoRepairConfig** | [**VmwareAutoRepairConfig**](VmwareAutoRepairConfig.md) |  |  [optional] |
|**bootstrapClusterMembership** | **String** | The bootstrap cluster this VMware admin cluster belongs to. |  [optional] |
|**controlPlaneNode** | [**VmwareAdminControlPlaneNodeConfig**](VmwareAdminControlPlaneNodeConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time at which VMware admin cluster was created. |  [optional] [readonly] |
|**description** | **String** | A human readable description of this VMware admin cluster. |  [optional] |
|**endpoint** | **String** | Output only. The DNS name of VMware admin cluster&#39;s API server. |  [optional] [readonly] |
|**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |  [optional] |
|**fleet** | [**Fleet**](Fleet.md) |  |  [optional] |
|**imageType** | **String** | The OS image type for the VMware admin cluster. |  [optional] |
|**loadBalancer** | [**VmwareAdminLoadBalancerConfig**](VmwareAdminLoadBalancerConfig.md) |  |  [optional] |
|**localName** | **String** | Output only. The object name of the VMware OnPremAdminCluster custom resource. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs. |  [optional] [readonly] |
|**name** | **String** | Immutable. The VMware admin cluster resource name. |  [optional] |
|**networkConfig** | [**VmwareAdminNetworkConfig**](VmwareAdminNetworkConfig.md) |  |  [optional] |
|**onPremVersion** | **String** | The Anthos clusters on the VMware version for the admin cluster. |  [optional] |
|**platformConfig** | [**VmwarePlatformConfig**](VmwarePlatformConfig.md) |  |  [optional] |
|**preparedSecrets** | [**VmwareAdminPreparedSecretsConfig**](VmwareAdminPreparedSecretsConfig.md) |  |  [optional] |
|**reconciling** | **Boolean** | Output only. If set, there are currently changes in flight to the VMware admin cluster. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of VMware admin cluster. |  [optional] [readonly] |
|**status** | [**ResourceStatus**](ResourceStatus.md) |  |  [optional] |
|**uid** | **String** | Output only. The unique identifier of the VMware admin cluster. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time at which VMware admin cluster was last updated. |  [optional] [readonly] |
|**vcenter** | [**VmwareAdminVCenterConfig**](VmwareAdminVCenterConfig.md) |  |  [optional] |



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



