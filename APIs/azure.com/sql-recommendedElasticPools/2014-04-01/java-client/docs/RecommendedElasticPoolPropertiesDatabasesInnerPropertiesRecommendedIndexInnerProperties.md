

# RecommendedElasticPoolPropertiesDatabasesInnerPropertiesRecommendedIndexInnerProperties

Represents the properties of a database recommended index.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | The proposed index action. You can create a missing index, drop an unused index, or rebuild an existing index to improve its performance. |  [optional] [readonly] |
|**columns** | **List&lt;String&gt;** | Columns over which to build index |  [optional] [readonly] |
|**created** | **OffsetDateTime** | The UTC datetime showing when this resource was created (ISO8601 format). |  [optional] [readonly] |
|**estimatedImpact** | [**List&lt;RecommendedElasticPoolPropertiesDatabasesInnerPropertiesRecommendedIndexInnerPropertiesEstimatedImpactInner&gt;**](RecommendedElasticPoolPropertiesDatabasesInnerPropertiesRecommendedIndexInnerPropertiesEstimatedImpactInner.md) | The estimated impact of doing recommended index action. |  [optional] [readonly] |
|**includedColumns** | **List&lt;String&gt;** | The list of column names to be included in the index |  [optional] [readonly] |
|**indexScript** | **String** | The full build index script |  [optional] [readonly] |
|**indexType** | [**IndexTypeEnum**](#IndexTypeEnum) | The type of index (CLUSTERED, NONCLUSTERED, COLUMNSTORE, CLUSTERED COLUMNSTORE) |  [optional] [readonly] |
|**lastModified** | **OffsetDateTime** | The UTC datetime of when was this resource last changed (ISO8601 format). |  [optional] [readonly] |
|**reportedImpact** | [**List&lt;RecommendedElasticPoolPropertiesDatabasesInnerPropertiesRecommendedIndexInnerPropertiesEstimatedImpactInner&gt;**](RecommendedElasticPoolPropertiesDatabasesInnerPropertiesRecommendedIndexInnerPropertiesEstimatedImpactInner.md) | The values reported after index action is complete. |  [optional] [readonly] |
|**schema** | **String** | The schema where table to build index over resides |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The current recommendation state. |  [optional] [readonly] |
|**table** | **String** | The table on which to build index. |  [optional] [readonly] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| CREATE | &quot;Create&quot; |
| DROP | &quot;Drop&quot; |
| REBUILD | &quot;Rebuild&quot; |



## Enum: IndexTypeEnum

| Name | Value |
|---- | -----|
| CLUSTERED | &quot;CLUSTERED&quot; |
| NONCLUSTERED | &quot;NONCLUSTERED&quot; |
| COLUMNSTORE | &quot;COLUMNSTORE&quot; |
| CLUSTERED_COLUMNSTORE | &quot;CLUSTERED COLUMNSTORE&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| PENDING | &quot;Pending&quot; |
| EXECUTING | &quot;Executing&quot; |
| VERIFYING | &quot;Verifying&quot; |
| PENDING_REVERT | &quot;Pending Revert&quot; |
| REVERTING | &quot;Reverting&quot; |
| REVERTED | &quot;Reverted&quot; |
| IGNORED | &quot;Ignored&quot; |
| EXPIRED | &quot;Expired&quot; |
| BLOCKED | &quot;Blocked&quot; |
| SUCCESS | &quot;Success&quot; |



