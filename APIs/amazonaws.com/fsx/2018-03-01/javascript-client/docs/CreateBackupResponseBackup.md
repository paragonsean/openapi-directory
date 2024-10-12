# AmazonFsx.CreateBackupResponseBackup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupId** | **String** |  | 
**lifecycle** | [**BackupLifecycle**](BackupLifecycle.md) |  | 
**failureDetails** | [**BackupFailureDetails**](BackupFailureDetails.md) |  | [optional] 
**type** | [**BackupType**](BackupType.md) |  | 
**progressPercent** | **Number** | Displays the current percent of progress of an asynchronous task. | [optional] 
**creationTime** | **Date** |  | 
**kmsKeyId** | **String** |  | [optional] 
**resourceARN** | **String** |  | [optional] 
**tags** | **Array** |  | [optional] 
**fileSystem** | [**BackupFileSystem**](BackupFileSystem.md) |  | 
**directoryInformation** | [**BackupDirectoryInformation**](BackupDirectoryInformation.md) |  | [optional] 
**ownerId** | **String** | An Amazon Web Services account ID. This ID is a 12-digit number that you use to construct Amazon Resource Names (ARNs) for resources. | [optional] 
**sourceBackupId** | **String** | The ID of the source backup. Specifies the backup that you are copying. | [optional] 
**sourceBackupRegion** | **String** |  | [optional] 
**resourceType** | [**ResourceType**](ResourceType.md) |  | [optional] 
**volume** | [**Volume**](Volume.md) |  | [optional] 


