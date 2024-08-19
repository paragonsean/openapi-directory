

# AutomatedBackupPolicy

Message describing the user-specified automated backup policy. All fields in the automated backup policy are optional. Defaults for each field are provided if they are not set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupWindow** | **String** | The length of the time window during which a backup can be taken. If a backup does not succeed within this time window, it will be canceled and considered failed. The backup window must be at least 5 minutes long. There is no upper bound on the window. If not set, it defaults to 1 hour. |  [optional] |
|**enabled** | **Boolean** | Whether automated automated backups are enabled. If not set, defaults to true. |  [optional] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels to apply to backups created using this configuration. |  [optional] |
|**location** | **String** | The location where the backup will be stored. Currently, the only supported option is to store the backup in the same region as the cluster. If empty, defaults to the region of the cluster. |  [optional] |
|**quantityBasedRetention** | [**QuantityBasedRetention**](QuantityBasedRetention.md) |  |  [optional] |
|**timeBasedRetention** | [**TimeBasedRetention**](TimeBasedRetention.md) |  |  [optional] |
|**weeklySchedule** | [**WeeklySchedule**](WeeklySchedule.md) |  |  [optional] |



