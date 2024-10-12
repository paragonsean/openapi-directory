

# PlatformImageProperties

Properties of platform image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataDisks** | [**List&lt;DataDisk&gt;**](DataDisk.md) | Data disks used by the platform image. |  [optional] |
|**details** | [**ImageDetails**](ImageDetails.md) |  |  [optional] |
|**osDisk** | [**OsDisk**](OsDisk.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELED | &quot;Canceled&quot; |



