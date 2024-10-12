# SearchManagementClient.SearchServiceReadableProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitionCount** | **Number** | The number of partitions in the Search service; if specified, it can be 1, 2, 3, 4, 6, or 12. | [optional] 
**provisioningState** | **String** | The state of the last provisioning operation performed on the Search service. | [optional] [readonly] 
**replicaCount** | **Number** | The number of replicas in the Search service. If specified, it must be a value between 1 and 6 inclusive. | [optional] 
**sku** | [**Sku**](Sku.md) |  | [optional] 
**status** | **String** | The status of the Search service. | [optional] [readonly] 
**statusDetails** | **String** | The details of the Search service status. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `succeeded` (value: `"succeeded"`)

* `provisioning` (value: `"provisioning"`)

* `failed` (value: `"failed"`)





## Enum: StatusEnum


* `running` (value: `"running"`)

* `provisioning` (value: `"provisioning"`)

* `deleting` (value: `"deleting"`)

* `degraded` (value: `"degraded"`)

* `disabled` (value: `"disabled"`)

* `error` (value: `"error"`)




