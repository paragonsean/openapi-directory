

# BackupInfo

Represents a backup point which can be used to trigger a restore.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationName** | **String** | Name of the Service Fabric application this partition backup belongs to. |  [optional] |
|**backupChainId** | **UUID** | Unique backup chain ID. All backups part of the same chain has the same backup chain id. A backup chain is comprised of 1 full backup and multiple incremental backups. |  [optional] |
|**backupId** | **UUID** | Unique backup ID . |  [optional] |
|**backupLocation** | **String** | Location of the backup, relative to the backup store. |  [optional] |
|**backupType** | **BackupType** |  |  [optional] |
|**creationTimeUtc** | **OffsetDateTime** | The date time when this backup was taken. |  [optional] |
|**epochOfLastBackupRecord** | [**Epoch**](Epoch.md) |  |  [optional] |
|**failureError** | [**FabricErrorError**](FabricErrorError.md) |  |  [optional] |
|**lsnOfLastBackupRecord** | **String** | LSN of the last record in this backup. |  [optional] |
|**partitionInformation** | [**PartitionInformation**](PartitionInformation.md) |  |  [optional] |
|**serviceManifestVersion** | **String** | Manifest Version of the service this partition backup belongs to. |  [optional] |
|**serviceName** | **String** | Name of the Service Fabric service this partition backup belongs to. |  [optional] |



