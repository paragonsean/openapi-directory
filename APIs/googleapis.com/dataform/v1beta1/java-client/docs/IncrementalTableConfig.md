

# IncrementalTableConfig

Contains settings for relations of type `INCREMENTAL_TABLE`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**incrementalPostOperations** | **List&lt;String&gt;** | SQL statements to be executed after inserting new rows into the relation. |  [optional] |
|**incrementalPreOperations** | **List&lt;String&gt;** | SQL statements to be executed before inserting new rows into the relation. |  [optional] |
|**incrementalSelectQuery** | **String** | The SELECT query which returns rows which should be inserted into the relation if it already exists and is not being refreshed. |  [optional] |
|**refreshDisabled** | **Boolean** | Whether this table should be protected from being refreshed. |  [optional] |
|**uniqueKeyParts** | **List&lt;String&gt;** | A set of columns or SQL expressions used to define row uniqueness. If any duplicates are discovered (as defined by &#x60;unique_key_parts&#x60;), only the newly selected rows (as defined by &#x60;incremental_select_query&#x60;) will be included in the relation. |  [optional] |
|**updatePartitionFilter** | **String** | A SQL expression conditional used to limit the set of existing rows considered for a merge operation (see &#x60;unique_key_parts&#x60; for more information). |  [optional] |



