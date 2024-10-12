# AirbyteConfigurationApi.WebBackendConnectionListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionId** | **String** |  | 
**destination** | [**DestinationSnippetRead**](DestinationSnippetRead.md) |  | 
**isSyncing** | **Boolean** |  | 
**latestSyncJobCreatedAt** | **Number** | epoch time of the latest sync job. null if no sync job has taken place. | [optional] 
**latestSyncJobStatus** | [**JobStatus**](JobStatus.md) |  | [optional] 
**name** | **String** |  | 
**scheduleData** | [**ConnectionScheduleData**](ConnectionScheduleData.md) |  | [optional] 
**scheduleType** | [**ConnectionScheduleType**](ConnectionScheduleType.md) |  | [optional] 
**schemaChange** | [**SchemaChange**](SchemaChange.md) |  | 
**source** | [**SourceSnippetRead**](SourceSnippetRead.md) |  | 
**status** | [**ConnectionStatus**](ConnectionStatus.md) |  | 


