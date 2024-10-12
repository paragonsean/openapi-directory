

# MssqlDbUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copyOnly** | **Boolean** | Boolean value that specifies whether or not to perform copy-only backups of the database. When true, database backups are copy-only backups. When false, database backups are full backups. |  [optional] |
|**logBackupFrequencyInSeconds** | **Integer** | Seconds between two log backups. A value of 0 disables log backup. |  [optional] |
|**logRetentionHours** | **Integer** | Number of hours to retain a log backup. When the value is set to -1 the Rubrik cluster retains the log backup until the database snapshots that precede the log backup have expired. |  [optional] |
|**configuredSlaDomainId** | **String** | SLA Domain ID assigned to instance. Existing snapshots of the instance will be retained with the configuration of specified SLA Domain. |  [optional] |
|**useConfiguredDefaultLogRetention** | **Boolean** | Determines whether to use the configured default value of log backup retention. |  [optional] |
|**isPaused** | **Boolean** | Whether to pause or resume backups/archival for this database. |  [optional] |
|**maxDataStreams** | **Integer** | Maximum number of parallel data streams that can be used to back up the database. |  [optional] |
|**postBackupScript** | [**MssqlScriptDetail**](MssqlScriptDetail.md) |  |  [optional] |
|**preBackupScript** | [**MssqlScriptDetail**](MssqlScriptDetail.md) |  |  [optional] |
|**shouldForceFull** | **Boolean** | Determines whether to force a full for the next snapshot of a SQL Server database. When this value is true, the Rubrik cluster takes a full snapshot. This value is false by default and is reset to false after a successful full snapshot. |  [optional] |



