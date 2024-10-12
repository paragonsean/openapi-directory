# ComputeDiskAdminManagementClient.DiskMigrationJobsCreateRequestInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actualSizeGB** | **Number** | The actual size of disk in GB. | [optional] [readonly] 
**diskId** | **String** | The disk id. | [optional] 
**diskSku** | **String** | Disk Sku. | [optional] 
**diskType** | **String** | Disk resource type. | [optional] 
**managedBy** | **String** | Compute resource Uri which owns this disk. | [optional] [readonly] 
**provisionSizeGB** | **Number** | The provision size of disk in GB. | [optional] [readonly] 
**sharePath** | **String** | The disk share path. | [optional] 
**status** | **String** | Disk State. | [optional] 
**userResourceId** | **String** | The disk resource Uri from user view. | [optional] [readonly] 



## Enum: DiskSkuEnum


* `Standard_LRS` (value: `"Standard_LRS"`)

* `Standard_ZRS` (value: `"Standard_ZRS"`)

* `Standard_GRS` (value: `"Standard_GRS"`)

* `Standard_RAGRS` (value: `"Standard_RAGRS"`)

* `Premium_LRS` (value: `"Premium_LRS"`)

* `StandardSSD_LRS` (value: `"StandardSSD_LRS"`)

* `UltraSSD_LRS` (value: `"UltraSSD_LRS"`)





## Enum: DiskTypeEnum


* `Undefined` (value: `"Undefined"`)

* `Disk` (value: `"Disk"`)

* `Snapshot` (value: `"Snapshot"`)

* `RestorePoint` (value: `"RestorePoint"`)

* `ManagedBlob` (value: `"ManagedBlob"`)





## Enum: StatusEnum


* `Undefined` (value: `"Undefined"`)

* `Unattached` (value: `"Unattached"`)

* `Attached` (value: `"Attached"`)

* `Reserved` (value: `"Reserved"`)

* `ActiveSAS` (value: `"ActiveSAS"`)

* `Unknown` (value: `"Unknown"`)

* `All` (value: `"All"`)

* `Recommended` (value: `"Recommended"`)

* `OfflineMigration` (value: `"OfflineMigration"`)

* `OnlineMigration` (value: `"OnlineMigration"`)




