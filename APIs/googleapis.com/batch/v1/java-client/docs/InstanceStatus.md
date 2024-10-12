

# InstanceStatus

VM instance status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootDisk** | [**Disk**](Disk.md) |  |  [optional] |
|**machineType** | **String** | The Compute Engine machine type. |  [optional] |
|**provisioningModel** | [**ProvisioningModelEnum**](#ProvisioningModelEnum) | The VM instance provisioning model. |  [optional] |
|**taskPack** | **String** | The max number of tasks can be assigned to this instance type. |  [optional] |



## Enum: ProvisioningModelEnum

| Name | Value |
|---- | -----|
| PROVISIONING_MODEL_UNSPECIFIED | &quot;PROVISIONING_MODEL_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| SPOT | &quot;SPOT&quot; |
| PREEMPTIBLE | &quot;PREEMPTIBLE&quot; |



