

# AzureFileShareRestoreRequest

AzureFileShare Restore Request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copyOptions** | [**CopyOptionsEnum**](#CopyOptionsEnum) | Options to resolve copy conflicts. |  [optional] |
|**recoveryType** | [**RecoveryTypeEnum**](#RecoveryTypeEnum) | Type of this recovery. |  [optional] |
|**restoreFileSpecs** | [**List&lt;RestoreFileSpecs&gt;**](RestoreFileSpecs.md) | List of Source Files/Folders(which need to recover) and TargetFolderPath details |  [optional] |
|**restoreRequestType** | [**RestoreRequestTypeEnum**](#RestoreRequestTypeEnum) | Restore Type (FullShareRestore or ItemLevelRestore) |  [optional] |
|**sourceResourceId** | **String** | Source storage account ARM Id |  [optional] |
|**targetDetails** | [**TargetAFSRestoreInfo**](TargetAFSRestoreInfo.md) |  |  [optional] |



## Enum: CopyOptionsEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CREATE_COPY | &quot;CreateCopy&quot; |
| SKIP | &quot;Skip&quot; |
| OVERWRITE | &quot;Overwrite&quot; |
| FAIL_ON_CONFLICT | &quot;FailOnConflict&quot; |



## Enum: RecoveryTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ORIGINAL_LOCATION | &quot;OriginalLocation&quot; |
| ALTERNATE_LOCATION | &quot;AlternateLocation&quot; |
| RESTORE_DISKS | &quot;RestoreDisks&quot; |
| OFFLINE | &quot;Offline&quot; |



## Enum: RestoreRequestTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| FULL_SHARE_RESTORE | &quot;FullShareRestore&quot; |
| ITEM_LEVEL_RESTORE | &quot;ItemLevelRestore&quot; |



