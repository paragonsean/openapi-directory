

# JobConfigurationTableCopy

JobConfigurationTableCopy configures a job that copies data from one table to another. For more information on copying tables, see [Copy a table](https://cloud.google.com/bigquery/docs/managing-tables#copy-table).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createDisposition** | **String** | Optional. Specifies whether the job is allowed to create new tables. The following values are supported: * CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table. * CREATE_NEVER: The table must already exist. If it does not, a &#39;notFound&#39; error is returned in the job result. The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion. |  [optional] |
|**destinationEncryptionConfiguration** | [**EncryptionConfiguration**](EncryptionConfiguration.md) |  |  [optional] |
|**destinationExpirationTime** | **String** | Optional. The time when the destination table expires. Expired tables will be deleted and their storage reclaimed. |  [optional] |
|**destinationTable** | [**TableReference**](TableReference.md) |  |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | Optional. Supported operation types in table copy job. |  [optional] |
|**sourceTable** | [**TableReference**](TableReference.md) |  |  [optional] |
|**sourceTables** | [**List&lt;TableReference&gt;**](TableReference.md) | [Pick one] Source tables to copy. |  [optional] |
|**writeDisposition** | **String** | Optional. Specifies the action that occurs if the destination table already exists. The following values are supported: * WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema and table constraints from the source table. * WRITE_APPEND: If the table already exists, BigQuery appends the data to the table. * WRITE_EMPTY: If the table already exists and contains data, a &#39;duplicate&#39; error is returned in the job result. The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| OPERATION_TYPE_UNSPECIFIED | &quot;OPERATION_TYPE_UNSPECIFIED&quot; |
| COPY | &quot;COPY&quot; |
| SNAPSHOT | &quot;SNAPSHOT&quot; |
| RESTORE | &quot;RESTORE&quot; |
| CLONE | &quot;CLONE&quot; |



