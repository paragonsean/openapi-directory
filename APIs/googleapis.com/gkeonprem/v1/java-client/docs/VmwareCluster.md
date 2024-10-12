

# VmwareCluster

Resource that represents a VMware user cluster. ##

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminClusterMembership** | **String** | Required. The admin cluster this VMware user cluster belongs to. This is the full resource name of the admin cluster&#39;s fleet membership. In the future, references to other resource types might be allowed if admin clusters are modeled as their own resources. |  [optional] |
|**adminClusterName** | **String** | Output only. The resource name of the VMware admin cluster hosting this user cluster. |  [optional] [readonly] |
|**annotations** | **Map&lt;String, String&gt;** | Annotations on the VMware user cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |  [optional] |
|**antiAffinityGroups** | [**VmwareAAGConfig**](VmwareAAGConfig.md) |  |  [optional] |
|**authorization** | [**Authorization**](Authorization.md) |  |  [optional] |
|**autoRepairConfig** | [**VmwareAutoRepairConfig**](VmwareAutoRepairConfig.md) |  |  [optional] |
|**binaryAuthorization** | [**BinaryAuthorization**](BinaryAuthorization.md) |  |  [optional] |
|**controlPlaneNode** | [**VmwareControlPlaneNodeConfig**](VmwareControlPlaneNodeConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time at which VMware user cluster was created. |  [optional] [readonly] |
|**dataplaneV2** | [**VmwareDataplaneV2Config**](VmwareDataplaneV2Config.md) |  |  [optional] |
|**deleteTime** | **String** | Output only. The time at which VMware user cluster was deleted. |  [optional] [readonly] |
|**description** | **String** | A human readable description of this VMware user cluster. |  [optional] |
|**disableBundledIngress** | **Boolean** | Disable bundled ingress. |  [optional] |
|**enableControlPlaneV2** | **Boolean** | Enable control plane V2. Default to false. |  [optional] |
|**endpoint** | **String** | Output only. The DNS name of VMware user cluster&#39;s API server. |  [optional] [readonly] |
|**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |  [optional] |
|**fleet** | [**Fleet**](Fleet.md) |  |  [optional] |
|**loadBalancer** | [**VmwareLoadBalancerConfig**](VmwareLoadBalancerConfig.md) |  |  [optional] |
|**localName** | **String** | Output only. The object name of the VMware OnPremUserCluster custom resource on the associated admin cluster. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs. |  [optional] [readonly] |
|**name** | **String** | Immutable. The VMware user cluster resource name. |  [optional] |
|**networkConfig** | [**VmwareNetworkConfig**](VmwareNetworkConfig.md) |  |  [optional] |
|**onPremVersion** | **String** | Required. The Anthos clusters on the VMware version for your user cluster. |  [optional] |
|**reconciling** | **Boolean** | Output only. If set, there are currently changes in flight to the VMware user cluster. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of VMware user cluster. |  [optional] [readonly] |
|**status** | [**ResourceStatus**](ResourceStatus.md) |  |  [optional] |
|**storage** | [**VmwareStorageConfig**](VmwareStorageConfig.md) |  |  [optional] |
|**uid** | **String** | Output only. The unique identifier of the VMware user cluster. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time at which VMware user cluster was last updated. |  [optional] [readonly] |
|**upgradePolicy** | [**VmwareClusterUpgradePolicy**](VmwareClusterUpgradePolicy.md) |  |  [optional] |
|**validationCheck** | [**ValidationCheck**](ValidationCheck.md) |  |  [optional] |
|**vcenter** | [**VmwareVCenterConfig**](VmwareVCenterConfig.md) |  |  [optional] |
|**vmTrackingEnabled** | **Boolean** | Enable VM tracking. |  [optional] |



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



