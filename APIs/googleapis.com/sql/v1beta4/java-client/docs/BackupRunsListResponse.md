

# BackupRunsListResponse

Backup run list results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | [**List&lt;BackupRun&gt;**](BackupRun.md) | A list of backup runs in reverse chronological order of the enqueued time. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#backupRunsList&#x60;. |  [optional] |
|**nextPageToken** | **String** | The continuation token, used to page through large result sets. Provide this value in a subsequent request to return the next page of results. |  [optional] |



