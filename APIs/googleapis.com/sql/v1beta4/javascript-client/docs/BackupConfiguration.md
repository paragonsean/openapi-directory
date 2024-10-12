# CloudSqlAdminApi.BackupConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupRetentionSettings** | [**BackupRetentionSettings**](BackupRetentionSettings.md) |  | [optional] 
**binaryLogEnabled** | **Boolean** | (MySQL only) Whether binary log is enabled. If backup configuration is disabled, binarylog must be disabled as well. | [optional] 
**enabled** | **Boolean** | Whether this configuration is enabled. | [optional] 
**kind** | **String** | This is always &#x60;sql#backupConfiguration&#x60;. | [optional] 
**location** | **String** | Location of the backup | [optional] 
**pointInTimeRecoveryEnabled** | **Boolean** | Whether point in time recovery is enabled. | [optional] 
**replicationLogArchivingEnabled** | **Boolean** | Reserved for future use. | [optional] 
**startTime** | **String** | Start time for the daily backup configuration in UTC timezone in the 24 hour format - &#x60;HH:MM&#x60;. | [optional] 
**transactionLogRetentionDays** | **Number** | The number of days of transaction logs we retain for point in time restore, from 1-7. | [optional] 


