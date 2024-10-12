

# BatchAccountProperties

Account specific properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountEndpoint** | **String** | The account endpoint used to interact with the Batch service. |  [optional] [readonly] |
|**activeJobAndJobScheduleQuota** | **Integer** |  |  [optional] [readonly] |
|**autoStorage** | [**AutoStorageProperties**](AutoStorageProperties.md) |  |  [optional] |
|**dedicatedCoreQuota** | **Integer** |  |  [optional] [readonly] |
|**keyVaultReference** | [**KeyVaultReference**](KeyVaultReference.md) |  |  [optional] |
|**lowPriorityCoreQuota** | **Integer** |  |  [optional] [readonly] |
|**poolAllocationMode** | **PoolAllocationMode** |  |  [optional] |
|**poolQuota** | **Integer** |  |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioned state of the resource |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELLED | &quot;Cancelled&quot; |



