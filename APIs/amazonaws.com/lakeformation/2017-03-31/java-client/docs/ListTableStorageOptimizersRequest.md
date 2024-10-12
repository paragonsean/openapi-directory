

# ListTableStorageOptimizersRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogId** | **String** | The Catalog ID of the table. |  [optional] |
|**databaseName** | **String** | Name of the database where the table is present. |  |
|**tableName** | **String** | Name of the table. |  |
|**storageOptimizerType** | [**StorageOptimizerTypeEnum**](#StorageOptimizerTypeEnum) | The specific type of storage optimizers to list. The supported value is &lt;code&gt;compaction&lt;/code&gt;. |  [optional] |
|**maxResults** | **Integer** | The number of storage optimizers to return on each call. |  [optional] |
|**nextToken** | **String** | A continuation token, if this is a continuation call. |  [optional] |



## Enum: StorageOptimizerTypeEnum

| Name | Value |
|---- | -----|
| COMPACTION | &quot;COMPACTION&quot; |
| GARBAGE_COLLECTION | &quot;GARBAGE_COLLECTION&quot; |
| ALL | &quot;ALL&quot; |



