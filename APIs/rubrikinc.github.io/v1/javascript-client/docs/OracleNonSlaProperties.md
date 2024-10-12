# RubrikRestApi.OracleNonSlaProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostLogRetentionHours** | **Number** | Specifies an interval in hours. The next log snapshot job deletes archived Oracle redo log files whose &#39;nextTime&#39; field specifies a time more than the specified number of hours ago. To immediately delete archived redo log files regardless of age, specify an interval of -1. To preserve all archived redo log files, specify an interval of -2. | 
**hostMount** | **String** | Path where the NFS share is mounted on the host. | 
**logBackupFrequencyInMinutes** | **Number** | Specifies an interval in minutes. This interval is the period between successive log backups. | 
**logRetentionHours** | **Number** | Specifies an interval in hours. Log backups are retained for the duration of the interval. | 
**numChannels** | **Number** | Number of channels used to backup the Oracle database. | 


