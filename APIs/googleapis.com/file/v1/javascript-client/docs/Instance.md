# CloudFilestoreApi.Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the instance was created. | [optional] [readonly] 
**description** | **String** | The description of the instance (2048 characters or less). | [optional] 
**etag** | **String** | Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other. | [optional] 
**fileShares** | [**[FileShareConfig]**](FileShareConfig.md) | File system shares on the instance. For this version, only a single file share is supported. | [optional] 
**kmsKeyName** | **String** | KMS key name used for data encryption. | [optional] 
**labels** | **{String: String}** | Resource labels to represent user provided metadata. | [optional] 
**name** | **String** | Output only. The resource name of the instance, in the format &#x60;projects/{project}/locations/{location}/instances/{instance}&#x60;. | [optional] [readonly] 
**networks** | [**[NetworkConfig]**](NetworkConfig.md) | VPC networks to which the instance is connected. For this version, only a single network is supported. | [optional] 
**satisfiesPzi** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**state** | **String** | Output only. The instance state. | [optional] [readonly] 
**statusMessage** | **String** | Output only. Additional information about the instance state, if available. | [optional] [readonly] 
**suspensionReasons** | **[String]** | Output only. Field indicates all the reasons the instance is in \&quot;SUSPENDED\&quot; state. | [optional] [readonly] 
**tier** | **String** | The service tier of the instance. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `REPAIRING` (value: `"REPAIRING"`)

* `DELETING` (value: `"DELETING"`)

* `ERROR` (value: `"ERROR"`)

* `RESTORING` (value: `"RESTORING"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `SUSPENDING` (value: `"SUSPENDING"`)

* `RESUMING` (value: `"RESUMING"`)

* `REVERTING` (value: `"REVERTING"`)





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




