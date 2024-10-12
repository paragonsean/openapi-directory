

# Instance

A Filestore instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when the instance was created. |  [optional] [readonly] |
|**description** | **String** | The description of the instance (2048 characters or less). |  [optional] |
|**etag** | **String** | Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other. |  [optional] |
|**fileShares** | [**List&lt;FileShareConfig&gt;**](FileShareConfig.md) | File system shares on the instance. For this version, only a single file share is supported. |  [optional] |
|**kmsKeyName** | **String** | KMS key name used for data encryption. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Resource labels to represent user provided metadata. |  [optional] |
|**name** | **String** | Output only. The resource name of the instance, in the format &#x60;projects/{project}/locations/{location}/instances/{instance}&#x60;. |  [optional] [readonly] |
|**networks** | [**List&lt;NetworkConfig&gt;**](NetworkConfig.md) | VPC networks to which the instance is connected. For this version, only a single network is supported. |  [optional] |
|**satisfiesPzi** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The instance state. |  [optional] [readonly] |
|**statusMessage** | **String** | Output only. Additional information about the instance state, if available. |  [optional] [readonly] |
|**suspensionReasons** | [**List&lt;SuspensionReasonsEnum&gt;**](#List&lt;SuspensionReasonsEnum&gt;) | Output only. Field indicates all the reasons the instance is in \&quot;SUSPENDED\&quot; state. |  [optional] [readonly] |
|**tier** | [**TierEnum**](#TierEnum) | The service tier of the instance. |  [optional] |



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
| SUSPENDING | &quot;SUSPENDING&quot; |
| RESUMING | &quot;RESUMING&quot; |
| REVERTING | &quot;REVERTING&quot; |



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



