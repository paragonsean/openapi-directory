

# ConsumerSourceDataSetProperties

Properties of consumer source dataSet

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSetId** | **String** | DataSet Id |  [optional] [readonly] |
|**dataSetLocation** | **String** | Location of the data set. |  [optional] [readonly] |
|**dataSetName** | **String** | DataSet name |  [optional] [readonly] |
|**dataSetPath** | **String** | DataSet path |  [optional] [readonly] |
|**dataSetType** | [**DataSetTypeEnum**](#DataSetTypeEnum) | Type of data set |  [optional] [readonly] |



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



