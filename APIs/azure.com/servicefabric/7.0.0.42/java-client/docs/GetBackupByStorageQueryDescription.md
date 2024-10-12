

# GetBackupByStorageQueryDescription

Describes additional filters to be applied, while listing backups, and backup storage details from where to fetch the backups.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupEntity** | [**BackupEntity**](BackupEntity.md) |  |  |
|**endDateTimeFilter** | **OffsetDateTime** | Specifies the end date time in ISO8601 till which to enumerate backups. If not specified, backups are enumerated till the end. |  [optional] |
|**latest** | **Boolean** | If specified as true, gets the most recent backup (within the specified time range) for every partition under the specified backup entity. |  [optional] |
|**startDateTimeFilter** | **OffsetDateTime** | Specifies the start date time in ISO8601 from which to enumerate backups. If not specified, backups are enumerated from the beginning. |  [optional] |
|**storage** | [**BackupStorageDescription**](BackupStorageDescription.md) |  |  |



