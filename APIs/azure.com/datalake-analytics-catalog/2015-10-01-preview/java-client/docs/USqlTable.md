

# USqlTable

A Data Lake Analytics catalog U-SQL table item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnList** | [**List&lt;USqlTableColumn&gt;**](USqlTableColumn.md) | the list of columns in this table |  [optional] |
|**databaseName** | **String** | the name of the database. |  [optional] |
|**distributionInfo** | [**USqlDistributionInfo**](USqlDistributionInfo.md) |  |  [optional] |
|**externalTable** | [**ExternalTable**](ExternalTable.md) |  |  [optional] |
|**indexList** | [**List&lt;USqlIndex&gt;**](USqlIndex.md) | the list of indices in this table |  [optional] |
|**partitionKeyList** | **List&lt;String&gt;** | the list of partition keys in the table |  [optional] |
|**schemaName** | **String** | the name of the schema associated with this table and database. |  [optional] |
|**tableName** | **String** | the name of the table. |  [optional] |
|**computeAccountName** | **String** | the name of the Data Lake Analytics account. |  [optional] |
|**version** | **UUID** | the version of the catalog item. |  [optional] |



