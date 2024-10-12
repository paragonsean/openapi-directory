

# OracleDataGuardGroupUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostLogRetentionHours** | **Integer** | Specifies an interval in hours. For Oracle archived redo log files whose nextTime is before (now - interval), the next log snapshot job will delete them from the host. Set to 0 for inheriting the value from its parent; -1 for immediate deletion; and -2 to skip log deletion. |  [optional] |
|**hostMount** | **String** | Path where the NFS share is mounted on the host. |  [optional] |
|**logBackupFrequencyInMinutes** | **Integer** | Specifies an interval in minutes. This interval is the period between successive log backups. |  [optional] |
|**logRetentionHours** | **Integer** | Specifies an interval in hours. Log backups are retained for the duration of the interval. |  [optional] |
|**numChannels** | **Integer** | Number of channels used to backup the Oracle database. |  [optional] |
|**preferredDGMemberUniqueNames** | **List&lt;String&gt;** | Ordered list of database unique names to use for backup. |  [optional] |
|**shouldBackupFromPrimaryOnly** | **Boolean** | Value that indicates whether to backup from the PRIMARY member only, or from any available member. |  [optional] |



