# StorageCacheMgmtClient.StorageTargetProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clfs** | [**ClfsTarget**](ClfsTarget.md) |  | [optional] 
**junctions** | [**[NamespaceJunction]**](NamespaceJunction.md) | List of Cache namespace junctions to target for namespace associations. | [optional] 
**nfs3** | [**Nfs3Target**](Nfs3Target.md) |  | [optional] 
**provisioningState** | **String** | ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property | [optional] 
**targetType** | **String** | Type of the Storage Target. | [optional] 
**unknown** | [**UnknownTarget**](UnknownTarget.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Cancelled` (value: `"Cancelled"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Updating` (value: `"Updating"`)





## Enum: TargetTypeEnum


* `nfs3` (value: `"nfs3"`)

* `clfs` (value: `"clfs"`)

* `unknown` (value: `"unknown"`)




