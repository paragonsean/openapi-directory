

# USqlTablePartition

A Data Lake Analytics catalog U-SQL table partition item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createDate** | **OffsetDateTime** | the creation time of the partition |  [optional] |
|**databaseName** | **String** | the name of the database. |  [optional] |
|**indexId** | **Integer** | the index ID for this partition. |  [optional] |
|**label** | **List&lt;String&gt;** | the list of labels associated with this partition. |  [optional] |
|**parentName** | [**DdlName**](DdlName.md) |  |  [optional] |
|**partitionName** | **String** | the name of the table partition. |  [optional] |
|**schemaName** | **String** | the name of the schema associated with this table partition and database. |  [optional] |
|**computeAccountName** | **String** | the name of the Data Lake Analytics account. |  [optional] |
|**version** | **UUID** | the version of the catalog item. |  [optional] |



