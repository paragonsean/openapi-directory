

# ContinuousBackupConfig

ContinuousBackupConfig describes the continuous backups recovery configurations of a cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether ContinuousBackup is enabled. |  [optional] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**recoveryWindowDays** | **Integer** | The number of days that are eligible to restore from using PITR. To support the entire recovery window, backups and logs are retained for one day more than the recovery window. If not set, defaults to 14 days. |  [optional] |



