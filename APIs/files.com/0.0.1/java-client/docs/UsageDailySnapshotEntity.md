

# UsageDailySnapshotEntity

List Usage Daily Snapshots

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiUsageAvailable** | **Boolean** | True if the API usage fields &#x60;read_api_usage&#x60; and &#x60;write_api_usage&#x60; can be relied upon.  If this is false, we suggest hiding that value from any UI. |  [optional] |
|**currentStorage** | **Integer** | GB of Files Native Storage used on this day. |  [optional] |
|**date** | **LocalDate** | The date of this usage record |  [optional] |
|**deletedFilesCountedInMinimum** | **Integer** | GB of Files Native Storage used on this day for files that have been permanently deleted but were uploaded less than 30 days ago, and are still billable. |  [optional] |
|**deletedFilesStorage** | **Integer** | GB of Files Native Storage used on this day for files that have been deleted and are stored as backups. |  [optional] |
|**id** | **Integer** | ID of the usage record |  [optional] |
|**readApiUsage** | **Integer** | Read API Calls used on this day. Note: only updated for days before the current day. |  [optional] |
|**rootStorage** | **Integer** | GB of Files Native Storage used for the root folder.  Included here because this value will not be part of &#x60;usage_by_top_level_dir&#x60; |  [optional] |
|**usageByTopLevelDir** | **Object** | Usage broken down by each top-level folder |  [optional] |
|**userCount** | **Integer** | Number of billable users as of this day. |  [optional] |
|**writeApiUsage** | **Integer** | Write API Calls used on this day. Note: only updated for days before the current day. |  [optional] |



