

# GroupSyncResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**group** | **String** | The name of the group |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**totalTimeSeconds** | **BigDecimal** | The duration of the group sync in seconds |  [optional] |
|**updatedImageCount** | **Integer** | The number of images updated by the this group sync, across all accounts. This is typically only non-zero for vulnerability feeds which update images&#39; vulnerability results during the sync. |  [optional] |
|**updatedRecordCount** | **Integer** | The number of feed data records synced down as either updates or new records |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILURE | &quot;failure&quot; |



