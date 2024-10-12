# AwsLakeFormation.ListTableStorageOptimizersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogId** | **String** | The Catalog ID of the table. | [optional] 
**databaseName** | **String** | Name of the database where the table is present. | 
**tableName** | **String** | Name of the table. | 
**storageOptimizerType** | **String** | The specific type of storage optimizers to list. The supported value is &lt;code&gt;compaction&lt;/code&gt;. | [optional] 
**maxResults** | **Number** | The number of storage optimizers to return on each call. | [optional] 
**nextToken** | **String** | A continuation token, if this is a continuation call. | [optional] 



## Enum: StorageOptimizerTypeEnum


* `COMPACTION` (value: `"COMPACTION"`)

* `GARBAGE_COLLECTION` (value: `"GARBAGE_COLLECTION"`)

* `ALL` (value: `"ALL"`)




