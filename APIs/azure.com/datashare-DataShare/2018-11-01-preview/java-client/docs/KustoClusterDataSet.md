

# KustoClusterDataSet

A kusto cluster data set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**KustoClusterDataSetProperties**](KustoClusterDataSetProperties.md) |  |  |
|**kind** | [**KindEnum**](#KindEnum) | Kind of data set. |  |
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
| ADLS_GEN1_FOLDER | &quot;AdlsGen1Folder&quot; |
| ADLS_GEN1_FILE | &quot;AdlsGen1File&quot; |
| KUSTO_CLUSTER | &quot;KustoCluster&quot; |
| KUSTO_DATABASE | &quot;KustoDatabase&quot; |
| SQL_DB_TABLE | &quot;SqlDBTable&quot; |
| SQL_DW_TABLE | &quot;SqlDWTable&quot; |



