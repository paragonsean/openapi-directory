

# FeedSyncResult

The result of a sync of a single feed

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feed** | **String** | The name of the feed synced |  [optional] |
|**groups** | [**List&lt;GroupSyncResult&gt;**](GroupSyncResult.md) | Array of group sync results |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The result of the sync operations, either co |  [optional] |
|**totalTimeSeconds** | **BigDecimal** | The duratin, in seconds, of the sync of the feed, the sum of all the group syncs |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILURE | &quot;failure&quot; |



