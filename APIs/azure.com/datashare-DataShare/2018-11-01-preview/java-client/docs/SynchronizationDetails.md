

# SynchronizationDetails

Synchronization details at data set level

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSetId** | **String** | Id of data set |  [optional] [readonly] |
|**dataSetType** | [**DataSetTypeEnum**](#DataSetTypeEnum) | Type of the data set |  [optional] [readonly] |
|**durationMs** | **Integer** | Duration of data set level copy |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | End time of data set level copy |  [optional] [readonly] |
|**filesRead** | **Long** | The number of files read from the source data set |  [optional] [readonly] |
|**filesWritten** | **Long** | The number of files written into the sink data set |  [optional] [readonly] |
|**message** | **String** | Error message if any |  [optional] [readonly] |
|**name** | **String** | Name of the data set |  [optional] [readonly] |
|**rowsCopied** | **Long** | The number of files copied into the sink data set |  [optional] [readonly] |
|**rowsRead** | **Long** | The number of rows read from the source data set. |  [optional] [readonly] |
|**sizeRead** | **Long** | The size of the data read from the source data set in bytes |  [optional] [readonly] |
|**sizeWritten** | **Long** | The size of the data written into the sink data set in bytes |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | Start time of data set level copy |  [optional] [readonly] |
|**status** | **String** | Raw Status |  [optional] [readonly] |
|**vCore** | **Long** | The vCore units consumed for the data set synchronization |  [optional] [readonly] |



## Enum: DataSetTypeEnum

| Name | Value |
|---- | -----|
| BLOB | &quot;Blob&quot; |
| CONTAINER | &quot;Container&quot; |
| BLOB_FOLDER | &quot;BlobFolder&quot; |
| ADLS_GEN2_FILE_SYSTEM | &quot;AdlsGen2FileSystem&quot; |
| ADLS_GEN2_FOLDER | &quot;AdlsGen2Folder&quot; |
| ADLS_GEN2_FILE | &quot;AdlsGen2File&quot; |
| ADLS_GEN1_FOLDER | &quot;AdlsGen1Folder&quot; |
| ADLS_GEN1_FILE | &quot;AdlsGen1File&quot; |
| KUSTO_CLUSTER | &quot;KustoCluster&quot; |
| KUSTO_DATABASE | &quot;KustoDatabase&quot; |
| SQL_DB_TABLE | &quot;SqlDBTable&quot; |
| SQL_DW_TABLE | &quot;SqlDWTable&quot; |



