

# UpdateDatabaseDdlMetadata

Metadata type for the operation returned by UpdateDatabaseDdl.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;DdlStatementActionInfo&gt;**](DdlStatementActionInfo.md) | The brief action info for the DDL statements. &#x60;actions[i]&#x60; is the brief info for &#x60;statements[i]&#x60;. |  [optional] |
|**commitTimestamps** | **List&lt;String&gt;** | Reports the commit timestamps of all statements that have succeeded so far, where &#x60;commit_timestamps[i]&#x60; is the commit timestamp for the statement &#x60;statements[i]&#x60;. |  [optional] |
|**database** | **String** | The database being modified. |  [optional] |
|**progress** | [**List&lt;OperationProgress&gt;**](OperationProgress.md) | The progress of the UpdateDatabaseDdl operations. All DDL statements will have continuously updating progress, and &#x60;progress[i]&#x60; is the operation progress for &#x60;statements[i]&#x60;. Also, &#x60;progress[i]&#x60; will have start time and end time populated with commit timestamp of operation, as well as a progress of 100% once the operation has completed. |  [optional] |
|**statements** | **List&lt;String&gt;** | For an update this list contains all the statements. For an individual statement, this list contains only that statement. |  [optional] |
|**throttled** | **Boolean** | Output only. When true, indicates that the operation is throttled e.g. due to resource constraints. When resources become available the operation will resume and this field will be false again. |  [optional] [readonly] |



