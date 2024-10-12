

# Instance

A Filestore instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacityGb** | **String** | The storage capacity of the instance in gigabytes (GB &#x3D; 1024^3 bytes). This capacity can be increased up to &#x60;max_capacity_gb&#x60; GB in multipliers of &#x60;capacity_step_size_gb&#x60; GB. |  [optional] |
|**capacityStepSizeGb** | **String** | Output only. The increase/decrease capacity step size. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The time when the instance was created. |  [optional] [readonly] |
|**description** | **String** | The description of the instance (2048 characters or less). |  [optional] |
|**directoryServices** | [**DirectoryServicesConfig**](DirectoryServicesConfig.md) |  |  [optional] |
|**etag** | **String** | Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other. |  [optional] |
|**fileShares** | [**List&lt;FileShareConfig&gt;**](FileShareConfig.md) | File system shares on the instance. For this version, only a single file share is supported. |  [optional] |
|**kmsKeyName** | **String** | KMS key name used for data encryption. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Resource labels to represent user provided metadata. |  [optional] |
|**maxCapacityGb** | **String** | Output only. The max capacity of the instance. |  [optional] [readonly] |
|**maxShareCount** | **String** | The max number of shares allowed. |  [optional] |
|**multiShareEnabled** | **Boolean** | Indicates whether this instance uses a multi-share configuration with which it can have more than one file-share or none at all. File-shares are added, updated and removed through the separate file-share APIs. |  [optional] |
|**name** | **String** | Output only. The resource name of the instance, in the format &#x60;projects/{project_id}/locations/{location_id}/instances/{instance_id}&#x60;. |  [optional] [readonly] |
|**networks** | [**List&lt;NetworkConfig&gt;**](NetworkConfig.md) | VPC networks to which the instance is connected. For this version, only a single network is supported. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Immutable. The protocol indicates the access protocol for all shares in the instance. This field is immutable and it cannot be changed after the instance has been created. Default value: &#x60;NFS_V3&#x60;. |  [optional] |
|**satisfiesPzi** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The instance state. |  [optional] [readonly] |
|**statusMessage** | **String** | Output only. Additional information about the instance state, if available. |  [optional] [readonly] |
|**suspensionReasons** | [**List&lt;SuspensionReasonsEnum&gt;**](#List&lt;SuspensionReasonsEnum&gt;) | Output only. Field indicates all the reasons the instance is in \&quot;SUSPENDED\&quot; state. |  [optional] [readonly] |
|**tier** | [**TierEnum**](#TierEnum) | The service tier of the instance. |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| FILE_PROTOCOL_UNSPECIFIED | &quot;FILE_PROTOCOL_UNSPECIFIED&quot; |
| NFS_V3 | &quot;NFS_V3&quot; |
| NFS_V4_1 | &quot;NFS_V4_1&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| REPAIRING | &quot;REPAIRING&quot; |
| DELETING | &quot;DELETING&quot; |
| ERROR | &quot;ERROR&quot; |
| RESTORING | &quot;RESTORING&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| REVERTING | &quot;REVERTING&quot; |
| SUSPENDING | &quot;SUSPENDING&quot; |
| RESUMING | &quot;RESUMING&quot; |



## Enum: List&lt;SuspensionReasonsEnum&gt;

| Name | Value |
|---- | -----|
| SUSPENSION_REASON_UNSPECIFIED | &quot;SUSPENSION_REASON_UNSPECIFIED&quot; |
| KMS_KEY_ISSUE | &quot;KMS_KEY_ISSUE&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| TIER_UNSPECIFIED | &quot;TIER_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| PREMIUM | &quot;PREMIUM&quot; |
| BASIC_HDD | &quot;BASIC_HDD&quot; |
| BASIC_SSD | &quot;BASIC_SSD&quot; |
| HIGH_SCALE_SSD | &quot;HIGH_SCALE_SSD&quot; |
| ENTERPRISE | &quot;ENTERPRISE&quot; |
| ZONAL | &quot;ZONAL&quot; |
| REGIONAL | &quot;REGIONAL&quot; |



