# RubrikRestApi.MssqlSlaRelatedProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyOnly** | **Boolean** | Boolean value that specifies whether or not to perform copy-only backups of the database. When true, database backups are copy-only backups. When false, database backups are full backups. | [optional] 
**logBackupFrequencyInSeconds** | **Number** | Seconds between two log backups. A value of 0 disables log backup. | [optional] 
**logRetentionHours** | **Number** | Number of hours to retain a log backup. When the value is set to -1 the Rubrik cluster retains the log backup until the database snapshots that precede the log backup have expired. | [optional] 


