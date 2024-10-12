

# ADLSGen2FileSystemDataSetMapping

An ADLS Gen2 file system data set mapping.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**ADLSGen2FileSystemDataSetMappingProperties**](ADLSGen2FileSystemDataSetMappingProperties.md) |  |  |
|**kind** | [**KindEnum**](#KindEnum) | Kind of data set mapping. |  |
|**id** | **String** | The resource id of the azure resource |  [optional] [readonly] |
|**name** | **String** | Name of the azure resource |  [optional] [readonly] |
|**type** | **String** | Type of the azure resource |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| BLOB | &quot;Blob&quot; |
| CONTAINER | &quot;Container&quot; |
| BLOB_FOLDER | &quot;BlobFolder&quot; |
| ADLS_GEN2_FILE_SYSTEM | &quot;AdlsGen2FileSystem&quot; |
| ADLS_GEN2_FOLDER | &quot;AdlsGen2Folder&quot; |
| ADLS_GEN2_FILE | &quot;AdlsGen2File&quot; |
| KUSTO_CLUSTER | &quot;KustoCluster&quot; |
| KUSTO_DATABASE | &quot;KustoDatabase&quot; |
| SQL_DB_TABLE | &quot;SqlDBTable&quot; |
| SQL_DW_TABLE | &quot;SqlDWTable&quot; |



