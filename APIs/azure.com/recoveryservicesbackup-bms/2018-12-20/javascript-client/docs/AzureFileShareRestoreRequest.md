# RecoveryServicesBackupClient.AzureFileShareRestoreRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyOptions** | **String** | Options to resolve copy conflicts. | [optional] 
**recoveryType** | **String** | Type of this recovery. | [optional] 
**restoreFileSpecs** | [**[RestoreFileSpecs]**](RestoreFileSpecs.md) | List of Source Files/Folders(which need to recover) and TargetFolderPath details | [optional] 
**restoreRequestType** | **String** | Restore Type (FullShareRestore or ItemLevelRestore) | [optional] 
**sourceResourceId** | **String** | Source storage account ARM Id | [optional] 
**targetDetails** | [**TargetAFSRestoreInfo**](TargetAFSRestoreInfo.md) |  | [optional] 



## Enum: CopyOptionsEnum


* `Invalid` (value: `"Invalid"`)

* `CreateCopy` (value: `"CreateCopy"`)

* `Skip` (value: `"Skip"`)

* `Overwrite` (value: `"Overwrite"`)

* `FailOnConflict` (value: `"FailOnConflict"`)





## Enum: RecoveryTypeEnum


* `Invalid` (value: `"Invalid"`)

* `OriginalLocation` (value: `"OriginalLocation"`)

* `AlternateLocation` (value: `"AlternateLocation"`)

* `RestoreDisks` (value: `"RestoreDisks"`)

* `Offline` (value: `"Offline"`)





## Enum: RestoreRequestTypeEnum


* `Invalid` (value: `"Invalid"`)

* `FullShareRestore` (value: `"FullShareRestore"`)

* `ItemLevelRestore` (value: `"ItemLevelRestore"`)




