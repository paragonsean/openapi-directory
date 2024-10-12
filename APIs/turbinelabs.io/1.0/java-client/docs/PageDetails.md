

# PageDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**direction** | [**DirectionEnum**](#DirectionEnum) | The direction walked from the ref_id when building this page. |  [optional] |
|**hasMore** | **Boolean** | Whether or not there are more entries to be requested after this page. |  [optional] |
|**refId** | **String** | The ID used as a reference when building this page. |  [optional] |
|**totalEntries** | **Integer** | How many total entries would have been returned in the time window if it had not been paginated.  |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| BEFORE | &quot;before&quot; |
| AFTER | &quot;after&quot; |



