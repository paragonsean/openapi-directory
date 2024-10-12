# AzureSqlDatabase.DatabasePropertiesRecommendedIndexInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The proposed index action. You can create a missing index, drop an unused index, or rebuild an existing index to improve its performance. | [optional] [readonly] 
**columns** | **[String]** | Columns over which to build index | [optional] [readonly] 
**created** | **Date** | The UTC datetime showing when this resource was created (ISO8601 format). | [optional] [readonly] 
**estimatedImpact** | [**[DatabasePropertiesRecommendedIndexInnerPropertiesEstimatedImpactInner]**](DatabasePropertiesRecommendedIndexInnerPropertiesEstimatedImpactInner.md) | The estimated impact of doing recommended index action. | [optional] [readonly] 
**includedColumns** | **[String]** | The list of column names to be included in the index | [optional] [readonly] 
**indexScript** | **String** | The full build index script | [optional] [readonly] 
**indexType** | **String** | The type of index (CLUSTERED, NONCLUSTERED, COLUMNSTORE, CLUSTERED COLUMNSTORE) | [optional] [readonly] 
**lastModified** | **Date** | The UTC datetime of when was this resource last changed (ISO8601 format). | [optional] [readonly] 
**reportedImpact** | [**[DatabasePropertiesRecommendedIndexInnerPropertiesEstimatedImpactInner]**](DatabasePropertiesRecommendedIndexInnerPropertiesEstimatedImpactInner.md) | The values reported after index action is complete. | [optional] [readonly] 
**schema** | **String** | The schema where table to build index over resides | [optional] [readonly] 
**state** | **String** | The current recommendation state. | [optional] [readonly] 
**table** | **String** | The table on which to build index. | [optional] [readonly] 



## Enum: ActionEnum


* `Create` (value: `"Create"`)

* `Drop` (value: `"Drop"`)

* `Rebuild` (value: `"Rebuild"`)





## Enum: IndexTypeEnum


* `CLUSTERED` (value: `"CLUSTERED"`)

* `NONCLUSTERED` (value: `"NONCLUSTERED"`)

* `COLUMNSTORE` (value: `"COLUMNSTORE"`)

* `CLUSTERED COLUMNSTORE` (value: `"CLUSTERED COLUMNSTORE"`)





## Enum: StateEnum


* `Active` (value: `"Active"`)

* `Pending` (value: `"Pending"`)

* `Executing` (value: `"Executing"`)

* `Verifying` (value: `"Verifying"`)

* `Pending Revert` (value: `"Pending Revert"`)

* `Reverting` (value: `"Reverting"`)

* `Reverted` (value: `"Reverted"`)

* `Ignored` (value: `"Ignored"`)

* `Expired` (value: `"Expired"`)

* `Blocked` (value: `"Blocked"`)

* `Success` (value: `"Success"`)




