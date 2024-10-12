

# BMSRPQueryObject

Filters to list backup copies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endDate** | **OffsetDateTime** | Backup copies created before this time. |  [optional] |
|**extendedInfo** | **Boolean** | In Get Recovery Point, it tells whether extended information about recovery point is asked. |  [optional] |
|**restorePointQueryType** | [**RestorePointQueryTypeEnum**](#RestorePointQueryTypeEnum) | RestorePoint type |  [optional] |
|**startDate** | **OffsetDateTime** | Backup copies created after this time. |  [optional] |



## Enum: RestorePointQueryTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| FULL | &quot;Full&quot; |
| LOG | &quot;Log&quot; |
| DIFFERENTIAL | &quot;Differential&quot; |
| FULL_AND_DIFFERENTIAL | &quot;FullAndDifferential&quot; |
| ALL | &quot;All&quot; |



