# StorageCacheMgmtClient.CacheProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cacheSizeGB** | **Number** | The size of this Cache, in GB. | [optional] 
**health** | [**CacheHealth**](CacheHealth.md) |  | [optional] 
**mountAddresses** | **[String]** | Array of IP addresses that can be used by clients mounting this Cache. | [optional] [readonly] 
**provisioningState** | **String** | ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property | [optional] 
**subnet** | **String** | A fully qualified URL. | [optional] 
**upgradeStatus** | [**CacheUpgradeStatus**](CacheUpgradeStatus.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Cancelled` (value: `"Cancelled"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Updating` (value: `"Updating"`)




