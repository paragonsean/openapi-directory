

# WebBackendConnectionListItem

Information about a connection that shows up in the connection list view.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionId** | **UUID** |  |  |
|**destination** | [**DestinationSnippetRead**](DestinationSnippetRead.md) |  |  |
|**isSyncing** | **Boolean** |  |  |
|**latestSyncJobCreatedAt** | **Long** | epoch time of the latest sync job. null if no sync job has taken place. |  [optional] |
|**latestSyncJobStatus** | **JobStatus** |  |  [optional] |
|**name** | **String** |  |  |
|**scheduleData** | [**ConnectionScheduleData**](ConnectionScheduleData.md) |  |  [optional] |
|**scheduleType** | **ConnectionScheduleType** |  |  [optional] |
|**schemaChange** | **SchemaChange** |  |  |
|**source** | [**SourceSnippetRead**](SourceSnippetRead.md) |  |  |
|**status** | **ConnectionStatus** |  |  |



