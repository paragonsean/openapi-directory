

# VmwareNodePool

Resource VmwareNodePool represents a VMware node pool. ##

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Annotations on the node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |  [optional] |
|**config** | [**VmwareNodeConfig**](VmwareNodeConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time at which this node pool was created. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. The time at which this node pool was deleted. If the resource is not deleted, this must be empty |  [optional] [readonly] |
|**displayName** | **String** | The display name for the node pool. |  [optional] |
|**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |  [optional] |
|**name** | **String** | Immutable. The resource name of this node pool. |  [optional] |
|**nodePoolAutoscaling** | [**VmwareNodePoolAutoscalingConfig**](VmwareNodePoolAutoscalingConfig.md) |  |  [optional] |
|**onPremVersion** | **String** | Anthos version for the node pool. Defaults to the user cluster version. |  [optional] |
|**reconciling** | **Boolean** | Output only. If set, there are currently changes in flight to the node pool. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the node pool. |  [optional] [readonly] |
|**status** | [**ResourceStatus**](ResourceStatus.md) |  |  [optional] |
|**uid** | **String** | Output only. The unique identifier of the node pool. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time at which this node pool was last updated. |  [optional] [readonly] |



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



