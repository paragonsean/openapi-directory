# ServiceFabricClientApis.TimeBasedBackupScheduleDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runDays** | [**[DayOfWeek]**](DayOfWeek.md) | List of days of a week when to trigger the periodic backup. This is valid only when the backup schedule frequency type is weekly. | [optional] 
**runTimes** | **[Date]** | Represents the list of exact time during the day in ISO8601 format. Like &#39;19:00:00&#39; will represent &#39;7PM&#39; during the day. Date specified along with time will be ignored. | 
**scheduleFrequencyType** | [**BackupScheduleFrequencyType**](BackupScheduleFrequencyType.md) |  | 


