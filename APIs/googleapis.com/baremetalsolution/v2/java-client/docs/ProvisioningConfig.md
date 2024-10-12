

# ProvisioningConfig

A provisioning configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudConsoleUri** | **String** | Output only. URI to Cloud Console UI view of this provisioning config. |  [optional] [readonly] |
|**customId** | **String** | Optional. The user-defined identifier of the provisioning config. |  [optional] |
|**email** | **String** | Email provided to send a confirmation with provisioning config to. Deprecated in favour of email field in request messages. |  [optional] |
|**handoverServiceAccount** | **String** | A service account to enable customers to access instance credentials upon handover. |  [optional] |
|**instances** | [**List&lt;InstanceConfig&gt;**](InstanceConfig.md) | Instances to be created. |  [optional] |
|**location** | **String** | Optional. Location name of this ProvisioningConfig. It is optional only for Intake UI transition period. |  [optional] |
|**name** | **String** | Output only. The system-generated name of the provisioning config. This follows the UUID format. |  [optional] [readonly] |
|**networks** | [**List&lt;NetworkConfig&gt;**](NetworkConfig.md) | Networks to be created. |  [optional] |
|**pod** | **String** | Optional. Pod name. Pod is an independent part of infrastructure. Instance can be connected to the assets (networks, volumes, nfsshares) allocated in the same pod only. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of ProvisioningConfig. |  [optional] [readonly] |
|**statusMessage** | **String** | Optional status messages associated with the FAILED state. |  [optional] |
|**ticketId** | **String** | A generated ticket id to track provisioning request. |  [optional] |
|**updateTime** | **String** | Output only. Last update timestamp. |  [optional] [readonly] |
|**volumes** | [**List&lt;VolumeConfig&gt;**](VolumeConfig.md) | Volumes to be created. |  [optional] |
|**vpcScEnabled** | **Boolean** | If true, VPC SC is enabled for the cluster. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| DRAFT | &quot;DRAFT&quot; |
| SUBMITTED | &quot;SUBMITTED&quot; |
| PROVISIONING | &quot;PROVISIONING&quot; |
| PROVISIONED | &quot;PROVISIONED&quot; |
| VALIDATED | &quot;VALIDATED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| FAILED | &quot;FAILED&quot; |



