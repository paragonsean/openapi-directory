# CloudFilestoreApi.Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacityGb** | **String** | The storage capacity of the instance in gigabytes (GB &#x3D; 1024^3 bytes). This capacity can be increased up to &#x60;max_capacity_gb&#x60; GB in multipliers of &#x60;capacity_step_size_gb&#x60; GB. | [optional] 
**capacityStepSizeGb** | **String** | Output only. The increase/decrease capacity step size. | [optional] [readonly] 
**createTime** | **String** | Output only. The time when the instance was created. | [optional] [readonly] 
**description** | **String** | The description of the instance (2048 characters or less). | [optional] 
**directoryServices** | [**DirectoryServicesConfig**](DirectoryServicesConfig.md) |  | [optional] 
**etag** | **String** | Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other. | [optional] 
**fileShares** | [**[FileShareConfig]**](FileShareConfig.md) | File system shares on the instance. For this version, only a single file share is supported. | [optional] 
**kmsKeyName** | **String** | KMS key name used for data encryption. | [optional] 
**labels** | **{String: String}** | Resource labels to represent user provided metadata. | [optional] 
**maxCapacityGb** | **String** | Output only. The max capacity of the instance. | [optional] [readonly] 
**maxShareCount** | **String** | The max number of shares allowed. | [optional] 
**multiShareEnabled** | **Boolean** | Indicates whether this instance uses a multi-share configuration with which it can have more than one file-share or none at all. File-shares are added, updated and removed through the separate file-share APIs. | [optional] 
**name** | **String** | Output only. The resource name of the instance, in the format &#x60;projects/{project_id}/locations/{location_id}/instances/{instance_id}&#x60;. | [optional] [readonly] 
**networks** | [**[NetworkConfig]**](NetworkConfig.md) | VPC networks to which the instance is connected. For this version, only a single network is supported. | [optional] 
**protocol** | **String** | Immutable. The protocol indicates the access protocol for all shares in the instance. This field is immutable and it cannot be changed after the instance has been created. Default value: &#x60;NFS_V3&#x60;. | [optional] 
**satisfiesPzi** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**state** | **String** | Output only. The instance state. | [optional] [readonly] 
**statusMessage** | **String** | Output only. Additional information about the instance state, if available. | [optional] [readonly] 
**suspensionReasons** | **[String]** | Output only. Field indicates all the reasons the instance is in \&quot;SUSPENDED\&quot; state. | [optional] [readonly] 
**tier** | **String** | The service tier of the instance. | [optional] 



## Enum: ProtocolEnum


* `FILE_PROTOCOL_UNSPECIFIED` (value: `"FILE_PROTOCOL_UNSPECIFIED"`)

* `NFS_V3` (value: `"NFS_V3"`)

* `NFS_V4_1` (value: `"NFS_V4_1"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `REPAIRING` (value: `"REPAIRING"`)

* `DELETING` (value: `"DELETING"`)

* `ERROR` (value: `"ERROR"`)

* `RESTORING` (value: `"RESTORING"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `REVERTING` (value: `"REVERTING"`)

* `SUSPENDING` (value: `"SUSPENDING"`)

* `RESUMING` (value: `"RESUMING"`)





## Enum: [SuspensionReasonsEnum]


* `SUSPENSION_REASON_UNSPECIFIED` (value: `"SUSPENSION_REASON_UNSPECIFIED"`)

* `KMS_KEY_ISSUE` (value: `"KMS_KEY_ISSUE"`)





## Enum: TierEnum


* `TIER_UNSPECIFIED` (value: `"TIER_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `PREMIUM` (value: `"PREMIUM"`)

* `BASIC_HDD` (value: `"BASIC_HDD"`)

* `BASIC_SSD` (value: `"BASIC_SSD"`)

* `HIGH_SCALE_SSD` (value: `"HIGH_SCALE_SSD"`)

* `ENTERPRISE` (value: `"ENTERPRISE"`)

* `ZONAL` (value: `"ZONAL"`)

* `REGIONAL` (value: `"REGIONAL"`)




