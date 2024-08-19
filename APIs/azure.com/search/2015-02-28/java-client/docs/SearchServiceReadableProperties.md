

# SearchServiceReadableProperties

Defines all the properties of an Azure Search service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**partitionCount** | **Integer** | The number of partitions in the Search service; if specified, it can be 1, 2, 3, 4, 6, or 12. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The state of the last provisioning operation performed on the Search service. |  [optional] [readonly] |
|**replicaCount** | **Integer** | The number of replicas in the Search service. If specified, it must be a value between 1 and 6 inclusive. |  [optional] |
|**sku** | [**Sku**](Sku.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the Search service. |  [optional] [readonly] |
|**statusDetails** | **String** | The details of the Search service status. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;succeeded&quot; |
| PROVISIONING | &quot;provisioning&quot; |
| FAILED | &quot;failed&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| PROVISIONING | &quot;provisioning&quot; |
| DELETING | &quot;deleting&quot; |
| DEGRADED | &quot;degraded&quot; |
| DISABLED | &quot;disabled&quot; |
| ERROR | &quot;error&quot; |



