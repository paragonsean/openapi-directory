

# StorageDatabasecenterPartnerapiV1mainBackupConfiguration

Configuration for automatic backups

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automatedBackupEnabled** | **Boolean** | Whether customer visible automated backups are enabled on the instance. |  [optional] |
|**backupRetentionSettings** | [**StorageDatabasecenterPartnerapiV1mainRetentionSettings**](StorageDatabasecenterPartnerapiV1mainRetentionSettings.md) |  |  [optional] |
|**pointInTimeRecoveryEnabled** | **Boolean** | Whether point-in-time recovery is enabled. This is optional field, if the database service does not have this feature or metadata is not available in control plane, this can be omitted. |  [optional] |



