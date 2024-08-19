# BatchManagement.BatchAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountEndpoint** | **String** | The account endpoint used to interact with the Batch service. | [optional] [readonly] 
**activeJobAndJobScheduleQuota** | **Number** |  | [optional] [readonly] 
**autoStorage** | [**AutoStorageProperties**](AutoStorageProperties.md) |  | [optional] 
**dedicatedCoreQuota** | **Number** | For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned. | [optional] [readonly] 
**dedicatedCoreQuotaPerVMFamily** | [**[VirtualMachineFamilyCoreQuota]**](VirtualMachineFamilyCoreQuota.md) | A list of the dedicated core quota per Virtual Machine family for the Batch account. For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned. | [optional] [readonly] 
**dedicatedCoreQuotaPerVMFamilyEnforced** | **Boolean** | Batch is transitioning its core quota system for dedicated cores to be enforced per Virtual Machine family. During this transitional phase, the dedicated core quota per Virtual Machine family may not yet be enforced. If this flag is false, dedicated core quota is enforced via the old dedicatedCoreQuota property on the account and does not consider Virtual Machine family. If this flag is true, dedicated core quota is enforced via the dedicatedCoreQuotaPerVMFamily property on the account, and the old dedicatedCoreQuota does not apply. | [optional] [readonly] 
**keyVaultReference** | [**KeyVaultReference**](KeyVaultReference.md) |  | [optional] 
**lowPriorityCoreQuota** | **Number** | For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned. | [optional] [readonly] 
**poolAllocationMode** | [**PoolAllocationMode**](PoolAllocationMode.md) |  | [optional] 
**poolQuota** | **Number** |  | [optional] [readonly] 
**provisioningState** | **String** | The provisioned state of the resource | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Invalid` (value: `"Invalid"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Cancelled` (value: `"Cancelled"`)




