# DataprocMetastoreApi.ScheduledBackup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupLocation** | **String** | Optional. A Cloud Storage URI of a folder, in the format gs:///. A sub-folder containing backup files will be stored below it. | [optional] 
**cronSchedule** | **String** | Optional. The scheduled interval in Cron format, see https://en.wikipedia.org/wiki/Cron The default is empty: scheduled backup is not enabled. Must be specified to enable scheduled backups. | [optional] 
**enabled** | **Boolean** | Optional. Defines whether the scheduled backup is enabled. The default value is false. | [optional] 
**latestBackup** | [**LatestBackup**](LatestBackup.md) |  | [optional] 
**nextScheduledTime** | **String** | Output only. The time when the next backups execution is scheduled to start. | [optional] [readonly] 
**timeZone** | **String** | Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), e.g. America/Los_Angeles or Africa/Abidjan. If left unspecified, the default is UTC. | [optional] 


